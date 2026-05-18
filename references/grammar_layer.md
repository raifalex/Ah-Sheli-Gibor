# Grammar Layer — Israeli Tech Hebrew (2025)

This is the canonical grammar reference for the Ah Sheli Gibor skill. The rewriting protocol (`SKILL.md` §STEP 4) reads from here. Every rule here has a worked example.

---

## §1. Loanword verb conjugation — binyan pi'el default

Israeli tech Hebrew absorbs English verbs into **binyan pi'el** as the default. The consonants of the English verb stem become the Hebrew root.

### Procedure

1. Take the English verb stem (e.g., *deploy* → d-p-l, *commit* → k-m-t)
2. Insert it into the pi'el pattern: present `מַ_ַ_ֵ_`, past `_ִי_ֵ_`, future `אֲ_ַ_ֵ_`
3. Add Hebrew suffixes for person/gender/number

### The 10 priority verbs — full conjugation table

| Infinitive | Present (ms) | Past (3ms) | Past (1pl) | Future (1s) |
|---|---|---|---|---|
| **לדיפלוי** | מדיפלוי | דיפלוי | דיפלוינו | אדיפלוי |
| **לקומיט** | מקומיט | קומיט | קומיטנו | אקומיט |
| **לפוש** | מפוש | פוש | פושנו | אפוש |
| **למרג'** | ממרג' | מירג' | מירג'נו | אמרג' |
| **לשיפ** | משיפ | שיפ | שיפנו | אשיפ |
| **לדבג / לדיבג** | מדבג | דיבג | דיבגנו | אדבג |
| **לריפקטר** | מריפקטר | ריפקטר | ריפקטרנו | אריפקטר |
| **לסקייל** | מסקייל | סקייל | סקיילנו | אסקייל |
| **לפיין-טיון** | מפיין-טיון | פיין-טיון | פיין-טיוננו | אפיין-טיון |
| **לאמבד** | מאמבד | אמבד | אמבדנו | אאמבד |

### Hif'il exceptions

Verbs with causative semantics ("cause to do X") sometimes enter hif'il:

- **להרצות** (to run [tests/scripts]) — *מריץ / הריץ / ירוץ*. Wholly Hebrew; the English "run" did not need to be borrowed.
- **להפעיל** (to activate/run a service) — *מפעיל / הפעיל*. Native Hebrew preserved.

Pure anglicisms with causative meaning still default to pi'el: *לסקייל* (to scale up = cause to grow) is pi'el, not hif'il.

### "לעשות X" → "לX" — modern preference

Pre-2020 Israeli tech Hebrew often used periphrastic forms: *לעשות קומיט, לעשות פוש, לעשות דיפלוי*. In 2025 these sound dated. The pi'el verb form is current: *לקומיט, לפוש, לדיפלוי*.

Exception: when the action is one-off or non-iterative, the periphrastic can be acceptable: *"בוא נעשה ריפקטור גדול בסוף הרבעון"* — here *ריפקטור* is a noun-event, not a verb-action, so the analytical form fits.

---

## §2. Loanword noun gender and plural

### Defaults

- **Gender:** masculine (זכר) — default for nearly all tech loanwords
- **Plural:** -ים (masculine plural) regardless of source-language gender or content

### Gender lookup table (15 priority nouns)

| Noun | Gender | Plural | With definite |
|---|---|---|---|
| פיצ'ר | ז' | פיצ'רים | הפיצ'ר |
| באג | ז' | באגים | הבאג |
| ספרינט | ז' | ספרינטים | הספרינט |
| דשבורד | ז' | דשבורדים | הדשבורד |
| פייפליין | ז' | פייפליינים | הפייפליין |
| סטייקהולדר | ז' | סטייקהולדרים | הסטייקהולדר |
| פרומפט | ז' | פרומפטים | הפרומפט |
| מודל | ז' | מודלים | המודל |
| טיקט | ז' | טיקטים | הטיקט |
| רילייס | ז' | רילייסים | הרילייס |
| דיפלוימנט | ז' | דיפלוימנטים | הדיפלוימנט |
| ריוויו | ז' | ריווייאים / ריווויים | הריוויו |
| קומיט | ז' | קומיטים | הקומיט |
| בראנץ' | ז' | בראנצ'ים | הבראנץ' |
| איטרציה | נ' | איטרציות | האיטרציה |

### Feminine exceptions

Words ending in inherently feminine sounds (-ה, -ת) or with established Hebrew feminine origins:

- **גרסה** (נ') — איטרציה (נ'), ארכיטקטורה (נ'), תשתית (נ'), מערכת (נ'), פלטפורמה (נ'), טכנולוגיה (נ'), קונפיגורציה (נ'), פונקציה (נ'), אופטימיזציה (נ')

### Plural mismatches to avoid

- ❌ פיצ'רות → ✅ פיצ'רים (loanword plural is -ים even though *feature* is content-neutral in English)
- ❌ באגות → ✅ באגים
- ❌ מודלות → ✅ מודלים

---

## §3. Construct state (סמיכות) for compound nouns

Hebrew has two ways to express "X of Y":

1. **Smikhut** (construct state): *מנהל מוצר* (product manager), *ראש צוות* (team lead), *בעל תפקיד* (role owner)
2. **Analytical with של**: *המנהל של המוצר* (less preferred for tech compounds)

### Rule for tech Hebrew

- **Two Hebrew nouns** → use smikhut: *מנהל המוצר, ראש המערכת, מהנדס התשתית*
- **One Hebrew + one English noun** → either:
  - Smikhut with English noun on right: *מנהל ה-product, ראש ה-team*
  - Full English compound: *ה-Product Manager*
- **Two English nouns** → keep both English: *ה-Product Manager, ה-Tech Lead*

### Anti-pattern: hybrid with של and definite article

❌ *המנהל של הפרודקט* — broken; sounds like a direct translation of "the manager of the product"
✅ *מנהל המוצר* — correct smikhut
✅ *ה-Product Manager* — correct full English

### Worked examples

| Source register | Construct |
|---|---|
| English: "the product manager" | מנהל המוצר *or* ה-Product Manager |
| English: "the platform's reliability" | מהימנות הפלטפורמה |
| English: "stakeholder buy-in" | תמיכת הסטייקהולדרים *or* buy-in מהסטייקהולדרים |
| English: "the team's velocity" | מהירות הצוות |
| English: "tech lead of the API team" | ראש הצוות של ה-API *or* tech lead של צוות ה-API |

---

## §4. Preposition binding with loanwords

Three patterns based on the script of the loanword:

### Pattern A — English-script loanword (kept in English letters)

Hebrew prefix attaches with **hyphen**:

- **ב-MCP**, ב-AWS, ב-Kubernetes
- **ל-IAM**, ל-CloudTrail, ל-Claude
- **מ-Postgres**, מ-Kafka
- **ה-MCP**, ה-Pinecone, ה-IAM (definite article)

Anti-patterns:
- ❌ בMCP (no hyphen)
- ❌ ה MCP (space)
- ❌ האי-איי-אם (Hebraized — never)

### Pattern B — Loanword transliterated to Hebrew

Hebrew prefix attaches **directly** as in native words:

- **בפיצ'ר**, בבאג, בספרינט
- **לדשבורד**, לפייפליין, לסטייקהולדר
- **מהסטייקהולדר**, מהדשבורד
- **הפיצ'ר**, הבאג (definite article — no hyphen)

### Pattern C — Hebrew compound with English part

Treat the English part as a unit; use hyphen at the boundary:

- ב-RAG פייפליין → "in the RAG pipeline"
- ל-MCP סרבר → "to the MCP server"
- מה-vector DB → "from the vector DB"

### Definite article on English-script loanwords

`ה-` always attaches via hyphen and replaces the indefinite. Never duplicate with native Hebrew "ה" plus full-Hebrew loanword:

- ✅ ה-MCP / ✅ הפיצ'ר
- ❌ ה-הפיצ'ר / ❌ ההMCP

---

## §5. Register-specific grammar

The same content requires different output per register. This is the rendering layer on top of the vocabulary and grammar layers above.

### Slack / standup

- **Sentence:** short, often subject-less ellipsis
- **Punctuation:** light; periods OK at line ends
- **Jargon density:** maximum; all anglicized loanwords
- **Filler:** *אז* mildly acceptable at start of message; no others

**Example:**
> דיפלוינו. עלה. הכל ירוק.
> אבל יש קפיצה ב-latency בשרת eu-west-1, מסתכלים.

### Technical blog

- **Sentence:** full, medium-length, 1–3 clauses
- **Punctuation:** standard
- **Jargon density:** medium; contextualize first occurrence
- **Structure:** intro paragraph, technical body, takeaway

**Example:**
> השבוע ריפקטרנו את ה-payment service שלנו ופירקנו אותו לשלושה microservices. המטרה היתה להפריד את ה-billing logic מה-fraud detection, כי שני הזרמים התחילו להתנגש בלוגיקה משותפת.
> השינוי הוריד את ה-latency של ה-checkout ב-30% והפך את ה-on-call לפשוט יותר.

### LinkedIn

- **Sentence:** medium; first-person voice
- **Punctuation:** standard + occasional rhetorical breaks
- **Jargon density:** medium; story-driven
- **Structure:** hook → personal narrative → insight → CTA (often subtle)

**Example:**
> רצינו לשתף משהו שלמדנו הרבה ממנו הרבעון.
> שיפנו פיצ'ר חדש שמרכז את כל ה-AI agents הפנימיים שלנו תחת MCP אחד מאוחד.
> זה לקח שלושה ספרינטים יותר ממה שצפינו — אבל ה-payback היה משמעותי. מאז שעלינו: 40% פחות overhead ב-onboarding של agents חדשים, ואפס באגים של context-leak בין agents.
> מי שמריץ agentic AI בפרודקשן בטח מכיר את הכאב הזה. נשמח לדבר.

### Investor pitch

- **Sentence:** medium-formal; full clauses; assertive
- **Punctuation:** standard
- **Jargon density:** controlled; English terms in parentheses where clarifying
- **Structure:** problem → traction → moat → ask

**Example:**
> החברה השיגה Product-Market Fit ב-Q3 2025 ומציגה צמיחה של 40% רבעון-על-רבעון ב-ARR.
> הפלטפורמה שלנו, שמבוססת על ארכיטקטורת RAG ייעודית (Retrieval-Augmented Generation), מעבדת כיום כ-3 מיליון בקשות בחודש עבור 50 לקוחות enterprise.
> הצוות מונה 18 איש; אנחנו מגייסים סבב Series A של 12 מיליון דולר להרחבת ה-go-to-market בארה"ב ולהכפלת צוות ה-engineering.

### PR / RFC document

- **Sentence:** precise, short; minimal qualification
- **Punctuation:** standard + heavy use of bullet lists
- **Jargon density:** minimal; precision over style
- **Structure:** context → proposal → alternatives → impact → rollout

**Example:**
> # הצעת שינוי ארכיטקטוני: הפרדת ה-auth service
>
> **רקע:** ה-auth service הנוכחי מטפל גם ב-session management וגם ב-permission resolution. בהיקף הנוכחי (12 צרכנים פנימיים, 4M בקשות/יום), הצימוד הזה יוצר latency tail בעיתי.
>
> **הצעה:** לפצל ל-auth-session (חסר-state, מטפל ב-JWT validation בלבד) ול-auth-permissions (stateful, עם cache פנימי).
>
> **השפעה צפויה:** הורדת latency p99 מ-140ms ל-60ms; הכפלת ה-throughput המקסימלי.

---

## §6. Cross-cutting grammar checks (always)

Run these before outputting any rewritten text:

1. **Definite article** after demonstrative/possessive — ✅ ההנחה הזאת, ✅ הסוכן הזה
2. **Partitive verb agreement** — ✅ חלקכם חתם, ✅ רוב הצוות מסכים
3. **No "אני הולך ל-"** — ✅ אני אטען, אני אראה
4. **"את" before definite direct object** — ✅ קוראים את האירוע, ✅ מציגים את ה-diff
5. **Approximation marker כ-** — ✅ כ-150 מיליון, ✅ לפני כשמונה-עשר חודשים
6. **No filler words** in written register — remove *אז, כאילו, פשוט, למעשה, בעצם*
7. **Numbers digital** for mid-sentence delivery — ✅ 18 חודשים, ✅ 150 מיליון
8. **Product names stay English** — ✅ AWS, ✅ Claude, ✅ Cursor (never translate)
9. **Hyphen before English-script after prefix** — ✅ ב-MCP, ✅ ה-IAM
10. **No -ing on Hebrew verbs** — ❌ דפלויאינג, ✅ מדיפלוי (or noun: דיפלוימנט)

---

*Source attribution: §1 conjugation tables from ah-sheli-gibor-spec-v2 (2026-05-18). §2 gender defaults from spec + Israeli tech corpus observation. §3 smikhut rules from classical Hebrew grammar + hebrew_style_guide.md §3. §4 preposition binding from hebrew_style_guide.md §2. §5 register grammar from spec + hebrew_style_guide.md §1. §6 from hebrew_style_guide.md §3 + §7.*
