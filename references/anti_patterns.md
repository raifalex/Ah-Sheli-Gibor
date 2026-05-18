# Anti-patterns — Bad Output This Skill Must Never Produce

These are the failure modes that immediately mark a rewrite as inauthentic. Cross-check every output against this table in STEP 5 (Authenticity Review). A single anti-pattern is enough to disqualify the rewrite and trigger a rewrite of that clause.

---

## Morphology errors

### ❌ -ing suffix on Hebrew verbs

| ❌ Wrong | ✅ Correct | Why |
|---|---|---|
| עשינו דפלויאינג של הפיצ'ר | דיפלוינו את הפיצ'ר | Hebrew has no -ing suffix. Use the pi'el verb form or a Hebrew noun (דיפלוימנט) |
| התחלנו קומיטינג עם רוטציה | התחלנו לקומיט ברוטציה | Same issue |
| מבצעים סקיילינג של ה-DB | מסקיילים את ה-DB | Same issue |

### ❌ Periphrastic "לעשות X" when pi'el verb exists

In 2025 the pi'el verb form is current; *לעשות קומיט* sounds dated.

| ❌ Wrong | ✅ Correct |
|---|---|
| לעשות קומיט | לקומיט |
| לעשות פוש | לפוש |
| לעשות מרג' | למרג' |
| לעשות דיפלוי | לדיפלוי |
| לעשות דיבוג | לדבג / לדיבג |

**Acceptable exception:** when the action is a one-off significant event, the noun-event form fits: *"בוא נעשה ריפקטור גדול בסוף הרבעון"* — here *ריפקטור* is a noun event, not the iterative verb action.

### ❌ Wrong plural for loanwords

| ❌ Wrong | ✅ Correct |
|---|---|
| פיצ'רות | פיצ'רים |
| באגות | באגים |
| מודלות | מודלים |
| ספרינטות | ספרינטים |

Loanword plurals are **almost universally -ים**, regardless of source-language gender.

### ❌ Wrong gender agreement

| ❌ Wrong | ✅ Correct |
|---|---|
| הפיצ'ר הזאת | הפיצ'ר הזה (פיצ'ר ז') |
| הבאג הזאת | הבאג הזה (באג ז') |
| המודל הזאת | המודל הזה (מודל ז') |
| הארכיטקטורה הזה | הארכיטקטורה הזאת (ארכיטקטורה נ') |

See `grammar_layer.md` §2 for the full gender table.

---

## Code-switching errors

### ❌ Missing hyphen on English-script + Hebrew prefix

| ❌ Wrong | ✅ Correct |
|---|---|
| בMCP | ב-MCP |
| לAWS | ל-AWS |
| מKafka | מ-Kafka |
| הIAM | ה-IAM |

### ❌ Hebrew transliteration of product names

| ❌ Wrong | ✅ Correct |
|---|---|
| השתמשנו בקלוד | השתמשנו ב-Claude |
| עברנו לאמזון-וב-סרוויסיס | עברנו ל-AWS |
| ה-קוּרסוּר עזר | ה-Cursor עזר |
| הפינקון שלנו | ה-Pinecone שלנו |

Product names, platform names, company names — always English.

### ❌ -ים suffix on English-script noun

| ❌ Wrong | ✅ Correct |
|---|---|
| ה-MCP-ים | ה-MCPs |
| ה-roles-ים | ה-roles |
| ה-tokens-ים | ה-tokens |

When the noun stays in English script, the plural takes English -s. Hebrew -ים only attaches to fully-transliterated loanwords.

---

## Smikhut / possessive errors

### ❌ Hybrid construct with של on translated head

| ❌ Wrong | ✅ Correct |
|---|---|
| המנהל של הפרודקט | מנהל המוצר *or* ה-Product Manager |
| הראש של הטים | ראש הצוות *or* ה-Tech Lead |
| הסטייקהולדרים של הפרויקט | סטייקהולדרי הפרויקט *or* הסטייקהולדרים בפרויקט |

When both sides are Hebrew, use smikhut. When mixing scripts, use full English compound or smikhut with English on the right.

### ❌ Doubled definite article

| ❌ Wrong | ✅ Correct |
|---|---|
| ה-המנהל של המוצר | מנהל המוצר |
| ה-הפיצ'ר | הפיצ'ר |
| ה-ה-MCP | ה-MCP |

---

## Spelling and transliteration errors

| ❌ Wrong | ✅ Correct | Why |
|---|---|---|
| סטיקהולדר | סטייקהולדר | Double vowels preserved (stake → סטייק) |
| פיצר | פיצ'ר | Gershayim (') marks the ch sound |
| מרגר / מרגג'ר | מנג'ר / מנגר | English manager — gershayim for ג |
| דשבורד (with קמץ) | דשבורד | No vowel marks in modern tech writing |

---

## Register errors

### ❌ Slack-style ellipsis in formal documents

Bad in investor-pitch or pr-rfc:
> "סקיילנו פי 10. ירד latency. הכל סבבה."

Good in those registers:
> "במהלך הרבעון הרחבנו את התשתית פי 10 והורדנו את ה-latency של ה-API ב-60%."

### ❌ Investor-pitch formality in slack

Bad in slack/standup:
> "במהלך הספרינט הנוכחי השלמנו את כל המשימות הקריטיות במסגרת ה-roadmap הרבעוני."

Good in slack/standup:
> "סגרנו את כל הקריטיים. נשארו 3 nice-to-have."

### ❌ Filler words in written text

| ❌ Wrong | ✅ Correct |
|---|---|
| אז למעשה החלטנו פשוט לעבור ל-microservices | החלטנו לעבור ל-microservices |
| בעצם המודל עובד טוב כאילו 90% מהזמן | המודל עובד טוב 90% מהזמן |

*אז, כאילו, פשוט, למעשה, בעצם* — remove from technical-blog, linkedin, investor-pitch, pr-rfc. Acceptable in slack/standup only as a sentence-opening connector.

---

## Anglicism / translation errors

### ❌ "אני הולך ל-" — literal translation of "I'm going to"

| ❌ Wrong | ✅ Correct |
|---|---|
| אני הולך לטעון שלוש טענות | אטען שלוש טענות / אני אטען |
| אנחנו הולכים להריץ אינפרנס | נריץ אינפרנס / אנחנו נריץ |

Use Hebrew future tense. *אני הולך ל-* only when literally signaling movement to the next bit.

### ❌ Missing את before definite direct object

| ❌ Wrong | ✅ Correct |
|---|---|
| קראנו האירוע | קראנו את האירוע |
| ראינו ה-diff | ראינו את ה-diff |

In scripted/precise text always include את. Casual slack/standup tolerates dropping it but written tech Hebrew does not.

### ❌ "בערך" instead of approximation prefix כ-

| ❌ Wrong | ✅ Correct |
|---|---|
| לפני בערך שמונה-עשר חודשים | לפני כשמונה-עשר חודשים |
| בערך 150 מיליון משתמשים | כ-150 מיליון משתמשים |

*בערך* sounds awkward in spoken/written professional Hebrew. Use *כ-* prefix.

---

## Pre-2025 AI vocabulary

Israeli tech AI Hebrew evolved sharply in 2024-2025. Pre-2025 hype-era language sounds dated.

| ❌ 2022-era (dated) | ✅ 2025-current |
|---|---|
| הצ'אטGPT שלנו | המודל שלנו / ה-LLM שלנו |
| בינה מלאכותית גנרטיבית (over-used as buzzword) | AI / מודל גנרטיבי (used precisely) |
| GPT-3 / GPT-4 ב-2025 הקשר | Claude / GPT-4o / Sonnet 4.6 / קונקרטי |
| AI שיחתי | agentic AI / סוכן AI |

---

## Final authenticity check — the native speaker test

After applying all the above, read the output as a 2025 Israeli engineer at Monday, Wix, or Mobileye. Ask:

1. Does any phrase sound like a translation rather than original Hebrew thought?
2. Is there jargon overuse where plain Hebrew would be more natural?
3. Is the rhythm right for the target register?
4. Would I, as a native, write this — or am I tolerating something a translator produced?

If any answer is "no" / "yes (problem)" — rewrite the clause. Iterate until clean. Output only the final version.
