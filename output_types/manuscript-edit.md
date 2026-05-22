# Output Type: Manuscript Edit

Editorial revision of an existing Hebrew manuscript. Produces tracked-changes output or restructured draft, depending on the requested edit level.

## When this output type is right

- **Developmental edit** — restructure chapter / section flow, identify weak arguments, recommend cuts/additions
- **Line edit** — sentence-level polishing: rhythm, word choice, persona consistency
- **Copy edit** — grammar, punctuation, spelling, consistency (registered against Academy of Hebrew Language standards)
- **Proofreading pass** — final typographical / formatting / number-format / Hebrew-English code-switching consistency
- **Authenticity / voice edit** — making translated content sound like original Hebrew

## Three edit levels — pick one or invoke all three

### Level 1 — Developmental edit (highest)

Focus: structure, argument, flow, persuasion, voice consistency.

Output format:
- Margin notes on each section
- "Big move" recommendations at the top (what restructure would most improve the chapter)
- Argument-tree analysis: does each claim earn its premises?
- Voice-consistency annotations: where does the persona drift?

### Level 2 — Line edit

Focus: sentence-level polish, rhythm, word choice.

Output format:
- Sentence-by-sentence rewrites (track changes style)
- Reason for each change (grammar / rhythm / persona / clarity)
- Cumulative voice fingerprint maintained

### Level 3 — Copy edit + proofread

Focus: errors-only.

Output format:
- Markup with all grammar / spelling / punctuation / formatting errors
- Style-sheet entries (consistency: "Apple's iPhone" not "Apple iPhone"; "פרודקשן" not "פרודקציה"; etc.)
- Number-format check, English-Hebrew code-switching consistency check

## Hebrew-specific edit considerations

- **Smikhut consistency** — check that smikhut is used consistently across the manuscript
- **Code-switching density** — flag drift (sudden shift in English-script density)
- **Number format** — digital throughout (manuscript convention)
- **Quotation marks** — Hebrew style consistent ("כך" not "כך")
- **Date format** — Israeli convention (DD/MM/YYYY)
- **Definite article rules** — every demonstrative gets its ה
- **Filler-word removal** — flag every אז/כאילו/בעצם/למעשה/פשוט for removal (per genre)
- **Anaphora** — every pronoun has unambiguous antecedent
- **Anglicism removal** — flag "אני הולך ל-" calques

## Persona consistency check

When the manuscript has a designated persona (e.g., Yoel / Shira / Itamar), the edit checks:

- **Voice fingerprint** — does each chapter / section open in the persona's voice?
- **Distinctive moves** — are the persona's signature moves present?
- **Register holds** — vocabulary band consistent
- **Sentence rhythm** — matches persona signature (Yoel short-short-LONG; Shira LONG-short; etc.)

## Output formats

### Markdown with edits inline

```markdown
## Original
> ההנחה הזה היתה בטוחה במשך 15 שנה.

## Edit
> ההנחה הזאת הייתה בטוחה במשך 15 שנה.

## Reason
> Gender agreement: הנחה is feminine, so demonstrative must be הזאת (not הזה).
> Verb form: היתה → הייתה per Academy spelling.
```

### Track-changes (for Word / Google Docs)

The skill outputs Markdown with strikethrough on deletions and bold on additions:

> ההנחה ~~הזה~~ **הזאת** ~~היתה~~ **הייתה** בטוחה במשך 15 שנה.

### Editorial memo (for developmental edit)

Long-form memo addressed to author:

```
לכותב/ת,

המסמך הזה מסכם את הפסקה הראשונה של הביקורת הפיתוחית. שלוש המלצות גדולות:

1. **פרק 3 חזק; פרק 4 חלש.** העבר את הסיפור של רותם מפרק 4 לראש פרק 3.
2. **הטיעון בפרק 7 לא מבוסס.** הוספת ראיון עם ע. שפר תעלה את האמינות משמעותית.
3. **קול נועה דועך אחרי פרק 9.** החזר אותו בפרקים 10-12.

הערות פרטניות מצורפות במרגינים בקובץ.

בכבוד,
[שמך]
```

## Validation gates (pre-output)

- [ ] Edit level explicit (developmental / line / copy / proofread)
- [ ] Every change has stated reason
- [ ] Persona consistency maintained across edits
- [ ] Hebrew grammar rules applied consistently
- [ ] No "improvements" that change the author's intent
- [ ] Editorial memo addresses big-picture moves before line-level
- [ ] Style sheet captures consistency decisions for future passes

## When to use which level

| Stage | Level |
|---|---|
| Draft 1 → Draft 2 | Developmental |
| Draft 2 → Draft 3 | Line edit |
| Draft 3 → submission to publisher | Copy edit |
| Galley proofs → print | Proofread |

## Related output types

- For original chapter writing: `book-chapter`
- For sample chapters in a proposal: `book-proposal`
- For shorter-form edits (article): apply same methodology, scoped down
