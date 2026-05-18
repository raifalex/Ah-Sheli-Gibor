#!/usr/bin/env python3
"""
Ah Sheli Gibor — Hebrew validation script (v0.3.0)

Runs grammar and phrasing checks against Hebrew text.

Two modes:
  --no-model  : regex-based rules only (fast, no dependencies beyond stdlib)
  default     : regex + DictaBERT parse-based checks (requires transformers + torch)

Usage:
  python hebrew_validate.py <text_file>
  python hebrew_validate.py --no-model <text_file>
  python hebrew_validate.py --json <text_file>     # machine-readable output
  echo "..." | python hebrew_validate.py --stdin
  python hebrew_validate.py --help

Install model dependencies (optional):
  pip install transformers torch sentencepiece

The DictaBERT model is fetched from HuggingFace on first run (~800MB).
License: model is CC BY 4.0; this script is MIT (matches the skill).
"""

import argparse
import json
import re
import sys
from typing import Iterable

# ---- Regex-based rule catalog ------------------------------------------------

# Each rule: (id, category, pattern, severity, message, fix_hint)
RULES = [
    # CATEGORY A — Morphology
    (
        "A1", "morphology",
        r"[א-ת]+ינג(?=\s|[\.\,\!\?]|$)",
        "error",
        "Hebrew verb with -ing suffix detected. Hebrew has no -ing inflection.",
        "Use pi'el present (מ-) form: 'דיפלוי-ing' → 'מדיפלוי'.",
    ),
    (
        "A2", "morphology",
        r"לעשות\s+(קומיט|פוש|דיפלוי|מרג'|דיבג|שיפ|ריוויו|ריפקטור)",
        "warning",
        "Periphrastic 'לעשות X' form is dated when a pi'el verb exists.",
        "Use the pi'el infinitive directly: לעשות קומיט → לקומיט.",
    ),

    # CATEGORY D — Prepositions
    (
        "D1", "preposition",
        r"(?<![א-ת\-])([בלמכש])([A-Z][A-Za-z0-9]{0,})",
        "error",
        "Hebrew prefix attached to English-script noun without hyphen.",
        "Insert hyphen: בMCP → ב-MCP. Rule applies for ב, ל, מ, כ, ש before capital-letter English.",
    ),
    (
        "D2", "preposition",
        r"\b([בלמכ])-([א-ת])",
        "info",
        "Hyphen used with full-Hebrew loanword (only required for English-script).",
        "Verify: ב-פיצ'ר → likely should be בפיצ'ר. Only English-script needs the hyphen.",
    ),

    # CATEGORY E — Definite article
    (
        "E1", "definite-article",
        # Match noun NOT starting with ה (so we don't false-positive on already-articled forms)
        # followed by demonstrative
        r"(?<![א-ת])(?!ה)([א-ת]{3,})\s+(הזה|הזאת|הזו|הזאתי|אלה|אלו)\b",
        "warning",
        "Possible missing definite article ה before demonstrative.",
        "Add ה- to the preceding noun: 'הנחה הזאת' → 'ההנחה הזאת'.",
    ),
    (
        "E2", "definite-article",
        # Only match explicitly-doubled article: ה-ה or two consecutive ה- prefixes
        r"\bה-ה[א-ת]",
        "error",
        "Doubled definite article ה-ה detected.",
        "Use single definite article only.",
    ),

    # CATEGORY G — Anglicism / calque
    (
        "G1", "anglicism",
        r"אני\s+הולך\s+ל[א-ת]+",
        "warning",
        "English calque 'I am going to' — use Hebrew future tense instead.",
        "אני הולך לטעון → אני אטען.",
    ),
    (
        "G2", "anglicism",
        r"בערך\s*\d",
        "warning",
        "'בערך + number' is colloquial; tech writing uses prefix כ- for approximation.",
        "לפני בערך 18 חודשים → לפני כ-18 חודשים.",
    ),
    (
        "G4", "anglicism",
        r"(?:^|[\s\.\,\!\?])(אז|כאילו|בעצם|למעשה|פשוט)(?=\s)",
        "info",
        "Filler word detected. Acceptable only in slack/standup register.",
        "Remove אז / כאילו / בעצם / למעשה / פשוט unless slack register.",
    ),

    # CATEGORY H — Spelling
    (
        "H1", "spelling",
        r"\bסטיקהולדר",
        "error",
        "Mis-spelling — double-vowel transliteration of 'stake' is required.",
        "סטיקהולדר → סטייקהולדר.",
    ),
    (
        "H2", "spelling",
        r"(?<![א-ת])(פיצר|מנגר)(?![א-ת])",
        "warning",
        "Missing gershayim on transliterated word with non-Hebrew sound.",
        "פיצר → פיצ'ר ; מנגר → מנג'ר.",
    ),

    # CATEGORY K — Numbers
    (
        "K4", "number-format",
        r"(?<![א-ת\-])ב(\d{4})\b",
        "warning",
        "Year prefixed with ב without hyphen.",
        "ב2026 → ב-2026.",
    ),

    # CATEGORY L — 2026 currency
    (
        "L1", "vocabulary-currency",
        r"הצ'אט.?ג'?י?פ?י?ט?י?\s*שלנו",
        "warning",
        "Dated 2022-era buzzword usage of ChatGPT as generic LLM.",
        "Use 'ה-LLM שלנו' / 'המודל שלנו' / specific model name.",
    ),
]


def check_regex_rules(text: str) -> list[dict]:
    """Run all regex rules over the text and return found issues."""
    issues = []
    for rule_id, category, pattern, severity, message, fix in RULES:
        for m in re.finditer(pattern, text):
            issues.append({
                "rule_id": rule_id,
                "category": category,
                "severity": severity,
                "position": m.start(),
                "match": m.group(0),
                "message": message,
                "fix_hint": fix,
                "line": text.count("\n", 0, m.start()) + 1,
            })
    return issues


# ---- DictaBERT model-based checks --------------------------------------------

def load_dictabert():
    """Load DictaBERT-parse. Returns (tokenizer, model) or raises."""
    from transformers import AutoTokenizer, AutoModel
    tokenizer = AutoTokenizer.from_pretrained(
        "dicta-il/dictabert-parse", trust_remote_code=True
    )
    model = AutoModel.from_pretrained(
        "dicta-il/dictabert-parse", trust_remote_code=True
    )
    model.eval()
    return tokenizer, model


def check_model_rules(text: str, tokenizer, model) -> list[dict]:
    """Run DictaBERT-based checks on the text. Returns issues."""
    issues = []
    # Split into sentences (heuristic: period / newline / question)
    sentences = [s.strip() for s in re.split(r"[\.\!\?]\s+|\n", text) if s.strip()]
    if not sentences:
        return issues

    try:
        results = model.predict(sentences, tokenizer, output_style="json")
    except Exception as e:
        return [{
            "rule_id": "MODEL-ERROR",
            "category": "model-runtime",
            "severity": "info",
            "message": f"DictaBERT parse failed: {e}",
            "fix_hint": "Falling back to regex-only checks.",
            "match": "",
            "position": 0,
            "line": 0,
        }]

    for sent_idx, sent_result in enumerate(results):
        tokens = sent_result.get("tokens", [])
        sentence_text = sent_result.get("text", "")

        # Rule B1/B2: gender agreement noun-adjective (look for nsubj or det+noun pairs)
        for i, tok in enumerate(tokens):
            morph = tok.get("morph") or {}
            feats = morph.get("feats") or {}
            syntax = tok.get("syntax") or {}

            # Smikhut detection
            if feats.get("Definite") == "Cons":
                # This is a construct (smikhut head)
                # Check that the next token is an absolute noun (the chain member)
                if i + 1 < len(tokens):
                    next_tok = tokens[i + 1]
                    next_morph = next_tok.get("morph") or {}
                    next_pos = next_morph.get("pos")
                    if next_pos == "NOUN":
                        # Verify the chain member has correct definiteness
                        # Skip: this requires more semantic analysis
                        pass

            # Check: subject-verb gender/number agreement
            dep_func = syntax.get("dep_func")
            if dep_func == "nsubj":
                head_idx = syntax.get("dep_head_idx")
                if head_idx is not None and 0 <= head_idx < len(tokens):
                    head_tok = tokens[head_idx]
                    head_morph = head_tok.get("morph") or {}
                    head_feats = head_morph.get("feats") or {}
                    head_pos = head_morph.get("pos", "")

                    if head_pos == "VERB":
                        # Compare subject's gender/number with verb's
                        subj_gender = feats.get("Gender")
                        verb_gender = head_feats.get("Gender")
                        subj_number = feats.get("Number")
                        verb_number = head_feats.get("Number")

                        if subj_gender and verb_gender and subj_gender != verb_gender:
                            issues.append({
                                "rule_id": "B2",
                                "category": "agreement",
                                "severity": "error",
                                "position": 0,
                                "match": f"{tok.get('token', '')} ... {head_tok.get('token', '')}",
                                "message": f"Gender agreement mismatch: subject={subj_gender}, verb={verb_gender}",
                                "fix_hint": "Match verb gender to subject's grammatical gender.",
                                "line": sent_idx + 1,
                            })

                        if subj_number and verb_number and subj_number != verb_number:
                            issues.append({
                                "rule_id": "B3",
                                "category": "agreement",
                                "severity": "error",
                                "position": 0,
                                "match": f"{tok.get('token', '')} ... {head_tok.get('token', '')}",
                                "message": f"Number agreement mismatch: subject={subj_number}, verb={verb_number}",
                                "fix_hint": "Match verb number to subject (singular/plural).",
                                "line": sent_idx + 1,
                            })

    return issues


# ---- Reporting ---------------------------------------------------------------

def format_text_report(issues: list[dict], text: str) -> str:
    """Human-readable report."""
    if not issues:
        return "✓ No issues found. The text passes all enabled checks."

    by_severity = {"error": [], "warning": [], "info": []}
    for issue in issues:
        by_severity.setdefault(issue.get("severity", "info"), []).append(issue)

    lines = []
    lines.append(f"Found {len(issues)} issue(s):")
    lines.append(f"  - {len(by_severity['error'])} error(s)")
    lines.append(f"  - {len(by_severity['warning'])} warning(s)")
    lines.append(f"  - {len(by_severity['info'])} info note(s)")
    lines.append("")

    for severity in ("error", "warning", "info"):
        if not by_severity[severity]:
            continue
        lines.append(f"=== {severity.upper()} ===")
        for issue in by_severity[severity]:
            lines.append(
                f"[{issue['rule_id']}] {issue['category']} (line {issue.get('line', '?')})"
            )
            if issue.get("match"):
                lines.append(f"  Matched: \"{issue['match']}\"")
            lines.append(f"  {issue['message']}")
            lines.append(f"  Fix: {issue['fix_hint']}")
            lines.append("")
    return "\n".join(lines)


def format_json_report(issues: list[dict]) -> str:
    """Machine-readable JSON report."""
    return json.dumps(
        {
            "issue_count": len(issues),
            "by_severity": {
                "error": sum(1 for i in issues if i.get("severity") == "error"),
                "warning": sum(1 for i in issues if i.get("severity") == "warning"),
                "info": sum(1 for i in issues if i.get("severity") == "info"),
            },
            "issues": issues,
        },
        ensure_ascii=False,
        indent=2,
    )


# ---- CLI ---------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Validate Hebrew text per Ah Sheli Gibor rules.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("file", nargs="?", help="Path to text file (Hebrew, UTF-8). Omit with --stdin.")
    parser.add_argument("--no-model", action="store_true", help="Skip DictaBERT; regex-only.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of text.")
    parser.add_argument("--stdin", action="store_true", help="Read text from stdin.")
    args = parser.parse_args()

    # Get input text
    if args.stdin:
        text = sys.stdin.read()
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        parser.error("provide a file path or use --stdin")

    if not text.strip():
        print("Empty input. Nothing to check.", file=sys.stderr)
        sys.exit(1)

    # Run regex checks
    issues = check_regex_rules(text)

    # Optionally run model-based checks
    if not args.no_model:
        try:
            tokenizer, model = load_dictabert()
            issues.extend(check_model_rules(text, tokenizer, model))
        except ImportError:
            print(
                "Note: 'transformers' not installed; skipping DictaBERT checks. "
                "Install with: pip install transformers torch",
                file=sys.stderr,
            )
        except Exception as e:
            print(
                f"Note: DictaBERT load failed ({e}); falling back to regex only.",
                file=sys.stderr,
            )

    # Output
    if args.json:
        print(format_json_report(issues))
    else:
        print(format_text_report(issues, text))

    # Exit code reflects severity
    severities = {i.get("severity") for i in issues}
    if "error" in severities:
        sys.exit(2)
    elif "warning" in severities:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
