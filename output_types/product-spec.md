# Output Type: Product Spec (PRD)

Product Requirements Document. Specification for what to build. Bridge between PM, engineering, design.

## When this output type is right

- **PRD for new feature** — engineering team alignment
- **PRD for new product line** — broader scope
- **Spec for design partnership** — bilateral feature negotiation
- **Spec for vendor / external** — work-for-hire specification

## Length

3–15 pages. Most feature PRDs: 5–8.

## Structural template

### Header
- Title + version + date + author + reviewers
- Status (draft / in-review / approved / shipped)
- Linked design doc + ticket

### Problem statement (~½ page)
- User problem we're solving
- Why now / why this priority
- Success metric (single primary KPI)

### Solution overview (~½ page)
- High-level approach in 3–5 sentences
- What changes for users

### User stories (1–2 pages)
Format: "As [user-type], I want [capability] so that [outcome]."
Cover happy path + edge cases.

### Functional requirements (~1–3 pages)
Numbered (FR-1, FR-2, ...). Each must be testable / verifiable.

### Non-functional requirements (~1 page)
Performance, security, compliance, accessibility, internationalization.

### Acceptance criteria (~1 page)
Per user story, the conditions for "done".

### Out of scope (½ page)
Explicit list of what this PRD does NOT cover.

### Dependencies (½ page)
Other teams / services / decisions this PRD depends on.

### Timeline + milestones (½ page)
Phased rollout with dates.

### Open questions (½ page)
Unresolved decisions with owners.

## Hebrew-specific conventions

- **PM Hebrew register** (per `references/hebrew_variations.md` product-management mode)
- **User stories** can be Hebrew or bilingual
- **Acronyms preserved English** (PRD / KPI / SLA / SLO / FR / NFR / GTM)
- **Numbers digital**
- **Acceptance criteria precise + testable**

## Persona pairings

- **יואל** (founder-PM voice — assertive, mission-frame)
- **דנה** (analytical-PM voice — sharp, data-anchor)
- **נועה** (user-research-PM voice — user-empathetic)

## Validation gates

- [ ] Single primary KPI named
- [ ] User stories cover happy + edge cases
- [ ] All FRs testable
- [ ] Acceptance criteria explicit
- [ ] Out-of-scope section present
- [ ] Open questions surfaced with owners
- [ ] Persona voice held (PM register)
- [ ] Hebrew grammar clean
