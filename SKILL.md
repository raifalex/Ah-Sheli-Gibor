---
name: ah-sheli-gibor
description: "Produce authentic 2026-era Israeli tech Hebrew across 5 output types — rewrite, pitch, speech, talking-cards, teleprompter — with correct binyan/gender/smikhut grammar, 5-register awareness (slack, technical-blog, linkedin, investor-pitch, pr-rfc), and a choice of 6 voice personas (3 men, 3 women): the tech-founder (יואל), the literary speechwriter (שירה), the comedian (גלעד), the panelist-pundit (דנה), the veteran journalist (איתמר), and the contemporary creator (נועה). The skill interviews the user for context (use case, audience, mood, persona) before producing output. Every output is validated against Hebrew grammar rules and current 2026 talk-jargon style. Use when the user supplies text or a topic and wants authentic Israeli tech Hebrew output — rewriting an article, drafting a pitch, writing a keynote, preparing panel cards, or scripting a teleprompter. Do NOT use for general Hebrew translation (use DeepL or DictaLM), formal Academy-of-Hebrew documents, RTL CSS work (use hebrew-rtl-best-practices), Hebrew document generation (use hebrew-document-generator), or non-tech content (use hebrew-content-writer)."
license: MIT
allowed-tools: ''
compatibility: Works with Claude, Claude Code, Cursor. Optimized for Claude Sonnet 4.6+ and Claude Opus 4.7. Hebrew RTL rendering depends on the host environment.
---

# Ah Sheli Gibor — Israeli Tech Hebrew Production Skill

> "אח שלי גיבור" — the affectionate startup-nation address. This skill produces Hebrew text that sounds like a 2026 Israeli tech professional actually wrote it.

## What this skill does

Produces authentic 2026-era Israeli tech Hebrew across **5 output types**:

1. **Rewrite** — comprehend source text and reconstruct in target register
2. **Pitch** — investor / customer / internal / elevator pitch decks and scripts
3. **Speech** — keynotes, commencements, memorials, founder town-halls, award speeches
4. **Talking cards** — panel prep, TV interview cards, board meeting navigators
5. **Teleprompter** — verbatim broadcast/recorded-video scripts with delivery annotations

Every output is **voiced by one of 6 personas** (you choose, or the skill chooses based on context):

- **יואל "יו-יו" שריג** (M) — tech-founder, high-energy, dense code-switching
- **שירה לב** (F) — literary speechwriter, classical-modern Hebrew balance
- **גלעד אש** (M) — comedian, deadpan, slang-fluent but selective
- **דנה אלמוג** (F) — TV panelist-pundit, debate-tested, sharp soundbites
- **איתמר חוזה** (M) — veteran feature journalist, patient long-form authority
- **נועה אופק** (F) — contemporary creator, intimate, vulnerable, fluid Hebrew-English

Every output is **validated** before delivery against:
- Hebrew grammar (binyan / gender / smikhut / preposition binding / definite-article rules)
- Current 2026 talk-jargon style (corpus-grounded vocabulary, no dated language)
- Persona consistency (the chosen voice holds across the output)

## When to invoke

Trigger phrases the skill responds to:
- "rewrite in Israeli tech Hebrew"
- "write me a pitch for [X]"
- "draft a speech / keynote in Hebrew"
- "prepare talking cards for [scenario]"
- "teleprompter script for [recording]"
- "make this sound like [persona name] wrote it"
- "Israeli LinkedIn voice"
- Any input text or topic with an implicit ask for production-grade Israeli tech Hebrew

## When NOT to use this skill

- General Hebrew translation → use DeepL or DictaLM 3.0
- Formal Academy-of-Hebrew documents → use `hebrew-content-writer`
- Hebrew RTL CSS or layout → use `hebrew-rtl-best-practices`
- Hebrew PDF/DOCX/PPTX generation → use `hebrew-document-generator`
- Niqud/vowelization → use Dicta Nakdan API
- Non-tech content (legal, medical, literary, news) → use `hebrew-content-writer`

---

## Operating protocol — 6 steps

Execute in order. Do not skip steps.

### STEP 0 — INTERVIEW

When invoked, identify what the user supplied and what's missing. The skill needs five things before producing output. Ask only what's not already given.

| Variable | Options | Default if not specified |
|---|---|---|
| **Output type** | rewrite / pitch / speech / talking-cards / teleprompter | infer from request; if ambiguous, ask |
| **Use context** | where will this be used, who's the audience, what platform | ask if not stated |
| **Purpose** | inform / persuade / entertain / sell / mobilize / celebrate / mourn | infer from output type + context |
| **Mood / tone** | confident / warm / urgent / measured / playful / serious / vulnerable | infer from persona + context |
| **Persona** | יואל / שירה / גלעד / דנה / איתמר / נועה / auto | ask once if not specified; "auto" chooses based on output type + context |

**Interview rules:**

- **Ask at most 3 questions** at any one time. Don't drown the user.
- **Combine related questions** into a single ask when sensible.
- **If 4/5 variables are clear from context**, proceed without asking — name your inferences in one line ("ממשיך עם: speech, audience=board, mood=urgent, persona=יואל. אם זה לא נכון — תקן אותי.").
- **Persona "auto"** is fine if the user doesn't have a preference — the skill picks based on the output-type → persona pairing table (see persona files for pairings).
- **In subsequent turns** in the same session, remember the answers; don't re-ask.

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

### STEP 5 — VALIDATE

Two-stage validation pass on every output. **This step is non-negotiable.**

#### 5a — Hebrew Grammar Check

Apply the 10-point checklist from `references/grammar_layer.md` §6:

1. Anglicized verbs follow correct binyan (pi'el default; conjugation accurate)
2. Loanword nouns carry correct gender and plural
3. Compound nouns use smikhut or analytical form (never both)
4. Preposition + loanword binding (hyphen for English-script, direct for Hebrew-script)
5. Definite article correct after demonstratives/possessives
6. Partitive verb agreement (חלקכם חתם, not חתמתם)
7. "את" before definite direct objects in scripted text
8. Approximation marker כ- before numbers (not "בערך")
9. No filler words (אז, כאילו, פשוט, למעשה, בעצם)
10. Product names preserved English (AWS, Claude, Anthropic, etc.)

For each violation found, fix it and re-validate.

#### 5b — Talk-Jargon Currency Check

Verify every piece of jargon used:

- **Corpus-grounded** — appears in `corpus/jargon.json` with confidence "high" or "medium"
- **OR persona signature** — appears in the chosen persona's signature-phrases list
- **OR Academy-approved** — appears as `standard_hebrew_equivalent` in a corpus entry

For each jargon term that fails all three:
- If the term is genuinely current 2026 usage and you know it, flag for corpus addition (note in output: "TODO: add to corpus")
- If the term is uncertain, replace it with a corpus-grounded alternative
- If no alternative exists in the right register, fall back to standard Hebrew

**Avoid 2022–2023 dated language entirely.** Especially in the AI/ML domain: don't write "ChatGPT שלנו" generically (use "ה-LLM שלנו" or specific model name); don't write "בינה מלאכותית גנרטיבית" as a buzzword (use precisely or skip).

#### 5c — Persona Consistency Check

Read the output as if you are the chosen persona. Ask:
- Does the voice hold across every paragraph?
- Are the persona's distinctive moves present (or appropriately absent)?
- Does the persona's "what they don't do" list hold?
- Could this paragraph have been written by a different persona without anyone noticing? If yes — strengthen the voice.

#### 5d — Anti-pattern Check

Cross-check against `references/anti_patterns.md`. Any anti-pattern present means rewrite that clause.

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
| **יואל "יו-יו" שריג** | M | tech-founder | investor pitch, LinkedIn announcements, founder town-hall, board meeting |
| **שירה לב** | F | literary speechwriter | formal keynotes, commencement, memorials, op-eds, founder letters |
| **גלעד אש** | M | comedian | conference keynote openers, company offsites, awards-show MCing, satire |
| **דנה אלמוג** | F | TV panelist-pundit | panel prep, debate prep, op-eds, soundbite speeches, hostile-press Q&A |
| **איתמר חוזה** | M | veteran journalist | long-form features, corporate biographies, retrospective speeches, investigative pieces |
| **נועה אופק** | F | contemporary creator | vulnerable LinkedIn, podcast intros, intimate small-group keynotes, founder-personal newsletters |

User can select by name ("voice = יואל" / "speak as שירה") or let the skill auto-select.

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
- לפיין-טיון → מפיין-טיון / פיין-טיון / אפיין-טיון
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

## Versioning

- **v0.1.0** — scaffold + ~30 seed corpus entries + 5 register tests + rewrite-only methodology
- **v0.1.1** — npx installer added
- **v0.2.0** (current) — adds: 6 personas with full profiles, 4 new output types (pitch / speech / talking-cards / teleprompter), interview protocol (STEP 0), formal validation pass (STEP 5 — grammar + jargon currency + persona consistency + anti-patterns), upgraded description to 2026
- **v0.3.0** (planned) — corpus expansion to 100 entries (70% 2025–2026 web-dated), persona signature-phrase validation against fresh web sources, automated grammar validation via DictaBERT integration
- **v1.0.0** (planned) — 300+ corpus entries, additional personas (Arabic-Hebrew, religious-Hebrew), persona learning from user-supplied samples
