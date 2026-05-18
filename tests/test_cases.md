# Test Cases v0

Five test cases, one per register. Pass criteria: ≥3/5 expected jargon terms used correctly **and** 0 grammar errors against `references/grammar_layer.md`.

Results recorded in `test_results_v0.md`.

---

## TC-001 — Slack / standup register

**Input (English):**
> Hey team — we deployed the new search feature to prod last night. Two bugs surfaced in the first 30 minutes around the embedding pipeline, both fixed and re-deployed. Latency is back to normal. Monitoring closely until EOD.

**Target register:** slack

**Expected jargon terms (must appear):**
1. דיפלוינו / לדיפלוי
2. פיצ'ר
3. באג / באגים
4. פייפליין (embedding)
5. latency (kept English, with prefix-hyphen)

**Expected grammar checks:**
- Verb dיפלוי conjugated correctly (past 1pl: דיפלוינו)
- Definite article on פיצ'ר (הפיצ'ר)
- Hyphen on ב-prod / ה-latency
- Elliptical, subject-drop style appropriate to slack

**Pass criteria:** ≥3 of 5 jargon terms used correctly + 0 grammar errors.

---

## TC-002 — Technical blog register

**Input (English):**
> We recently refactored our CI/CD pipeline. The old setup ran tests sequentially across 8 services, which took ~45 minutes per build. After splitting into parallel job pools per service and caching the build artifacts in S3, we cut the average build time to under 10 minutes. The biggest win came from a small change: we stopped re-running unit tests on infrastructure-only changes.

**Target register:** technical-blog

**Expected jargon terms (must appear):**
1. ריפקטרנו / לריפקטר
2. פייפליין (CI/CD)
3. שירותים / services (microservices context)
4. דיפלוי / בילד
5. טסטים / unit tests

**Expected grammar checks:**
- Pi'el conjugation of ריפקטר
- Smikhut or analytical form for "CI/CD pipeline"
- Approximation marker כ- before *45 minutes*
- Hyphen on ב-S3
- Full sentences appropriate to blog register

**Pass criteria:** ≥3 of 5 jargon terms used correctly + 0 grammar errors.

---

## TC-003 — LinkedIn register

**Input (English):**
> 18 months ago, we set out to build something we believed the market needed but couldn't articulate yet. Today we're announcing the launch of [Product] — and the journey here has been everything we hoped for, plus a lot we didn't expect. Massive thanks to the team that shipped through three major architecture rewrites, two pivots, and one near-death-experience fundraise. To our investors, our design partners, and the friends-and-family who tested half-broken builds: thank you. We're just getting started.

**Target register:** linkedin

**Expected jargon terms (must appear):**
1. שיפנו / לשיפ
2. פיבוט / פיבוטים
3. ארכיטקטורה (rewrite context)
4. רראונד / סבב גיוס
5. כ- approximation marker on "18 months"

**Expected grammar checks:**
- Personal first-person voice (אני / אנחנו)
- Story arc structure
- Approximation marker on number
- No filler words (אז / כאילו / בעצם removed)
- "לפני כ-18 חודשים" (not "לפני בערך")

**Pass criteria:** ≥3 of 5 jargon terms used correctly + 0 grammar errors.

---

## TC-004 — Investor pitch register

**Input (English):**
> Our company has achieved Product-Market Fit in Q3 2025, demonstrating 40% quarter-over-quarter growth in ARR. Our platform — built on a proprietary RAG architecture — currently processes approximately 3 million requests per month for 50 enterprise customers. The team is 18 strong; we are raising a Series A of $12M to expand go-to-market in the US and double the engineering team.

**Target register:** investor-pitch

**Expected jargon terms (must appear):**
1. Product-Market Fit (kept English in parens or full)
2. ARR (kept English)
3. RAG (kept English)
4. ארכיטקטורה
5. פלטפורמה

**Expected grammar checks:**
- Formal Hebrew sentence structure
- Numbers digital (40%, 3 מיליון, 50, 18, 12 מיליון)
- Approximation marker (כ-3 מיליון)
- Product names / acronyms preserved in English
- Full clauses, no ellipsis

**Pass criteria:** ≥3 of 5 jargon terms used correctly + 0 grammar errors.

---

## TC-005 — PR/RFC document, AI/ML 2025 layer

**Input (English):**
> # Proposal: Migrate from external RAG service to in-house MCP-based retrieval
>
> **Context:** Our current Q&A bot relies on an external RAG provider with significant per-token cost and no control over the embedding model. As query volume scales, the unit economics degrade.
>
> **Proposal:** Build an internal MCP server that exposes our document corpus to the LLM via the Model Context Protocol. Use Qdrant as the vector store and fine-tune the embedding model on our own conversations.
>
> **Expected outcome:** 60% cost reduction, full control over embedding quality, ability to add new corpora without provider involvement.

**Target register:** pr-rfc with AI/ML 2025 vocabulary

**Expected jargon terms (must appear):**
1. RAG (kept English) / RAG פייפליין
2. MCP סרבר
3. וקטור DB / Qdrant
4. לפיין-טיון / מפיין-טיון
5. אמבדינג / embedding

**Expected grammar checks:**
- Structured RFC format (sections, bullets)
- Precise sentences, minimal jargon-overload
- Pi'el conjugation of פיין-טיון
- Hyphen on ל-MCP, ב-Qdrant
- "כ-60%" or "60%" approximation handling
- Smikhut for "המודל של ה-embedding" → "מודל ה-embedding" *or* smikhut alt

**Pass criteria:** ≥3 of 5 jargon terms used correctly + 0 grammar errors.

---

## Pass gate

v0.1.0 ships when: TC-001 passes (dry-run validation that the skill works end-to-end). TC-002 through TC-005 are written but not required to pass for v0.1.0 — they become the regression suite for v0.2.0.

v0.2.0 will gate on: 4/5 tests passing + expanded test count to 20.
