# Hebrew Variation Modes

The skill produces Hebrew across multiple linguistic registers, domains, and emotional bands. A *variation mode* combines a vocabulary band, a source-selection bundle, and a set of grammatical conventions to consistently produce Hebrew in a specific register.

This document defines 8 variation modes. The user selects one at STEP 0 (Interview) — or the skill picks one based on context and goal.

---

## Why modes matter

A grammatically-correct Hebrew sentence in tech-formal register would sound out of place in a memorial speech, even if both are grammatically perfect. Different domains require different vocabulary, different code-switching density, different formality, and different validation. The variation modes encode these trade-offs explicitly.

---

## Mode 1 — `tech-formal` (DEFAULT)

The default mode for Israeli tech production: blog posts, LinkedIn updates, investor pitches, internal documentation, technical RFCs.

**Vocabulary band:** Tech-informal + tech-formal, with English code-switching for acronyms and product names.

**Persona affinity:** Yoel / Itamar / Dana

**Code-switching density:** 15-30% English-script

**Sources used:**
- Generation: Claude with Hebrew system prompt + `corpus/jargon.json`
- Validation: DictaBERT-parse + Hspell
- Reference: Academy of the Hebrew Language + Morfix
- Currency check: `corpus/jargon.json` (2025+ tech terms)

**Defining grammar rules:**
- Anglicized verbs follow pi'el (לדיפלוי, לקומיט)
- English-script nouns with hyphen-prefix (ב-MCP, ה-IAM)
- Numbers digital
- Smikhut preferred over analytical "X של Y" when both parts Hebrew
- No filler words

**When to use:** Default for all Israeli tech professional writing.

---

## Mode 2 — `legal-technical`

Israeli legal-technical writing — contracts, technical legal opinions, regulatory documents, statute commentary, IP / patent documents, terms-of-service.

**Vocabulary band:** Formal Hebrew + precise legal terminology + tech English only when unavoidable.

**Persona affinity:** Shira / Itamar (no Yoel — too casual; no Gilad — never)

**Code-switching density:** <10% English-script

**Sources used:**
- Generation: Claude with legal-aware Hebrew prompt + Legal-heBERT terminology
- Validation: **Legal-heBERT** + DictaBERT-parse
- Reference: Academy of the Hebrew Language + Israeli legal glossary
- **Deterministic output:** when invoked, temperature=0 and output is reproducible (critical for contract reliability)

**Defining grammar rules:**
- Formal Hebrew verbs preferred over anglicized loanwords ("יפרוס" preferred over "ידיפלוי" in a contract)
- Precise legal terminology (תניה / סעיף / זכויות / חובות / אחריות / תשלום)
- Numbers spelled out for legal weight when stakes high ("שמונה-עשר חודשים" not "18 חודשים")
- Smikhut mandatory; analytical "X של Y" only when required for clarity
- Citation format: per Israeli legal convention (חוק X, סעיף Y(z))
- Anaphora extremely strict — every pronoun must have unambiguous antecedent

**Cultural notes:**
- Use formal pronouns and structures (לכבוד, הואיל ו-, להלן)
- Date format: full Israeli format (DD/MM/YYYY in body, "ביום X לחודש Y בשנת Z" for legal weight)

**When to use:** Israeli employment contracts, NDAs, IP assignments, ToS, privacy policies, statute commentary.

---

## Mode 3 — `medical`

Israeli medical Hebrew — clinical documentation, patient communication, medical research, drug labels, consent forms.

**Vocabulary band:** Mixed — formal Hebrew + medical terminology (often Latin-derived) + English for drug names and protocols.

**Persona affinity:** Itamar / Shira (precision-first)

**Code-switching density:** 10-20% (Latin/English medical terms preserved)

**Sources used:**
- Generation: Claude with medical-aware Hebrew prompt
- Validation: **hebrew_medical_ner_v5** + DictaBERT-parse
- Reference: Israeli Ministry of Health terminology + Academy of the Hebrew Language

**Defining grammar rules:**
- Drug names: kept English (Aspirin, Metformin, Claritin) — never transliterate
- Medical conditions: standard Hebrew (סוכרת, יתר לחץ דם, פיברומיאלגיה) with English in parens on first use
- Protocols: numbered, with explicit gendering when patient-facing
- Privacy: never include identifying patient details in output without explicit auth
- Anaphora: extremely strict (every "הוא" / "היא" must have explicit antecedent)

**Special considerations:**
- Patient-facing text must use second-person singular formal (אתה / את) — never third-person
- Consent forms must use simple Hebrew at 8th-grade reading level
- Drug dosing: digital with units (5 mg, 250 mcg)

**When to use:** Clinical notes, patient communication, informed consent, medical research papers in Hebrew, drug labels for Israeli market.

---

## Mode 4 — `biblical-rabbinic`

Biblical, Talmudic, liturgical, or rabbinic Hebrew register. Used for religious commentary, ceremonial speech, traditional Jewish education content.

**Vocabulary band:** Classical Hebrew lexicon, biblical / Talmudic vocabulary, traditional cantillation references.

**Persona affinity:** Shira (literary) — no other persona fits

**Code-switching density:** ~0% English

**Sources used:**
- Generation: **BEREL_3.0** or hebrew_bible_ai
- Validation: BEREL_3.0
- Reference: Tanakh + Talmud + classical Hebrew lexica + Academy of the Hebrew Language

**Defining grammar rules:**
- Classical Hebrew morphology (less constrained than Modern)
- Biblical word order variants acceptable
- Quotation: with proper citation (פסוק כא בפרק ב' של ספר בראשית)
- Ceremonial register (אדוננו / רבותינו / הקדוש ברוך הוא)
- Nikud often included (ceremonial / liturgical text), unlike Modern Hebrew

**When to use:** Religious commentary, Talmudic discussion, ceremonial speech, traditional Jewish education, blessings, eulogies in traditional register.

---

## Mode 5 — `gender-emotional`

Emotionally-aware Hebrew with gender-sensitivity. Used for personal narrative, vulnerable LinkedIn posts, memorial speeches, therapeutic writing, mental-health communication.

**Vocabulary band:** Personal / emotional / register-flexible; tracks the speaker's grammatical gender and emotional register precisely.

**Persona affinity:** Noa / Shira

**Code-switching density:** 15-30% (Noa-fluid style)

**Sources used:**
- Generation: Claude with emotion-aware Hebrew prompt
- Validation: **hebEMO** (8 emotion categories: anger, fear, joy, sadness, anticipation, surprise, trust, disgust)
- Cross-check: heBERT_sentiment for pos/neg/neu polarity

**Defining grammar rules:**
- Speaker gender consistency — every verb / adjective / pronoun matches the speaker's stated gender
- If gender is unspecified, the skill asks before producing first-person Hebrew
- Emotion vocabulary precise (sadness ≠ grief ≠ regret — each has distinct Hebrew)
- Pronouns: explicit when shifting reference (avoid ambiguous הוא / היא)
- Honor the emotional arc — don't undercut vulnerability with bravado

**8 emotion categories (hebEMO):**
| English | Hebrew | Hebrew word examples |
|---|---|---|
| anger | כעס | כועס, רוגז, זעם, התרגזות |
| fear | פחד | פחד, חרדה, בעתה, חשש |
| joy | שמחה | שמחה, אושר, חדווה, שלווה |
| sadness | עצב | עצב, צער, יגון, אבל |
| anticipation | ציפייה | ציפייה, התרגשות, מצפה, מקווה |
| surprise | הפתעה | הפתעה, תמיהה, השתאות |
| trust | אמון | אמון, אמונה, ביטחון, ידידות |
| disgust | גועל | גועל, סלידה, מיאוס |

**When to use:** Vulnerable LinkedIn posts, personal narrative, memorial speeches (alongside `biblical-rabbinic` for ceremonial), therapy content, mental-health Hebrew.

**Honoring gender expression:**
- Hebrew has grammatical gender — every "אני" inflects through verb forms
- The skill asks the user's gender expression at the start of any gender-emotional task
- The skill respects non-binary expression where the user requests it — though Hebrew morphology defaults to binary, alternative forms (אתם/n, אני בלא-מגדר) can be used per user request
- The skill never assumes gender from name

---

## Mode 6 — `slang-cultural`

Israeli colloquial Hebrew with cultural explanation layer. Used for casual content, podcast intros, founder-vulnerable posts, satire / comedy, content explaining Israeli culture to non-Israelis.

**Vocabulary band:** Casual + slang + cultural references + heavy code-switching.

**Persona affinity:** Gilad / Noa / Yoel (in casual moments)

**Code-switching density:** 20-40%

**Sources used:**
- Generation: **DictaLM-3.0-24B-Thinking** (best Hebrew model for cultural nuance)
- Validation: hebert-finetuned-hebrew-metaphor + cultural-explanation generator
- Reference: israeli.md output style + Hebrew slang corpus + Eliezer Bot Yehudah

**Defining grammar rules:**
- Slang appears naturally — but with explanation layer attached for non-Israeli readers
- Cultural references explicit (יום הזיכרון / רוטשילד / חלוקה / שכונה)
- Code-switching is the point, not a bug
- Filler words tolerated (אז / סבבה / בקיצור)

**Slang explanation layer (key feature):**

When the skill produces output in slang-cultural mode, it can append an explanation layer:

```
[Hebrew with slang]:
"יאללה, חברה, בקיצור — סקיילנו פי 10 בלי לגעת בקוד. סבבה?"

[Cultural explanation, on request]:
- "יאללה" — Arabic-origin Hebrew slang meaning "let's go" / "come on"
- "סבבה" — Arabic-origin (sababa) meaning "cool / okay / good" — universal Israeli affirmation
- "בקיצור" — "in short" — opens a summary statement
- Tone: founder-mode urgency with friendly directness
```

The explanation layer is **opt-in** — user requests it explicitly. Default output is the natural Hebrew without footnotes.

**When to use:** Podcast intros, comic openers, satire, content explaining Israeli tech culture to international audiences, casual LinkedIn, founder-vulnerable posts.

---

## Mode 7 — `bilingual`

Hebrew-English bilingual text. Used for content that genuinely needs both languages (international company communication, bilingual marketing, code with Hebrew comments, EN-HE side-by-side documentation).

**Vocabulary band:** Hebrew main + English supplementary, or alternating per paragraph.

**Persona affinity:** Yoel / Noa / Itamar (depending on which language carries the emotional weight)

**Code-switching density:** N/A — both languages are full content

**Sources used:**
- Generation: Claude with bilingual prompt
- Validation: **neodictabert-bilingual** + neodictabert-bilingual-embed for cross-lingual coherence
- Reference: Helsinki-NLP opus-mt-en-he + DeepL for back-translation check

**Defining grammar rules:**
- Each language follows its own grammar (don't apply Hebrew rules to English text)
- When alternating: clear paragraph or section breaks
- Side-by-side: align by paragraph, mark which is original
- Mixed in single sentence: the dominant language sets the grammar; the other language is loanword treatment

**When to use:** International company internal comms, bilingual marketing, EN-HE side-by-side product documentation, code with Hebrew comments + English code.

---

## Mode 8 — `creative-lyrics`

Hebrew creative writing — poetry, song lyrics, fiction, experimental form. Used when literary expression matters more than information density.

**Vocabulary band:** Full range — from classical Hebrew to contemporary slang — chosen for sound, rhythm, meaning layering.

**Persona affinity:** Shira (literary) / Gilad (comic) / Noa (vulnerable)

**Code-switching density:** Variable — sometimes 0% (pure Hebrew poetic), sometimes high (modern bilingual song lyrics)

**Sources used:**
- Generation: **gemma-3_4b_hebrew-lyrics-finetune** for lyrics; DictaLM-3.0-24B-Thinking for prose
- Validation: hebert-finetuned-hebrew-metaphor + Claude authenticity review (subjective)
- Reference: Hebrew literary corpus + Bialik / Amichai / Keret as style anchors

**Defining grammar rules:**
- Grammar can bend deliberately for effect — but bends are intentional, not accidental
- Rhyme / rhythm / meter take precedence over standard rules
- Metaphor and figurative language welcome
- Sound symbolism — choose words that *sound* like what they mean
- Repetition is a feature — refrain structure encouraged

**When to use:** Hebrew lyrics, poetry, creative fiction, experimental prose, advertisement copy with literary weight.

---

## Mode selection — interview question

In STEP 0 (Interview), the skill asks:

> "Variation mode? (1) tech-formal (default) — startup-nation tech Hebrew. (2) legal-technical — contracts, deterministic. (3) medical — clinical Hebrew. (4) biblical-rabbinic — ceremonial / religious. (5) gender-emotional — personal narrative, vulnerable. (6) slang-cultural — casual + cultural explanation. (7) bilingual — Hebrew + English. (8) creative-lyrics — poetry / lyrics / experimental. (auto) — infer from context."

If the user doesn't pick, the skill infers from context:
- Pitch / blog / linkedin → **tech-formal**
- Contract / ToS / privacy → **legal-technical**
- Clinical notes → **medical**
- Religious / ceremonial → **biblical-rabbinic**
- Personal / memorial / vulnerable → **gender-emotional**
- Podcast / comic / satire → **slang-cultural**
- Side-by-side docs / international comms → **bilingual**
- Lyrics / poetry → **creative-lyrics**

---

## Mode-mode combinations (advanced)

Sometimes a piece needs two modes:
- **Memorial speech** = `biblical-rabbinic` (ceremonial frame) + `gender-emotional` (personal anchor)
- **Founder vulnerable post** = `gender-emotional` (vulnerability) + `tech-formal` (still tech context)
- **Slang explainer** = `slang-cultural` (the slang) + `bilingual` (for international audience)

The skill handles this by alternating modes between sections — the user just describes the use-case.

---

## Updating modes

New variation modes can be added when:
1. A coherent vocabulary band emerges in a new domain
2. At least one specialized model exists for the domain
3. A persona affinity is clear
4. The grammar rules are documented

Open a PR with the new mode definition + source bundle + grammar rules.
