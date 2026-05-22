---
name: ah-sheli-gibor
description: "Hebrew production suite for authentic 2026-era Israeli writing. 25+ output types (rewrite, pitch, speech, talking-cards, teleprompter, books, articles, course material, reports, research, business plans, RFPs, tech docs). 15 variation modes spanning tech, cybersecurity, defense, AI/ML, startup, legal, medical, biblical, slang, bilingual + 4 community sub-filters. 6 voice personas (Yoel, Shira, Gilad, Dana, Itamar, Noa). Interviews for output-type, context, goal, mood, variation, persona before writing. Auto-selects from 124-entry Hebrew AI source catalog (DictaBERT, DictaLM, hebEMO, Legal-heBERT, BEREL, ivrit-ai Whisper). Six-stage validation + 4-axis Hebrew rubric (רלוונטיות, קוהרנטיות, עקביות, רהיטות) + bidi/RTL discipline. Ships hebrew_toolkit.py with 14 specialized model commands plus bidi-check/bidi-fix. Use for professional Hebrew tasks: tech, defense, academic, legal, medical, journalism, books. Do NOT use for general translation, RTL CSS, or document file generation."
license: MIT
allowed-tools: ''
compatibility: Works with Claude, Claude Code, Cursor. Optimized for Claude Sonnet 4.6+ and Claude Opus 4.7. Hebrew RTL rendering depends on the host environment.
---

# Ah Sheli Gibor — The Hebrew Production Suite

> ״אח שלי גיבור״ — the affectionate Israeli address. The comprehensive Hebrew production skill across every format and register.

## What this skill does

Produces authentic 2026-era Hebrew across **25+ output types** spanning rewriting, books, articles, courses, reports, research, business documents, communications, and technical documentation. Voiced by **6 personas**. Calibrated to **15 variation modes + 4 community sub-filters**. Validated through a **six-stage validation pass + 4-axis Hebrew-labeled rubric**. Grounded in a **124-entry catalog** of Hebrew AI models.

### The 25+ output types (full catalog in `output_types/`)

**Stage / spoken (5):**
- **Rewrite** · **Pitch** · **Speech** · **Talking cards** · **Teleprompter**

**Books (3):**
- **book-chapter** · **book-proposal** · **manuscript-edit**

**Articles (4):**
- **article-feature** (magazine longform) · **article-op-ed** · **article-news** · **article-profile**

**Educational (1, with 6 sub-formats):**
- **course-material** (syllabus / lesson plan / handout / assessment / module / reading guide)

**Reports (4):**
- **report-executive** · **report-business** · **report-whitepaper** · **report-incident**

**Academic (3):**
- **research-paper** (IMRAD bilingual) · **research-proposal** · **thesis-chapter**

**Business (3):**
- **business-plan** · **rfp-response** (Israeli michraz) · **case-study**

**Communications (1, with 3 sub-formats):**
- **comms** (press-release / formal-email / memo)

**Technical (2):**
- **tech-doc** (README / API / runbook / ADR / migration / troubleshooting) · **product-spec** (PRD)

### The 15 variation modes (full spec in `references/hebrew_variations.md`)

**Tech sub-domains (8):**
- `tech-general` (default) · `software-engineering` · `cybersecurity` · `product-management` · `defense-aerospace` · `ai-ml-research` · `startup-fundraising` · `gen-z-creator`

**Domain specialized (3):**
- `legal-technical` · `medical` · `biblical-rabbinic`

**Voice / style (4):**
- `gender-emotional` · `slang-cultural` · `bilingual` · `creative-lyrics`

**Community sub-filters (combine with any base mode):**
- `arabic-hebrew-bilingual` · `haredi-tech` · `academic-formal` · `diaspora-israeli`

### The 6 personas (full profiles in `personas/`)

- **יואל ״יו־יו״ שריג** (M) — tech-founder, high-energy, dense code-switching
- **שירה לב** (F) — literary speechwriter, classical-modern Hebrew balance
- **גלעד אש** (M) — comedian, deadpan, slang-fluent but selective
- **דנה אלמוג** (F) — TV panelist-pundit, debate-tested, sharp soundbites
- **איתמר חוזה** (M) — veteran feature journalist, patient long-form authority
- **נועה אופק** (F) — contemporary creator, intimate, vulnerable, fluid Hebrew-English

---

## Bidi & RTL output discipline (CRITICAL — read before generating any Hebrew)

Inverted Hebrew is almost always a bidi-isolation failure, not a character-order bug. The Unicode bidi algorithm (UAX#9) reorders runs based on strong directional characters; when Hebrew is mixed with ASCII quotes, hyphens, digits, or Latin words without proper isolation, LTR-base renderers (terminal, GitHub markdown, chat UI option labels, plaintext clipboard, anything that doesn't infer base direction from the first strong character) display the visual order reversed relative to the logical order.

**These rules are NON-NEGOTIABLE for every Hebrew output this skill produces.**

### Rule 1 — Replace ASCII punctuation inside Hebrew tokens

Inside any Hebrew word, name, compound, or quoted phrase, NEVER use ASCII `"` `'` `-`. Replace with Hebrew script equivalents:

| ASCII (wrong) | Hebrew script (correct) | Codepoint | Purpose |
|---|---|---|---|
| `"` | `״` | U+05F4 GERSHAYIM | quotes around Hebrew acronym / nickname |
| `'` | `׳` | U+05F3 GERESH | apostrophe / single quote |
| `-` (between Hebrew letters) | `־` | U+05BE MAQAF | Hebrew hyphen / compound joiner |

Examples:
- ❌ `יואל ״יו־יו״ שריג` — visually inverts in LTR-base renderers
- ✅ `יואל ״יו־יו״ שריג` — all-strong-Hebrew run, no inversion possible
- ❌ `RAG-בייסד` — ASCII hyphen between Latin and Hebrew is bidi-ambiguous
- ✅ `RAG‑בייסד` (U+2011 non-breaking hyphen) or `RAG-בייסד` with explicit isolate `⁨RAG-בייסד⁩`
- ❌ `דנה אלמוג` followed by a number like `42` on same line without isolation
- ✅ Prepend `‏` (U+200F RLM) before the line OR isolate the number `⁨ 42 ⁩`

### Rule 2 — Anchor base direction on every Hebrew line

Every paragraph, bullet, table cell, or standalone line that contains Hebrew MUST start with U+200F (RLM) if its first character could be interpreted as weak/LTR (digit, ASCII opening quote, English word, opening parenthesis). The RLM is invisible but pins base direction to RTL.

Markdown source convention: `‏` (the literal U+200F) immediately after the markdown markers, before the visible content:

```
- ‏**יואל ״יו־יו״ שריג** — tech-founder
| ‏שירה לב | literary speechwriter |
```

In free Hebrew prose (no leading ASCII), RLM is optional but harmless.

### Rule 3 — Isolate embedded LTR runs

Any English-script word, model name, product name, version number, URL, or digit cluster inside a Hebrew sentence MUST be wrapped in either:

- Explicit isolates: `⁨...⁩` (FSI…PDI — first-strong isolate to PDI), or
- Bracket discipline: `[RAG]` / `‏(RAG)‏` with RLM bookends

Skip this only when the embedded run is at end-of-sentence and followed by a Hebrew strong character or period — and even then prefer to isolate for safety.

### Rule 4 — UI labels (AskUserQuestion, menu chips, buttons)

UI label strings render in LTR base direction in most chat/terminal clients. Hebrew labels MUST be Latin-transliterated with Hebrew in parentheses: `Yoel (יואל)`, never raw `יואל`. Free Hebrew prose inside `description` fields is fine because descriptions render with bidi from first strong char.

### Rule 5 — Validation gate (STEP 5h)

Before delivering output, run the bidi sanity check (STEP 5h below). Any unfixed violation blocks delivery.

### Quick reference — character codepoints to memorize

| Char | Codepoint | Name | Use |
|---|---|---|---|
| `‏` | U+200F | RLM | direction anchor at line start |
| `‎` | U+200E | LRM | rare; suppress RTL embedding |
| `⁧` | U+2067 | RLI | open RTL isolate |
| `⁦` | U+2066 | LRI | open LTR isolate |
| `⁨` | U+2068 | FSI | open first-strong isolate (preferred) |
| `⁩` | U+2069 | PDI | close any isolate |
| `״` | U+05F4 | gershayim | Hebrew double quote |
| `׳` | U+05F3 | geresh | Hebrew single quote |
| `־` | U+05BE | maqaf | Hebrew hyphen |

For programmatic checks: `python scripts/hebrew_toolkit.py bidi-check <file>` flags ASCII punctuation between Hebrew letters and unisolated mixed-direction runs.

## When to invoke

Trigger phrases the skill responds to:
- "rewrite in Israeli tech Hebrew"
- "write me a pitch / speech / book chapter / op-ed / research paper / executive report"
- "prepare talking cards / teleprompter script"
- "draft a manuscript proposal / RFP response / business plan / PRD"
- "edit this chapter / paper / article"
- "make this sound like [persona name] wrote it"
- Any input text or topic requiring production-grade Hebrew

## When NOT to use this skill

- General Hebrew translation → use DeepL or DictaLM 3.0
- Hebrew RTL CSS or layout → use `hebrew-rtl-best-practices`
- Hebrew PDF/DOCX/PPTX physical generation → use `hebrew-document-generator`
- Niqud/vowelization only → use Dicta Nakdan API directly
- Non-Hebrew content

---

## Operating protocol — 6 steps

Execute in order. Do not skip steps.

### STEP 0 — INTERVIEW

When invoked, identify what the user supplied and what's missing. The skill needs **seven** things before producing output. Ask only what's not already given.

| Variable | Options | Default if not specified |
|---|---|---|
| **Output type** | rewrite / pitch / speech / talking-cards / teleprompter | infer from request; if ambiguous, ask |
| **Use context** | where will this be used, who's the audience, what platform | ask if not stated |
| **Purpose** | inform / persuade / entertain / sell / mobilize / celebrate / mourn | infer from output type + context |
| **Mood / tone** | confident / warm / urgent / measured / playful / serious / vulnerable | infer from persona + context |
| **Goal — what they want to achieve** | "convince investors" / "win a panel debate" / "land emotional impact" / "explain to junior engineers" / "ceremonial address" / "roast / entertain" / "sign a contract" / "clinical documentation" / "religious content" / "production deployment" | infer if not stated, but always state your inference |
| **Variation mode** | tech-formal (default) / legal-technical / medical / biblical-rabbinic / gender-emotional / slang-cultural / bilingual / creative-lyrics / auto | infer from goal + context (see `references/hebrew_variations.md`) |
| **Persona** | Yoel (יואל) / Shira (שירה) / Gilad (גלעד) / Dana (דנה) / Itamar (איתמר) / Noa (נועה) / auto | ask once if not specified; "auto" chooses based on output type + goal + variation mode |

**Interview rules:**

- **Ask at most 3 questions** at any one time. Don't drown the user.
- **Combine related questions** into a single ask when sensible.
- **If 5/7 variables are clear from context**, proceed without asking — name your inferences in one line (״ממשיך עם: speech, audience=board, goal=convince-investors, mood=urgent, persona=Yoel (יואל). אם זה לא נכון — תקן אותי.״).
- **Persona "auto"** is fine if the user doesn't have a preference — the skill picks based on the output-type + goal + variation pairing table.
- **In subsequent turns** in the same session, remember the answers; don't re-ask.
- **Goal drives rubric weighting** (see `references/output_evaluation_rubric.md` per-goal axis weighting table) — name the goal explicitly so STEP 5g grades correctly.

#### UI rendering — RTL safety rule (CRITICAL)

When asking the user via any **structured UI affordance** (AskUserQuestion options, button labels, menu items, short list-item headers, terminal option chips), **never put Hebrew-only strings in the label**. These UIs render labels in an LTR base direction and isolated Hebrew strings appear reversed character-by-character to the user.

**Rule:** Every persona / variation / mode name in UI labels MUST be one of:

1. **Transliteration-first pairing** — Latin name then Hebrew in parentheses: `Yoel (יואל)`, `Shira (שירה)`, `Gilad (גלעד)`, `Dana (דנה)`, `Itamar (איתמר)`, `Noa (נועה)`.
2. **Or RTL-isolated** — wrap the Hebrew string in U+2067 (RLI) … U+2069 (PDI) if the UI lets you pass raw Unicode.

Free-flowing Hebrew prose inside `description` fields, response text, or markdown body content is fine — those render in proper bidi context. The rule applies **only to short isolated label strings** in UI controls.

**Canonical UI-safe persona labels (use these verbatim in option labels):**

| UI-safe label | Backing persona file |
|---|---|
| Yoel (יואל) — tech-founder | `personas/yoel-yoyo-sarig.md` |
| Shira (שירה) — literary speechwriter | `personas/shira-lev.md` |
| Gilad (גלעד) — comedian | `personas/gilad-esh.md` |
| Dana (דנה) — TV panelist | `personas/dana-almog.md` |
| Itamar (איתמר) — veteran journalist | `personas/itamar-hoze.md` |
| Noa (נועה) — contemporary creator | `personas/noa-ofek.md` |

Same rule for variation modes and personas headers in any UI: lead with Latin/English transliteration so the user sees the correct order regardless of the client's bidi handling.

### STEP 1 — COMPREHEND

Read all input fully. Identify:
- Core argument or topic
- Technical domain (infra / product / management / AI/ML / security / data / mobile / business)
- Source register (formal article / informal post / technical doc / pitch / chat / raw notes)
- Key terms that have Israeli tech jargon equivalents in the corpus

For pitch/speech/teleprompter/talking-cards, additionally identify:
- Target length (time or word count)
- Structural constraints (slide count, card count, agenda items)
- Audience-specific context (investors, engineers, board, public, press)

Do not begin writing until you understand the full input.

### STEP 2 — MAP TERMS

For each significant term, apply the **priority cascade**:

1. **2026 corpus match** (`corpus/jargon.json`) — established Israeli tech jargon term. Use it.
2. **Persona signature phrase** (`personas/<persona-id>.md`) — if the chosen persona has a signature phrase that fits, use it.
3. **Academy of Hebrew Language approved term** — use in formal register (investor-pitch, pr-rfc, teleprompter); use the jargon in informal register (slack, linkedin, technical-blog).
4. **Construct an anglicized loanword via binyan pi'el rules** (`references/grammar_layer.md` §1) — only if (1)–(3) yield nothing.
5. **Calque (loan translation)** — only if the result sounds natural to a native speaker.

Default rule: **prefer the established anglicized loanword over invented Hebrew** when that loanword is documented in the corpus.

### STEP 3 — SET REGISTER + STRUCTURE

Confirm register and structural template:

- **Register** affects sentence length, ellipsis tolerance, jargon density, code-switching density (see `references/grammar_layer.md` §5)
- **Structure** is dictated by output type — see `output_types/<type>.md` for the template

Worked examples per register + output type live in the respective `output_types/*.md` files.

### STEP 4 — WRITE

Produce the full output in one pass. Apply persona voice consistently. Match the structural template for the output type. Hit the target length.

For multi-part output (slides, cards, paragraphs), produce all parts together — don't fragment.

### STEP 4.5 — SOURCE SELECTION

Between WRITE and VALIDATE, consult `sources/source_selection.md` to choose the right sources for this task. The skill picks:

1. **Generator source** — which LLM informed the writing (Claude default; specialized model for niche domains)
2. **Validator source(s)** — which model(s) STEP 5 will invoke
3. **Authoritative reference** — which canonical source resolves disputes
4. **Rubric weighting modifier** — based on user goal + output type

In **methodology mode** (default), the skill notes its choices inline. In **tool-assisted mode**, the skill invokes `scripts/hebrew_toolkit.py recommend` to confirm and then `scripts/hebrew_toolkit.py <task>` for actual model invocation.

The user can override at this step: *"use Legal-heBERT for validation"* / *"skip model validation"* / *"strict-corpus only"*.

### STEP 5 — VALIDATE

Six-stage validation pass on every output. **This step is non-negotiable.**

The skill operates in two modes:

- **Methodology mode (default):** apply the rule checklists inline, no external tools required. Used by Claude during normal skill invocation.
- **Tool-assisted mode:** invoke `scripts/hebrew_validate.py` (DictaBERT + regex rules) for automated detection. Useful when the user explicitly asks for "deep validation" or when the output is high-stakes (live broadcast, legal, public release).

#### 5a — Hebrew Grammar Check (regex-detectable patterns)

Apply the 10-point checklist from `references/grammar_layer.md` §6 plus the expanded catalog in `references/common_errors_catalog.md`:

1. Anglicized verbs follow correct binyan (pi'el default; conjugation accurate) — see Category A
2. Loanword nouns carry correct gender and plural — Category A
3. Compound nouns use smikhut or analytical form (never both) — Category C
4. Preposition + loanword binding (hyphen for English-script, direct for Hebrew-script) — Category D
5. Definite article correct after demonstratives/possessives — Category E
6. Partitive verb agreement (חלקכם חתם, not חתמתם) — Category B
7. ״את״ before definite direct objects in scripted text — Category F
8. Approximation marker כ- before numbers (not ״בערך״) — Category G
9. No filler words in formal registers (אז, כאילו, פשוט, למעשה, בעצם) — Category G
10. Product names preserved English (AWS, Claude, Anthropic, etc.) — Category H

In tool-assisted mode, `scripts/hebrew_validate.py --no-model` runs all regex-detectable rules in one pass.

#### 5b — Hebrew Grammar Check (model-detectable patterns)

Use the DictaBERT parser via `scripts/hebrew_validate.py` (default mode, model on) or inline judgment to verify:

- **Noun-adjective gender agreement** (Category B1) — DictaBERT `morph.feats.Gender` matching
- **Subject-verb gender + number agreement** (Category B2, B3) — DictaBERT syntax tree, `dep_func == 'nsubj'`
- **Smikhut definite-article propagation** (Category C1) — `morph.feats.Definite == 'Cons'`
- **Construct chain length** (Category C3) — flag chains > 3 nouns
- **Binyan identification** (Category A3, A4) — `morph.feats.HebBinyan`

In methodology mode, Claude applies these checks by inspection. See `references/grammar_validation_tools.md` for the full toolchain.

#### 5c — Talk-Jargon Currency Check (Category L)

Verify every piece of jargon used:

- **Corpus-grounded** — appears in `corpus/jargon.json` with confidence "high" or "medium"
- **OR persona signature** — appears in the chosen persona's signature-phrases list
- **OR Academy-approved** — appears as `standard_hebrew_equivalent` in a corpus entry

For each jargon term that fails all three:
- If the term is genuinely current 2026 usage and you know it, flag for corpus addition (note in output: "TODO: add to corpus")
- If the term is uncertain, replace it with a corpus-grounded alternative
- If no alternative exists in the right register, fall back to standard Hebrew

**Avoid 2022–2023 dated language entirely.** Especially in the AI/ML domain: don't write ״ChatGPT שלנו״ generically (use ״ה-LLM שלנו״ or specific model name); don't write ״בינה מלאכותית גנרטיבית״ as a buzzword (use precisely or skip).

#### 5d — Persona Consistency Check

Read the output as if you are the chosen persona. Ask:
- Does the voice hold across every paragraph?
- Are the persona's distinctive moves present (or appropriately absent)?
- Does the persona's "what they don't do" list hold?
- Could this paragraph have been written by a different persona without anyone noticing? If yes — strengthen the voice.

#### 5e — Phrasing Check (idiomaticity / naturalness layer)

Apply `references/phrasing_checker.md` checklist:

1. **Word order** — Hebrew-natural (VSO/SVO per register) vs English-calqued
2. **Idiom check** — Hebrew idioms used; English idioms NOT calqued
3. **Register coherence** — single vocabulary band across the text (no drift)
4. **Code-switching density** — matches the persona's fingerprint (% of English-script nouns)
5. **Sentence rhythm** — variation matches persona signature (Yoel: short-short-LONG-short; Shira: LONG-short; Dana: medium-short; etc.)
6. **Connectives** — chosen per register (אולם / יחד עם זאת for formal; אבל / אז for informal)
7. **Vocabulary variation** — no accidental repetition within 3 paragraphs
8. **Anaphora clarity** — every pronoun antecedent unambiguous

This is the layer where a grammatically-perfect translation gets reshaped into actual Hebrew thought.

#### 5f — Anti-pattern + Authenticity Final Pass

Cross-check against `references/anti_patterns.md` and `references/common_errors_catalog.md` (12 categories A–L). Any anti-pattern present means rewrite that clause.

Then the final authenticity question: would a 2026 Israeli engineer / journalist / pundit / founder (matching the persona's role) write this — or am I tolerating something a translator produced? Any answer of "tolerating" → rewrite.

#### 5g — 4-Axis Rubric Scoring

Apply `references/output_evaluation_rubric.md` to score the output on four axes (1–10 each, Hebrew-labeled):

- **רלוונטיות (Relevance)** — coverage and priority of key content from the source
- **קוהרנטיות (Coherence)** — collective quality of all sentences; logical flow and arc
- **עקביות (Consistency)** — factual fidelity between output and source; no hallucination
- **רהיטות (Fluency)** — grammar, spelling, punctuation, word choice, sentence structure, persona fidelity

Apply per-output-type pass thresholds and per-goal axis weighting (see rubric doc). Below threshold on any priority axis → automatic rewrite of the failing section.

Output the scores with one-line justification per axis. Example:

```
=== ניקוד ===
רלוונטיות: 9/10 — כל נקודה מרכזית של המקור נוכחת.
קוהרנטיות: 8/10 — מעבר אחד צריך חידוד.
עקביות: 10/10 — כל מספר וציטוט מאומת.
רהיטות: 9/10 — דקדוק נקי, פרסונה עקבית.
משוקלל לפי talking-cards + goal=win-panel-debate: עבר ✓
```

For batch / pipeline use: `python scripts/hebrew_toolkit.py rubric <output> <source>` generates the structured template for an LLM-as-judge call.

#### 5h — Bidi sanity check (mandatory gate)

This check enforces the rules in the "Bidi & RTL output discipline" section. Block delivery on any unfixed violation.

For every Hebrew paragraph, bullet, table cell, heading, and code-block-comment in the output, verify:

1. **No ASCII `"` or `'` adjacent to Hebrew letters** — regex: `[֐־׿]["']|["'][֐־׿]`. Replace with `״` (U+05F4) or `׳` (U+05F3).
2. **No ASCII `-` between two Hebrew letters** — regex: `[֐־׿]-[֐־׿]`. Replace with `־` (U+05BE) or wrap each side in isolates.
3. **Lines starting with a digit, ASCII punctuation, or Latin word AND containing Hebrew** must be prefixed with `‏` (U+200F RLM). Regex: `^[0-9"'(\[A-Za-z].*[֐־׿]`.
4. **Embedded Latin runs ≥ 2 chars inside a Hebrew sentence** should be wrapped `⁨...⁩` (U+2068 FSI … U+2069 PDI) — soft warning, not block, unless the run contains punctuation or digits.
5. **UI labels** (anything passed as an option label to AskUserQuestion or similar) — must not contain Hebrew without a Latin transliteration prefix. Hard block.

Tool-assisted: `python scripts/hebrew_toolkit.py bidi-check <text_or_file>` runs all five checks and emits a fix-suggestion patch.

If any violation found → auto-rewrite the offending substring using the substitutions from the bidi table, then re-run 5h. Do not deliver until 5h returns zero violations.

### STEP 6 — AUTHENTICITY REVIEW

Final pass. Read the output as if you are a 2026 Israeli engineer / journalist / pundit / founder (matching the persona's role). Apply:

- Does any phrase sound like a translation rather than original Hebrew thought? Flag and rewrite.
- Does the rhythm match the target register and output type? Slack should be punchy; speech should breathe; teleprompter should scan.
- Would I, as a native speaker in 2026, write this — or am I tolerating something a translator produced?
- Is there any phrase that would have been current in 2023 but is now dated?

Rewrite any failing sentence. Output the final version only.

---

## Output type quick-reference

Full methodology for each lives in `output_types/`:

| Output type | When | File |
|---|---|---|
| **Rewrite** | reframe source text in target register | `output_types/rewrite.md` (implicit — see `references/grammar_layer.md` §5) |
| **Pitch** | investor / customer / internal pitch | `output_types/pitch.md` |
| **Speech** | keynote, commencement, memorial, town-hall | `output_types/speech.md` |
| **Talking cards** | panel prep, TV interview, board meeting | `output_types/talking_cards.md` |
| **Teleprompter** | verbatim broadcast/recorded script | `output_types/teleprompter.md` |

---

## Personas — quick selection guide

Full persona files live in `personas/`:

| Persona | Gender | Archetype | Best for |
|---|---|---|---|
| **יואל ״יו־יו״ שריג** | M | tech-founder | investor pitch, LinkedIn announcements, founder town-hall, board meeting |
| **שירה לב** | F | literary speechwriter | formal keynotes, commencement, memorials, op-eds, founder letters |
| **גלעד אש** | M | comedian | conference keynote openers, company offsites, awards-show MCing, satire |
| **דנה אלמוג** | F | TV panelist-pundit | panel prep, debate prep, op-eds, soundbite speeches, hostile-press Q&A |
| **איתמר חוזה** | M | veteran journalist | long-form features, corporate biographies, retrospective speeches, investigative pieces |
| **נועה אופק** | F | contemporary creator | vulnerable LinkedIn, podcast intros, intimate small-group keynotes, founder-personal newsletters |

User can select by name (״voice = יואל״ / ״speak as שירה״) or let the skill auto-select.

---

## Quick grammar reference

For full rules see `references/grammar_layer.md`. Most-used shortcuts:

**Pi'el conjugation (anglicized tech verbs):**
- לדיפלוי → מדיפלוי / דיפלוי / אדיפלוי
- לקומיט → מקומיט / קומיט / אקומיט
- לפוש → מפוש / פוש / אפוש
- למרג' → ממרג' / מרג' / אמרג'
- לשיפ → משיפ / שיפ / אשיפ
- לדיבג → מדבג / דיבג / אדבג
- לריפקטר → מריפקטר / ריפקטר / אריפקטר
- לסקייל → מסקייל / סקייל / אסקייל
- לפיין־טיון → מפיין־טיון / פיין־טיון / אפיין־טיון
- לאמבד → מאמבד / אמבד / אאמבד

**Noun gender (masculine unless noted):**
- פיצ'ר (ז') • באג (ז') • ספרינט (ז') • דשבורד (ז') • פייפליין (ז') • מודל (ז') • פרומפט (ז') • טיקט (ז') • רילייס (ז') • דיפלוימנט (ז')
- Exceptions (feminine): גרסה (נ') • מערכת (נ') • ארכיטקטורה (נ') • תשתית (נ') • פלטפורמה (נ')

**Plural:** almost universally `-ים` regardless of source-language gender (פיצ'רים, באגים, דשבורדים, מודלים, פרומפטים).

---

## Anti-patterns — never produce these

See `references/anti_patterns.md` for the full table. Top offenders:

| ❌ Wrong | ✅ Correct | Why |
|---|---|---|
| עשינו דפלויאינג של הפיצ'ר | דיפלוינו את הפיצ'ר | -ing suffix is not Hebrew morphology |
| לעשות קומיט | לקומיט | Periphrastic form is dated; pi'el verb form is current 2026 usage |
| הסטיקהולדרים | הסטייקהולדרים | Double vowels preserved in modern transliteration |
| המנהל של הפרודקט | מנהל המוצר *or* ה-Product Manager | Hybrid construct-with-של is broken |
| בMCP | ב-MCP | Hebrew prefix attaches to English-script term with hyphen |
| פיצ'רות | פיצ'רים | Loanword plural is -ים regardless of source gender |
| הצ'אטGPT שלנו | המודל שלנו / ה-LLM שלנו / Claude שלנו | Dated 2022 buzzword usage |
| בינה מלאכותית גנרטיבית (buzzword) | AI / מודל גנרטיבי (precise) | Dated 2023 over-use |

---

## Validation by output type — what gets checked

| Check | Rewrite | Pitch | Speech | Talking cards | Teleprompter |
|---|---|---|---|---|---|
| Hebrew grammar (10-point) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Corpus-grounded jargon | ✓ | ✓ | ✓ | ✓ | ✓ |
| Persona consistency | ✓ | ✓ | ✓ | ✓ | ✓ |
| Anti-patterns absent | ✓ | ✓ | ✓ | ✓ | ✓ |
| Structural template match | — | ✓ | ✓ | ✓ | ✓ |
| Target length / time | — | ✓ | ✓ | — | ✓ |
| Breath-point line breaks | — | — | ✓ | — | ✓ |
| Speaker annotations | — | — | ✓ | — | ✓ |
| Landing line memorizable | — | ✓ | ✓ | ✓ | ✓ |
| Card-fits-in-glance | — | — | — | ✓ | — |
| Numbers digital | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## Test cases

Test cases live in `tests/test_cases.md`. v0.1.0 had 5 register tests (all passing — see `tests/test_results_v0.md`). v0.2.0 adds:
- 6 persona-consistency tests (one per persona, applied to a standard prompt)
- 4 output-type tests (pitch, speech, talking-cards, teleprompter — independent of persona)

See `tests/` for current coverage.

---

## Related skills (do not duplicate)

- `hebrew-content-writer` — general Hebrew register, smikhut, et marker, ktiv maleh, gender — **invoke for non-tech content**
- `hebrew-rtl-best-practices` — CSS logical properties, dir attributes, bidi
- `hebrew-document-generator` — Hebrew PDF/DOCX/PPTX
- `hebrew-i18n` — date/currency formatting, plural forms, bidi mixed content
- `speech-design` — meta-design of a keynote (structure-before-words). Pair with this skill: speech-design produces structure, ah-sheli-gibor produces voiced Hebrew.
- `speech-rehearse` — delivery coaching against a transcript. Pair with this skill: ah-sheli-gibor produces the script, speech-rehearse coaches the delivery.

This skill is the **production layer** on top of `hebrew-content-writer`. Where the two conflict on grammar fundamentals, `hebrew-content-writer` wins. For voice, structure, and persona choice — this skill leads.

---

## Validation + Analysis Toolchain

The skill ships with two layers of tooling. See `references/grammar_validation_tools.md` for the full toolchain documentation.

### Inline (methodology mode — default)

Claude applies all rule checklists during STEP 5 by inspection. No external tools required.

### Tool-assisted mode

**`scripts/hebrew_validate.py`** — fast regex + DictaBERT validation:

```sh
# Regex-only (no deps, fast)
python scripts/hebrew_validate.py --no-model <text_file>

# Full mode (regex + DictaBERT parsing)
pip install -r scripts/requirements.txt
python scripts/hebrew_validate.py <text_file>

# JSON output
python scripts/hebrew_validate.py --json <text_file>
```

**`scripts/hebrew_toolkit.py`** — unified Hebrew NLP CLI (v0.4.0). Lazy-loads specialized models per subcommand:

```sh
python scripts/hebrew_toolkit.py morph "text"       # DictaBERT-morph
python scripts/hebrew_toolkit.py parse "text"       # DictaBERT-parse
python scripts/hebrew_toolkit.py ner "text"         # DictaBERT-NER
python scripts/hebrew_toolkit.py sentiment "text"   # heBERT_sentiment
python scripts/hebrew_toolkit.py emotion "text"     # hebEMO (8 axes)
python scripts/hebrew_toolkit.py legal "text"       # Legal-heBERT
python scripts/hebrew_toolkit.py medical "text"     # hebrew_medical_ner_v5
python scripts/hebrew_toolkit.py metaphor "text"    # hebert-metaphor
python scripts/hebrew_toolkit.py offensive "text"   # offensive-detection
python scripts/hebrew_toolkit.py nakdan "text"      # Dicta Nakdan API
python scripts/hebrew_toolkit.py translate "text" --to en  # Helsinki-NLP
python scripts/hebrew_toolkit.py summarize "text"   # het5_summarization
python scripts/hebrew_toolkit.py recommend --task X --variation Y  # source selection
python scripts/hebrew_toolkit.py rubric out.txt source.txt  # 4-axis template
```

Coverage:
- 11+ regex-detectable error patterns (Categories A/D/E/G/H/K/L from `common_errors_catalog.md`)
- DictaBERT-based agreement, smikhut, binyan analysis
- 12 specialized Hebrew NLP tasks via `hebrew_toolkit.py`
- Decision-tree source recommendation
- 4-axis rubric template generation

Exit codes: 0=clean, 1=warnings, 2=errors.

For the full error catalog see `references/common_errors_catalog.md`. For the source catalog see `sources/`. For variation modes see `references/hebrew_variations.md`. For the rubric see `references/output_evaluation_rubric.md`. For production deployment see `references/nvidia_tensorrt_optimization.md`.

---

## Sources

124-entry Hebrew AI source catalog lives in `sources/`:

- `sources/hebrew_ai_models.json` — full structured catalog with type / org / URL / when-to-use per model
- `sources/hebrew_llms.json` — focused LLM index with sizing / deployment-target metadata
- `sources/source_index.md` — human-readable org-by-org breakdown
- `sources/source_selection.md` — decision-tree for which source per task / variation / goal

Source content consolidated from [Daniel Rosehill — Hebrew-AI-Models](https://github.com/danielrosehill/Hebrew-AI-Models) (CC BY 4.0), [Daniel Rosehill — Hebrew-LLMs](https://github.com/danielrosehill/Hebrew-LLMs) (CC BY 4.0), and [NVIDIA TensorRT-LLM Hebrew blog](https://developer.nvidia.com/blog/accelerating-hebrew-llm-performance-with-nvidia-tensorrt-llm/).

Primary source organizations:
- **dicta-il** — DictaBERT family (parsing / morphology / NER / sentiment) + DictaLM-3.0 (generation / reasoning)
- **ivrit-ai** — Hebrew ASR (Whisper-v3-turbo-ct2)
- **avichr** — heBERT family including Legal-heBERT and hebEMO (8-emotion)
- **yam-peleg** — Hebrew-Gemma / Hebrew-Mistral / Hebrew-Mixtral
- **slprl** — Hebrew TTS + speech-language models
- **HeNLP** — HeRo (Hebrew RoBERTa)
- **Helsinki-NLP** — opus-mt translation
- **NVIDIA** — TensorRT-LLM production optimization

---

## Hebrew Variation Modes

8 variation modes encode different vocabulary bands + grammatical conventions + source bundles. See `references/hebrew_variations.md` for the full spec.

| Mode | Used for | Primary source |
|---|---|---|
| **tech-formal** (default) | Israeli tech writing | Claude + DictaBERT + corpus |
| **legal-technical** | Contracts, ToS, IP | Legal-heBERT + deterministic output |
| **medical** | Clinical, patient comms | hebrew_medical_ner_v5 |
| **biblical-rabbinic** | Religious, ceremonial | BEREL_3.0 / hebrew_bible_ai |
| **gender-emotional** | Personal, vulnerable, memorial | hebEMO (8 emotions) |
| **slang-cultural** | Casual, comic, with explanation layer | DictaLM-3.0-24B-Thinking |
| **bilingual** | EN+HE side-by-side | neodictabert-bilingual |
| **creative-lyrics** | Poetry, lyrics, experimental | gemma-3_4b_hebrew-lyrics-finetune |

---

## Versioning

- **v0.1.0** — scaffold + ~30 seed corpus + 5 register tests + rewrite-only methodology
- **v0.1.1** — npx installer
- **v0.2.0** — 6 personas + 4 output types + interview (STEP 0) + initial validation
- **v0.3.0** — expanded 6-stage validation + phrasing checker + grammar tools + 12-category error catalog + DictaBERT-powered validator script
- **v0.4.0** — 124-source catalog + 8 variation modes + source-selection decision logic (STEP 4.5) + 4-axis output rubric (STEP 5g) + user-goal interview question + `hebrew_toolkit.py` with 14 specialized-model subcommands
- **v0.5.0** — **Comprehensive scope expansion + rebrand as the Hebrew production suite**: 25+ output types (added books / articles / courses / reports / research / business / communications / technical docs) + 15 variation modes (added software-engineering, cybersecurity, product-management, defense-aerospace, ai-ml-research, startup-fundraising, gen-z-creator) + 4 community sub-filters (arabic-hebrew-bilingual, haredi-tech, academic-formal, diaspora-israeli)
- **v0.5.1** — **RTL safety rule for UI labels**: STEP 0 now mandates Latin-transliteration-first persona names (`Yoel (יואל)` etc.) in any AskUserQuestion option / menu chip / button label. Fixes Hebrew option labels appearing character-reversed in LTR-base UI clients.
- **v0.5.2** — **Bidi & RTL output discipline (STEP 5h validation gate)**: comprehensive rules to prevent Hebrew inversion in any LTR-base renderer (terminal, GitHub markdown, plaintext, chat UIs). Mandates Hebrew gershayim (`״`) / geresh (`׳`) / maqaf (`־`) instead of ASCII `"` `'` `-` adjacent to Hebrew runs. Mandates FSI/PDI isolation of Latin runs inside Hebrew sentences. Mandates RLM prefix for digit-leading lines. Updates persona table to use `יואל ״יו־יו״ שריג` instead of inversion-prone `יואל "יו-יו" שריג`. Ships `hebrew_toolkit.py bidi-check` (detects 4 violation classes) and `bidi-fix` (auto-applies fixable substitutions, safely skips YAML frontmatter / fenced code blocks / long structural strings).
- **v0.5.3** (current) — **Compress SKILL.md `description` to ≤1024 chars** for Claude Cowork compatibility. Trimmed from 1731 → 989 chars while preserving all trigger keywords (output types, variation modes, persona names, validation+rubric, do-not-use list).
- **v0.6.0** (planned) — audio rehearsal loop (TTS + ASR feedback); visual deliverable pipeline (markdown → PDF / Gamma decks); corpus expansion to 200+ 2025–2026 web-sourced entries
- **v0.7.0** (planned) — educational mode (explain corrections); strict-corpus mode (refuse non-grounded terms); self-improvement feedback loop; custom persona from user samples; test matrix expansion (5 → 60 cases)
- **v1.0.0** (planned) — 300+ corpus entries, additional personas, CI / GitHub Action integration
