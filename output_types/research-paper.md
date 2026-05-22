# Output Type: Research Paper

Peer-reviewed academic paper. IMRAD format (Introduction / Methods / Results / Discussion). Israeli universities (Hebrew U, Technion, Bar-Ilan, TAU, IDC) and international venues.

## When this output type is right

- **Conference paper** — IsraNLP, AISTATS, NeurIPS, ICML, EMNLP, ACL
- **Journal paper** — Nature, Science, IEEE TSE, JMLR, etc.
- **Workshop paper** — shorter conference adjunct
- **arXiv preprint** — pre-publication research
- **Israeli academic publication** — peer-reviewed Hebrew journal

## Length

Conference paper: 6–12 pages (standard format). Journal: 15–40. Workshop: 4–8. arXiv: variable.

## Structural template (IMRAD)

### Title page
- Title (Hebrew + English if bilingual venue)
- Authors + affiliations (Hebrew U, Technion, etc.)
- Corresponding author email
- Keywords (5–8)

### Abstract (~150–300 words, bilingual)
- Background (1 sentence)
- Problem (1 sentence)
- Approach (2 sentences)
- Results (2 sentences)
- Conclusion / implication (1 sentence)
- **For Israeli universities: Hebrew abstract + English abstract**

### Introduction (~1–2 pages)
- Problem motivation
- Related work review (key prior work)
- Gap / question this paper addresses
- Contribution statement (numbered)
- Paper organization

### Background / related work (~1–2 pages)
- Comprehensive prior-work review
- Position this paper within the literature

### Methods / approach (~2–4 pages)
- Detailed methodology
- Mathematical formulation if applicable
- Algorithms / pseudocode
- Reproducibility details

### Experimental setup (~1–2 pages)
- Datasets
- Baselines
- Evaluation metrics
- Hyperparameters
- Compute resources

### Results (~2–4 pages)
- Main results table
- Ablation studies
- Qualitative analysis
- Comparison to baselines

### Discussion (~1–2 pages)
- What the results mean
- Limitations honestly stated
- Future work

### Conclusion (~½ page)
- Summary of contributions
- Broader impact

### References
Full bibliography in venue-specific format.

### Appendices (optional)
- Additional results
- Proofs
- Hyperparameter sweeps
- Reproducibility checklist

## Hebrew-specific conventions

- **Bilingual abstract mandatory** for Israeli academic submissions
- **Mathematical notation preserved** Latin/Greek
- **Technical terms**: Hebrew with English in parens on first use
- **Citation format**: per venue (IEEE / ACM / APA / Chicago)
- **Smikhut precise** for compound terms (רשתות עצביות / שיטות הסקה / מודלי שפה)
- **Hebrew tech research vocabulary**: התפלגות / שגיאת הכללה / יכולת הסקה / תשומת לב / אמבדינג / קוונטיזציה
- **English-script preserved** for: Transformer / GPT / LLaMA / Mistral / Gemma

## Persona pairings

| Paper type | Best persona |
|---|---|
| Israeli academic submission | **איתמר** (formal-classical authority) or **שירה** (literary clarity) |
| International conference (English-led) | **איתמר** for Hebrew version |
| Bilingual (Hebrew + English) | **שירה** for Hebrew, English original |

## Validation gates

- [ ] Bilingual abstract (Hebrew + English)
- [ ] All contributions numbered explicitly
- [ ] Methods reproducible
- [ ] Ablation study present
- [ ] Limitations honest
- [ ] Citations consistent
- [ ] Persona voice formal-academic
- [ ] Hebrew technical terminology precise
- [ ] Length within venue spec

## Related output types

- For grant / proposal: `research-proposal`
- For thesis chapter: `thesis-chapter`
- For non-peer-reviewed: `report-whitepaper`
- For conference talk: `speech` + `talking-cards`
