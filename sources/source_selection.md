# Source Selection — Decision Logic

This is the skill's STEP 4.5 reference: given a task + goal + variation mode, pick the right source from the catalog.

## How the skill uses this document

When the skill executes STEP 4.5 (between WRITE and VALIDATE), it reads the user's interview answers (output type, context, purpose, mood, goal, persona, variation mode) and consults this decision tree to choose:

1. Which LLM (if any) to consult for generation assistance
2. Which validator to invoke during STEP 5
3. Which authoritative reference to defer to for disputes
4. Whether any specialized domain models apply

The user can override the auto-selection by naming a source directly: "use Legal-heBERT" / "validate with DictaBERT-large-parse" / "skip model validation."

---

## Decision tree by task

### Task: Generate / rewrite Hebrew tech content

| Sub-task | Recommended primary | Fallback |
|---|---|---|
| Generate or rewrite (default — used by Claude itself) | Claude Opus 4.7 with Hebrew system prompt + `corpus/jargon.json` | DictaLM-3.0-24B-Thinking |
| Production-deployed Hebrew generation at scale | DictaLM-2.0-Instruct + NVIDIA TensorRT-LLM + Triton | DictaLM-3.0-Nemotron-12B-Instruct |
| Edge / on-device Hebrew generation | DictaLM-3.0-1.7B-Instruct | hebrew-mistral-7b-instruct-gguf |
| Apple Silicon (M-series Mac) | Hebrew-Gemma-11B-V2-mlx-4bit | DictaLM-3.0-1.7B-Instruct |
| Long-document Hebrew (>32K tokens) | Hebrew-Mistral-7B-200K | Claude 1M-context |
| Slang / idiom / cultural-nuance generation | DictaLM-3.0-24B-Thinking | Claude with Hebrew slang prompt |
| Hebrew lyrics / poetry / creative | gemma-3_4b_hebrew-lyrics-finetune | Claude with creative-Hebrew prompt |

### Task: Validate Hebrew grammar

| Sub-task | Recommended primary | Fallback |
|---|---|---|
| Morphological analysis (binyan, gender, plural) | `hebrew_toolkit.py morph` → DictaBERT-morph | dictabert-large-parse |
| Syntactic parsing (smikhut, agreement) | `hebrew_toolkit.py parse` → DictaBERT-parse | dictabert-large-parse |
| Word segmentation (prefix detection) | dictabert-seg | YAP |
| Lemmatization (find base form) | dictabert-lex | Morfix lookup |
| Spell check (Academy-compliant) | Hspell (CLI / Python) | Online tools (Rephrasely / Sapling) |
| Authoritative grammar rulings | Academy of the Hebrew Language | Morfix + Rav-Milim |
| Conjugation table lookup | Morfix | DictaBERT-morph output |
| Punctuation restoration | verbit/hebrew_punctuation | Manual |
| Diacritization (add nikud) | `hebrew_toolkit.py nakdan` → Dicta Nakdan API | dictabert-large-char-menaked locally |

### Task: Validate Hebrew semantics / content

| Sub-task | Recommended primary | Fallback |
|---|---|---|
| Sentiment (pos/neg/neu) | `hebrew_toolkit.py sentiment` → heBERT_sentiment | dictabert-sentiment |
| Emotion detection (8 categories) | `hebrew_toolkit.py emotion` → hebEMO | Claude with explicit emotion prompt |
| Named entity recognition | `hebrew_toolkit.py ner` → dictabert-ner | heBERT_NER |
| Metaphor / figurative language | `hebrew_toolkit.py metaphor` → hebert-finetuned-hebrew-metaphor | DictaLM-3.0-Thinking |
| Offensive language detection | `hebrew_toolkit.py offensive` → hebrew-offensive-detection | Offensive-Hebrew |
| Question-answering over Hebrew document | dictabert-heq | hebert_parashoot |

### Task: Domain-specific Hebrew

| Domain | Recommended primary | Fallback |
|---|---|---|
| Legal Hebrew | `hebrew_toolkit.py legal` → Legal-heBERT | DictaLM-3.0-Thinking + legal corpus |
| Medical Hebrew | `hebrew_toolkit.py medical` → hebrew_medical_ner_v5 | DictaLM-3.0-Thinking + medical glossary |
| Biblical / Rabbinic Hebrew | BEREL_3.0 | hebrew_bible_ai |
| Math education in Hebrew | hebrew-math-tutor-v1 | Claude with Hebrew system prompt |
| Hebrew → SQL | Llama-3.1-8b-Hebrew2SQL | Claude code-generation |
| Code generation with Hebrew comments | Claude / Cursor | DictaLM-3.0-24B-Thinking |

### Task: Translation

| Direction | Recommended primary | Fallback |
|---|---|---|
| EN → HE high-quality | DeepL API (paid) | `hebrew_toolkit.py translate --to he` → Helsinki-NLP opus-mt-en-he |
| HE → EN high-quality | DeepL API (paid) | `hebrew_toolkit.py translate --to en` → Helsinki-NLP opus-mt-tc-big-he-en |
| Bidirectional EN↔HE | english-hebrew-translation (T5) | DeepL |
| Cross-lingual summarization HE → EN | cross_summarization_he_en | DeepL + then summarize |

### Task: Speech (ASR / TTS)

| Sub-task | Recommended primary | Fallback |
|---|---|---|
| Hebrew speech → text | `hebrew_toolkit.py asr` → ivrit-ai/whisper-large-v3-turbo-ct2 | wav2vec2-xls-r-1b-hebrew |
| Multi-speaker transcription | whisper-large-v3-turbo-ct2 + pyannote-speaker-diarization-3.1 | Manual |
| Hebrew text → speech | SIMS-7B + phonikud | HebTTS |
| IPA phoneme extraction | whisper-heb-ipa | Manual phonemization |
| Prosody-aware Hebrew speech | StresSLM / WhiStress / PAST | Standard ASR |

### Task: Document processing

| Sub-task | Recommended primary | Fallback |
|---|---|---|
| OCR Hebrew handwriting | testing-trOCR-hebrew-handwritten | Manual transcription |
| Post-OCR correction | paleo-hebrew-mt5-post-ocr-processing | Manual review |
| Paleo-Hebrew / ancient text | paleo-hebrew-qwen3-vl-lora-post-ocr-processing | Specialist consultation |
| Hebrew summarization | `hebrew_toolkit.py summarize` → het5_summarization | Claude with Hebrew prompt |

### Task: Retrieval / RAG

| Sub-task | Recommended primary | Fallback |
|---|---|---|
| Hebrew sentence embeddings | sentence-transformers-alephbert | neodictabert-bilingual-embed |
| Bilingual HE-EN embeddings | neodictabert-bilingual-embed | Multilingual e5 |
| Long-context Hebrew encoding | LongHeRo | Hebrew-Mistral-7B-200K |

---

## Decision tree by variation mode

Each Hebrew variation mode comes with a default source bundle. The skill automatically applies these when the user picks a mode.

### Mode: Tech-formal (default)
**Sources bundle:**
- Generation: Claude with Hebrew system prompt + `corpus/jargon.json`
- Validation: DictaBERT-parse + Hspell
- Reference: Academy of the Hebrew Language + Morfix
- Currency check: `corpus/jargon.json` (2025+ tech terms)

### Mode: Legal-technical
**Sources bundle:**
- Generation: Claude + Legal-heBERT-aware prompt (deterministic output)
- Validation: Legal-heBERT for legal-specific terminology + DictaBERT-parse for grammar
- Reference: Academy + Israeli legal glossary
- **Output guarantee:** deterministic (temperature=0 if using LLM). Critical for contract reliability.

### Mode: Medical
**Sources bundle:**
- Generation: Claude + hebrew_medical_ner_v5-aware prompt
- Validation: hebrew_medical_ner_v5 (entity detection)
- Reference: Israeli Ministry of Health terminology + Academy

### Mode: Biblical / Rabbinic
**Sources bundle:**
- Generation: BEREL_3.0 / hebrew_bible_ai for source-text-aware completion
- Validation: BEREL_3.0
- Reference: Academy + classical Hebrew lexica

### Mode: Gender-emotional
**Sources bundle:**
- Generation: Claude with emotion-aware prompt + hebEMO scoring
- Validation: hebEMO (8 emotion categories) + sentiment cross-check
- Special: gendered phrasing audit (Hebrew has grammatical gender — verify the speaker's intended gender expression matches)

### Mode: Slang-cultural
**Sources bundle:**
- Generation: DictaLM-3.0-24B-Thinking (best for cultural nuance)
- Validation: hebert-finetuned-hebrew-metaphor (metaphor detection) + cultural-explanation layer
- Reference: israeli.md output style + Hebrew slang corpus
- Special: include cultural explanation alongside the slang — never use slang opaquely; explain when needed.

### Mode: Bilingual
**Sources bundle:**
- Generation: Claude with bilingual prompt
- Validation: neodictabert-bilingual + neodictabert-bilingual-embed for cross-lingual coherence
- Reference: Helsinki-NLP MT models + DeepL for back-translation check

### Mode: Creative-lyrics
**Sources bundle:**
- Generation: gemma-3_4b_hebrew-lyrics-finetune
- Validation: hebert-finetuned-hebrew-metaphor + Claude authenticity review
- Reference: Hebrew lyrics corpus

---

## Decision tree by user goal

The user's stated goal (from STEP 0 interview) further refines source selection:

| Goal | Source modifier |
|---|---|
| "Convince investors" | Generation: pitch register + Yoel persona. Validation: rubric weighting on רהיטות (fluency) and קוהרנטיות (coherence). |
| "Win a panel debate" | Talking-cards output type + Dana persona. Validation: rubric weighting on עקביות (consistency — every claim must trace to a source). |
| "Land emotional impact" | Speech / linkedin output + Shira or Noa persona. Add hebEMO scoring as STEP 5g secondary check. Rubric weighting on קוהרנטיות (coherence). |
| "Explain to junior engineers" | Technical-blog output + Itamar or Yoel persona. Lower jargon density; add cultural-explanation layer if slang appears. |
| "Memorial / ceremonial address" | Speech output + Shira persona. Add Dicta Nakdan diacritization for ceremonial Hebrew. |
| "Roast / entertain" | Gilad persona. Allow slang-cultural variation mode. |
| "Sign a contract / legal-binding" | Legal-technical variation mode. Deterministic output. Legal-heBERT validation. |
| "Clinical documentation" | Medical variation mode. hebrew_medical_ner_v5 validation. |
| "Religious content" | Biblical-rabbinic variation mode. BEREL_3.0 generation. |
| "Production deployment" | Add TensorRT-LLM reference (`references/nvidia_tensorrt_optimization.md`). |

---

## Decision tree by output-type validation requirements

Different output types have different validation priorities. The rubric thresholds vary:

| Output type | Priority axes (highest first) | Pass threshold |
|---|---|---|
| **Rewrite** | רהיטות (fluency) > רלוונטיות (relevance) > קוהרנטיות > עקביות | All ≥ 7 |
| **Pitch** | קוהרנטיות > רלוונטיות > עקביות > רהיטות | קוהרנטיות ≥ 8, others ≥ 7 |
| **Speech** | קוהרנטיות > רהיטות > רלוונטיות > עקביות | קוהרנטיות ≥ 8, רהיטות ≥ 8, others ≥ 7 |
| **Talking-cards** | עקביות > רהיטות > קוהרנטיות > רלוונטיות | עקביות ≥ 9 (facts must hold), others ≥ 7 |
| **Teleprompter** | רהיטות > עקביות > קוהרנטיות > רלוונטיות | רהיטות ≥ 9 (must scan at reading speed), others ≥ 7 |

Below threshold on any axis → automatic rewrite of the failing section.

---

## Override mechanism

The user can override any auto-selection:

```
"Use Legal-heBERT for validation."
"Don't use DictaBERT — methodology mode only."
"Skip the medical NER check."
"Use Claude only for grading the rubric — no other model."
"Force tech-formal mode regardless of context."
```

The skill confirms the override in STEP 0 and adjusts the source bundle accordingly.

---

## Programmatic source recommendation

For batch / pipeline use, the skill exposes `hebrew_toolkit.py recommend`:

```sh
python scripts/hebrew_toolkit.py recommend --task validate-grammar --output pitch --persona yoel
# Returns JSON: { "primary": "dictabert-parse", "fallback": "dictabert-large-parse", "reference": "academy-of-hebrew-language" }

python scripts/hebrew_toolkit.py recommend --task generate --variation legal
# Returns: { "primary": "claude + legal-hebert prompt", "validator": "legal-hebert", "deterministic": true }
```

This makes the decision tree machine-readable for CI / batch / RAG pipelines.

---

## Updating the decision tree

When new models enter the catalog (`hebrew_ai_models.json`), update this file with:
1. Which task the new model addresses
2. Whether it replaces an existing primary or is a new fallback
3. Whether it warrants its own variation mode

Open a PR with the new entries — see `CONTRIBUTING.md`.
