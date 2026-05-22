# Hebrew Offensive-Language Taxonomy & LLM Annotation Protocol

**Source**: Liebeskind, C. & Yefet, Y. (2026). *Improving Hebrew offensive language classification using LLM-assisted human-in-the-loop annotation*. Lodz Papers in Pragmatics. DOI: [10.1515/lpp-2025-0093](https://doi.org/10.1515/lpp-2025-0093). Published Feb 27, 2026. Funded by the Israeli Innovation Authority.

This document distills the paper's actionable contributions into a reusable layer for the Ah Sheli Gibor skill — applicable to:

- **Tone/register validation** during STEP 5 (Phrasing Check + Authenticity Review)
- **Variation modes** `slang-cultural`, `gender-emotional`, `gen-z-creator` where edge cases (vulgar / aggressive / discrediting language) must be caught and flagged
- **Talking-cards / panel prep** outputs where hostile-press Q&A or attack-line preparation needs nuanced register control
- **Op-ed / debate-prep** outputs (persona Dana אלמוג) where the line between sharp soundbite and offensive overreach matters

---

## The 6-level Hierarchical Taxonomy

Apply sequentially. If a clause fails at any level, the lower levels still inform the rewrite.

| # | Level | Question | Output |
|---|---|---|---|
| 1 | **Offensiveness** | Is this clause offensive at all? | yes / no |
| 2 | **Target** | Whom does it target? | individual / group / institution / abstraction / none |
| 3 | **Target presence** | Is the target named, implied, or absent? | named / implied / absent |
| 4 | **Vulgarity** | Is the language itself vulgar (independent of intent)? | none / mild / strong |
| 5 | **Offense strength** | How forceful is the offense? | mild / moderate / severe |
| 6 | **Specific aspect** | What dimension of attack? | threat / discrediting / dehumanizing / sarcasm / mockery / criticism / disagreement |

**Why hierarchical**: explicit threats are easy to detect (high inter-annotator agreement). Discrediting attacks ("X is incompetent at their job") are harder — they can read as legitimate criticism. The taxonomy lets the skill distinguish *sharp* (legitimate, Dana's bread and butter) from *offensive* (out of bounds for any persona).

---

## The Two-Step Refinement Method

The paper's central methodological innovation. Apply when classification is ambiguous:

1. **Step 1 — Top-2 candidate selection**: instead of asking the model to pick THE category, ask it to identify the *two most plausible* categories.
2. **Step 2 — Discriminative refinement**: present the two candidates back and ask the model to choose between them with explicit reasoning.

**Why this works**: LLMs over-select dominant/frequent classes when forced into single-choice classification. Two-step decouples recall (step 1, broad) from precision (step 2, narrow), reducing false positives on rare categories.

**How to apply in the skill**: when STEP 5d (persona consistency) or STEP 5e (phrasing check) is uncertain — e.g., "is this Dana being sharp or being mean?" — apply two-step:
- Step 1: "List the top 2 categories from {sharp-but-legitimate, discrediting-attack, dehumanizing, dry-humor, sarcasm}"
- Step 2: "Choose between the two, with one sentence of reasoning grounded in the specific lexical choices"

---

## Prompting Strategies — When to Use Which

The paper compared four prompting strategies. Each has a clear regime where it dominates:

| Strategy | When to use |
|---|---|
| **Few-shot** | Stable categories with clear lexical markers — e.g., explicit threats, named-target identification. Provide 3–5 Hebrew examples in the prompt. |
| **Role-based** | Register-sensitive categories — vulgarity, offense strength. Set role: "you are a Hebrew sociolinguist annotating register". |
| **Chain-of-thought** | Ambiguous categories — discrediting vs criticism, sarcasm vs sincere praise. Force step-by-step reasoning before the final label. |
| **LLM-as-judge** | Final aggregation across multiple classifications. Use when 2+ specialist runs disagree. |

For the Ah Sheli Gibor skill, the default is chain-of-thought (it composes well with STEP 5g's rubric reasoning).

---

## Hebrew-Specific Pitfalls Identified by the Paper

These directly inform STEP 5e phrasing checks:

1. **Null-subject ambiguity** — Hebrew drops the subject pronoun. Without an explicit subject, "מסבך את כולם" can read as criticism *of the listener* or *of an absent third party*. **Skill rule**: if a critical clause has no explicit subject AND no clear discourse antecedent, flag for clarification or insert the pronoun.

2. **Verb-fronting in informal Hebrew** — VSO order ("יורדים על המוצר") creates ambiguity about target identification. Compare to canonical SVO ("הם יורדים על המוצר"). **Skill rule**: in panel-prep / debate-prep outputs, prefer SVO when target identification matters.

3. **Imperative-form criticism** — Hebrew imperatives (תפסיק, תוריד) inside critique can read as escalating ("stop doing that!") or as colloquial register-marker ("hey, drop it"). **Skill rule**: in formal-register outputs (keynote, op-ed, board memo), replace imperative criticism with conditional/subjunctive ("כדאי להפסיק", "ראוי להוריד").

4. **Hebrew profanity is social-distance-graded** — what's vulgar between close friends (e.g., כפרה, אחי, חרא של מוצר) is offensive between strangers/colleagues. **Skill rule**: every output type has a default social-distance setting (founder town-hall = close; investor pitch = formal). Persona ↔ social-distance mismatches trigger STEP 5d.

5. **Implicit-criticism markers** — Hebrew has subtle markers that flip criticism into mockery: enclitic particles like ה־, demonstratives like זה, וכאלה. **Skill rule**: scan for these in the final pass; if their effect changes the offense strength, flag.

---

## Inter-Annotator Reliability Thresholds

The paper reports Cohen's kappa across categories. Translation to the skill's rubric:

| Category | Expected agreement | Skill threshold |
|---|---|---|
| Explicit threat | high (κ > 0.8) | hard-block; no persona may use |
| Named-target dehumanization | high | hard-block |
| Dehumanization (group) | medium-high | hard-block |
| Sarcasm | medium (κ ~ 0.6) | persona-dependent; Gilad אש may use, others may not |
| Discrediting attack | low-medium | flag for user confirmation |
| Sharp criticism | low | allow for Dana אלמוג / Gilad אש; flag for others |
| Disagreement | high | allow universally |

When the skill is uncertain in the low-medium range, fall back to the two-step refinement above.

---

## Integration Points in SKILL.md

Reference this document from:

- **STEP 5d** (Persona Consistency Check) — for the "sharp vs. offensive" question
- **STEP 5e** (Phrasing Check) — for the 5 Hebrew-specific pitfalls
- **STEP 5g** (4-axis Rubric) — `רהיטות` axis can lose points for register-misalignment that this taxonomy detects
- **Variation modes** `slang-cultural` and `gen-z-creator` — explicit instructions to consult this taxonomy
- **Persona Dana אלמוג** — her "sharp soundbite" mode must distinguish sharp from offensive via the 6-level taxonomy
- **Persona Gilad אש** — comedy/satire mode requires explicit vulgarity check (level 4) and offense-strength cap (level 5 ≤ moderate)

---

## When to Cite This Paper

If the skill produces output for academic/research contexts about Hebrew register, NLP, or offensive-language detection, cite as:

> Liebeskind, C. & Yefet, Y. (2026). Improving Hebrew offensive language classification using LLM-assisted human-in-the-loop annotation. *Lodz Papers in Pragmatics*. DOI: 10.1515/lpp-2025-0093.
