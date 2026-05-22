# Ah Sheli Gibor

> **אח שלי גיבור** — the affectionate Israeli address.
> **The comprehensive Hebrew production suite.** 25+ output types · 15 variation modes · 6 voice personas · 124-source AI catalog · six-stage validation · 4-axis Hebrew-labeled rubric. Production-grade.

[![npm version](https://img.shields.io/npm/v/ah-sheli-gibor.svg)](https://www.npmjs.com/package/ah-sheli-gibor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## What you get

A Claude Skill that produces **professional-grade Hebrew across every format and register you actually need** — books, articles, speeches, pitches, research papers, executive reports, course materials, talking cards, teleprompter scripts, technical documentation, and more. With the **right voice**, the **right register**, **validated grammar**, and **source-aware generation**.

This is not a translator. It's a Hebrew **producer** that comprehends source content and reconstructs it in the target format, persona, and variation mode the situation needs.

### Why this exists

**Israeli Hebrew is fragmented.** A pitch to investors needs different vocabulary than a memorial speech. A medical clinical note needs different grammar than a haredi-tech LinkedIn post. A cybersecurity incident report needs different cadence than a poetry chapbook. Generic translation tools flatten all of this into the same beige Hebrew.

The Ah Sheli Gibor suite gives you 25+ format specs × 15 register modes × 6 voice personas × 124 AI sources. Every combination produces Hebrew that **a 2026 Israeli professional in that specific context would actually write**.

### What makes it trustworthy

- **Anti-hallucination guards** — every term traces to corpus (2025+ source-dated) or a documented persona signature
- **Provenance tracking** — corpus entries carry URL + date; sources cited
- **Academy of Hebrew Language alignment** — formal rulings respected
- **2025-only source rule** — no dated 2022–2023 buzzwords
- **Deterministic legal output** — contracts produce reproducibly (temperature=0)
- **6-stage validation** — every output checked across grammar, jargon currency, persona, phrasing, anti-patterns, rubric
- **4-axis Hebrew-labeled rubric** — רלוונטיות / קוהרנטיות / עקביות / רהיטות, each 1-10
- **Native-speaker authenticity test** as the final pass

---

## Installation

### One-line install (recommended)

```sh
npx ah-sheli-gibor
```

Installs from the npm registry to `~/.claude/skills/ah-sheli-gibor/`. Restart Claude Code afterward.

### Alternative — from GitHub source

```sh
npx github:raifalex/Ah-Sheli-Gibor
```

### Global install

```sh
npm install -g ah-sheli-gibor
ah-sheli-gibor
```

### Installer options

```sh
npx ah-sheli-gibor                  # default install (~/.claude/skills/)
npx ah-sheli-gibor --update         # git pull latest
npx ah-sheli-gibor --uninstall      # remove
npx ah-sheli-gibor --target <path>  # custom path
npx ah-sheli-gibor --dry-run        # preview without installing
npx ah-sheli-gibor --help
```

Requires Node ≥14 and `git`.

### Optional Hebrew NLP toolkit

For the automated validator + 14 specialized-model subcommands:

```sh
cd ~/.claude/skills/ah-sheli-gibor
pip install -r scripts/requirements.txt   # transformers + torch + sentencepiece
```

### Supported agents

claude-code · cursor · github-copilot · windsurf · opencode · codex · gemini-cli

---

## Quick examples

### Example 1 — Founder LinkedIn announcement

**Input:**
> "Write a LinkedIn announcement for closing a $14M Series A. Voice = Yoel. Add details: 22 enterprise customers, $2.1M ARR, 142% NRR."

**Output (Yoel voice):**
> רגע נדיר.
>
> אחרי 18 חודשים של בנייה, שלושה rewrites של ה-architecture, ופיבוט אחד שכמעט הרג אותנו — סגרנו היום Series A של 14 מיליון דולר.
>
> מה למדנו: רוב הצוותים שמנסים להטמיע AI agents מתקשעים על אותה בעיה — context handoff בין agents. כולם פתרו את זה לרוחב; אנחנו פתרנו לעומק. זה bet ששילם.
>
> 22 לקוחות enterprise. $2.1M ARR. NRR של 142%. צוות של 9 שבונה כמו 30.
>
> מגייסים founding engineers עכשיו. אם זה מדבר אליך — דבר איתי.

### Example 2 — Executive board memo

**Input:**
> "Board memo recommending we raise the GTM budget by $4.2M for Q3-Q4. Persona = Yoel. Format = report-executive."

**Output (excerpt, Hebrew-formal):**
> **לכבוד:** דירקטוריון SecureFlow
> **מאת:** דני שריג, מנכ"ל
> **תאריך:** 22/05/2026
> **נושא:** המלצה לאישור הרחבת תקציב GTM ב-4.2 מיליון דולר
>
> ## תקציר מנהלים
> מאז סבב ה-Series B צמחנו פי 2.4 ב-ARR. ה-pipeline ב-Enterprise תפח ב-340%. בקצב הנוכחי אנחנו מתקרבים לחסם עקב חוסר ב-AE capacity. מבקשים אישור להגדלת תקציב ה-GTM ב-4.2 מיליון דולר.
>
> **המלצה:** לאשר.
>
> [... full memo continues with Background / Analysis / Risks / Next Steps ...]

### Example 3 — Cybersecurity panel talking cards

**Input:**
> "Talking cards for a TechGym infosec panel on AI agent security. Persona = Dana. Variation = cybersecurity."

**Output (excerpt):**
> ### CARD 1.1 ▶ 00:00 · OPENING CLAIM
>
> השאלה היא לא איך — השאלה היא מתי.
>
> ה-Shared Responsibility Model שלכם הניח אדם. וההנחה הזאת שגויה היום בכל סביבת ענן שמריצה AI agent.
>
> זה לא קר. זה מדויק.
>
> ◼ [BEAT] ◼

---

## The 25+ output types

| Category | Output types |
|---|---|
| **Stage / spoken** | rewrite · pitch · speech · talking-cards · teleprompter |
| **Books** | book-chapter · book-proposal · manuscript-edit |
| **Articles** | article-feature · article-op-ed · article-news · article-profile |
| **Educational** | course-material (syllabus / lesson / handout / assessment / module / reading-guide) |
| **Reports** | report-executive · report-business · report-whitepaper · report-incident |
| **Academic** | research-paper (IMRAD) · research-proposal · thesis-chapter |
| **Business** | business-plan · rfp-response (Israeli michraz) · case-study |
| **Communications** | comms (press-release / formal-email / memo) |
| **Technical** | tech-doc (README / API / runbook / ADR / migration / troubleshooting) · product-spec (PRD) |

Each output type has its own structural template, validation gates, and persona pairings. Full specs in `output_types/`.

---

## The 15 variation modes + 4 sub-filters

### Tech sub-domains (8)

| Mode | When to use |
|---|---|
| **`tech-general`** (default) | General Israeli tech writing — fallback |
| **`software-engineering`** | Developer / DevOps / SRE register |
| **`cybersecurity`** | Israeli infosec community (SOC / IR / DFIR / INCD) |
| **`product-management`** | PM voice — roadmap / OKRs / KPIs / NPS |
| **`defense-aerospace`** | Israeli defense (Elbit / MAFAT / Rafael / IAI) |
| **`ai-ml-research`** | Academic + industrial ML |
| **`startup-fundraising`** | Founder ↔ investor |
| **`gen-z-creator`** | TikTok / Instagram / podcast |

### Domain specialized (3)

| Mode | When to use |
|---|---|
| **`legal-technical`** | Contracts, ToS, IP — deterministic output |
| **`medical`** | Clinical, patient comms, drug labels |
| **`biblical-rabbinic`** | Religious, ceremonial, Talmudic |

### Voice / style (4)

| Mode | When to use |
|---|---|
| **`gender-emotional`** | Personal narrative, vulnerable, memorial |
| **`slang-cultural`** | Casual + cultural-explanation layer |
| **`bilingual`** | Hebrew + English side-by-side |
| **`creative-lyrics`** | Poetry, lyrics, experimental |

### Community sub-filters (combine with any base mode)

| Sub-filter | When to use |
|---|---|
| **`arabic-hebrew-bilingual`** | Arab-Israeli, Druze, Circassian tech professionals |
| **`haredi-tech`** | Bnei Brak / Beit Shemesh tech (9,700+ workers, 6,900 women) |
| **`academic-formal`** | Israeli university research register |
| **`diaspora-israeli`** | Bay Area / NYC / Berlin Israeli expats |

Full spec: `references/hebrew_variations.md`.

---

## The 6 personas

| Persona | M/F | Archetype | Signature |
|---|---|---|---|
| **יואל ״יו־יו״ שריג** | M | tech-founder | Series-A confidence, dense English code-switching |
| **שירה לב** | F | literary speechwriter | Classical-modern Hebrew, recurring images |
| **גלעד אש** | M | comedian | Deadpan, slang-fluent, Hebrew setup + English punch |
| **דנה אלמוג** | F | TV panelist-pundit | Debate-trained soundbites, rhetorical-question framing |
| **איתמר חוזה** | M | veteran journalist | Patient long-form, classical Hebrew, deferred conclusions |
| **נועה אופק** | F | contemporary creator | Intimate, vulnerable, fluid Hebrew-English |

Pick by name (*"voice = יואל"* / *"speak as שירה"*) or let the skill auto-select based on output type + goal + variation mode.

Full persona profiles: `personas/`.

---

## The interview (STEP 0)

When invoked, the skill asks (at most 3 questions, combining related ones):

| # | Variable | Example |
|---|---|---|
| 1 | **Output type** | rewrite / pitch / speech / book-chapter / research-paper / etc. |
| 2 | **Use context** | who's the audience, what platform |
| 3 | **Purpose** | inform / persuade / entertain / sell / mobilize / celebrate / mourn |
| 4 | **Mood** | confident / warm / urgent / measured / playful / serious / vulnerable |
| 5 | **Goal — what you want to achieve** | "convince investors" / "win a panel debate" / "land emotional impact" / "ceremonial address" / "sign a contract" / "clinical documentation" / "publish a chapter" / "submit a grant" |
| 6 | **Variation mode** | (1 of 15) + optional sub-filter |
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

**Per-output-type pass thresholds:**

| Output type | Priority axis | Threshold |
|---|---|---|
| Rewrite | רהיטות | All ≥ 7 |
| Pitch | קוהרנטיות | קוהרנטיות ≥ 8 |
| Speech | קוהרנטיות + רהיטות | both ≥ 8 |
| **Talking cards** | עקביות | **עקביות ≥ 9** (debate-grade) |
| **Teleprompter** | רהיטות | **רהיטות ≥ 9** (reading-speed) |
| **Research paper** | עקביות | **עקביות ≥ 9** (factual rigor) |
| **Legal contract** | עקביות + רהיטות | both ≥ 9 (deterministic + precise) |
| **Incident report** | עקביות | **עקביות ≥ 9** (audit-grade) |

Goal further weights axes. Full spec: `references/output_evaluation_rubric.md`.

---

## Six-stage validation

Every output passes through:

| Stage | What it checks | Tools |
|---|---|---|
| **5a** Regex grammar | Pattern-based errors (Categories A/D/E/G/H/K/L) | `hebrew_validate.py --no-model` |
| **5b** Model grammar | Agreement, smikhut, binyan, gender/number | DictaBERT-parse |
| **5c** Jargon currency | Every term traces to corpus (2025+) or persona | `corpus/jargon.json` + Academy |
| **5d** Persona consistency | Voice fingerprint across paragraphs | `personas/*.md` |
| **5e** Phrasing / idiomaticity | Word order, idioms, register, code-switching density | `references/phrasing_checker.md` |
| **5f** Anti-patterns + authenticity | 12-category error catalog + native-speaker test | `references/common_errors_catalog.md` |
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
| LLMs (generation/reasoning/instruction) | 30 | DictaLM-3.0-24B-Thinking, Hebrew-Mixtral-8x22B |
| ASR | 15 | ivrit-ai whisper-large-v3-turbo-ct2 |
| TTS | 9 | SIMS-7B + phonikud, HebTTS |
| BERT foundation | 11 | DictaBERT, NeoDictaBERT-bilingual, HeRo |
| NER | 3 | dictabert-ner, heBERT_NER |
| Sentiment / emotion | 4 | heBERT_sentiment, hebEMO (8 categories) |
| Morphology / parsing | 7 | dictabert-parse, dictabert-large-parse |
| Diacritization | 3 | Dicta Nakdan API |
| Translation | 3 | Helsinki-NLP opus-mt, DeepL API |
| Summarization | 4 | het5_summarization |
| Domain-specialized | 6 | Legal-heBERT, hebrew_medical_ner_v5, BEREL_3.0 |
| Embeddings | 3 | sentence-transformers-alephbert |
| OCR / vision | 3 | testing-trOCR-hebrew-handwritten |
| Speech foundation | 4 | mhubert-base-25hz, StresSLM, PAST |
| Authoritative references | 4 | Academy of Hebrew Language, Morfix, Rav-Milim, MILA |
| Runtime optimization | 1 | NVIDIA TensorRT-LLM (DictaLM-2.0) |

Full structured catalog: `sources/hebrew_ai_models.json` + `sources/source_index.md` + `sources/source_selection.md`.

---

## The hebrew_toolkit.py CLI

14 subcommands invoking specialized Hebrew models on demand. Lazy-loads per subcommand.

```sh
python scripts/hebrew_toolkit.py morph ״ההנחה הזאת...״         # DictaBERT-morph
python scripts/hebrew_toolkit.py parse "..."                    # DictaBERT-parse → dep tree
python scripts/hebrew_toolkit.py ner "..."                      # DictaBERT-NER
python scripts/hebrew_toolkit.py sentiment "..."                # heBERT_sentiment
python scripts/hebrew_toolkit.py emotion "..."                  # hebEMO → 8 emotion scores
python scripts/hebrew_toolkit.py legal "..."                    # Legal-heBERT embeddings
python scripts/hebrew_toolkit.py medical "..."                  # medical NER
python scripts/hebrew_toolkit.py metaphor "..."                 # hebert-metaphor
python scripts/hebrew_toolkit.py offensive "..."                # offensive-detection
python scripts/hebrew_toolkit.py nakdan "..."                   # Dicta Nakdan diacritization
python scripts/hebrew_toolkit.py translate "..." --to en        # Helsinki-NLP MT
python scripts/hebrew_toolkit.py summarize @article.txt         # het5_summarization
python scripts/hebrew_toolkit.py recommend --task X --variation Y
python scripts/hebrew_toolkit.py rubric output.txt source.txt   # 4-axis template
```

Output: structured JSON. Input: literal Hebrew text or `@filepath`.

---

## Production deployment

For high-volume Hebrew LLM serving: **DictaLM-2.0-Instruct + NVIDIA TensorRT-LLM + Triton Inference Server**. Near-constant latency at 16+ concurrent requests on a single A100.

Cost crossover from Claude API to self-hosted: ~5–10M Hebrew tokens/month.

Full recipe: `references/nvidia_tensorrt_optimization.md`.

---

## When NOT to use this skill

- General Hebrew translation → use DeepL or DictaLM directly
- Hebrew RTL CSS / web layout → use `hebrew-rtl-best-practices`
- Hebrew PDF / DOCX / PPTX physical generation → use `hebrew-document-generator`
- Niqud / vowelization only → use Dicta Nakdan directly
- Non-Hebrew content

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
├── corpus/jargon.json                  # Vocabulary corpus with provenance
│
├── personas/                           # The 6 voices
│   ├── yoel-yoyo-sarig.md              ├── shira-lev.md           ├── gilad-esh.md
│   ├── dana-almog.md                   ├── itamar-hoze.md         └── noa-ofek.md
│
├── output_types/                       # 25+ output types (NEW v0.5.0 expanded)
│   ├── pitch.md   speech.md   talking_cards.md   teleprompter.md
│   ├── book-chapter.md   book-proposal.md   manuscript-edit.md
│   ├── article-feature.md   article-op-ed.md   article-news.md   article-profile.md
│   ├── course-material.md
│   ├── report-executive.md   report-business.md   report-whitepaper.md   report-incident.md
│   ├── research-paper.md   research-proposal.md   thesis-chapter.md
│   ├── business-plan.md   rfp-response.md   case-study.md
│   ├── comms.md   tech-doc.md   product-spec.md
│
├── sources/                            # 124-entry AI catalog (v0.4.0)
│   ├── hebrew_ai_models.json   hebrew_llms.json   source_index.md   source_selection.md
│
├── references/
│   ├── grammar_layer.md                # Binyan / gender / smikhut / preposition rules
│   ├── grammar_validation_tools.md     # DictaBERT / Hspell / Nakdan toolchain
│   ├── common_errors_catalog.md        # 12-category error catalog (A-L)
│   ├── anti_patterns.md                # Bad-output table
│   ├── phrasing_checker.md             # Idiomaticity / naturalness layer
│   ├── hebrew_variations.md            # 15 variation modes (NEW v0.5.0 expanded)
│   ├── output_evaluation_rubric.md     # 4-axis Hebrew-labeled scoring
│   └── nvidia_tensorrt_optimization.md # Production deployment
│
├── research/contemporary_voices_2026.md
│
├── scripts/
│   ├── hebrew_validate.py              # Fast regex + DictaBERT validator
│   ├── hebrew_toolkit.py               # Unified Hebrew NLP CLI (14 subcommands)
│   └── requirements.txt
│
├── bin/install.js                      # npx installer
├── tests/                              # Test cases + results
└── examples/rewrites/                  # Before/after examples
```

---

## Versioning

- **v0.1.0** — scaffold + 30 seed corpus + 5 tests + rewrite-only
- **v0.1.1** — npx installer
- **v0.2.0** — 6 personas + 4 output types + interview + initial validation
- **v0.3.0** — 6-stage validation + phrasing checker + grammar tools + DictaBERT validator
- **v0.4.0** — 124-source catalog + 8 variation modes + STEP 4.5 source selection + STEP 5g 4-axis rubric + user-goal interview + `hebrew_toolkit.py` (14 subcommands)
- **v0.5.0** (current) — **comprehensive scope expansion + rebrand as the Hebrew production suite**: 25+ output types (added books / articles / courses / reports / research / business / communications / technical docs) + 15 variation modes (added software-engineering / cybersecurity / product-management / defense-aerospace / ai-ml-research / startup-fundraising / gen-z-creator) + 4 community sub-filters (arabic-hebrew-bilingual / haredi-tech / academic-formal / diaspora-israeli)
- **v0.6.0** (planned) — audio rehearsal loop (TTS + ASR feedback); visual deliverable pipeline (markdown → PDF / Gamma decks); corpus expansion to 200+ 2025–2026 web-sourced entries
- **v0.7.0** (planned) — educational mode; strict-corpus mode; self-improvement feedback loop; custom persona from user samples
- **v1.0.0** (planned) — 300+ corpus entries, additional personas, CI / GitHub Action integration

---

## License

MIT. See `LICENSE`. Underlying model licenses (DictaBERT CC BY 4.0; Hspell AGPL-3.0; Gemma / Llama / Mistral per their respective licenses) — verify before commercial use.

---

## Contributing

See `CONTRIBUTING.md`. Pull requests welcome — especially for:
- 2025–2026 corpus entries from Israeli sources
- New variation-mode entries
- New output-type specifications
- Test cases for personas × variation modes × output types
- Custom persona profiles built from public Israeli voice samples

---

*Built with the help of Claude Opus 4.7 (1M context). Catalog sources: Daniel Rosehill, NVIDIA Developer Blog, dicta-il, ivrit-ai, avichr, yam-peleg, onlplab, imvladikon, slprl, HeNLP, Helsinki-NLP, Norod78, Slasky, thewh1teagle, Intel, NNLP-IL.*
