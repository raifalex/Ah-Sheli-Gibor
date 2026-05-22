# Hebrew Variation Modes

The skill produces Hebrew across multiple linguistic registers, domains, sub-domains, communities, and emotional bands. A *variation mode* combines a vocabulary band, a source-selection bundle, and a set of grammatical conventions to consistently produce Hebrew in a specific register.

**v0.5.0: 15 variation modes** spanning general tech, specialized tech sub-domains, professional domains, communities, and creative registers.

This document defines all 15. The user selects one at STEP 0 (Interview) — or the skill picks one based on context and goal.

---

## Why modes matter

A grammatically-correct Hebrew sentence in software-engineering register would sound out of place in a memorial speech, even if both are grammatically perfect. Different domains require different vocabulary, different code-switching density, different formality, and different validation. The variation modes encode these trade-offs explicitly.

---

## The 15 modes at a glance

| # | Mode | Primary use | Persona affinity | Code-switching density |
|---|---|---|---|---|
| 1 | **`tech-general`** (DEFAULT) | General Israeli tech writing — fallback | Yoel / Itamar / Dana | 15-30% |
| 2 | **`software-engineering`** | Developer / DevOps / SRE register | Yoel / Gilad | 30-45% |
| 3 | **`cybersecurity`** | Israeli infosec community | Dana / Yoel / Itamar | 25-40% |
| 4 | **`product-management`** | PM voice — business+user vocab | Yoel / Dana / Noa | 25-35% |
| 5 | **`defense-aerospace`** | Israeli defense industry | Itamar / Shira / Yoel | 10-25% |
| 6 | **`ai-ml-research`** | Academic + industrial ML | Itamar / Shira | 15-30% |
| 7 | **`startup-fundraising`** | Founder ↔ investor | Yoel | 30-45% |
| 8 | **`gen-z-creator`** | TikTok / Instagram / podcast | Noa / Gilad | 30-45% |
| 9 | **`legal-technical`** | Contracts, IP, ToS | Shira / Itamar | <10% |
| 10 | **`medical`** | Clinical, patient comms | Itamar / Shira | 10-20% |
| 11 | **`biblical-rabbinic`** | Religious / ceremonial | Shira | ~0% |
| 12 | **`gender-emotional`** | Personal, vulnerable | Noa / Shira | 15-30% |
| 13 | **`slang-cultural`** | Casual + cultural-explanation layer | Gilad / Noa / Yoel | 20-40% |
| 14 | **`bilingual`** | Hebrew + English side-by-side | Yoel / Noa / Itamar | n/a |
| 15 | **`creative-lyrics`** | Poetry, lyrics, experimental | Shira / Gilad / Noa | variable |

---

## Mode 1 — `tech-general` (DEFAULT)

General-purpose Israeli tech writing. Used when no specific sub-domain applies, or when the content spans multiple domains.

**Vocabulary band:** Tech-informal + tech-formal, with English code-switching for acronyms and product names.

**Persona affinity:** Yoel / Itamar / Dana

**Code-switching density:** 15-30%

**Sources:** Claude + `corpus/jargon.json` + DictaBERT + Academy

**Defining grammar rules:**
- Anglicized verbs follow pi'el (לדיפלוי, לקומיט)
- English-script nouns with hyphen-prefix (ב-MCP, ה-IAM)
- Numbers digital
- Smikhut preferred over analytical when both parts Hebrew
- No filler words in formal output

**When to use:** Default. General tech blog, LinkedIn, internal docs, when domain isn't clearly engineering/PM/cyber/etc.

---

## Mode 2 — `software-engineering`

Narrower than `tech-general`. The register engineers use writing to other engineers — PRs, RFCs, technical debate, code review, runbooks, post-mortems.

**Vocabulary band:** Engineering-jargon-heavy + heavy English loanword density.

**Persona affinity:** Yoel / Gilad (post-mortems benefit from Gilad's dryness)

**Code-switching density:** 30-45%

**Sources:** Claude + `corpus/jargon.json` (engineering subset) + DictaBERT-parse for grammar

**Defining grammar rules:**
- Anglicized verbs are dominant (לקומיט, לפוש, למרג', לדיפלוי, לדבג, לריפקטר, לסקייל)
- Tooling names always English (Kubernetes / Docker / Terraform / Helm / Vault / Consul / Argo)
- ARchitecture acronyms always English (CI/CD / CDN / VPC / LB / WAF / RBAC)
- Operational verbs: לדפלוי / לרולבק / לפעיל / לכבות / לסקייל
- Code is always English, comments may be Hebrew

**Distinctive vocabulary:**
דבאופס · פייפליין · רולבק · קונטיינר · קוברנטיס · לקומיט · לפוש · למרג' · לדיפלוי · לדבג · לריפקטר · לסקייל · pipeline failed · build broken · merge conflict · feature flag · canary deploy · blue-green · trunk-based development

**Sample sentence:**
> "ה-pipeline נפל על ה-integration tests. ריפקטרנו את ה-test fixtures ושיפנו ל-canary. אחרי 30 דקות של monitoring, מרג'נו ל-main."

**When to use:** PR descriptions, code review comments, RFCs, technical blog (engineering depth), runbooks, post-mortems, internal eng-all messages.

---

## Mode 3 — `cybersecurity`

Israeli infosec community register. CISO-grade Hebrew. Heavy on incident-language, compliance-aware, references INCD (Israeli National Cyber Directorate) and the broader Israeli cyber ecosystem.

**Vocabulary band:** Security-incident vocabulary + technical Hebrew + Israeli regulatory references.

**Persona affinity:** Dana (panel-grade soundbites) / Yoel (CTO/CISO mode) / Itamar (investigative)

**Code-switching density:** 25-40%

**Sources:** Claude + Israeli cyber corpus + DictaBERT-parse + Hspell

**Defining grammar rules:**
- Security acronyms preserved English (SOC / IR / DFIR / SIEM / EDR / XDR / MDR / SOAR / NDR / DLP / IAM / PAM / ZTNA / SASE)
- Compliance frames: Tikun 13 / NIS / GDPR / SOC 2 / ISO 27001
- Acronyms for Israeli orgs in Hebrew: INCD / מערך הסייבר הלאומי

**Distinctive vocabulary:**
סייבר · אבטחת סייבר · אבטחת מידע · INCD · מערך הסייבר הלאומי · פריצה · תקיפה · פולשים · חומת אש · הצפנה · פגיעות · CVE · zero-day · ransomware · phishing · social engineering · privilege escalation · lateral movement · exfiltration · C2 · IOC · TTP · MITRE ATT&CK · MITRE ATLAS · threat intel · DFIR · IR playbook · containment · eradication · recovery · post-incident review

**Sample sentence:**
> "ה-SOC זיהה תקיפת ransomware ב-3:47 בבוקר. הופעל IR playbook. תוך 12 דקות חתכנו את ה-affected segment מהרשת. ה-DFIR בעבודה מולנו עכשיו."

**When to use:** Security advisories, incident reports, CISO board updates, security panel prep, blue-team / red-team writeups, MITRE-aligned threat reports, BSidesTLV / RSAC talks, INCD-aligned communications.

---

## Mode 4 — `product-management`

PM voice. Distinct from engineering — business + user vocab, less code, more frameworks (RICE, OKRs, Jobs-to-be-Done).

**Vocabulary band:** Business-strategy + UX vocabulary + metrics-driven.

**Persona affinity:** Yoel (founder-PM) / Dana (analyst-PM) / Noa (user-research PM)

**Code-switching density:** 25-35%

**Sources:** Claude + `corpus/jargon.json` (PM subset)

**Defining grammar rules:**
- PM acronyms preserved English (PMF / GTM / ICP / OKRs / KPIs / NPS / CSAT / DAU / MAU / WAU / LTV / CAC / churn / retention)
- Hebrew: מנהל מוצר / מנהלת מוצר (smikhut), צוות מוצר, יחידה עסקית
- Verbs: לפרויוטז / לסקופ / לדפליין / לבולץ' / לארגן spec

**Distinctive vocabulary:**
מנהל המוצר · roadmap · sprint planning · backlog grooming · user story · acceptance criteria · OKRs · KPIs · NPS · CSAT · DAU · MAU · WAU · churn · retention · adoption · funnel · activation · onboarding · time-to-value · jobs-to-be-done · north-star metric · WAU/MAU ratio · LTV/CAC · payback period · GTM · ICP · TAM/SAM/SOM

**Sample sentence:**
> "מנהל המוצר העלה את הספרינט הבא ל-roadmap. ה-acceptance criteria כתובים כ-jobs-to-be-done. ה-north-star metric הוא WAU של ה-paid tier."

**When to use:** Product Requirements Documents (PRDs), roadmap docs, OKR planning, sprint planning notes, customer-success communications, product launch comms.

---

## Mode 5 — `defense-aerospace` 🇮🇱

Israeli defense industry Hebrew (Elbit Systems / Rafael / IAI / MAFAT / IMOD). Acronym-heavy. Classification-aware. Engineering-precise. **Directly relevant for users working at Israeli defense companies.**

**Vocabulary band:** Acronymized military-technical Hebrew + classification markers + engineering precision.

**Persona affinity:** Itamar (long-form defense feature) / Shira (formal address) / Yoel (engineering-PM in defense context)

**Code-switching density:** 10-25% (more Hebrew than software, less than ML research)

**Sources:** Claude + defense-corpus + DictaBERT + Academy

**Defining grammar rules:**
- Heavy use of Hebrew acronyms (ראשי-תיבות): צה"ל / מפא"ת / מפע"ם / כטב"מ / מל"ט / מצ"מ / רצ"ר / חצ"מ / מק"ס / חיב"ה
- English acronyms preserved: C4I / C5ISR / EW / IFF / ECM / ECCM / SIGINT / IMINT / HUMINT / SAR / IRST / LIDAR / AESA / GMTI
- Classification markers: כללי / מסווג / סודי / סודי-ביותר (never include classified content; the markers themselves can be referenced)
- Smikhut dominates (מערכת לוחמה אלקטרונית / יחידת מחקר ופיתוח / חטיבת חימוש מודרני)

**Distinctive vocabulary:**
מפא"ת (MAFAT) · ממר"ם (Mamram) · 8200 / יחידה שמונה-מאתיים · רפא"ל · אלביט · תע"א (IAI) · מל"מ · אגף תקשוב · מערכת לוחמה אלקטרונית · לוחמה אלקטרונית התקפית (offensive EW) · לוחמה אלקטרונית הגנתית · מערכת מכ"ם · מערכת בקרה אווירית · כטב"מ (UAV) · מל"ט · רחפן תוקפני · רחפן מתאבד · loitering munition · כיפת ברזל · קלע דוד · חץ-3 · iron beam · לייזר ביעורי · BMD · TBM · SAM · ASAT · ATGM · IFV · MBT · APC · MRAP · MRSI

**Sample sentence:**
> "מערך הבינה של חטיבת הטכנולוגיה במפא"ת אישר את העברת התוכניות לאלביט להמשך פיתוח. ה-loitering munition בגרסה החדשה כולל יכולת multi-target engagement, עם עדכון מל"מ לתקיפה מדויקת."

**When to use:** Israeli defense industry communication (Elbit / Rafael / IAI), MAFAT proposals, IDF tech briefings, defense conference talks, defense industry analyst reports, defense-adjacent product specs.

**Compliance reminder:** This mode produces Hebrew suitable for OPEN-SOURCE / UNCLASSIFIED defense communication. Never use the skill to draft content that includes operational classified material; the skill has no security clearance and shouldn't be used for classified workflow.

---

## Mode 6 — `ai-ml-research`

Academic + industrial ML Hebrew. Distinct from product AI: papers, benchmarks, ablations, embeddings. Less English-loanword, more precise terminology.

**Vocabulary band:** Mathematical + technical Hebrew + Latin-derived ML terms + paper-citation conventions.

**Persona affinity:** Itamar (technical-feature) / Shira (literary keynote on AI)

**Code-switching density:** 15-30%

**Sources:** Claude + DictaLM-3.0-Thinking for cultural nuance + academic Hebrew corpus

**Defining grammar rules:**
- Mathematical notation preserved English (∇L, σ², ⟨q,k⟩)
- Architecture names preserved English (Transformer / GPT / LLaMA / Mistral / Gemma)
- Hebrew technical terms: התפלגות / שגיאת הכללה / יכולת הסקה / תשומת לב / אמבדינג / קוונטיזציה / קליברציה
- Citation format: surname-year (Vaswani-2017) within text; full citation at end
- Bilingual abstracts standard (Hebrew + English)

**Distinctive vocabulary:**
מודל / רשת עצבית / טרנספורמר / תשומת לב / אמבדינג / ייצוג סמוי · benchmark · ablation study · ablation · validation set · test set · few-shot · zero-shot · in-context learning · chain-of-thought · self-consistency · reasoning · RAG · retrieval-augmented · fine-tuning · LoRA · QLoRA · PEFT · RLHF · DPO · GRPO · constitutional AI · alignment · safety · interpretability · mechanistic interpretability · representation engineering · scaling laws · emergent capabilities

**Sample sentence:**
> "המודל החדש מציג שיפור של 4.2 נקודות ב-MMLU בהשוואה לקו הבסיס. ה-ablation מראה שה-LoRA על attention layers (ולא על MLP) הוא ה-driver העיקרי. אנחנו משערים ש-attention patterns הם הרכיב הקריטי בהעברה למשימות מתמטיות."

**When to use:** Academic papers in Hebrew (with bilingual abstract), technical AI/ML blog posts, conference talks (ML4HCT / IsraNLP), grant proposals (ISF / MAFAT AI research), industrial ML team docs.

---

## Mode 7 — `startup-fundraising`

Founder ↔ investor Hebrew. Distinct from generic pitch — fundraising-specific.

**Vocabulary band:** VC vocabulary + cap-table arithmetic + Israeli VC ecosystem.

**Persona affinity:** Yoel (founder-mode)

**Code-switching density:** 30-45%

**Sources:** Claude + Israeli VC corpus + Yoel persona signatures

**Defining grammar rules:**
- VC acronyms preserved English (SAFE / convertible / pro-rata / participation / liquidation preference / ratchet / vesting cliff / acceleration / drag-along / tag-along)
- Funding rounds: pre-seed / seed / Series A/B/C/D / bridge / extension
- Israeli VCs mentioned: a16z / Sequoia / Insight / Founders Fund + Israeli (Vintage / Pitango / 83North / Aleph / TLV / Magma / Battery / Bessemer / Greylock)
- Hebrew: גיוס / סיבוב / שווי / דילולציה / שותף / משקיע מוביל

**Distinctive vocabulary:**
SAFE / convertible note / term sheet / valuation / pre-money / post-money / liquidation preference / participation / drag-along / tag-along / pro-rata / vesting cliff / acceleration / ESOP / ARR / MRR / ACV / TCV / LTV / CAC / payback / churn / gross retention / net retention / NRR / GTM / ICP fit / land-and-expand / משקיע מוביל / אנג'ל / חבר דירקטוריון / observer / סבב גשר · runway · burn rate · cash-out date · profitability path · default-alive · default-dead · operating leverage

**Sample sentence:**
> "סגרנו Series A של 14 מיליון דולר ב-pre-money valuation של 56 מיליון. ה-lead — קרן a16z. ה-NRR שלנו עומד על 142%, ה-payback ב-7.5 חודשים. ה-runway החדש: 24 חודשים, עם תוכנית להגיע לdefault-alive ב-Q3 2027."

**When to use:** Pitch decks for VCs, investor updates (monthly / quarterly), data rooms, board materials, founder communications during raise, term-sheet review communications.

---

## Mode 8 — `gen-z-creator`

TikTok / Instagram / podcast register. Short-form punch language. Slang-fluent.

**Vocabulary band:** Israeli Gen-Z slang + content-creator vocabulary + meme-aware references.

**Persona affinity:** Noa (intimate creator) / Gilad (comic angle)

**Code-switching density:** 30-45%

**Sources:** Claude + Israeli Gen-Z slang corpus + Noa/Gilad persona signatures

**Defining grammar rules:**
- Slang acceptable and encouraged: יאללה / סבבה / בסה / חחח / על הפנים / על האש / שש-שבע / פייר / לגיט / אגדה
- Run-on sentences for energy
- Hashtags and emoji acceptable when context permits (TikTok comments, Instagram captions)
- Heavy English drops for comic effect (lol / sus / based / mid / no cap / fr)

**Distinctive vocabulary:**
יאללה · סבבה · בסה (disappointment) · חחח (LOL) · על הפנים (terrible) · על האש (lit / fire) · שש-שבע · פייר (fair) · לגיט · אגדה (legend, "G.O.A.T") · ענק (huge) · מסע (journey, sometimes ironic) · vibe · vibing · vibe check · main character energy · the moment · ate · slay · serving · iconic · era · era of X · gatekeep · gaslight · girlboss / boyboss · simp · stan · cap / no cap · fr / fr fr

**Sample sentence:**
> "אחיה, ה-launch אתמול היה אגדה. סבבה לגמרי. ה-engagement על TikTok על הפנים — over 100K views ב-6 שעות. main character energy fr. נמשיך בעירה הזאת."

**When to use:** TikTok scripts, Instagram captions, podcast intros, Gen-Z founder voice, content marketing aimed at <25 audience, creator-economy communications.

---

## Mode 9 — `legal-technical`

Israeli legal-technical Hebrew. Contracts, ToS, IP, regulatory documents.

**Vocabulary band:** Formal Hebrew + precise legal terminology + tech English only when unavoidable.

**Persona affinity:** Shira / Itamar (no Yoel — too casual; no Gilad — never)

**Code-switching density:** <10% English-script

**Sources:** Claude + Legal-heBERT (with deterministic temperature=0)

**Defining grammar rules:**
- Formal Hebrew verbs preferred over anglicized loanwords ("יפרוס" preferred over "ידיפלוי" in a contract)
- Precise legal terminology (תניה / סעיף / זכויות / חובות / אחריות / תשלום)
- Numbers spelled out for legal weight when stakes high
- Smikhut mandatory; analytical "X של Y" only when required for clarity
- Citation format: per Israeli legal convention (חוק X, סעיף Y(z))
- Anaphora extremely strict — every pronoun must have unambiguous antecedent

**Cultural notes:**
- Use formal pronouns and structures (לכבוד, הואיל ו-, להלן)
- Date format: full Israeli format (DD/MM/YYYY in body, "ביום X לחודש Y בשנת Z" for legal weight)
- **Deterministic output** — when produced, output is reproducible (temperature=0)

**When to use:** Israeli employment contracts, NDAs, IP assignments, ToS, privacy policies, statute commentary, regulatory filings.

---

## Mode 10 — `medical`

Israeli medical Hebrew. Clinical documentation, patient communication, medical research, drug labels, consent forms.

**Vocabulary band:** Mixed — formal Hebrew + medical terminology (often Latin-derived) + English for drug names and protocols.

**Persona affinity:** Itamar / Shira (precision-first)

**Code-switching density:** 10-20%

**Sources:** Claude + hebrew_medical_ner_v5 + DictaBERT-parse

**Defining grammar rules:**
- Drug names: kept English (Aspirin, Metformin, Claritin) — never transliterate
- Medical conditions: standard Hebrew (סוכרת, יתר לחץ דם, פיברומיאלגיה) with English in parens on first use
- Protocols: numbered, with explicit gendering when patient-facing
- Privacy: never include identifying patient details in output without explicit auth
- Anaphora: extremely strict (every "הוא" / "היא" must have explicit antecedent)

**Special considerations:**
- Patient-facing text must use second-person singular formal (אתה / את) — never third-person
- Consent forms must use simple Hebrew at 8th-grade reading level
- Drug dosing: digital with units (5 mg, 250 mcg)

**When to use:** Clinical notes, patient communication, informed consent, medical research papers in Hebrew, drug labels for Israeli market.

---

## Mode 11 — `biblical-rabbinic`

Biblical, Talmudic, liturgical, or rabbinic Hebrew. Used for religious commentary, ceremonial speech, traditional Jewish education content.

**Vocabulary band:** Classical Hebrew lexicon, biblical / Talmudic vocabulary, traditional cantillation references.

**Persona affinity:** Shira (literary) — no other persona fits

**Code-switching density:** ~0% English

**Sources:** BEREL_3.0 / hebrew_bible_ai

**Defining grammar rules:**
- Classical Hebrew morphology (less constrained than Modern)
- Biblical word order variants acceptable
- Quotation: with proper citation (פסוק כא בפרק ב' של ספר בראשית)
- Ceremonial register (אדוננו / רבותינו / הקדוש ברוך הוא / השם)
- Nikud often included (ceremonial / liturgical text), unlike Modern Hebrew

**When to use:** Religious commentary, Talmudic discussion, ceremonial speech, traditional Jewish education, blessings, eulogies in traditional register.

---

## Mode 12 — `gender-emotional`

Emotionally-aware Hebrew with gender-sensitivity. Personal narrative, vulnerable LinkedIn posts, memorial speeches, therapeutic writing, mental-health communication.

**Vocabulary band:** Personal / emotional / register-flexible; tracks the speaker's grammatical gender and emotional register precisely.

**Persona affinity:** Noa / Shira

**Code-switching density:** 15-30%

**Sources:** Claude + hebEMO (8 emotion categories) + heBERT_sentiment

**Defining grammar rules:**
- Speaker gender consistency — every verb / adjective / pronoun matches the speaker's stated gender
- If gender is unspecified, the skill asks before producing first-person Hebrew
- Emotion vocabulary precise (sadness ≠ grief ≠ regret — each has distinct Hebrew)
- Pronouns: explicit when shifting reference (avoid ambiguous הוא / היא)
- Honor the emotional arc — don't undercut vulnerability with bravado

**8 emotion categories (hebEMO):**
| English | Hebrew | Hebrew word examples |
|---|---|---|
| anger | כעס | כועס, רוגז, זעם, התרגזות |
| fear | פחד | פחד, חרדה, בעתה, חשש |
| joy | שמחה | שמחה, אושר, חדווה, שלווה |
| sadness | עצב | עצב, צער, יגון, אבל |
| anticipation | ציפייה | ציפייה, התרגשות, מצפה, מקווה |
| surprise | הפתעה | הפתעה, תמיהה, השתאות |
| trust | אמון | אמון, אמונה, ביטחון, ידידות |
| disgust | גועל | גועל, סלידה, מיאוס |

**When to use:** Vulnerable LinkedIn posts, personal narrative, memorial speeches (alongside `biblical-rabbinic` for ceremonial), therapy content, mental-health Hebrew.

**Honoring gender expression:**
- Hebrew has grammatical gender — every "אני" inflects through verb forms
- The skill asks the user's gender expression at the start of any gender-emotional task
- The skill respects non-binary expression where the user requests it

---

## Mode 13 — `slang-cultural`

Israeli colloquial Hebrew with cultural-explanation layer. Casual content, podcast intros, founder-vulnerable posts, satire / comedy, content explaining Israeli culture to non-Israelis.

**Vocabulary band:** Casual + slang + cultural references + heavy code-switching.

**Persona affinity:** Gilad / Noa / Yoel (in casual moments)

**Code-switching density:** 20-40%

**Sources:** DictaLM-3.0-24B-Thinking + israeli.md output style + Hebrew slang corpus

**Defining grammar rules:**
- Slang appears naturally — but with explanation layer attached for non-Israeli readers
- Cultural references explicit (יום הזיכרון / רוטשילד / חלוקה / שכונה)
- Code-switching is the point, not a bug
- Filler words tolerated (אז / סבבה / בקיצור)

**Slang explanation layer (key feature):**

When the skill produces output in slang-cultural mode, it can append an explanation layer (opt-in):

```
[Hebrew with slang]:
"יאללה, חברה, בקיצור — סקיילנו פי 10 בלי לגעת בקוד. סבבה?"

[Cultural explanation, on request]:
- "יאללה" — Arabic-origin Hebrew slang meaning "let's go" / "come on"
- "סבבה" — Arabic-origin (sababa) meaning "cool / okay / good"
- "בקיצור" — "in short" — opens a summary statement
- Tone: founder-mode urgency with friendly directness
```

**When to use:** Podcast intros, comic openers, satire, content explaining Israeli tech culture to international audiences, casual LinkedIn, founder-vulnerable posts.

---

## Mode 14 — `bilingual`

Hebrew-English bilingual text. Content that genuinely needs both languages (international company communication, bilingual marketing, code with Hebrew comments, EN-HE side-by-side documentation).

**Vocabulary band:** Hebrew main + English supplementary, or alternating per paragraph.

**Persona affinity:** Yoel / Noa / Itamar (depending on which language carries the emotional weight)

**Code-switching density:** N/A — both languages are full content

**Sources:** Claude + neodictabert-bilingual + opus-mt + DeepL for back-translation check

**Defining grammar rules:**
- Each language follows its own grammar (don't apply Hebrew rules to English text)
- When alternating: clear paragraph or section breaks
- Side-by-side: align by paragraph, mark which is original
- Mixed in single sentence: the dominant language sets the grammar; the other language is loanword treatment

**When to use:** International company internal comms, bilingual marketing, EN-HE side-by-side product documentation, code with Hebrew comments + English code.

---

## Mode 15 — `creative-lyrics`

Hebrew creative writing — poetry, song lyrics, fiction, experimental form.

**Vocabulary band:** Full range — from classical Hebrew to contemporary slang — chosen for sound, rhythm, meaning layering.

**Persona affinity:** Shira (literary) / Gilad (comic) / Noa (vulnerable)

**Code-switching density:** Variable — sometimes 0% (pure Hebrew poetic), sometimes high (modern bilingual song lyrics)

**Sources:** gemma-3_4b_hebrew-lyrics-finetune for lyrics; DictaLM-3.0-24B-Thinking for prose

**Defining grammar rules:**
- Grammar can bend deliberately for effect — but bends are intentional, not accidental
- Rhyme / rhythm / meter take precedence over standard rules
- Metaphor and figurative language welcome
- Sound symbolism — choose words that *sound* like what they mean
- Repetition is a feature — refrain structure encouraged

**When to use:** Hebrew lyrics, poetry, creative fiction, experimental prose, advertisement copy with literary weight.

---

## Community-aware sub-modes (apply on top of any base mode)

These aren't standalone modes — they're CULTURAL SUB-FILTERS that combine with any of the 15 base modes:

### `arabic-hebrew-bilingual` (sub-filter)
- For Arab-Israeli, Druze, Circassian tech professionals
- Adds Arabic code-switching patterns documented in research
- Combines with any base mode: e.g., `software-engineering + arabic-hebrew-bilingual`
- Sources: neodictabert-bilingual + Arabic-Hebrew bilingual corpus
- When to use: content authored by or addressed to Arabic-speaking Israeli tech professionals

### `haredi-tech` (sub-filter)
- For Bnei Brak / Beit Shemesh tech community (9,700+ workers, 6,900 women)
- More formal Hebrew, religious-cultural register markers (השם / בעזרת ה' / להבדיל)
- Combines with software-engineering / product-management / startup-fundraising / etc.
- Sources: Claude + custom haredi-tech corpus (planned v0.6)
- When to use: content for / by Bnei Brak tech ecosystem; women-in-haredi-tech communications

### `academic-formal` (sub-filter)
- For Israeli university research register (Hebrew U / Technion / Bar-Ilan / TAU)
- More pure-Hebrew, passive voice, citation conventions, formal-academic structure
- Combines with ai-ml-research / cybersecurity / medical / legal-technical
- Sources: Claude + academic Hebrew style guides
- When to use: peer-reviewed paper, thesis chapter, grant application, conference paper

### `diaspora-israeli` (sub-filter)
- For Bay Area / NYC / Berlin / London Israeli expat tech professionals
- Heavier English code-switching than home-Israelis
- Cultural-distance markers ("back in Israel...", "כשהייתי בארץ...")
- Combines with any base mode
- When to use: content authored by Israeli expats or addressed to diaspora Israeli tech community

---

## Mode selection — interview question

In STEP 0 (Interview), the skill asks:

> "Variation mode? (or 'auto' to infer from context.)
> Tech: (1) tech-general default · (2) software-engineering · (3) cybersecurity · (4) product-management · (5) defense-aerospace · (6) ai-ml-research · (7) startup-fundraising · (8) gen-z-creator
> Domains: (9) legal-technical · (10) medical · (11) biblical-rabbinic
> Voice/style: (12) gender-emotional · (13) slang-cultural · (14) bilingual · (15) creative-lyrics
> Sub-filters (combine with base): arabic-hebrew-bilingual · haredi-tech · academic-formal · diaspora-israeli"

If the user doesn't pick, the skill infers from context.

---

## Mode combinations (advanced)

Some pieces need two modes or a mode + sub-filter:

- **Memorial speech** = `biblical-rabbinic` (ceremonial frame) + `gender-emotional` (personal anchor)
- **Founder vulnerable post** = `gender-emotional` (vulnerability) + `tech-general` (still tech context)
- **Cyber + investor pitch** = `cybersecurity` (substance) + `startup-fundraising` (investor framing)
- **Defense + ML research** = `defense-aerospace` (industry) + `ai-ml-research` (technical depth)
- **Haredi female tech founder pitch** = `startup-fundraising` (base) + `haredi-tech` sub-filter
- **Arab-Israeli engineer blog** = `software-engineering` (base) + `arabic-hebrew-bilingual` sub-filter

The skill handles this by alternating modes between sections — the user just describes the use-case.

---

## Updating modes

New variation modes can be added when:
1. A coherent vocabulary band emerges in a new domain
2. At least one specialized model exists for the domain OR the corpus differentiates clearly
3. A persona affinity is clear
4. The grammar rules are documented

Open a PR with the new mode definition + source bundle + grammar rules.

---

*v0.5.0 — 15 modes + 4 sub-filters — 2026-05-22.*
