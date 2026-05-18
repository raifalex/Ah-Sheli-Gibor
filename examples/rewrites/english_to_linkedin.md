# Example Rewrite — English Blog Post → Hebrew LinkedIn Post

Shows how the skill comprehends content in English and reconstructs it in the Israeli tech LinkedIn voice — first-person, story-driven, with controlled jargon and a closing hook.

---

## Source (English)

> ### Lessons from scaling our agentic AI platform from 0 to 10,000 daily active users
>
> When we started building our agentic AI platform 14 months ago, we made a series of architectural bets that we weren't sure would hold up. Most of them did. Some didn't. Here are three things we got wrong, and what we'd do differently.
>
> **1. We underestimated the cost of context.** Our early agents passed full conversation history with every model call. At low volume, this was fine. At scale, our token bill grew 6x faster than user growth.
>
> **2. We over-engineered the tool-use layer.** We built our own MCP-equivalent before Anthropic's MCP existed. The day MCP was announced, we spent two weeks throwing away our internal framework and migrating to MCP. Should have waited.
>
> **3. We hired too late.** The team of three that built v1 was running on fumes by the time we closed our seed round. We should have hired the fourth engineer six months earlier.
>
> If you're building in agentic AI today, the playbook is changing weekly. Talk to people who shipped recently. The lessons from 2023 don't apply.

---

## Rewrite — Hebrew LinkedIn (target register)

> רצינו לשתף שלושה דברים שטעינו בהם בדרך מ-0 ל-10,000 משתמשים יומיים פעילים על הפלטפורמה האגנטית שלנו — אחרי 14 חודשי בנייה.
>
> **1. לא תמחרנו נכון את עלות הקונטקסט.** ה-agents הראשונים שלנו העבירו את כל היסטוריית השיחה עם כל קריאה ל-model. בהיקפים קטנים זה היה בסדר. כשסקיילנו, החשבון על הטוקנים גדל פי 6 מהר יותר מצמיחת המשתמשים.
>
> **2. עשינו over-engineering לשכבת ה-tool-use.** בנינו MCP פנימי שלנו לפני ש-MCP של Anthropic בכלל היה קיים. ביום שה-MCP הוכרז, שרפנו שבועיים לזרוק את הפריימוורק הפנימי ולעבור ל-MCP הסטנדרטי. אם היינו מחכים — היינו חוסכים שבועיים.
>
> **3. גייסנו מאוחר מדי.** הצוות של שלושה שבנה את v1 היה שרוף עד הסוף עד שסגרנו את ה-seed. את המהנדס הרביעי היינו צריכים לגייס חצי שנה מוקדם יותר.
>
> מי שבונה היום בעולם של agentic AI — הפלייבוק משתנה כל שבוע. תדברו עם אנשים ששיפו לאחרונה. השיעורים של 2023 כבר לא רלוונטיים.

---

## Register-specific choices documented

**Voice:**
- First-person plural "אנחנו" implied throughout, makes the story personal
- Direct address to reader at the close ("מי שבונה היום...")
- Self-deprecating honesty ("שטעינו בהם", "שרפנו שבועיים") — LinkedIn rhetorical pattern

**Jargon calibration:**
- ה-agents, ה-model, ה-MCP — English-script with prefix-hyphen (these are technical anchors)
- אגנטית (transliterated adjective) — 2025 vocabulary, signals current
- סקיילנו — pi'el verb form, current
- over-engineering kept English (full English term, no Hebrew calque)
- פריימוורק — transliterated noun
- v1, seed — kept English (version label, funding stage)

**Numbers:**
- 0, 10,000, 14, 6, v1, 2023 — digital throughout, idiomatic for LinkedIn
- "פי 6" — Hebrew multiplication idiom (not "x6")

**Grammar:**
- "ה-MCP של Anthropic בכלל היה קיים" — definite article + smikhut variant + adverb בכלל for emphasis
- "אם היינו מחכים — היינו חוסכים" — Hebrew counterfactual conditional, current usage
- Approximation absent because numbers are exact

**Story arc:**
- Hook → three points (numbered) → closing rule → CTA-implicit
- No "אז" / "כאילו" / "בעצם" filler
- Sign-off shifts from past-tense narrative to imperative ("תדברו")

**What was kept structurally identical:**
- Three numbered points with bold lead-ins
- Same factual content
- Same emotional arc (early-confidence → specific-mistakes → forward-looking advice)

**What was reshaped:**
- "Most of them did. Some didn't." → consolidated into the lead paragraph
- The 6x bill → "פי 6" idiom that lands harder in Hebrew
- "Should have waited" → "אם היינו מחכים — היינו חוסכים שבועיים" (counterfactual is more natural in Hebrew than English-style "should have")
- "running on fumes" → "שרוף עד הסוף" (cultural translation)
- "talk to people who shipped recently" → "תדברו עם אנשים ששיפו לאחרונה" (imperative + pi'el verb)

---

This is what authentic rewriting looks like. Not translation. Reconstruction.
