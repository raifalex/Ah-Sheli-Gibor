# Phrasing Checker — Hebrew Idiomaticity & Naturalness Layer

This document covers the layer *above* grammar correctness: a sentence can be grammatically perfect and still sound wrong. Hebrew has its own rhythms, word orders, idioms, and code-switching norms. This is the checklist the skill's STEP 5e applies before finalizing output.

The grammar layer catches *errors*. The phrasing layer catches *unnaturalness*.

---

## What "phrasing" means here

Phrasing is everything that distinguishes a native-written Hebrew sentence from a grammatically-correct translation. It includes:

1. **Word order** — Hebrew default is VSO; SVO is fine; OSV awkward unless deliberately emphatic
2. **Idiomaticity** — Hebrew idioms used naturally, not translated; English idioms not calqued
3. **Register coherence** — vocabulary stays in the right band across the whole text
4. **Code-switching naturalness** — English-Hebrew mix follows established patterns
5. **Sentence rhythm** — variation in length, deliberate use of short and long
6. **Connective and discourse markers** — Hebrew connectives chosen for register
7. **Vocabulary variation** — repetition avoided unless deliberate
8. **Anaphora clarity** — pronoun reference unambiguous

---

## 1. Word order

### Hebrew default patterns

| Pattern | Frequency | Register |
|---|---|---|
| **Verb-Subject-Object (VSO)** | most common in formal Hebrew | declarative, news, formal writing |
| **Subject-Verb-Object (SVO)** | common in modern Hebrew | conversational, narrative, contemporary writing |
| **Topic-Comment (OS structure)** | special use | emphasis, contrast, fronting for focus |

### Tech-writing convention

- **Slack / Standup:** subject-drop common (no SVO needed): *"דיפלוינו לפרוד."*
- **Technical blog:** SVO is the default; VSO for emphasis: *"החליטה הקבוצה לעבור ל-microservices"* sounds heavier than *"הקבוצה החליטה..."*
- **LinkedIn:** SVO with personal voice: *"אני מאמין ש..."*
- **Investor pitch:** mixed; VSO for assertions, SVO for narrative: *"השיגה החברה PMF" / "החברה השיגה PMF"*
- **Pr-rfc / Teleprompter:** SVO for clarity at reading-speed

### Anti-patterns

- ❌ **English word order calqued directly:** *"החברה היא חברה ש..."* (sounds like a translator). Better: *"החברה היא X — Y..."* or restructure.
- ❌ **Inverted object-fronting without rhetorical reason:** *"את הפיצ'ר דיפלוינו"* — fine if emphatic, weird if default.
- ❌ **Adverb stranded at end:** *"דיפלוינו את הפיצ'ר בהצלחה רבה"* — Hebrew prefers adverbs closer to the verb.

---

## 2. Idiomaticity (Hebrew idioms vs. English calques)

### Strong Hebrew idioms preferred in tech writing

| Hebrew | Meaning | When |
|---|---|---|
| בסופו של דבר | "at the end of the day" | summary, conclusion |
| בשורה התחתונה | "the bottom line" | assertive close |
| על קצה המזלג | "in a nutshell" / "briefly" | introducing summary |
| ביד אחת | "single-handedly" | emphasizing solo achievement |
| על הפנים | "terrible" / "shitty" | slack-register critique |
| לסגור פינות | "to close out the details" | finishing-touches phase |
| לקרוא את המפה | "to read the room/situation" | strategic awareness |
| לעשות כיוון | "to course-correct" | strategy pivot |
| הראש הגדול | "rosh gadol" — initiative, going beyond | praise in tech culture |
| לתת פייט | "to put up a fight" | competitive framing |

### Calque red flags (English idioms translated literally)

| ❌ Calqued from English | ✅ Better Hebrew |
|---|---|
| *"בסוף היום"* (lit. "at the end of the day") | *"בסופו של דבר"* (idiomatic) |
| *"השורה התחתונה"* (lit. "the bottom line") | *"בשורה התחתונה"* (idiomatic preposition) |
| *"לחשוב מחוץ לקופסה"* (calque of "think outside the box") | *"לחשוב באופן יצירתי"* — or just use the English: *"to think outside the box"* |
| *"להרים את הרף"* (calque of "raise the bar") | acceptable, but check Hebrew: *"להעלות את הרמה"* often more natural |
| *"בסוף היום"* | *"בסופו של דבר"* |
| *"זה לא רוקט-סייאנס"* (calque) | usable for comic effect (גלעד persona) but not in formal |
| *"זה מה שזה"* (calque of "it is what it is") | acceptable in casual, not in formal |
| *"מסיבת ההפתעה"* used non-literally | sounds wrong in tech context |

### Persona-specific calque tolerance

- **גלעד (comedian)** — can use calques for comic effect, signaling self-awareness
- **נועה (creator)** — limited tolerance, only when the calque is the actual culture marker
- **דנה / שירה / איתמר** — zero tolerance; idiomatic Hebrew or none
- **יואל (founder)** — uses English directly if Hebrew idiom is forced

---

## 3. Register coherence

### Vocabulary bands

Each output should hold a **single register band** across all paragraphs. The most common phrasing failure is register drift mid-text.

| Band | Vocabulary type | Examples |
|---|---|---|
| **Casual/slack** | spoken Hebrew + free anglicisms | יאללה, סבבה, אחי, בלגן |
| **Tech-informal** | tech jargon + informal Hebrew | פיצ'ר, באג, ספרינט, דיפלוינו |
| **Tech-formal** | tech jargon + formal Hebrew frame | מערכת, ארכיטקטורה, תשתית, פלטפורמה |
| **Formal-classical** | classical Hebrew + measured tech | מערכת, מעמסה, אחריות, חזון, מדיניות |
| **Ceremonial** | literary Hebrew, biblical echoes | ראשית-וקץ, צו-השעה, חזון |

### Register-drift detection

Mark any sentence where the vocabulary band shifts. Common drifts:
- **Casual word in formal text:** *"היה לנו בלגן רציני בפרודקשן"* in an investor pitch
- **Formal word in casual text:** *"בשורה התחתונה, סקיילנו פי 10"* — fine; *"חזון החברה הוא לסקייל"* — heavy
- **Tech jargon in ceremonial text:** *"דיפלוינו את הברית הזאת"* — wrong

### Persona register fingerprint

| Persona | Primary band | Allowed drift to |
|---|---|---|
| **יואל** | tech-informal + heavy English | tech-formal for investor moments |
| **שירה** | formal-classical / ceremonial | tech-formal for content terms only |
| **גלעד** | casual/slack | tech-informal for the punch; never formal-classical |
| **דנה** | tech-formal | casual for one-line landing only |
| **איתמר** | formal-classical | tech-formal for jargon nouns |
| **נועה** | tech-informal | casual for vulnerable beats; tech-formal for credibility moments |

---

## 4. Code-switching naturalness

### Density bands

| Persona / register | English-script noun density | Notes |
|---|---|---|
| **יואל (founder)** | 30–40% of content nouns | Heavy on acronyms (ARR, GTM, ICP, MCP, RAG) |
| **דנה (panelist)** | 15–25% | Moderate; English for technical anchors |
| **שירה (literary)** | <10% | Only when no Hebrew equivalent |
| **גלעד (comedian)** | 15–25% | English for comic punchlines |
| **איתמר (journalist)** | <8% | Highly selective; English for proper nouns and unavoidable technical terms |
| **נועה (creator)** | 30–40% | Fluid, mid-sentence drops natural |

### Code-switching rules

1. **Hyphen before English-script noun with Hebrew prefix:** ב-MCP, ל-AWS, מ-Postgres
2. **No hyphen with full-Hebrew loanword:** בפיצ'ר, לדשבורד, מהסטייקהולדר
3. **Plural of English-script noun:** keep English `-s` (ה-MCPs, ה-tokens), NOT `-ים`
4. **Plural of Hebrew loanword:** use `-ים` (פיצ'רים, באגים)
5. **Verb form for borrowed English verb:** always Hebrew pi'el conjugation (לדיפלוי, לקומיט, לפוש), never the English verb form
6. **Mid-sentence English word for emphasis:** acceptable; English word IS the punch
7. **Acronyms:** keep English (API, RAG, MCP, LLM, OAuth, JWT, IAM, MFA, ARR, GTM)
8. **Proper nouns:** always English (AWS, Anthropic, Claude, Cursor, OpenAI, Wix, Monday)

### Anti-patterns

- ❌ *"בMCP"* (no hyphen) → ✅ *"ב-MCP"*
- ❌ *"קלוד"* (Hebrew transliteration of brand) → ✅ *"Claude"*
- ❌ *"ה-MCP-ים"* (mixed plural) → ✅ *"ה-MCPs"*
- ❌ *"עשינו דפלויאינג"* (English -ing inside Hebrew) → ✅ *"דיפלוינו"*
- ❌ *"לעשות קומיט"* (periphrastic) → ✅ *"לקומיט"*

---

## 5. Sentence rhythm

### Length variation

Native Hebrew writing varies sentence length deliberately. Watch for:

- **All-short:** punchy but exhausting (Dana risks this — counter with one longer sentence per beat)
- **All-long:** academic-sounding (Itamar risks this — counter with one short landing per paragraph)
- **Mid-length only:** boring (most translation drift — push toward variation)

### Rhythm patterns by persona

| Persona | Rhythm signature |
|---|---|
| **יואל** | short-short-LONG-short pattern. Punch, punch, build, land. |
| **שירה** | LONG-short. The build, then the landing line on its own. |
| **גלעד** | short-pause-twist. Setup short. Punchline shorter. Aside in parens. |
| **דנה** | medium-short. Three sentences per beat, the third shorter. |
| **איתמר** | LONG-LONG-short. Patient build, then the line that pins it. |
| **נועה** | medium-short-medium. Conversational unevenness; natural. |

---

## 6. Connectives & discourse markers

### Hebrew discourse markers by register

| Register | Connectives used |
|---|---|
| **Casual** | אז, אבל, ו-, כי, אז, מתישהו |
| **Tech-informal** | אבל, או, ובכן, יחד עם זאת |
| **Tech-formal** | יחד עם זאת, מצד שני, בנוסף, עם זאת, בכל מקרה |
| **Formal-classical** | אולם, אך, אשר, מאחר ש, מכיוון ש, כתוצאה מ |

### Persona connective preferences

- **דנה** prefers: *"השאלה היא..."*, *"בסוף היום..."*, *"השורה התחתונה היא..."*
- **שירה** prefers: *"אולם..."*, *"ובכל זאת..."*, *"ראוי לציין כי..."*, *"אם נחזור לרגע..."*
- **איתמר** prefers: *"ובכל זאת..."*, *"כדאי לציין..."*, *"אם נחזור לרגע אחורה..."*, *"במבט לאחור..."*
- **יואל** prefers: *"אבל..."*, *"אז..."*, *"השורה התחתונה..."*, *"וזה ה-bet ש..."*
- **גלעד** prefers: *"רגע..."*, *"בקיצור..."*, *"וזה, חברים, היה הרגע ש..."*
- **נועה** prefers: *"במחשבה שנייה..."*, *"אם להיות כנה..."*, *"אני חושבת ש..."*

---

## 7. Vocabulary variation

### Anti-repetition rules

- A single distinctive word should not repeat within 3 paragraphs without rhetorical reason
- Variation through synonyms (Rav-Milim lookups): *"מצוין / מעולה / יוצא דופן / מרשים"* across an opinion piece
- For Dana's repeated soundbite: deliberate repetition is fine (the soundbite IS the device)
- For Shira's recurring image: deliberate repetition is fine (it's the structural device)

### Sentence-opener variation

Native Hebrew avoids opening 3 consecutive sentences with the same word. Detect and vary.

---

## 8. Anaphora clarity (pronoun reference)

### Hebrew pronoun rules

- **הוא / היא / הם / הן** — must have unambiguous antecedent
- **זה / זאת / אלה** — refers to the immediately preceding noun or proposition
- **את עצמו / את עצמה** — reflexive; must match subject

### Tech writing pitfall

When mixing Hebrew and English-script nouns, anaphora can become ambiguous: *"ה-MCP server לא ענה. הוא היה down."* — is *הוא* the MCP server or the agent? Rule: re-name the antecedent if ambiguity is possible.

---

## Phrasing check protocol (STEP 5e in the skill)

Run these checks in order, after the grammar check (STEP 5a-5d):

1. **Word-order check** — is the sentence Hebrew-natural or English-calqued?
2. **Idiom check** — are Hebrew idioms used; are English idioms NOT calqued?
3. **Register coherence** — does the vocabulary band hold across the text?
4. **Code-switching density** — does the density match the persona's fingerprint?
5. **Rhythm variation** — are sentence lengths varied per persona rhythm?
6. **Connectives** — are connectives chosen per register?
7. **Vocabulary variation** — is repetition deliberate, not accidental?
8. **Anaphora clarity** — is every pronoun antecedent clear?

Any failure → rewrite the offending sentence and re-check.

---

*This is the v0.3.0 phrasing layer. v0.4.0 will add programmatic detection of word-order and idiomaticity patterns via DictaBERT + regex pipelines.*
