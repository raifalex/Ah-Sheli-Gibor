# Hebrew Grammar Validation Toolchain

This document is the technical companion to `references/grammar_layer.md`. Where the grammar layer describes the rules, this document lists the **tools that can validate those rules programmatically or via authoritative reference**.

The skill's STEP 5 (Validate) operates in two modes:

1. **Methodology mode (default)** — the skill applies the rule checklists from `grammar_layer.md` §6 and the anti-patterns from `anti_patterns.md` by inspection. No external tools required.
2. **Tool-assisted mode (optional)** — the skill (or the user) can run `scripts/hebrew_validate.py` against any output to get automated grammar/phrasing feedback grounded in the DictaBERT parser and rule-based regex checks.

---

## Tier 1 — Authoritative grammar references (use for rule disputes)

| Source | URL | Purpose | License |
|---|---|---|---|
| **Academy of the Hebrew Language** | https://hebrew-academy.org.il/ | The official Hebrew language authority. Settles spelling, grammar, terminology disputes. Publishes binding rulings on loanword integration and tech vocabulary. | Public reference |
| **Morfix** | https://www.morfix.co.il/ | Dictionary + full conjugation tables. Quickest lookup for binyan tense forms and gender of nouns. | Free web reference |
| **Rav-Milim** | https://www.ravmilim.co.il/ | Thesaurus and dictionary. Synonym discovery and register-variant selection. | Free (basic) |
| **MILA Hebrew Corpus** | http://mila.cs.technion.ac.il/ | Academic Hebrew NLP reference corpus from Bar-Ilan/Technion. Last fully maintained ~2020; still authoritative for morphology research. | Academic |
| **HebrewPod101 grammar overview** | https://www.hebrewpod101.com/blog/2021/03/18/hebrew-grammar-overview/ | Concise modern Hebrew grammar reference for tutorial-level lookup. | Free |
| **"Modern Hebrew: An Essential Grammar" (Coffin & Bolozky)** | Print + PDF circulating | Canonical academic Hebrew grammar reference. Used by university courses. | Book |

Use these to settle questions like *"is פיצ'ר masculine or feminine?"*, *"what's the imperative of לקומיט?"*, *"what does the Academy recommend for the verb form of fine-tuning?"*. The Academy's rulings override the corpus when there's a conflict.

---

## Tier 2 — Production tooling for automated validation

### DictaBERT (recommended — best-in-class)

**What it does:** joint Hebrew morphological + syntactic parser. Outputs JSON with per-token analysis: POS tag, gender, number, definiteness, lemma, dependency-tree position.

**Model:** `dicta-il/dictabert-parse` (also `dictabert-large-parse` for accuracy, `dictabert-tiny-parse` for speed).

**License:** CC BY 4.0 — free for any use including commercial.

**Auth:** none. Public HuggingFace model. Requires `trust_remote_code=True` due to custom model code.

**Install:**
```sh
pip install transformers torch
```

**Programmatic use:**
```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained('dicta-il/dictabert-parse', trust_remote_code=True)
model = AutoModel.from_pretrained('dicta-il/dictabert-parse', trust_remote_code=True)
model.eval()

text = "ההנחה הזאת הייתה בטוחה במשך 15 שנה"
result = model.predict([text], tokenizer, output_style='json')
# result[0]['tokens'] → list of per-token analyses
```

**What you can check with DictaBERT output:**
- Gender agreement in noun-adjective pairs (compare `morph.feats.Gender`)
- Subject-verb number agreement (use `syntax.dep_func == 'nsubj'`)
- Smikhut detection (`morph.feats.Definite == 'Cons'`)
- Definite article propagation in smikhut chains
- Binyan identification (`morph.feats.HebBinyan`)
- Tense consistency in narrative passages
- Construct-state versus analytical "X של Y" usage

**Reference:** [MRL Parsing Without Tears: The Case of Hebrew (arXiv 2403.06970)](https://arxiv.org/abs/2403.06970)

---

### Hspell + HspellPy

**What it does:** Hebrew spell-checker with morphological analyzer. Strict compliance with Academy of Hebrew Language niqqud-less spelling rules. ~24,000 base words with automatic inflection.

**License:** AGPL v3 — free for non-commercial use; commercial requires reading the AGPL terms carefully.

**Install (macOS via Homebrew):**
```sh
brew install hspell
hspell --help
```

**Install Python wrapper:**
```sh
pip install hspellpy
```

**Programmatic use:**
```python
import hspellpy
checker = hspellpy.Hspell()
is_correct, suggestions = checker.check_word("פיצ'ר")
```

**What it catches:**
- Missing or extra `אמות קריאה` (vowel letters)
- Non-Academy spelling variants
- Standard-Hebrew vocabulary errors

**Note:** Hspell expects ISO-8859-8 encoding for CLI use. Convert UTF-8 input with `iconv -f utf-8 -t iso8859-8` first. Python wrappers handle encoding automatically.

**Limitation:** Hspell does NOT understand tech loanwords by default. It will flag פיצ'ר, באג, MCP as "errors." Use it for the Hebrew-substrate validation, ignore its flags on loanwords (the skill's corpus is authoritative for loanwords).

---

### YAP (Yet Another Parser)

**What it does:** Morphosyntactic Hebrew parser from BGU Computational Linguistics. Performs morphological analysis + disambiguation + dependency parsing. Older than DictaBERT but well-tested.

**License:** Apache 2.0.

**Repo:** https://github.com/OnlpLab/yap

**Use case:** alternative to DictaBERT, faster for batch processing, no Python dependency (Go binary). Less accurate on contemporary tech loanwords.

---

### Dicta Nakdan (vowelization)

**What it does:** Adds niqqud (vowel marks) to unvocalized Hebrew text using neural diacritization. Useful for ceremonial text, religious quotation, ritual reading, and exact pronunciation guidance for speech delivery.

**Free version:** https://nakdan.dicta.org.il/
**Pro version:** https://nakdanpro.dicta.org.il/
**API endpoint:** https://nakdan.dicta.org.il/api (POST endpoint, undocumented publicly but discoverable from the web app's network calls)

**License:** Dicta's tools are open per their about page; verify per-use terms.

**Reference:** [Nakdan: Professional Hebrew Diacritizer (ACL 2020)](https://aclanthology.org/2020.acl-demos.23/)

**When to use:** the talking-cards / teleprompter output types don't normally need niqqud (per `references/grammar_layer.md` §7), but for memorial speeches, ceremonial passages, or biblical quotations the Nakdan can vocalize the relevant passage for the speaker's pronunciation reference.

---

### HebMorph (Lucene integration)

**What it does:** Hebrew analyzer plugin for Lucene/Elasticsearch search engines. Includes morphological analysis suitable for indexing Hebrew content.

**License:** AGPL v3.

**Repo:** https://github.com/synhershko/HebMorph

**Use case:** building a searchable index over Hebrew corpus content. Not directly used for grammar validation but pairs with the corpus when expanding to v1.0+.

---

## Tier 3 — Online checkers (use cautiously, not for primary validation)

These are commercial or hobby checkers. They're useful as a sanity check or for users without Python/transformers installed, but they're not as accurate as DictaBERT on contemporary tech Hebrew.

| Service | URL | Notes |
|---|---|---|
| **Rephrasely (Hebrew grammar)** | https://rephrasely.com/modes/hebrew-grammar-checker | Web tool, commercial, paywall on heavy use |
| **JustDone Hebrew** | https://justdone.com/grammar-check/hebrew-grammar-checker | Web tool, mixed quality |
| **Sapling (Hebrew spell)** | https://sapling.ai/lang/hebrew | Spell only, not grammar |
| **Stars21 Hebrew Spell** | https://www.stars21.com/spelling/hebrew/ | Spell only, free |
| **Hastewire** | https://hastewire.com/grammar-checker/he | Free Hebrew grammar checker |
| **LingVanex Hebrew Grammar** | https://lingvanex.com/services/grammar-checker-hebrew/ | Commercial, GDPR-compliant |

These services don't expose stable APIs and aren't suitable for the skill's automated validation. They're listed for completeness.

---

## Tier 4 — Generative LLM for Hebrew grammar questions

When the rule isn't in the catalog and no parser settles it, use a Hebrew-native LLM:

### DictaLM 3.0 24B Thinking

**Model:** `dicta-il/DictaLM-3.0-24B-Thinking` on HuggingFace

**Use case:** ask grammatical or stylistic questions in Hebrew, get reasoned answers in Hebrew. Best for *"is this sentence natural?"* / *"which preposition fits here?"* / *"is this binyan correct for this verb?"* type questions.

**Access:** HuggingFace Inference API or local GGUF download. Free with rate limits.

### Claude with explicit Hebrew system prompt

**Use case:** the skill itself, running on Claude, is the LLM-grounded Hebrew validator. Claude Opus 4.7 with an explicit Hebrew grammar prompt outperforms most dedicated Hebrew tooling on subjective phrasing and idiomaticity questions.

This is what the skill's STEP 5 (Validate) does in methodology mode.

---

## Tier 5 — Related Claude Skills

These skills are complementary; the Ah Sheli Gibor skill delegates to them in scope:

| Skill | What it covers | When to invoke |
|---|---|---|
| **hebrew-content-writer** | General Hebrew register, smikhut, et marker, ktiv maleh, gender, common writing mistakes, SEO | For non-tech content. Where it conflicts with this skill on fundamentals, **hebrew-content-writer wins**. |
| **hebrew-rtl-best-practices** | CSS logical properties, dir attributes, bidi text isolation, framework setup | For RTL rendering issues in HTML/web output. |
| **hebrew-document-generator** | Hebrew PDF / DOCX / PPTX generation with proper RTL paragraph properties and font support | For physical document output. |
| **hebrew-i18n** | Date / currency formatting, Hebrew plural forms (singular / dual / plural), bidi mixed content | For numerical and i18n formatting concerns. |

---

## Decision matrix: which tool for which check

| Check | Methodology mode | Tool-assisted mode |
|---|---|---|
| Gender of a noun | corpus lookup → grammar_layer.md §2 → Morfix | DictaBERT `morph.feats.Gender` |
| Binyan of a verb | corpus lookup → grammar_layer.md §1 → Morfix | DictaBERT `morph.feats.HebBinyan` |
| Subject-verb agreement | inspection against rule | DictaBERT syntax tree |
| Smikhut definite-article rule | inspection against grammar_layer.md §3 | DictaBERT `morph.feats.Definite=Cons` |
| Preposition + loanword hyphen | regex against `\b[בלמכש]-?(MCP\|IAM\|...)\b` | scripts/hebrew_validate.py rule |
| בערך → כ- correction | regex against `בערך \d` | scripts/hebrew_validate.py rule |
| "אני הולך ל-" anglicism | regex against pattern | scripts/hebrew_validate.py rule |
| Filler-word presence | regex against אז/כאילו/בעצם/למעשה/פשוט | scripts/hebrew_validate.py rule |
| Spelling (niqqud-less) | inspection vs corpus | Hspell (with loanword caveat) |
| Idiomaticity / naturalness | persona-voice review STEP 5c | DictaLM or Claude self-check |
| Word order naturalness | persona-voice review STEP 5c | LLM judgment |

---

## How the skill uses this toolchain

By default the skill runs in **methodology mode** — STEP 5 applies all the rule checklists inline without invoking external tools. This is the cheapest, fastest, and most portable path.

When the user requests **tool-assisted validation** (e.g., *"validate this output with DictaBERT"* or *"run the grammar script"*), the skill invokes `scripts/hebrew_validate.py` with the relevant flags. The script returns a structured issue report which the skill incorporates into STEP 5 output.

The user can also run `scripts/hebrew_validate.py` standalone against any Hebrew text file, independent of the skill's normal flow.

---

*Last updated: 2026-05-18 for v0.3.0.*
