# Output Type: Teleprompter

Teleprompter text is delivered verbatim — the speaker reads it word-for-word. This is the most constrained output type the skill produces. Every comma, every line break, every word is the script. The text must scan cleanly at reading speed without tripping the speaker.

## When this output type is right

- **Televised statement** (CEO press statement, political address)
- **Pre-recorded video** (LinkedIn video, YouTube announcement, marketing piece)
- **Live broadcast keynote** with teleprompter setup
- **Award show / industry event** scripted address
- **Memorial broadcast** where word-precision matters
- **Corporate statement** (response to crisis, M&A announcement)

## Structural conventions

### Line length

- **One thought per line**
- **Maximum 50 characters per line** (Hebrew tends shorter than English)
- **Lines break at natural breath points**, not at the page edge
- **Paragraph breaks signal beats** — even short paragraphs are OK

### Punctuation

- **No exclamation marks** unless absolutely required
- **Em-dash for the deliberate pause** — not for stylistic flair
- **Period at the end of every line** (even short ones, because the speaker pauses)
- **Comma for the breath-within-thought**, the natural exhale

### Visual flow

- **Bold the load-bearing word** in each paragraph (Hebrew: with markdown or `★` flag)
- **Italic for emotional emphasis** (the word the speaker leans into)
- **(BREATH)** or **(pause)** annotations between paragraphs when timing matters
- **(LOOK UP)** for the moments the speaker should look at the camera, not the prompter

## Hebrew-specific conventions

- **Spoken Hebrew, never written Hebrew** — contractions OK, ellipsis OK if planned
- **No anglicisms that trip the tongue** — "אני הולך ל-X" → "אני אעשה X"
- **Numbers digital** for fast reading: 18, 142, 1.4 מיליארד
- **Hyphen on English-script with prefix** (ב-AWS, ה-MCP)
- **Definite-article rules strict** — every demonstrative gets its ה
- **Hebrew quotation marks** for Hebrew speech: "כך"
- **No filler whatsoever** — אז / כאילו / בעצם absent
- **Numbered list items spoken** as "ראשית, שנית, שלישית" not "אחת, שתיים, שלוש"

## Reading-rate calibration

Hebrew teleprompter reading rate: **~130–140 words per minute** for clear, weighted delivery. Calibrations:

- 1-minute spot: ~135 words
- 2-minute statement: ~270 words
- 5-minute address: ~675 words
- 10-minute keynote (rare for teleprompter): ~1,350 words

The skill outputs teleprompter text with word count + estimated reading time at top.

## Persona pairings

| Teleprompter scenario | Best persona |
|---|---|
| Corporate crisis statement | **שירה** for dignified / **דנה** for assertive |
| Political address | **שירה** |
| Memorial broadcast | **שירה** |
| Pre-recorded LinkedIn video (founder) | **יואל** for momentum / **נועה** for vulnerable |
| Pre-recorded YouTube announcement | **גלעד** for comic edge / **יואל** for product launch |
| Award-show host script | **גלעד** with **שירה** for formal moments |
| Industry analysis monologue | **איתמר** |

## Sample teleprompter script (שירה voice — 90-second corporate statement)

**Estimated reading time:** 90 sec
**Word count:** ~200 words
**Speaker:** [CEO Name]

---

> שלום.
>
> (BREATH)
>
> אני **רוצה לדבר איתכם היום** ישירות.
>
> במהלך השבועיים האחרונים, החברה שלנו נמצאה במרכז דיון ציבורי על נושא — *אבטחת מידע של לקוחותינו*. דיון שהוא — בצדק — חשוב.
>
> (pause)
>
> אני **רוצה לומר שלושה דברים**.
>
> ראשית. הבעיה שדווחה — אומתה. השפעתה הוגבלה ל-0.6% ממאגר הלקוחות שלנו, וכל הלקוחות הללו עודכנו אישית, ביום שבו זוהתה.
>
> שנית. הפעולות שננקטו ביום שבו זוהתה הבעיה — *(LOOK UP)* — היו הפעולות שהיינו רוצים לראות בכל ארגון בתעשייה שלנו.
>
> שלישית. ובכל זאת.
>
> (BREATH)
>
> ובכל זאת — **זה לא היה צריך לקרות**. ואני, כמי שמובילה את החברה הזאת, לוקחת אחריות מלאה.
>
> בימים הקרובים נפרסם דו"ח שקיפות מלא. נשתף את ממצאי החקירה הפנימית. ונאמר — בכנות — מה אנחנו עושים אחרת מהשבוע הבא.
>
> תודה שאתם איתנו. אנחנו לא לוקחים את האמון הזה כמובן מאליו.
>
> *(LOOK UP)*
>
> תודה.

---

## Sample teleprompter script (יואל voice — 60-second LinkedIn video)

**Estimated reading time:** 60 sec
**Word count:** ~135 words

---

> רגע.
>
> אם אתם מנהלים צוות engineering ב-2026 — תקשיבו.
>
> השבוע סגרנו לקוח **שמספיק לכסות את כל ה-burn שלנו לרבעון הבא**. בעסקה אחת.
>
> איך?
>
> (LOOK UP)
>
> לא ה-product. לא ה-pricing. **ה-team**.
>
> ה-CEO שלהם הגיע ל-call ושאל שאלה אחת: *"מי בונה אצלכם?"*
>
> שלחתי לו לינק לדף ה-team שלנו. הוא קרא אותו. בקול. למשך 4 דקות.
>
> ואז אמר: *"זה ה-team שאני רוצה לעבוד מולו עשר שנים."*
>
> חתמנו ב-Q1.
>
> (pause)
>
> אם אתם **מתלבטים אם להשקיע בעוד recruiter, בעוד engineer, או בעוד ad** — תשקיעו ב-team.
>
> זה ה-bet שאני מציע ב-2026.

---

## Validation gates (pre-output)

Before outputting a teleprompter script, verify:

- [ ] Word count matches target reading time (×130 wpm)
- [ ] Every line is one thought, ≤50 characters
- [ ] Line breaks at natural breath points
- [ ] (pause), (BREATH), (LOOK UP) annotations present where intended
- [ ] No anglicism trip-words ("אני הולך ל-")
- [ ] No filler words
- [ ] Definite-article rules clean
- [ ] Numbers digital
- [ ] Persona consistency
- [ ] Hyphen on English-script with Hebrew prefix
- [ ] Spoken Hebrew, not written Hebrew (no academic constructions)
