# Output Evaluation Rubric — 4-Axis Scoring

Every output from the skill is evaluated on four axes, scored 1–10 each. This is STEP 5g of the validation protocol. The rubric is in Hebrew because it's the language of the output being evaluated.

---

## The four axes

### 1. רלוונטיות (Relevance) — 1 to 10

**Definition:** איכות בחירת התוכן החשוב מתוך המקור — האם הסיכום / הכתיבה מחדש / הפיץ' / הנאום בחר את הנקודות החשובות באמת מבין כל מה שאפשר היה לבחור.

**Sub-criteria:**
- **Coverage of key points** — did the output address the user's actual question / topic?
- **Selection precision** — are the chosen details the *most* important, or just easy ones?
- **Off-topic exclusion** — does the output stay on the asked topic?
- **Audience fit** — are the selected points relevant to the *audience* (investors / engineers / board / public)?

**Scoring guide:**

| Score | Description |
|---|---|
| 10 | Perfect selection — every word earns its place. Every key insight from the source is present. Nothing extraneous. |
| 9 | Excellent — minor missed nuance or one extraneous detail. |
| 8 | Strong — main points covered well; some priority calls debatable. |
| 7 | Acceptable — main points covered; some priority misses. |
| 6 | Marginal — most key points but obvious omissions or extras. |
| 5 | Weak — partial coverage; some misplaced emphasis. |
| 4 | Poor — important points missed; weight on wrong details. |
| ≤3 | Failed — output addresses a different topic or misses the substance. |

**How to score:** Read the source, list the 5–10 key points. Read the output. Score = (% of source key-points present and given correct weight).

---

### 2. קוהרנטיות (Coherence) — 1 to 10

**Definition:** האיכות הקולקטיבית של כל המשפטים יחד — האם הטקסט זורם, האם הוא בנוי באופן הגיוני, האם המעבר בין רעיונות חלק.

**Sub-criteria:**
- **Logical flow** — does each sentence follow from the prior?
- **Argument arc** — does the whole piece have a clear narrative / argument structure?
- **Transition smoothness** — are transitions between paragraphs/cards explicit and natural?
- **Tone consistency** — does the voice hold across the whole output?
- **Section structure** — are sections proportioned correctly (intro / body / close)?

**Scoring guide:**

| Score | Description |
|---|---|
| 10 | Perfect — output reads as one continuous coherent thought. Every transition earns its place. |
| 9 | Excellent — one minor flow issue or one transition that could be smoother. |
| 8 | Strong — coherent overall; some transitions are too abrupt or sections proportioned awkwardly. |
| 7 | Acceptable — coherent within paragraphs; some cross-paragraph stiffness. |
| 6 | Marginal — paragraphs are individually coherent but don't build to a whole. |
| 5 | Weak — paragraphs feel disconnected; argument arc is unclear. |
| 4 | Poor — paragraphs contradict each other in tone or logic. |
| ≤3 | Failed — output is a list of disconnected statements. |

**How to score:** Read the output aloud. Note where you stumble or where you'd insert "wait, what?" Score = 10 - (number of stumbles + transitions that feel abrupt).

---

### 3. עקביות (Consistency) — 1 to 10

**Definition:** ההתאמה העובדתית בין הפלט למקור המסוכם — האם כל עובדה, מספר, ציטוט, ושם בפלט נמצאים גם במקור (או נכונים אם הם תוכן חדש).

**Sub-criteria:**
- **Factual accuracy** — every claim traceable to source or independently verifiable
- **Number precision** — every number in the output matches the source exactly
- **Quote accuracy** — every quoted sentence is verbatim from source (or properly paraphrased)
- **Attribution** — every claim attributed to the right person / organization
- **Timeline accuracy** — every date / sequence matches the source
- **No hallucination** — no facts invented that aren't in the source

**Scoring guide:**

| Score | Description |
|---|---|
| 10 | Perfect — every fact verified against source. Zero hallucinations. Zero number errors. |
| 9 | Excellent — one minor paraphrase that slightly drifts but stays accurate. |
| 8 | Strong — all major facts correct; one minor number off or one minor attribution issue. |
| 7 | Acceptable — main facts correct; some paraphrase drift. |
| 6 | Marginal — facts mostly correct but at least one verifiable error. |
| 5 | Weak — multiple verifiable errors. |
| 4 | Poor — significant fabrication or misattribution. |
| ≤3 | Failed — substantial hallucination. Reject and rewrite. |

**How to score:** For each factual claim in output, cross-reference to source. Mark errors. Score = 10 - (number of errors × severity weight). One hallucinated number = -3. One wrong attribution = -2. One misquoted line = -3.

**Critical for talking-cards register:** עקביות must be ≥ 9 — facts must hold under hostile scrutiny in a debate or interview.

---

### 4. רהיטות (Fluency) — 1 to 10

**Definition:** איכות הסיכום במונחים של דקדוק, איות, פיסוק, בחירת מילים, ומבנה משפט — האם הטקסט נשמע כמו עברית שכותב מנוסה היה כותב.

**Sub-criteria:**
- **Grammar correctness** — binyan / gender / number / smikhut / preposition all clean
- **Spelling** — every word spelled correctly (Academy-compliant)
- **Punctuation** — Hebrew punctuation conventions followed
- **Word choice** — vocabulary fits the register; no awkward picks
- **Sentence structure** — natural Hebrew word order; varied length
- **Idiomaticity** — Hebrew idioms used naturally; no English calques
- **Persona fidelity** — voice matches the chosen persona

**Scoring guide:**

| Score | Description |
|---|---|
| 10 | Perfect — reads as if written by a native Hebrew speaker with the persona's voice. Zero grammar / spelling / punctuation errors. |
| 9 | Excellent — one minor word-choice that could be sharper. |
| 8 | Strong — clean overall; one or two awkward phrasings; persona consistent. |
| 7 | Acceptable — readable; some grammar slips or persona drift. |
| 6 | Marginal — readable but feels translated in places. |
| 5 | Weak — multiple grammar errors or persona break. |
| 4 | Poor — reads like a translation; multiple errors. |
| ≤3 | Failed — incomprehensible or wrong language register. |

**How to score:** Apply STEP 5a (regex grammar) + STEP 5b (model grammar) + STEP 5e (phrasing) + STEP 5d (persona consistency). Aggregate count of issues → subtract from 10.

**Critical for teleprompter register:** רהיטות must be ≥ 9 — must scan at reading speed without tripping.

---

## Per-output-type pass thresholds

Different output types weight axes differently. Below threshold on the *priority axis* triggers automatic rewrite of the failing section.

| Output type | Priority axes (highest first) | Pass thresholds |
|---|---|---|
| **Rewrite** | רהיטות > רלוונטיות > קוהרנטיות > עקביות | All ≥ 7 |
| **Pitch** | קוהרנטיות > רלוונטיות > עקביות > רהיטות | קוהרנטיות ≥ 8, others ≥ 7 |
| **Speech** | קוהרנטיות > רהיטות > רלוונטיות > עקביות | קוהרנטיות ≥ 8, רהיטות ≥ 8, others ≥ 7 |
| **Talking-cards** | עקביות > רהיטות > קוהרנטיות > רלוונטיות | **עקביות ≥ 9** (facts must hold), others ≥ 7 |
| **Teleprompter** | רהיטות > עקביות > קוהרנטיות > רלוונטיות | **רהיטות ≥ 9** (must scan at speed), others ≥ 7 |

---

## Per-goal axis weighting

The user's stated goal (STEP 0) further weights the rubric:

| Goal | Axis weighting |
|---|---|
| "Convince investors" | רהיטות + קוהרנטיות (1.5x weight); rest normal |
| "Win a panel debate" | עקביות (1.5x — facts in soundbite must hold); רהיטות (1.2x) |
| "Land emotional impact" | קוהרנטיות (1.5x — arc must hold); רהיטות (1.2x) |
| "Explain to junior engineers" | רלוונטיות (1.5x — covers the right points); רהיטות (1.2x — clarity) |
| "Memorial / ceremonial" | רהיטות (1.5x — every word weighted); קוהרנטיות (1.3x) |
| "Roast / entertain" | רהיטות (1.3x — comic timing) |
| "Sign a contract" | עקביות (2x — facts must be exact); רהיטות (1.5x) |
| "Production deployment" | רלוונטיות + עקביות (operational priorities) |

---

## Scoring methodology (STEP 5g execution)

The skill executes scoring in this order:

1. **Read source + output** in full
2. **Pull source key-points list** — what should be covered
3. **Score רלוונטיות** — how much of source key-points appear in output (with right priority)
4. **Score קוהרנטיות** — how well sentences and paragraphs flow
5. **Score עקביות** — fact-check every claim against source
6. **Score רהיטות** — Hebrew grammar + spelling + persona consistency
7. **Apply weighting** — output type + user goal
8. **Compute pass/fail** — any axis below threshold = section needs rewrite
9. **Output the scores + brief justification per axis**

Example output:

```
=== ניקוד ===
רלוונטיות: 9/10 — כל הנקודות העיקריות של המקור נוכחות. נקודה משנית אחת על monitoring חסרה.
קוהרנטיות: 8/10 — זרימה טובה; מעבר אחד בין BLOCK 2 ל-BLOCK 3 קצת חד.
עקביות: 10/10 — כל מספר, ציטוט, ושם מאומת מול המקור.
רהיטות: 9/10 — דקדוק נקי, פרסונת דנה עקבית; שאלה רטורית אחת קצת ארוכה.

ציון כולל (משוקלל לפי talking-cards): עבר ✓
המלצות לשיפור: לחדד מעבר 2→3; לקצר את השאלה הרטורית בכרטיס 1.3.
```

---

## How the skill invokes the rubric

In methodology mode, the skill (Claude) applies the rubric by reasoning through the four axes inline.

In tool-assisted mode:

```sh
python scripts/hebrew_toolkit.py rubric <output_file> <source_file>
# Returns JSON: { "relevance": 9, "coherence": 8, "consistency": 10, "fluency": 9, "weighted_pass": true, "notes": "..." }
```

The `rubric` subcommand uses Claude itself as the grader (LLM-as-judge approach), with the rubric template above as the system prompt. For batch scoring of many outputs against a benchmark, this is the right path.

---

## Calibration notes

- The rubric is **conservative** by design — a 10 means literally perfect. Most production outputs land in the 7-9 range.
- For high-stakes outputs (contracts, broadcasts), the pass threshold may be raised to ≥ 9 on all axes.
- For low-stakes outputs (internal slack, draft brainstorm), the threshold may be lowered to ≥ 6.
- The user can override pass thresholds via STEP 0: *"strict scoring, all axes ≥ 9"* or *"relaxed, drafts only."*

---

## Cross-references

- **`SKILL.md` STEP 5g** — invokes this rubric
- **`source_selection.md`** — picks which models inform consistency / fluency checks
- **`common_errors_catalog.md`** — feeds the fluency check
- **`grammar_layer.md`** — the grammar substrate for fluency scoring
