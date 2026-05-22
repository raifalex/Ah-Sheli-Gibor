#!/usr/bin/env python3
"""
Ah Sheli Gibor — Hebrew Analysis Toolkit (v0.4.0)

Unified CLI for invoking Hebrew NLP models on demand. Each subcommand
lazy-loads its model — you only pay the download cost for the models
you actually use.

Quickstart:

    # Install dependencies (one-time)
    pip install -r scripts/requirements.txt

    # Morphological analysis (DictaBERT-morph)
    python scripts/hebrew_toolkit.py morph "ההנחה הזאת הייתה בטוחה במשך 15 שנה."

    # Syntactic parse (DictaBERT-parse)
    python scripts/hebrew_toolkit.py parse "החברה השיגה PMF ברבעון השלישי."

    # Named-entity recognition (DictaBERT-NER)
    python scripts/hebrew_toolkit.py ner "אלכס רייף הציג ב-TechGym ב-2026."

    # Sentiment (heBERT_sentiment_analysis)
    python scripts/hebrew_toolkit.py sentiment "הפיצ'ר החדש מעולה."

    # Emotion across 8 categories (hebEMO)
    python scripts/hebrew_toolkit.py emotion "אני מאוכזב מההחלטה."

    # Diacritization (Dicta Nakdan API — requires network)
    python scripts/hebrew_toolkit.py nakdan "שלום עולם"

    # Translation (Helsinki-NLP opus-mt)
    python scripts/hebrew_toolkit.py translate "Hello world" --to he
    python scripts/hebrew_toolkit.py translate "שלום עולם" --to en

    # Summarization (het5_summarization)
    python scripts/hebrew_toolkit.py summarize @article.txt

    # Source recommendation (decision tree from source_selection.md)
    python scripts/hebrew_toolkit.py recommend --task validate-grammar --output pitch

    # Rubric scoring (LLM-graded — relevance/coherence/consistency/fluency)
    python scripts/hebrew_toolkit.py rubric output.txt source.txt

License: MIT (this script). Underlying models have varying licenses;
verify each model card before commercial use.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from typing import Any

# Lazy imports — only loaded when needed
_loaded_models: dict[str, Any] = {}


def _lazy_load(model_id: str, loader_fn):
    """Cache loaded models in process memory."""
    if model_id not in _loaded_models:
        _loaded_models[model_id] = loader_fn()
    return _loaded_models[model_id]


def _print_json(data: Any) -> None:
    """Print JSON with Hebrew-safe encoding."""
    print(json.dumps(data, ensure_ascii=False, indent=2))


def _read_input(text_or_path: str) -> str:
    """If input starts with @, treat as file path; else use as literal text."""
    if text_or_path.startswith("@"):
        with open(text_or_path[1:], "r", encoding="utf-8") as f:
            return f.read()
    return text_or_path


# ---------------------------------------------------------------------------
# Subcommand: morph (DictaBERT-morph)
# ---------------------------------------------------------------------------

def cmd_morph(args):
    text = _read_input(args.text)

    def loader():
        from transformers import AutoTokenizer, AutoModel
        tok = AutoTokenizer.from_pretrained("dicta-il/dictabert-morph", trust_remote_code=True)
        mdl = AutoModel.from_pretrained("dicta-il/dictabert-morph", trust_remote_code=True)
        mdl.eval()
        return tok, mdl

    try:
        tok, mdl = _lazy_load("morph", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    result = mdl.predict([text], tok)
    _print_json({"task": "morph", "text": text, "result": result})


# ---------------------------------------------------------------------------
# Subcommand: parse (DictaBERT-parse) — full morph+syntax
# ---------------------------------------------------------------------------

def cmd_parse(args):
    text = _read_input(args.text)

    def loader():
        from transformers import AutoTokenizer, AutoModel
        tok = AutoTokenizer.from_pretrained("dicta-il/dictabert-parse", trust_remote_code=True)
        mdl = AutoModel.from_pretrained("dicta-il/dictabert-parse", trust_remote_code=True)
        mdl.eval()
        return tok, mdl

    try:
        tok, mdl = _lazy_load("parse", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    result = mdl.predict([text], tok, output_style="json")
    _print_json({"task": "parse", "text": text, "result": result})


# ---------------------------------------------------------------------------
# Subcommand: ner (DictaBERT-NER)
# ---------------------------------------------------------------------------

def cmd_ner(args):
    text = _read_input(args.text)

    def loader():
        from transformers import pipeline
        return pipeline("ner", model="dicta-il/dictabert-ner", aggregation_strategy="simple")

    try:
        nlp = _lazy_load("ner", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    entities = nlp(text)
    # Convert numpy floats for JSON
    for e in entities:
        if "score" in e:
            e["score"] = float(e["score"])
        if "start" in e:
            e["start"] = int(e["start"])
        if "end" in e:
            e["end"] = int(e["end"])
    _print_json({"task": "ner", "text": text, "entities": entities})


# ---------------------------------------------------------------------------
# Subcommand: sentiment (heBERT_sentiment_analysis)
# ---------------------------------------------------------------------------

def cmd_sentiment(args):
    text = _read_input(args.text)

    def loader():
        from transformers import pipeline
        return pipeline("sentiment-analysis", model="avichr/heBERT_sentiment_analysis", tokenizer="avichr/heBERT_sentiment_analysis")

    try:
        nlp = _lazy_load("sentiment", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    result = nlp(text)
    for r in result:
        if "score" in r:
            r["score"] = float(r["score"])
    _print_json({"task": "sentiment", "text": text, "result": result})


# ---------------------------------------------------------------------------
# Subcommand: emotion (hebEMO across 8 categories)
# ---------------------------------------------------------------------------

# hebEMO is published as 8 separate fine-tunes — one per emotion
HEBEMO_MODELS = {
    "anger": "avichr/hebEMO_anger",
    "fear": "avichr/hebEMO_fear",
    "joy": "avichr/hebEMO_joy",
    "sadness": "avichr/hebEMO_sadness",
    "anticipation": "avichr/hebEMO_anticipation",
    "surprise": "avichr/hebEMO_surprise",
    "trust": "avichr/hebEMO_trust",
    "disgust": "avichr/hebEMO_disgust",
}

HEBEMO_HE = {
    "anger": "כעס",
    "fear": "פחד",
    "joy": "שמחה",
    "sadness": "עצב",
    "anticipation": "ציפייה",
    "surprise": "הפתעה",
    "trust": "אמון",
    "disgust": "גועל",
}


def cmd_emotion(args):
    text = _read_input(args.text)

    try:
        from transformers import pipeline
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    scores = {}
    for emotion_key, model_id in HEBEMO_MODELS.items():
        try:
            pipe = _lazy_load(f"emotion_{emotion_key}",
                              lambda mid=model_id: pipeline("text-classification", model=mid))
            result = pipe(text)
            top = result[0]
            scores[emotion_key] = {
                "hebrew": HEBEMO_HE[emotion_key],
                "label": top.get("label"),
                "score": float(top.get("score", 0.0)),
            }
        except Exception as e:
            scores[emotion_key] = {"hebrew": HEBEMO_HE[emotion_key], "error": str(e)}

    _print_json({"task": "emotion", "text": text, "scores": scores})


# ---------------------------------------------------------------------------
# Subcommand: legal (Legal-heBERT)
# ---------------------------------------------------------------------------

def cmd_legal(args):
    text = _read_input(args.text)

    def loader():
        from transformers import AutoTokenizer, AutoModelForMaskedLM
        tok = AutoTokenizer.from_pretrained("avichr/Legal-heBERT")
        mdl = AutoModelForMaskedLM.from_pretrained("avichr/Legal-heBERT")
        mdl.eval()
        return tok, mdl

    try:
        tok, mdl = _lazy_load("legal", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    # Legal-heBERT is a masked-LM; useful for legal terminology completion
    # and for embedding legal Hebrew. Here we return embedding stats.
    import torch
    with torch.no_grad():
        inputs = tok(text, return_tensors="pt", truncation=True, max_length=512)
        outputs = mdl(**inputs, output_hidden_states=True)
        # Get last hidden state mean as a sentence-level embedding
        hidden = outputs.hidden_states[-1]
        embedding = hidden.mean(dim=1).squeeze().tolist()

    _print_json({
        "task": "legal",
        "text": text,
        "embedding_dim": len(embedding),
        "embedding_sample": embedding[:8],
        "note": "Legal-heBERT loaded. Use the full embedding for legal-text similarity / classification tasks. For legal NER or term extraction, fine-tune on a legal NER dataset.",
    })


# ---------------------------------------------------------------------------
# Subcommand: medical (hebrew_medical_ner_v5)
# ---------------------------------------------------------------------------

def cmd_medical(args):
    text = _read_input(args.text)

    def loader():
        from transformers import pipeline
        return pipeline("ner", model="cp500/hebrew_medical_ner_v5", aggregation_strategy="simple")

    try:
        nlp = _lazy_load("medical_ner", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    entities = nlp(text)
    for e in entities:
        if "score" in e:
            e["score"] = float(e["score"])
        if "start" in e:
            e["start"] = int(e["start"])
        if "end" in e:
            e["end"] = int(e["end"])
    _print_json({"task": "medical", "text": text, "medical_entities": entities})


# ---------------------------------------------------------------------------
# Subcommand: metaphor (hebert-finetuned-hebrew-metaphor)
# ---------------------------------------------------------------------------

def cmd_metaphor(args):
    text = _read_input(args.text)

    def loader():
        from transformers import pipeline
        return pipeline("text-classification", model="tdklab/hebert-finetuned-hebrew-metaphor")

    try:
        nlp = _lazy_load("metaphor", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    result = nlp(text)
    for r in result:
        if "score" in r:
            r["score"] = float(r["score"])
    _print_json({"task": "metaphor", "text": text, "result": result})


# ---------------------------------------------------------------------------
# Subcommand: offensive (hebrew-offensive-detection)
# ---------------------------------------------------------------------------

def cmd_offensive(args):
    text = _read_input(args.text)

    def loader():
        from transformers import pipeline
        return pipeline("text-classification", model="KevynKrancenblum/hebrew-offensive-detection")

    try:
        nlp = _lazy_load("offensive", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    result = nlp(text)
    for r in result:
        if "score" in r:
            r["score"] = float(r["score"])
    _print_json({"task": "offensive", "text": text, "result": result})


# ---------------------------------------------------------------------------
# Subcommand: nakdan (Dicta Nakdan diacritization via HTTP API)
# ---------------------------------------------------------------------------

def cmd_nakdan(args):
    text = _read_input(args.text)

    # Dicta Nakdan API endpoint (publicly accessible at time of writing).
    # API contract is informally exposed; verify nakdan.dicta.org.il/api for
    # current schema before production use.
    url = "https://nakdan.dicta.org.il/api"
    payload = {
        "data": text,
        "genre": "modern",  # alternatives: "rabbinic", "biblical"
        "useTokenization": True,
        "addMorphology": False,
        "addNikud": True,
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "ah-sheli-gibor/0.4.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
            parsed = json.loads(data)
            _print_json({"task": "nakdan", "text": text, "result": parsed})
    except urllib.error.URLError as e:
        _print_json({
            "task": "nakdan",
            "text": text,
            "error": str(e),
            "note": "Nakdan API call failed. Verify network access and API schema at nakdan.dicta.org.il/api. Fallback: use dictabert-large-char-menaked locally.",
        })
        sys.exit(1)


# ---------------------------------------------------------------------------
# Subcommand: translate (Helsinki-NLP opus-mt)
# ---------------------------------------------------------------------------

def cmd_translate(args):
    text = _read_input(args.text)
    target = args.to.lower()

    if target == "he":
        model_id = "Helsinki-NLP/opus-mt-en-he"
    elif target == "en":
        model_id = "Helsinki-NLP/opus-mt-tc-big-he-en"
    else:
        print(f"Error: --to must be 'he' or 'en' (got {target!r})", file=sys.stderr)
        sys.exit(2)

    def loader():
        from transformers import pipeline
        return pipeline("translation", model=model_id)

    try:
        nlp = _lazy_load(f"translate_{target}", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    result = nlp(text)
    _print_json({"task": "translate", "source_text": text, "target": target, "translation": result[0]["translation_text"]})


# ---------------------------------------------------------------------------
# Subcommand: summarize (het5_summarization)
# ---------------------------------------------------------------------------

def cmd_summarize(args):
    text = _read_input(args.text)

    def loader():
        from transformers import pipeline
        return pipeline("summarization", model="imvladikon/het5_summarization")

    try:
        nlp = _lazy_load("summarize", loader)
    except ImportError:
        print("Error: transformers not installed. Run: pip install -r scripts/requirements.txt", file=sys.stderr)
        sys.exit(2)

    result = nlp(text, max_length=args.max_length, min_length=args.min_length)
    _print_json({"task": "summarize", "text_length": len(text), "summary": result[0]["summary_text"]})


# ---------------------------------------------------------------------------
# Subcommand: recommend (source-selection logic)
# ---------------------------------------------------------------------------

# Lightweight mirror of source_selection.md — for full text see that file.
RECOMMENDATIONS = {
    ("validate-grammar", None, None): {"primary": "dictabert-parse", "fallback": "hspell", "reference": "academy-of-hebrew-language"},
    ("validate-grammar", "pitch", None): {"primary": "dictabert-parse", "fallback": "dictabert-large-parse", "reference": "academy-of-hebrew-language"},
    ("validate-grammar", "talking-cards", None): {"primary": "dictabert-parse", "fallback": "dictabert-large-parse", "reference": "academy-of-hebrew-language", "note": "talking-cards require עקביות≥9 in rubric"},
    ("generate", None, None): {"primary": "claude-with-hebrew-prompt", "fallback": "dictalm-3.0-24b-thinking", "reference": "corpus/jargon.json"},
    ("generate", None, "legal-technical"): {"primary": "claude-with-legal-prompt", "validator": "legal-hebert", "deterministic": True, "note": "Use temperature=0 for contract reliability"},
    ("generate", None, "medical"): {"primary": "claude-with-medical-prompt", "validator": "hebrew-medical-ner-v5"},
    ("generate", None, "biblical-rabbinic"): {"primary": "berel-3.0", "validator": "berel-3.0"},
    ("generate", None, "slang-cultural"): {"primary": "dictalm-3.0-24b-thinking", "validator": "hebert-finetuned-hebrew-metaphor", "note": "Include cultural explanation layer"},
    ("generate", None, "gender-emotional"): {"primary": "claude-with-emotion-prompt", "validator": "hebemo", "note": "Verify speaker gender consistency"},
    ("generate", None, "bilingual"): {"primary": "claude-bilingual-prompt", "validator": "neodictabert-bilingual"},
    ("generate", None, "creative-lyrics"): {"primary": "gemma-3-4b-hebrew-lyrics", "validator": "hebert-finetuned-hebrew-metaphor"},
    ("translate", None, None): {"primary": "deepl-api", "fallback": "opus-mt-en-he OR opus-mt-tc-big-he-en"},
    ("asr", None, None): {"primary": "whisper-large-v3-turbo-ct2", "fallback": "wav2vec2-xls-r-1b-hebrew"},
    ("tts", None, None): {"primary": "sims-7b + phonikud", "fallback": "hebtts"},
    ("diacritize", None, None): {"primary": "dicta-nakdan-api", "fallback": "dictabert-large-char-menaked"},
    ("summarize", None, None): {"primary": "het5_summarization", "fallback": "claude-with-hebrew-prompt"},
    ("ner", None, None): {"primary": "dictabert-ner", "fallback": "hebert-ner"},
    ("sentiment", None, None): {"primary": "hebert_sentiment_analysis", "fallback": "dictabert-sentiment"},
    ("emotion", None, None): {"primary": "hebemo", "fallback": "claude-emotion-prompt"},
    ("deploy", None, None): {"primary": "dictalm-2.0-instruct + tensorrt-llm + triton", "note": "see references/nvidia_tensorrt_optimization.md"},
}


def cmd_recommend(args):
    task = args.task
    output = args.output
    variation = args.variation

    # Try most specific match first
    keys_to_try = [
        (task, output, variation),
        (task, None, variation),
        (task, output, None),
        (task, None, None),
    ]
    for key in keys_to_try:
        if key in RECOMMENDATIONS:
            rec = dict(RECOMMENDATIONS[key])
            rec["matched_key"] = {"task": key[0], "output": key[1], "variation": key[2]}
            _print_json({"task": "recommend", "input": {"task": task, "output": output, "variation": variation}, "recommendation": rec})
            return

    _print_json({
        "task": "recommend",
        "input": {"task": task, "output": output, "variation": variation},
        "recommendation": None,
        "note": "No specific recommendation. See sources/source_selection.md for the full decision tree.",
    })


# ---------------------------------------------------------------------------
# Subcommand: rubric (4-axis LLM-graded scoring)
# ---------------------------------------------------------------------------

def cmd_rubric(args):
    """
    Outputs the rubric template that an LLM (Claude) should fill in.
    This script doesn't grade the rubric itself — it produces the
    structured template + source/output pair for Claude to evaluate.
    Pipe output to Claude API for actual scoring.
    """
    output_text = _read_input(args.output_file)
    source_text = _read_input(args.source_file) if args.source_file else ""

    template = {
        "task": "rubric",
        "instructions_he": """
דרג את הפלט הבא בארבע מידות, כל אחת על סולם 1-10:

1. רלוונטיות — איכות בחירת התוכן החשוב מתוך המקור
2. קוהרנטיות — האיכות הקולקטיבית של כל המשפטים
3. עקביות — ההתאמה העובדתית בין הסיכום למקור המסוכם
4. רהיטות — איכות הסיכום במונחים של דקדוק, איות, פיסוק, בחירת מילים, ומבנה משפט

לכל מידה, ספק:
- ציון מספרי (1-10)
- 1-2 משפטי הסבר
- המלצות לשיפור (אם הציון מתחת ל-8)

החזר את התשובה כ-JSON עם השדות: relevance, coherence, consistency, fluency, notes, recommendations.
""",
        "output_to_evaluate": output_text,
        "source": source_text or "(no source provided — score coherence/fluency only)",
        "scoring_methodology": "see references/output_evaluation_rubric.md",
    }
    _print_json(template)


# ---------------------------------------------------------------------------
# CLI dispatch
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Ah Sheli Gibor — Hebrew NLP toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    p = subparsers.add_parser("morph", help="Morphological analysis (DictaBERT-morph)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_morph)

    p = subparsers.add_parser("parse", help="Syntactic + morphological parse (DictaBERT-parse)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_parse)

    p = subparsers.add_parser("ner", help="Named-entity recognition (DictaBERT-NER)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_ner)

    p = subparsers.add_parser("sentiment", help="Sentiment analysis (heBERT_sentiment)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_sentiment)

    p = subparsers.add_parser("emotion", help="8-emotion scoring (hebEMO)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_emotion)

    p = subparsers.add_parser("legal", help="Legal Hebrew embeddings (Legal-heBERT)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_legal)

    p = subparsers.add_parser("medical", help="Medical entity recognition (hebrew_medical_ner_v5)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_medical)

    p = subparsers.add_parser("metaphor", help="Metaphor detection (hebert-finetuned-hebrew-metaphor)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_metaphor)

    p = subparsers.add_parser("offensive", help="Offensive-language detection (hebrew-offensive-detection)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_offensive)

    p = subparsers.add_parser("nakdan", help="Diacritization via Dicta Nakdan API (requires network)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.set_defaults(func=cmd_nakdan)

    p = subparsers.add_parser("translate", help="Translate via Helsinki-NLP opus-mt")
    p.add_argument("text", help="Text to translate (or @file)")
    p.add_argument("--to", required=True, choices=["he", "en"], help="Target language")
    p.set_defaults(func=cmd_translate)

    p = subparsers.add_parser("summarize", help="Hebrew summarization (het5_summarization)")
    p.add_argument("text", help="Hebrew text (or @file)")
    p.add_argument("--max-length", type=int, default=200, dest="max_length")
    p.add_argument("--min-length", type=int, default=50, dest="min_length")
    p.set_defaults(func=cmd_summarize)

    p = subparsers.add_parser("recommend", help="Source-selection recommendation per task")
    p.add_argument("--task", required=True, help="e.g., generate / validate-grammar / translate / ner / asr / tts / diacritize / summarize / deploy")
    p.add_argument("--output", help="e.g., pitch / speech / talking-cards / teleprompter / rewrite")
    p.add_argument("--variation", help="e.g., tech-formal / legal-technical / medical / biblical-rabbinic / gender-emotional / slang-cultural / bilingual / creative-lyrics")
    p.set_defaults(func=cmd_recommend)

    p = subparsers.add_parser("rubric", help="Generate 4-axis rubric template for LLM grading")
    p.add_argument("output_file", help="Path to output text (or @file or literal)")
    p.add_argument("source_file", nargs="?", help="Optional: path to source text for consistency-axis grading")
    p.set_defaults(func=cmd_rubric)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
