# Example Rewrite — Slack to Technical Blog

Same content, two registers. Shows how the skill calibrates jargon density, sentence length, and grammar style based on the target.

---

## Source content (English, technical context)

We hit a performance regression last week. Investigation showed our new Redis caching layer was warming up too slowly on container restart, causing the first 30 seconds of traffic on each new pod to see 10x normal latency. We added a warmup script that pre-loads the cache before health checks pass, and the issue is gone.

---

## Rewrite 1 — Slack / standup register

> חברה, יש פוסט-מורטם קצר על הרגרסיה של השבוע.
> ה-Redis cache שלנו לא התחמם מספיק מהר ב-startup של ה-pod. ה-30 שניות הראשונות אחרי כל restart ראו latency פי 10. כתבנו warmup script שטוען את ה-cache לפני שה-health check עובר. נפתר. מצרף את ה-PR.

**Register markers:**
- Short sentences, often verb-first ("נפתר.")
- Subject-drop ("כתבנו" without "אנחנו")
- Dense English-script jargon with prefix-hyphens: ה-Redis, ה-pod, ה-health check
- Casual sign-off ("מצרף את ה-PR")
- No filler words

---

## Rewrite 2 — Technical blog register

> ## ניתוח רגרסיית ביצועים: warmup של Redis cache
>
> השבוע נתקלנו ברגרסיית ביצועים שהשפיעה על כל ה-pods חדשים בקלסטר שלנו. החקירה הראתה שה-Redis caching layer שהוספנו בספרינט הקודם התחמם לאט מדי בעלייה של container חדש.
>
> בפועל, ה-30 שניות הראשונות של תעבורה אחרי כל restart של pod ראו latency פי 10 מהממוצע — pages משתמשים שנפלו על pod חדש קיבלו חוויית טעינה גרועה במידה משמעותית.
>
> **הפתרון:** הוספנו warmup script שטוען מראש את ה-cache עם המפתחות הנפוצים ביותר, ורק אז ה-health check של ה-pod עובר. ה-pod לא מקבל תעבורה עד שה-cache מוכן.
>
> **תוצאות:**
> - 0 שניות של latency-spike אחרי restart
> - אין צורך לשנות לוגיקה בקוד המוצר
> - ה-warmup script רץ במקביל ל-init של ה-pod, מוסיף כ-4 שניות לזמן הכולל של עלייה — קטן מספיק שלא להפריע ל-rolling deploys

**Register markers:**
- Full sentences, structured paragraphs
- Heading + sub-sections + bulleted results
- Mix of Hebrew prose with hyphen-prefixed English: ה-pods, ה-cache, ה-health check, ה-warmup script
- Approximation marker: "כ-4 שניות"
- Quantified results (this is how blog posts close)
- No filler words

---

## What changed between registers

| Dimension | Slack | Blog |
|---|---|---|
| Sentence length | 1 clause, often elliptical | 2–3 clauses, full |
| Subject | dropped | named when shifting |
| Structure | linear narrative | sections + bullets |
| Heading | none | yes |
| Quantification style | inline ("פי 10") | inline + bulleted summary |
| Sign-off | casual artifact link | "תוצאות:" data summary |
| Jargon density | maximum | medium — contextualized first |

Same vocabulary, same facts. Different rhythm and structure.
