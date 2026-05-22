# Ah Sheli Gibor

> **אח שלי גיבור** — the affectionate Israeli startup-nation address. A Claude Skill for producing authentic 2026-era Israeli tech Hebrew at production grade — with the right voice, the right register, the right sources, and validated grammar.

---

## What this skill does

Produces authentic 2026-era Israeli tech Hebrew across **5 output types**, **8 variation modes**, and **6 voice personas** — with **source-aware generation**, **six-stage validation**, and a **4-axis output rubric**. Grounded in a **124-entry catalog** of Hebrew AI models / tools / references. Production-deployment optimized via NVIDIA TensorRT-LLM.

This is not a Hebrew translator. It's a Hebrew **producer** that comprehends source content and reconstructs it in the target register, persona, and variation mode the situation needs.

---

## Installation

### One-line install (recommended)

```sh
npx github:raifalex/Ah-Sheli-Gibor
```

Installs to `~/.claude/skills/ah-sheli-gibor/`. Restart Claude Code afterward.

### After npm publish

```sh
npx ah-sheli-gibor
# or:
npm install -g ah-sheli-gibor && ah-sheli-gibor
```

### Installer options

```sh
npx ah-sheli-gibor                  # default install
npx ah-sheli-gibor --update         # git pull latest
npx ah-sheli-gibor --uninstall      # remove
npx ah-sheli-gibor --target <path>  # custom path
npx ah-sheli-gibor --dry-run        # show plan
npx ah-sheli-gibor --help
```

Requires Node ≥14 and `git`.

### Optional Hebrew NLP toolkit

For the automated validator and the 12+ specialized model subcommands:

```sh
cd ~/.claude/skills/ah-sheli-gibor
pip install -r scripts/requirements.txt   # transformers + torch + sentencepiece
```

---

## Architecture at a glance

```
┌──────────────────────────────────────────────────────────────────┐
│                     User invokes the skill                         │
└──────────────────────────────┬───────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 0 — INTERVIEW                                                │
│  Gathers 7 inputs: output-type, context, purpose, mood,            │
│  GOAL, variation mode, persona. Asks ≤3 questions max.            │
└──────────────────────────────┬───────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 1 → 4 — COMPREHEND, MAP TERMS, SET REGISTER, WRITE           │
└──────────────────────────────┬───────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 4.5 — SOURCE SELECTION                                       │
│  Picks: generator source + validators + reference + rubric weights │
│  Catalog: sources/hebrew_ai_models.json (124 entries)             │
└──────────────────────────────┬───────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│  STEP 5 — SIX-STAGE VALIDATION                                     │
│  5a regex grammar  →  5b model grammar  →  5c jargon currency     │
│  5d persona consist →  5e phrasing/idiom →  5f anti-patterns      │
│  5g 4-axis rubric (רלוונטיות / קוהרנטיות / עקביות / רהיטות, 1-10) │
└──────────────────────────────┬───────────────────────────────────┘
                               ▼
                       Final Hebrew output
```

---

## The 5 output types

| Output type | What it does |
|---|---|
| **Rewrite** | Reframe source text in a target Israeli tech register |
| **Pitch** | Investor / customer / internal / elevator pitch decks |
| **Speech** | Keynotes, commencements, memorials, town-halls, awards |
| **Talking cards** | Panel prep, TV interview, board meetings, podcast appearances |
| **Teleprompter** | Verbatim broadcast / recorded-video scripts with delivery annotations |

Each output type has its own structural template, delivery annotations, and validation thresholds. Full specs in `output_types/`.

---

## The 6 personas

| Persona | M/F | Archetype | Signature voice |
|---|---|---|---|
| **יואל "יו-יו" שריג** | M | tech-founder | Series-A confidence, dense English code-switching, founder-mode urgency, mission framing |
| **שירה לב** | F | literary speechwriter | Classical-modern Hebrew, recurring images, emotional crescendos, dignified pauses |
| **גלעד אש** | M | comedian | Deadpan, slang-fluent but selective, Hebrew setup + English punch, self-aware references |
| **דנה אלמוג** | F | TV panelist-pundit | Debate-trained soundbites, rhetorical-question framing, single data-anchor per beat |
| **איתמר חוזה** | M | veteran journalist | Patient long-form, classical Hebrew, scene-setting, deferred conclusions |
| **נועה אופק** | F | contemporary creator | Intimate, vulnerable, fluid Hebrew-English, story-driven, personal-anchor opener |

Pick by name (*"voice = יואל"* / *"speak as שירה"*) or let the skill auto-select based on output type + goal + variation.

Full persona profiles with voice signature, vocabulary palette, distinctive moves, and sample paragraphs: `personas/`.

---

## The 8 variation modes

| Mode | When to use | Primary source |
|---|---|---|
| **tech-formal** (default) | Israeli tech writing | Claude + DictaBERT + corpus |
| **legal-technical** | Contracts, ToS, IP, statute commentary | Legal-heBERT + deterministic output |
| **medical** | Clinical notes, patient comms, informed consent | hebrew_medical_ner_v5 |
| **biblical-rabbinic** | Religious, ceremonial, Talmudic | BEREL_3.0 / hebrew_bible_ai |
| **gender-emotional** | Personal narrative, vulnerable, memorial | hebEMO (8 emotions) |
| **slang-cultural** | Casual + comic, with cultural-explanation layer | DictaLM-3.0-24B-Thinking |
| **bilingual** | Hebrew + English side-by-side | neodictabert-bilingual |
| **creative-lyrics** | Poetry, lyrics, experimental prose | gemma-3_4b_hebrew-lyrics-finetune |

Each variation mode encodes a vocabulary band + grammatical conventions + source bundle. Full spec: `references/hebrew_variations.md`.

---

## The interview (STEP 0)

When invoked, the skill asks (at most 3 questions, combining related ones):

| # | Variable | Example |
|---|---|---|
| 1 | **Output type** | rewrite / pitch / speech / talking-cards / teleprompter |
| 2 | **Use context** | who's the audience, what platform |
| 3 | **Purpose** | inform / persuade / entertain / sell / mobilize / celebrate / mourn |
| 4 | **Mood** | confident / warm / urgent / measured / playful / serious / vulnerable |
| 5 | **🆕 Goal — what you want to achieve** | "convince investors" / "win a panel debate" / "land emotional impact" / "ceremonial address" / "sign a contract" / "clinical documentation" / "production deployment" |
| 6 | **🆕 Variation mode** | tech-formal / legal-technical / medical / biblical-rabbinic / gender-emotional / slang-cultural / bilingual / creative-lyrics / auto |
| 7 | **Persona** | יואל / שירה / גלעד / דנה / איתמר / נועה / auto |

If 5/7 are clear from context, the skill proceeds — naming its inferences in one line.

---

## The 4-axis output rubric

Every output is scored (1–10 each):

| Hebrew | English | Definition |
|---|---|---|
| **רלוונטיות** | Relevance | Coverage and priority of key content from the source |
| **קוהרנטיות** | Coherence | Collective quality of all sentences; logical flow and arc |
| **עקביות** | Consistency | Factual fidelity between output and source; no hallucination |
| **רהיטות** | Fluency | Grammar, spelling, punctuation, word choice, sentence structure, persona fidelity |

**Per-output-type thresholds:**

| Output type | Priority axes | Pass threshold |
|---|---|---|
| Rewrite | רהיטות > רלוונטיות > קוהרנטיות > עקביות | All ≥ 7 |
| Pitch | קוהרנטיות > רלוונטיות > עקביות > רהיטות | קוהרנטיות ≥ 8, others ≥ 7 |
| Speech | קוהרנטיות > רהיטות > רלוונטיות > עקביות | קוהרנטיות ≥ 8, רהיטות ≥ 8 |
| **Talking cards** | עקביות > רהיטות > קוהרנטיות > רלוונטיות | **עקביות ≥ 9** (debate-grade) |
| **Teleprompter** | רהיטות > עקביות > קוהרנטיות > רלוונטיות | **רהיטות ≥ 9** (reading-speed) |

Goal further weights axes (e.g., *"sign a contract"* gives עקביות a 2× weight). Full spec: `references/output_evaluation_rubric.md`.

---

## Six-stage validation

Every output passes through:

| Stage | What it checks | Tools |
|---|---|---|
| **5a** Regex grammar | Pattern-based errors (Categories A/D/E/G/H/K/L) | `hebrew_validate.py --no-model` |
| **5b** Model grammar | Agreement, smikhut, binyan, gender/number | DictaBERT-parse via `hebrew_toolkit.py parse` |
| **5c** Jargon currency | Every term traces to corpus (2025+) or persona signature | `corpus/jargon.json` + Academy |
| **5d** Persona consistency | Voice fingerprint across paragraphs | `personas/*.md` |
| **5e** Phrasing / idiomaticity | Word order, idioms, register coherence, code-switching density, rhythm, connectives, anaphora | `references/phrasing_checker.md` |
| **5f** Anti-patterns + authenticity | 12-category catalog cross-check + native-speaker test | `references/common_errors_catalog.md` |
| **5g** 4-axis rubric | רלוונטיות / קוהרנטיות / עקביות / רהיטות (1-10 each) | LLM-graded with goal/output-type weighting |

Below threshold on any priority axis = automatic rewrite of the failing section.

---

## The 124-entry source catalog

Consolidated from:
- [Daniel Rosehill — Hebrew-AI-Models](https://github.com/danielrosehill/Hebrew-AI-Models) (CC BY 4.0)
- [Daniel Rosehill — Hebrew-LLMs](https://github.com/danielrosehill/Hebrew-LLMs) (CC BY 4.0)
- [NVIDIA Developer Blog — TensorRT-LLM for Hebrew](https://developer.nvidia.com/blog/accelerating-hebrew-llm-performance-with-nvidia-tensorrt-llm/)
- [NNLP-IL Hebrew-Resources](https://github.com/NNLP-IL/Hebrew-Resources)
- [Academy of the Hebrew Language](https://hebrew-academy.org.il/)

**By category:**

| Category | Count | Top picks |
|---|---|---|
| LLMs (generation/reasoning/instruction) | 30 | DictaLM-3.0-24B-Thinking, Hebrew-Mixtral-8x22B, DictaLM-2.0-Instruct |
| ASR | 15 | ivrit-ai whisper-large-v3-turbo-ct2 |
| TTS | 9 | SIMS-7B + phonikud, HebTTS |
| BERT foundation | 11 | DictaBERT, NeoDictaBERT-bilingual, HeRo |
| NER | 3 | dictabert-ner, heBERT_NER |
| Sentiment / emotion | 4 | heBERT_sentiment, hebEMO (8 categories) |
| Morphology / parsing | 7 | dictabert-parse, dictabert-large-parse, YAP |
| Diacritization | 3 | Dicta Nakdan API, dictabert-large-char-menaked |
| Translation | 3 | Helsinki-NLP opus-mt-en-he, DeepL API |
| Summarization | 4 | het5_summarization, hebrew-summarization-llm |
| **Domain-specialized** | 6 | **Legal-heBERT, hebrew_medical_ner_v5, BEREL_3.0**, hebrew-math-tutor-v1, Llama-3.1-8b-Hebrew2SQL, gemma-3_4b_hebrew-lyrics |
| Embeddings | 3 | sentence-transformers-alephbert, neodictabert-bilingual-embed |
| OCR / vision | 3 | testing-trOCR-hebrew-handwritten, paleo-hebrew-qwen3-vl-lora |
| Speech foundation | 4 | mhubert-base-25hz, StresSLM, PAST |
| Authoritative references | 4 | Academy of Hebrew Language, Morfix, Rav-Milim, MILA |
| Runtime optimization | 1 | NVIDIA TensorRT-LLM (DictaLM-2.0) |

Full structured catalog: `sources/hebrew_ai_models.json` (machine-readable) + `sources/source_index.md` (human-readable).

---

## Source selection (STEP 4.5)

The skill picks the right source per task. Examples:

| Task | Selected source | Why |
|---|---|---|
| Generate Hebrew tech blog | Claude + corpus/jargon.json | Default tech-formal mode; Claude excels at general Hebrew tech |
| Validate grammar | DictaBERT-parse via toolkit | Best parser; CC BY 4.0 |
| Validate slang explanation | DictaLM-3.0-24B-Thinking | Best Hebrew LLM for cultural nuance |
| Legal contract | Legal-heBERT + temperature=0 | Legal terminology + deterministic output |
| Medical clinical note | hebrew_medical_ner_v5 | Medical entity recognition |
| Memorial address | BEREL_3.0 + hebEMO | Ceremonial + emotion-aware |
| Production Hebrew LLM serving | DictaLM-2.0 + TensorRT-LLM + Triton | Scaled serving; near-constant latency at 16+ concurrent |
| Hebrew ASR | ivrit-ai whisper-large-v3-turbo-ct2 | Top Hebrew ASR; 22K+ downloads |
| Hebrew TTS | SIMS-7B + phonikud | Best contemporary Hebrew TTS |
| Diacritization (nikud) | Dicta Nakdan API | Live API; ceremonial-grade |
| Hebrew-English RAG embeddings | neodictabert-bilingual-embed | Best bilingual embeddings |

Full decision tree: `sources/source_selection.md`.

User can override: *"use Legal-heBERT"* / *"skip model validation"* / *"strict-corpus only"*.

---

## The hebrew_toolkit.py CLI

Unified runtime for the 12+ specialized models. Lazy-loads per subcommand.

```sh
python scripts/hebrew_toolkit.py morph "ההנחה הזאת..."         # DictaBERT-morph
python scripts/hebrew_toolkit.py parse "..."                    # DictaBERT-parse → dep tree
python scripts/hebrew_toolkit.py ner "..."                      # DictaBERT-NER → entities
python scripts/hebrew_toolkit.py sentiment "..."                # heBERT_sentiment
python scripts/hebrew_toolkit.py emotion "..."                  # hebEMO → 8 emotion scores
python scripts/hebrew_toolkit.py legal "..."                    # Legal-heBERT embeddings
python scripts/hebrew_toolkit.py medical "..."                  # medical NER
python scripts/hebrew_toolkit.py metaphor "..."                 # hebert-metaphor
python scripts/hebrew_toolkit.py offensive "..."                # offensive-detection
python scripts/hebrew_toolkit.py nakdan "..."                   # Dicta Nakdan diacritization
python scripts/hebrew_toolkit.py translate "..." --to en        # Helsinki-NLP MT
python scripts/hebrew_toolkit.py summarize @article.txt         # het5_summarization
python scripts/hebrew_toolkit.py recommend --task generate --variation legal-technical
python scripts/hebrew_toolkit.py rubric output.txt source.txt   # 4-axis rubric template
```

Output: structured JSON. Input: literal Hebrew text or `@filepath`.

---

## The hebrew_validate.py CLI

Fast regex + DictaBERT grammar validator.

```sh
# Regex-only (no deps)
python scripts/hebrew_validate.py --no-model your_text.md

# Full mode (regex + DictaBERT parsing)
python scripts/hebrew_validate.py your_text.md

# JSON output for CI integration
python scripts/hebrew_validate.py --json your_text.md
```

Detects 11+ regex-rule patterns + model-based agreement/smikhut/binyan checks. Exit codes: 0=clean, 1=warnings, 2=errors.

---

## Production deployment

For high-volume Hebrew LLM serving, the skill documents the production path: **DictaLM-2.0-Instruct + NVIDIA TensorRT-LLM + Triton Inference Server**. Near-constant latency at 16+ concurrent requests on a single A100.

Full recipe: `references/nvidia_tensorrt_optimization.md`.

Cost crossover from Claude API to self-hosted: ~5–10M Hebrew tokens/month.

---

## When NOT to use this skill

- General Hebrew translation → use DeepL or DictaLM directly
- Formal Academy-of-Hebrew documents → use `hebrew-content-writer`
- Hebrew RTL CSS / web layout → use `hebrew-rtl-best-practices`
- Hebrew PDF / DOCX / PPTX generation → use `hebrew-document-generator`
- Niqud / vowelization only → use Dicta Nakdan directly
- Non-tech content (literary fiction, news reporting) → use `hebrew-content-writer`

---

## File structure

```
ah-sheli-gibor/
├── SKILL.md                            # Operating instructions (the protocol)
├── metadata.json                       # Bilingual skill metadata
├── package.json                        # npm package + bin
├── README.md                           # This file
├── CONTRIBUTING.md                     # How to add corpus entries
├── LICENSE                             # MIT
│
├── corpus/
│   └── jargon.json                     # Vocabulary corpus with provenance
│
├── personas/                           # The 6 voices
│   ├── personas.json
│   ├── yoel-yoyo-sarig.md              # Tech founder (M)
│   ├── shira-lev.md                    # Literary speechwriter (F)
│   ├── gilad-esh.md                    # Comedian (M)
│   ├── dana-almog.md                   # TV panelist (F)
│   ├── itamar-hoze.md                  # Veteran journalist (M)
│   └── noa-ofek.md                     # Contemporary creator (F)
│
├── output_types/                       # The 5 outputs
│   ├── pitch.md
│   ├── speech.md
│   ├── talking_cards.md
│   └── teleprompter.md
│
├── sources/                            # 124-entry catalog (NEW v0.4.0)
│   ├── hebrew_ai_models.json
│   ├── hebrew_llms.json
│   ├── source_index.md
│   └── source_selection.md             # Decision tree
│
├── references/
│   ├── grammar_layer.md                # Binyan / gender / smikhut / preposition rules
│   ├── grammar_validation_tools.md     # Toolchain (DictaBERT / Hspell / Nakdan)
│   ├── common_errors_catalog.md        # 12-category error catalog (A-L)
│   ├── anti_patterns.md                # Bad-output table
│   ├── phrasing_checker.md             # Idiomaticity / naturalness layer
│   ├── hebrew_variations.md            # 8 variation modes (NEW v0.4.0)
│   ├── output_evaluation_rubric.md     # 4-axis scoring (NEW v0.4.0)
│   ├── nvidia_tensorrt_optimization.md # Production deployment (NEW v0.4.0)
│   └── sources.md                      # Source registry with provenance
│
├── research/
│   └── contemporary_voices_2026.md     # Persona research basis
│
├── scripts/
│   ├── hebrew_validate.py              # Fast regex + DictaBERT validator
│   ├── hebrew_toolkit.py               # Unified Hebrew NLP CLI (NEW v0.4.0)
│   └── requirements.txt                # transformers + torch
│
├── bin/
│   └── install.js                      # npx installer
│
├── tests/
│   ├── test_cases.md                   # 5 register tests
│   └── test_results_v0.md
│
└── examples/
    └── rewrites/                       # Before/after examples
```

---

## Versioning

- **v0.1.0** — scaffold + 30 seed corpus + 5 tests + rewrite-only
- **v0.1.1** — npx installer
- **v0.2.0** — 6 personas + 4 output types + interview (STEP 0) + initial validation
- **v0.3.0** — 6-stage validation + phrasing checker + grammar tools + 12-category error catalog + DictaBERT-powered validator
- **v0.4.0** (current) — **124-source catalog** (Rosehill + NVIDIA) + **8 variation modes** + **STEP 4.5 source selection** + **STEP 5g 4-axis rubric** (Hebrew-labeled) + **user-goal interview question** + **hebrew_toolkit.py** (14 subcommands invoking specialized models on demand) + **TensorRT-LLM production deployment guide**
- **v0.5.0** (planned) — corpus expansion to 200+ 2025–2026 web-sourced entries; custom persona from user samples; test matrix expansion (5 → 60 cases)
- **v0.6.0** (planned) — audio rehearsal loop (TTS + ASR feedback); visual deliverable pipeline (markdown → PDF / Gamma decks)
- **v0.7.0** (planned) — educational mode (explain corrections); strict-corpus mode; self-improvement feedback loop
- **v1.0.0** (planned) — 300+ corpus, additional personas (Arabic-Hebrew, religious-Hebrew), CI / GitHub Action integration

---

## License

MIT. See `LICENSE`. Underlying model licenses (DictaBERT CC BY 4.0; Hspell AGPL-3.0; Gemma / Llama / Mistral per their respective licenses) — verify before commercial use.

---

## Contributing

See `CONTRIBUTING.md`. Every new corpus entry must conform to the v2 schema and carry valid provenance.

Pull requests welcome — especially for:
- 2025–2026 corpus entries from Israeli tech sources
- New source-catalog entries (when new Hebrew models appear on HuggingFace)
- Test cases for personas × variation modes × output types
- Custom persona profiles built from public Israeli voice samples

---

*Built with the help of Claude Opus 4.7 (1M context). Catalog sources: Daniel Rosehill, NVIDIA Developer Blog, dicta-il, ivrit-ai, avichr, yam-peleg, onlplab, imvladikon, slprl, HeNLP, Helsinki-NLP, Norod78, Slasky, thewh1teagle.*
