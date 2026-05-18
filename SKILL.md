---
name: ah-sheli-gibor
description: "Rewrite any text into authentic 2025-era Israeli tech Hebrew (Tel Aviv startup register) with correct binyan/gender/smikhut grammar and register-aware style (slack, technical-blog, linkedin, investor-pitch, pr-rfc). Use when the user asks to rewrite in Israeli tech Hebrew, translate to startup-nation Hebrew, make text sound like a Tel Aviv engineer wrote it, or supplies an English or formal-Hebrew article and wants the Israeli tech register. The skill is rewriting-first — it comprehends source content and reconstructs it in the target register, not a word-by-word translation. Do NOT use for general Hebrew translation (use DeepL or DictaLM), formal Academy-of-Hebrew documents, RTL CSS work (use hebrew-rtl-best-practices), Hebrew document generation (use hebrew-document-generator), or non-tech content (use hebrew-content-writer)."
license: MIT
allowed-tools: ''
compatibility: Works with Claude, Claude Code, Cursor. Optimized for Claude Sonnet 4.6+ and Claude Opus 4.7. Hebrew RTL rendering depends on the host environment.
---

# Ah Sheli Gibor — Israeli Tech Hebrew Rewriting Skill

> "אח שלי גיבור" — the affectionate startup-nation address. This skill rewrites text into the way an Israeli tech professional would actually write it in 2025.

## What this skill does

Receives input text (any Hebrew or English: article, blog post, spec, email, pitch, LinkedIn post, Slack message) and produces a **fully rewritten version in authentic 2025-era Israeli tech Hebrew**. The output must pass the native-speaker test: an Israeli engineer at Monday, Wix, or Mobileye should read it and think "כן, זה נשמע נכון."

This is **rewriting, not translation**. The skill comprehends the source argument, then reconstructs it in the target register from the inside out.

## When to invoke

Trigger phrases the skill responds to:
- "rewrite in Israeli tech Hebrew"
- "make this sound like a Tel Aviv engineer"
- "startup-nation Hebrew version"
- "Israeli LinkedIn voice"
- "Hebrew slack/standup version"
- Any input text with an implicit ask for the Israeli tech register

If the user supplies content without specifying a register and the register materially changes the output, **ask once** which register: slack / technical-blog / linkedin / investor-pitch / pr-rfc. Otherwise proceed.

## When NOT to use this skill

- General Hebrew translation → use DeepL or DictaLM 3.0
- Formal Academy-of-Hebrew documents → use `hebrew-content-writer`
- Hebrew RTL CSS or layout → use `hebrew-rtl-best-practices`
- Hebrew PDF/DOCX/PPTX generation → use `hebrew-document-generator`
- Niqud/vowelization → use Dicta Nakdan API
- Non-tech content (legal, medical, literary) → use `hebrew-content-writer`

## Operating protocol — 5 steps

Execute these in order. Do not skip steps.

### STEP 1 — COMPREHEND

Read the input fully. Identify:
- Core topic and argument
- Technical domain (infra / product / management / AI/ML / security / data / mobile)
- Source register (formal article / informal post / technical doc / pitch / chat)
- Key terms that have Israeli tech jargon equivalents in the corpus

Do not begin writing until you understand the full argument.

### STEP 2 — MAP TERMS

For each significant term, apply this **priority cascade**:

1. **2025 corpus match** (`corpus/jargon.json`) — established Israeli tech jargon term. Use it.
2. **Academy of Hebrew Language approved term** — use in formal register (investor-pitch, pr-rfc); use the jargon in informal register (slack, linkedin, technical-blog).
3. **Construct an anglicized loanword via binyan pi'el rules** (`references/grammar_layer.md` §1) — only if (1) and (2) yield nothing and the English term is genuinely missing from Hebrew.
4. **Calque (loan translation)** — only if the result sounds natural to a native speaker. Otherwise prefer the loanword.

Default rule: **prefer the established anglicized loanword over invented Hebrew** when that loanword is documented in the 2025 corpus.

### STEP 3 — SET REGISTER

Confirm target register. If ambiguous, ask once. Register affects:

| Register | Sentence length | Ellipsis | Jargon density | Grammar style |
|---|---|---|---|---|
| **slack / standup** | very short | OK to drop subject | high, all anglicized | elliptical, verb-first |
| **technical-blog** | medium-long | full sentences | medium, contextualized | mix of jargon + standard |
| **linkedin** | medium | personal voice | medium, story-driven | direct address, "אני"/"אנחנו" |
| **investor-pitch** | medium-formal | full sentences | controlled, English in parens where helpful | formal Hebrew frame |
| **pr-rfc** | precise, short | full sentences | minimal jargon | near-formal, precision-first |

Worked examples per register live in `references/grammar_layer.md` §5.

### STEP 4 — WRITE AND GRAMMAR-CHECK

Write the full rewritten text. Then verify every clause:

- **Every anglicized verb** → correct binyan (pi'el default; hif'il exceptions documented), correct tense, correct person/gender agreement (`references/grammar_layer.md` §1)
- **Every loanword noun** → correct gender (default masculine; documented exceptions), correct plural (almost always -ים even for content-feminine words) (`references/grammar_layer.md` §2)
- **Every compound noun** → smikhut (סמיכות) if appropriate, or analytical "X של Y" — never both (`references/grammar_layer.md` §3)
- **Every preposition + loanword** → ב/ל/מ + hyphen for English-script terms (ב-MCP, not בMCP); native Hebrew prefix-binding for Hebrew-script loanwords (`references/grammar_layer.md` §4)
- **Every definite-article construction** → correct ה placement after demonstratives/possessives (ההנחה הזאת, not הנחה הזאת)
- **Every partitive** → verb agrees with the partitive head, not the implied plural (חלקכם חתם, not חלקכם חתמתם)
- **"את" marker** → present before definite direct objects in scripted/precise text

Fix every error before continuing.

### STEP 5 — AUTHENTICITY REVIEW

Read the output as if you are a 2025 Israeli engineer at Monday/Wix/Mobileye. Apply these checks:

- Does any phrase sound like a translation rather than original Hebrew thought? Flag and rewrite.
- Is there jargon overuse — places where plain Hebrew would be more natural? Flag and replace.
- Are filler words (אז, כאילו, פשוט, למעשה, בעצם) absent? Spoken Hebrew tolerates them; written tech Hebrew does not.
- Does the rhythm match the target register? Slack should be punchy; technical-blog should breathe.
- Are anti-patterns absent? Cross-check against `references/anti_patterns.md`.

Rewrite any failing sentence. Output the final version only.

## The corpus

The 2025 Israeli tech Hebrew vocabulary lives in `corpus/jargon.json`. Each entry has:
- Hebrew term + romanization + literal English source
- Full grammar: binyan, gender, plural, conjugation, smikhut form
- Register tags (which registers it's appropriate for)
- Example sentence + standard-Hebrew equivalent + cultural note
- Source provenance (URL + date) + confidence rating

**2025-only source rule:** Web-sourced entries must trace to a URL dated January 2025 or later. Pre-2025 jargon decays — Israeli tech language evolves fast, especially in the AI/ML layer (RAG, MCP, אגנטי AI, פיין-טיון). Local-bootstrapped entries (from your own materials) carry explicit provenance to those local files.

See `references/sources.md` for the full source registry.

## Quick grammar reference

For full rules see `references/grammar_layer.md`. Most-used shortcuts:

**Pi'el conjugation (anglicized tech verbs):**
- לדיפלוי → מדיפלוי / דיפלוי / אדיפלוי
- לקומיט → מקומיט / קומיט / אקומיט
- לפוש → מפוש / פוש / אפוש
- למרג' → ממרג' / מרג' / אמרג'
- לשיפ → משיפ / שיפ / אשיפ
- לריוויו → מריווי / ריווה / אריווה (variant: מריוויו / ריוויו / אריוויו)
- לדיבג → מדבג / דיבג / אדבג
- לריפקטור → מריפקטר / ריפקטר / אריפקטר
- לסקייל → מסקייל / סקייל / אסקייל
- לפיין-טיון → מפיין-טיון / פיין-טיון / אפיין-טיון
- לאמבד → מאמבד / אמבד / אאמבד

**Noun gender (masculine unless noted):**
- פיצ'ר (ז') • באג (ז') • ספרינט (ז') • דשבורד (ז') • פייפליין (ז') • מודל (ז') • פרומפט (ז') • טיקט (ז') • רילייס (ז') • דיפלוימנט (ז')
- Exceptions (feminine): גרסה (נ') • מערכת (נ') • ארכיטקטורה (נ') • תשתית (נ')

**Plural:** almost universally `-ים` regardless of source-language gender (פיצ'רים, באגים, דשבורדים, מודלים, פרומפטים).

## Anti-patterns — never produce these

See `references/anti_patterns.md` for the full table. Top offenders:

| ❌ Wrong | ✅ Correct | Why |
|---|---|---|
| עשינו דפלויאינג של הפיצ'ר | דיפלוינו את הפיצ'ר | -ing suffix is not Hebrew morphology |
| לעשות קומיט | לקומיט | Periphrastic form is dated; pi'el verb form is current 2025 usage |
| הסטיקהולדרים | הסטייקהולדרים | Double vowels preserved in modern transliteration |
| המנהל של הפרודקט | מנהל המוצר *or* ה-Product Manager | Hybrid construct-with-של is broken; use smikhut or full English |
| בMCP | ב-MCP | Hebrew prefix attaches to English-script term with hyphen |
| פיצ'רות | פיצ'רים | Loanword plural is -ים regardless of source gender |

## Test cases

Five v0 test cases live in `tests/test_cases.md`, one per register. Pass criteria: ≥3/5 expected jargon terms used correctly and 0 grammar errors. Results logged in `tests/test_results_v0.md`.

## Related skills (do not duplicate)

- `hebrew-content-writer` — general Hebrew register, smichut, et marker, ktiv maleh, gender — **invoke for non-tech content**
- `hebrew-rtl-best-practices` — CSS logical properties, dir attributes, bidi
- `hebrew-document-generator` — Hebrew PDF/DOCX/PPTX
- `hebrew-i18n` — date/currency formatting, plural forms, bidi mixed content

This skill is the **tech-jargon overlay** on top of `hebrew-content-writer`. Where the two conflict on grammar fundamentals, `hebrew-content-writer` wins.

## Versioning

v0.1.0 — scaffold + ~30 seed corpus entries + 5 test cases + full methodology.
Roadmap: v0.2.0 expands corpus to 200 2025-dated entries and tests to 20.
