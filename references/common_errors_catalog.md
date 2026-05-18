# Common Errors Catalog — Hebrew Tech Writing (2026)

Expanded anti-pattern catalog specifically calibrated for Hebrew tech writing in 2026. Use alongside `anti_patterns.md` (the short summary) for deep error categorization.

Each error has: pattern, why it's wrong, correct alternative, and which persona is most/least likely to make this mistake.

---

## CATEGORY A — Morphology errors (binyan / form)

### A1. -ing suffix attached to Hebrew verb

❌ *"עשינו דפלויאינג"* / *"קומיטינג"* / *"אנחנו דיבגינג"*
✅ *"דיפלוינו"* / *"קומיטנו"* / *"אנחנו מדבגים"*

**Why wrong:** Hebrew has no -ing inflection. The English progressive is rendered by Hebrew present tense (`מ-` prefix in pi'el).

**Detection:** regex `[א-ת]+ינג(\s|$)` — flag any token that looks like a Hebrew word with -ing.

### A2. Periphrastic "לעשות X" when pi'el verb exists

❌ *"לעשות קומיט"* / *"לעשות פוש"* / *"לעשות דיפלוי"*
✅ *"לקומיט"* / *"לפוש"* / *"לדיפלוי"*

**Why wrong:** The pi'el verb form is established 2025-2026 usage. The periphrastic is dated 2018-2022 transitional Hebrew.

**Exception:** when X is a one-off significant event (noun-event reading): *"בוא נעשה ריפקטור גדול בסוף הרבעון"* — here ריפקטור is a noun event, periphrasis OK.

### A3. Wrong binyan for borrowed verb

❌ *"לבדוג"* (pa'al for debug) / *"לדפלוי"* (pa'al for deploy)
✅ *"לדבג"* / *"לדיפלוי"* (pi'el)

**Why wrong:** Borrowed verbs default to pi'el in modern Hebrew (the binyan with maximal flexibility for foreign roots).

### A4. Wrong vowel pattern in pi'el

❌ *"מקאומיט"* (wrong vowel structure)
✅ *"מקומיט"*

**Why wrong:** Pi'el present masculine singular pattern is `מַ_ַ_ֵ_` → no extra vowel letter.

### A5. Misplaced gershayim

❌ *"פיצר"* (no gershayim) / *"פיצ'ער"* (wrong placement)
✅ *"פיצ'ר"* (gershayim marks the /tʃ/ sound)

**Why wrong:** Hebrew uses gershayim (') to mark non-Hebrew sounds. The convention is to place it on the consonant that approximates the foreign sound.

---

## CATEGORY B — Agreement errors

### B1. Gender agreement noun-adjective

❌ *"הפיצ'ר הזאת"* (feminine demonstrative on masculine noun)
✅ *"הפיצ'ר הזה"*

**Detection:** DictaBERT `morph.feats.Gender` mismatch between adjacent noun and adjective/demonstrative.

### B2. Gender agreement noun-verb

❌ *"הארכיטקטורה החזיק"* (masculine verb on feminine noun)
✅ *"הארכיטקטורה החזיקה"*

### B3. Number agreement subject-verb

❌ *"שלושת המהנדסים החליט"* (singular verb on plural subject)
✅ *"שלושת המהנדסים החליטו"*

### B4. Partitive agreement (subtle)

❌ *"חלקכם חתמתם"* / *"רוב הצוות מסכימים"*
✅ *"חלקכם חתם"* / *"רוב הצוות מסכים"*

**Why wrong:** After partitive expressions (חלק, רוב, מקצת, מיעוט), the verb agrees with the partitive head (singular), not the implied plural.

This is the **most common subtle error** in Hebrew tech writing. The English-thinking writer matches the implied plural; the Hebrew rule matches the partitive head.

### B5. Collective noun agreement

❌ *"הצוות החליטו"* (collective treated as plural)
✅ *"הצוות החליט"* (collective is grammatically singular)

**Exception:** when emphasizing the individual members: *"הצוות מסכימים זה עם זה"* — acceptable.

---

## CATEGORY C — Smikhut (construct state) errors

### C1. Definite article on the construct member

❌ *"המנהל המוצר"* / *"הראש הצוות"*
✅ *"מנהל המוצר"* / *"ראש הצוות"*

**Why wrong:** In smikhut, only the head (the second/absolute noun) takes the definite article; the construct (first noun) takes it indirectly through the chain.

**Detection:** regex `ה[א-ת]+\sה[א-ת]+` followed by morphological check that the first noun is in construct form.

### C2. Hybrid construct with של

❌ *"המנהל של הפרודקט"* (analytical with English noun)
✅ *"מנהל המוצר"* (smikhut) OR *"ה-Product Manager"* (full English)

**Why wrong:** Mixing analytical *של* with a translated head produces a translation-feeling sentence. Choose one mode.

### C3. Smikhut chain length

❌ *"מנהל פיתוח צוות פלטפורמה"* (4-noun chain)
✅ *"מנהל הפיתוח של צוות הפלטפורמה"* (break with של)

**Why wrong:** Smikhut chains beyond 2-3 nouns become hard to parse. Use של to break them.

### C4. Construct form not properly modified

❌ *"מנהל המוצר חכם"* (adjective on construct noun, ambiguous)
✅ *"מנהל המוצר החכם"* (adjective takes definite article, modifies the chain) OR *"המנהל החכם של המוצר"*

**Why wrong:** When modifying a smikhut chain, the adjective takes the chain's definiteness and follows the chain.

---

## CATEGORY D — Preposition errors

### D1. Missing hyphen on English-script with Hebrew prefix

❌ *"בMCP"* / *"לAWS"* / *"מKafka"*
✅ *"ב-MCP"* / *"ל-AWS"* / *"מ-Kafka"*

**Why wrong:** Hebrew prefix must connect via hyphen when attaching to English-script.

**Detection:** regex `\b[בלמכש](?=[A-Z])` (any short prefix immediately followed by capital English letter).

### D2. Hyphen with full-Hebrew loanword

❌ *"ב-פיצ'ר"* (hyphen with Hebrew loanword)
✅ *"בפיצ'ר"* (direct attachment)

**Why wrong:** Hyphen rule applies only to English-script targets; fully transliterated loanwords behave as native Hebrew nouns.

### D3. Wrong preposition selection

❌ *"לחשוב על"* in tech context → English calque "to think about"
✅ context-dependent; sometimes *"לחשוב בנושא"* or *"לבחון את"*

This is a softer error; usually about register and idiomaticity rather than strict grammar.

### D4. Double preposition

❌ *"בתוך ב-MCP"* / *"מתוך מ-AWS"*
✅ *"ב-MCP"* / *"מ-AWS"* (single preposition)

---

## CATEGORY E — Definite article errors

### E1. Missing ה after demonstrative/possessive

❌ *"הנחה הזאת"* / *"מודל הזה"*
✅ *"ההנחה הזאת"* / *"המודל הזה"*

**Why wrong:** In Hebrew, the noun preceding a demonstrative or possessive must take the definite article.

**Detection:** regex `(?<![֐-׿])[א-ת]+\s+(הזה|הזאת|הזו|אלה|זה|זאת|שלו|שלה)`

### E2. Doubled definite article

❌ *"ה-המנהל"* / *"ה-הפיצ'ר"*
✅ *"המנהל"* / *"הפיצ'ר"*

**Why wrong:** Single definite article only.

### E3. Definite article on construct (vs. absolute) noun

❌ *"המנהל המוצר"* (definite on construct)
✅ *"מנהל המוצר"* (definite only on absolute)

(See C1.)

---

## CATEGORY F — Particle errors

### F1. Missing את before definite direct object

❌ *"קראנו האירוע"* / *"ראינו ה-diff"*
✅ *"קראנו את האירוע"* / *"ראינו את ה-diff"*

**Why wrong:** Hebrew requires *את* before definite direct objects in formal/scripted writing. Casual Hebrew tolerates dropping it; tech writing in formal registers requires it.

**Persona variation:**
- **גלעד** can drop *את* for spoken-feeling effect
- **נועה** sometimes drops *את* for conversational flow
- **דנה / שירה / איתמר** never drop *את*

### F2. את before indefinite object

❌ *"קראנו את ספר"*
✅ *"קראנו ספר"*

**Why wrong:** *את* only with definite objects.

---

## CATEGORY G — Anglicism / calque errors

### G1. "אני הולך ל-" calqued from "I'm going to"

❌ *"אני הולך לטעון"* / *"אני הולך להראות"*
✅ *"אני אטען"* / *"אני אראה"* (Hebrew future tense)

**Exception:** *"אני הולך ל-"* only when literally signaling physical movement to next bit.

### G2. "בערך X מספר" instead of "כ-X מספר"

❌ *"לפני בערך 18 חודשים"* / *"בערך 150 מיליון משתמשים"*
✅ *"לפני כ-18 חודשים"* / *"כ-150 מיליון משתמשים"*

**Why wrong:** *בערך* is colloquial-spoken; tech writing uses prefix *כ-* for approximation.

### G3. "אני חושב ש-" overuse (calque of "I think that")

❌ Repeated *"אני חושב ש-"* / *"אנחנו חושבים ש-"* at the start of every paragraph
✅ Vary: *"לדעתי..."*, *"ראוי לציין כי..."*, *"נראה לי ש..."*, *"אני מעריך ש..."*

### G4. Filler word in formal writing

❌ *"אז למעשה החלטנו פשוט לעבור ל-microservices"*
✅ *"החלטנו לעבור ל-microservices"*

Filler words (אז, כאילו, פשוט, למעשה, בעצם) are removed in all formal registers (technical-blog, linkedin, investor-pitch, pr-rfc, teleprompter). One acceptable in slack/standup as opening connector.

---

## CATEGORY H — Spelling / transliteration errors

### H1. Single-vowel transliteration of double-vowel loanword

❌ *"סטיקהולדר"* (single vowel for stake)
✅ *"סטייקהולדר"* (double vowels preserved)

### H2. Missing gershayim on sounds without Hebrew equivalent

❌ *"פיצר"* / *"גמא"* / *"מנגר"*
✅ *"פיצ'ר"* / *"ג'מא"* / *"מנג'ר"*

### H3. Wrong gershayim placement

❌ *"ג'מא"* (wrong) for "gamma"
✅ *"גמא"* (correct, no gershayim needed for /g/)

### H4. Translation of brand names

❌ *"השתמשנו בקלוד"* (Hebrew transliteration of brand)
✅ *"השתמשנו ב-Claude"* (preserve English brand)

---

## CATEGORY I — Sentence-level errors

### I1. English sentence structure preserved

❌ *"החברה היא חברה שעוזרת ארגונים גדולים..."* (calques "the company is a company that helps...")
✅ *"החברה עוזרת לארגונים גדולים..."* (Hebrew direct verb)

### I2. Run-on without breath

❌ *"דיפלוינו את הפיצ'ר לפרודקשן והוא עלה ועכשיו הוא רץ ב-99.9% uptime ובכלל..."*
✅ Break into 2-3 sentences with natural breath points.

### I3. Stranded relative clause

❌ *"זה הפיצ'ר שאני חושב שצריך לעשות לו ריפקטור"* (multiple subordinations)
✅ Restructure: *"הפיצ'ר הזה צריך ריפקטור"* or *"לפי דעתי, צריך לריפקטור את הפיצ'ר הזה"*

---

## CATEGORY J — Register-drift errors

### J1. Slang in formal register

❌ Investor pitch with *"היה לנו בלגן רציני בפרודקשן"*
✅ *"חווינו תקלה משמעותית בייצור"* OR *"חווינו incident משמעותי בפרודקשן"*

### J2. Heavy formality in slack

❌ Slack message with *"במהלך הספרינט הנוכחי השלמנו..."*
✅ *"סגרנו את הקריטיים בספרינט"*

### J3. Mixed register in single sentence

❌ *"בשורה התחתונה, סקיילנו פי 10 והיה על הפנים"*
✅ *"סקיילנו פי 10. היה על הפנים."* (matched register: casual)
OR *"בשורה התחתונה, סקיילנו פי 10 — לא פשוט."* (matched register: formal)

---

## CATEGORY K — Number / date errors

### K1. Spelled-out number in tech writing

❌ *"שמונה-עשר חודשים"* in a blog post
✅ *"18 חודשים"*

**Exception:** ceremonial writing (Shira persona) may spell out for rhetorical weight: *"שמונה-עשר חודשים, חברה — שמונה-עשר חודשים..."*

### K2. Wrong percent representation

❌ *"שמונים אחוז"*
✅ *"80%"*

### K3. Date format inconsistency

❌ *"5 במאי 26"* (truncated year)
✅ *"5 במאי 2026"* OR *"05/05/2026"* (DD/MM/YYYY for Israel)

### K4. Year preceded by "ב-" without hyphen

❌ *"ב2026"*
✅ *"ב-2026"* (Israeli convention for year prefix)

---

## CATEGORY L — 2026 currency errors

### L1. Pre-2024 AI vocabulary

❌ *"הצ'אטGPT שלנו"* (used as generic LLM reference)
✅ *"ה-LLM שלנו"* / *"המודל שלנו"* / specific name (Claude, GPT-4o)

### L2. Over-used 2023 buzzwords

❌ *"בינה מלאכותית גנרטיבית"* used as a buzzword in every sentence
✅ Use *AI* / *מודל גנרטיבי* / specific term precisely; avoid as filler

### L3. Pre-MCP vocabulary

❌ *"plugin ל-LLM"* (pre-MCP terminology)
✅ *"MCP server"* / *"כלי MCP"* in 2026 context

---

## Detection sequencing (skill STEP 5)

The skill applies these checks in this order:

1. **Pass 1 — Regex anti-patterns** (Category A1, D1, E2, G1, G2, G4) — instant detection
2. **Pass 2 — Corpus-grounded vocabulary** (Category L1, L2, L3) — corpus lookup
3. **Pass 3 — Smikhut + agreement** (Category B, C, F) — inspection + optional DictaBERT
4. **Pass 4 — Phrasing checks** (Category G3, I, J) — see `phrasing_checker.md`
5. **Pass 5 — Persona consistency** — voice fingerprint check
6. **Pass 6 — Authenticity review** — native-speaker test

Each fail → fix the offending clause and re-validate from Pass 1.

---

*v0.3.0 — 2026-05-18.*
