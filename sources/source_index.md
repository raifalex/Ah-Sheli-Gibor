# Hebrew AI Source Index

A consolidated index of every Hebrew AI model, tool, reference, and runtime the Ah Sheli Gibor skill knows about. Use this as the human-readable companion to `hebrew_ai_models.json` (machine-readable) and `source_selection.md` (decision logic).

## Source provenance

Catalog content is consolidated from:

- **[Daniel Rosehill — Hebrew-AI-Models](https://github.com/danielrosehill/Hebrew-AI-Models)** — primary catalog of Hebrew LLMs / ASR / TTS / NLP / embeddings / translation / OCR. CC BY 4.0.
- **[Daniel Rosehill — Hebrew-LLMs](https://github.com/danielrosehill/Hebrew-LLMs)** — focused LLM list with sizing / quantization variants. CC BY 4.0.
- **[NVIDIA Developer Blog — Accelerating Hebrew LLM Performance with TensorRT-LLM](https://developer.nvidia.com/blog/accelerating-hebrew-llm-performance-with-nvidia-tensorrt-llm/)** — production-deployment optimization for DictaLM-2.0.
- **[DictaBERT collection (HuggingFace)](https://huggingface.co/collections/dicta-il/dictabert)** — 17+ DictaBERT variants.
- **[NNLP-IL Hebrew-Resources](https://github.com/NNLP-IL/Hebrew-Resources)** — tools and services index.
- **[Academy of the Hebrew Language](https://hebrew-academy.org.il/)** — authoritative grammar reference.
- **[Hspell / Ivrix Project](http://hspell.ivrix.org.il/)** — open-source Hebrew spell + morphological analyzer.

License of this curated catalog: MIT (matches the skill). Underlying model licenses vary per model card — verify before commercial use.

## Catalog statistics

- **Total entries:** 124
- **LLM entries:** 30
- **ASR entries:** 15
- **TTS entries:** 9
- **BERT foundation models:** 11
- **NER models:** 3
- **Sentiment models:** 3
- **Emotion model:** 1 (hebEMO — 8 categories)
- **Morphology / parsing:** 7
- **Diacritization:** 3 (incl. Nakdan API)
- **Translation:** 3
- **Summarization:** 4
- **Domain-specialized:** 6 (legal, medical, biblical, lyrics, math, SQL)
- **Embeddings:** 3
- **OCR / vision:** 3
- **Speech foundation:** 4
- **Authoritative references:** 4 (Academy, Morfix, Rav-Milim, MILA)
- **Runtime optimization:** 1 (NVIDIA TensorRT-LLM)
- **API services:** 2 (Nakdan, DeepL)

## Organization fingerprints

### dicta-il
The dominant Hebrew NLP organization in 2026. Owns the DictaBERT family (morphology / parsing / segmentation / NER / sentiment / QA / diacritization) and the DictaLM family (generative LLMs through DictaLM-3.0). License generally CC BY 4.0 for the model weights.

**Models in catalog:** 25+

**When to invoke:**
- Grammar / morphology / parsing → DictaBERT variants
- High-quality Hebrew generation → DictaLM-3.0-24B-Thinking
- Reasoning / cultural explanation / slang → DictaLM-3.0-24B-Thinking
- Production deployment → DictaLM-2.0-Instruct + NVIDIA TensorRT-LLM
- Diacritization → dictabert-large-char-menaked or Nakdan API

### ivrit-ai
The dominant Hebrew ASR organization. Top model: `whisper-large-v3-turbo-ct2` (22K+ downloads).

**Models in catalog:** 6

**When to invoke:**
- Hebrew speech-to-text → `whisper-large-v3-turbo-ct2`
- Multi-speaker transcription → pair with `pyannote-speaker-diarization-3.1`

### yam-peleg
Hebrew adaptations of large multilingual LLMs (Gemma, Mistral, Mixtral).

**Models in catalog:** 5

**When to invoke:**
- Long-context Hebrew (200K) → `Hebrew-Mistral-7B-200K`
- Large-scale Hebrew (MoE) → `Hebrew-Mixtral-8x22B`
- Gemma-licensed Hebrew chat → `Hebrew-Gemma-11B-Instruct`

### avichr
Foundation heBERT family — first widely-used Hebrew BERT, plus domain-specialized variants.

**Models in catalog:** 5

**When to invoke:**
- Legal Hebrew → **Legal-heBERT** (PRIMARY)
- Hebrew NER → `heBERT_NER`
- Hebrew sentiment → `heBERT_sentiment_analysis`
- Hebrew emotion (8 categories) → **hebEMO** (PRIMARY for gender-emotional mode)

### onlplab
Open NLP Lab — foundational AlephBERT.

**Models in catalog:** 1 (alephbert-base)

**When to invoke:** baseline Hebrew BERT for fine-tuning research; superseded by DictaBERT for production.

### imvladikon
Comprehensive Hebrew NLP — ASR (wav2vec2), embeddings, summarization, QA.

**Models in catalog:** 9

**When to invoke:**
- Hebrew ASR alternative to ivrit-ai → `wav2vec2-xls-r-1b-hebrew`
- Hebrew sentence embeddings → `sentence-transformers-alephbert`
- Hebrew T5 summarization → `het5_summarization`
- Cross-lingual HE→EN summarization → `cross_summarization_he_en`

### slprl (Speech Lab, Reichman / Technion)
Speech-language models, TTS, and prosody-aware Hebrew.

**Models in catalog:** 7

**When to invoke:**
- High-quality Hebrew TTS → SIMS-7B
- Stress / prosody-aware speech → StresSLM / PAST / WhiStress

### HeNLP
HeRo (Hebrew RoBERTa) family.

**Models in catalog:** 2

**When to invoke:**
- Alternative architecture to BERT for Hebrew → HeRo
- Long-context Hebrew encoder → LongHeRo (over 512 tokens)

### Helsinki-NLP
OPUS-MT translation.

**Models in catalog:** 2

**When to invoke:**
- EN → HE translation → `opus-mt-en-he`
- HE → EN translation → `opus-mt-tc-big-he-en`

### thewh1teagle
Community TTS / phonemization tools.

**Models in catalog:** 4

**When to invoke:**
- Hebrew phonemization for TTS → phonikud
- Community TTS pipeline → israwave + phonikud
- IPA phoneme extraction → whisper-heb-ipa

### Intel
Specialized educational LLMs.

**Models in catalog:** 1 (hebrew-math-tutor-v1)

### Norod78
Smaller fine-tunes, creative variants (bilingual, lyrics).

**Models in catalog:** 4

**When to invoke:**
- Hebrew lyrics / creative → `gemma-3_4b_hebrew-lyrics-finetune`
- Tiny bilingual → `SmolLM-135M-FakyPedia-EngHeb`

## Authoritative references

### Academy of the Hebrew Language
[hebrew-academy.org.il](https://hebrew-academy.org.il/)

The official Hebrew language authority. Settles disputes about spelling, grammar, terminology, loanword integration. **Cite when establishing canonical Hebrew forms.** The skill defers to Academy rulings when corpus and tradition conflict.

### Morfix
[morfix.co.il](https://www.morfix.co.il/)

Dictionary + full conjugation tables for verbs. Fastest lookup for binyan / gender / inflection.

### Rav-Milim
[ravmilim.co.il](https://www.ravmilim.co.il/)

Hebrew thesaurus. Use for synonym discovery and register-variant selection (when one verb is colloquial and another is formal).

### MILA Hebrew Corpus
[mila.cs.technion.ac.il](http://mila.cs.technion.ac.il/)

Academic Hebrew NLP reference corpus from Bar-Ilan / Technion. Maintained less actively; still authoritative for morphology research.

## Runtime optimization

### NVIDIA TensorRT-LLM for Hebrew
[developer.nvidia.com/blog/accelerating-hebrew-llm-performance-with-nvidia-tensorrt-llm/](https://developer.nvidia.com/blog/accelerating-hebrew-llm-performance-with-nvidia-tensorrt-llm/)

Production-grade Hebrew LLM serving. Target model: DictaLM-2.0-Instruct. Optimization: FP16 / INT4 quantization. Deployment: Triton Inference Server on A100 / H100.

See `references/nvidia_tensorrt_optimization.md` for the integration recipe.

## API services

### Dicta Nakdan
[nakdan.dicta.org.il](https://nakdan.dicta.org.il/)

Professional Hebrew diacritization. Adds nikud (vowel marks) to unvocalized Hebrew. API endpoint: `https://nakdan.dicta.org.il/api` (POST). Use for ceremonial / liturgical / TTS-prep text.

### DeepL API
[deepl.com](https://www.deepl.com/)

Highest-quality EN↔HE neural translation. Requires API key + paid tier for production volume. Use when cultural idiomaticity matters more than cost.

## How sources are wired into the skill

| Sub-step | What it does | Which sources it can invoke |
|---|---|---|
| STEP 4.5 — Source Selection | Picks the right source per task+goal | `source_selection.md` decision tree |
| STEP 5a — Regex grammar | Detects pattern-based errors | None (regex in `hebrew_validate.py`) |
| STEP 5b — Model grammar | Morphological / agreement / smikhut | DictaBERT-parse (via `scripts/hebrew_toolkit.py parse`) |
| STEP 5c — Talk-jargon currency | Verifies corpus-grounded terminology | `corpus/jargon.json` + Academy of Hebrew Language |
| STEP 5d — Persona consistency | Voice fingerprint | `personas/*.md` |
| STEP 5e — Phrasing | Idiomaticity / register | DictaLM-3.0-Thinking for ambiguous judgments |
| STEP 5f — Anti-patterns | Bad-output table | `common_errors_catalog.md` + `anti_patterns.md` |
| STEP 5g — 4-axis rubric | רלוונטיות / קוהרנטיות / עקביות / רהיטות scoring | Claude itself (the LLM grading), optionally cross-checked with DictaBERT-NER for consistency |

## Update cadence

- Catalog refreshed every release. v0.4.0 catalog generated 2026-05-22.
- New models added when they appear in Rosehill catalogs (auto-sync planned for v0.5.0).
- Specialized domain models tracked closely (legal, medical, biblical, gender-emotional).

## Read next

- **`source_selection.md`** — the decision tree: which source for which task
- **`../references/hebrew_variations.md`** — the 8 variation modes and which sources back each
- **`../references/output_evaluation_rubric.md`** — the 4-axis scoring used in STEP 5g
- **`../references/nvidia_tensorrt_optimization.md`** — production deployment recipe
- **`../scripts/hebrew_toolkit.py`** — runtime CLI that invokes the models
