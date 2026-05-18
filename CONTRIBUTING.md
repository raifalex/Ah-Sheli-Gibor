# Contributing to Ah Sheli Gibor

Thanks for wanting to expand the corpus. The rules below are non-negotiable — they're what keep the skill outputting authentic 2025-era Israeli tech Hebrew rather than drifting into outdated or fabricated jargon.

---

## The 2025-only source rule

Every web-sourced corpus entry must trace to a URL dated **2025-01-01 or later**.

Why: Israeli tech Hebrew evolved sharply in 2024–2025. AI/ML vocabulary (RAG, MCP, agentic AI, fine-tuning workflows) is largely 2024–2025-coined. Post-October-7 startup culture introduced new language patterns. Pre-2025 sources will encode outdated jargon and miss current vocabulary.

**Exempt from the date rule:**
- Reference grammar sources (Academy of the Hebrew Language, Morfix, Rav-Milim, MILA Corpus) — describe timeless rules
- Local-bootstrapped entries — author's own materials with explicit local provenance

If you cannot prove a 2025-or-later date for a web source, the entry is rejected.

---

## Corpus entry schema

Every entry in `corpus/jargon.json` must conform to this schema. Missing fields → rejection.

### Required fields

```json
{
  "term_he": "the term in Hebrew",
  "term_romanized": "the term in latin transliteration",
  "source_language": "English | Hebrew | English-acronym | Hebrew-grammar-rule",
  "literal_source": "the literal source word/phrase",
  "tech_usage_meaning": "what it means in Israeli tech context (in Hebrew)",
  "grammar": { ... },
  "register": ["slack", "standup", "technical-blog", "linkedin", "investor-pitch", "pr-rfc-comment", "all"],
  "example_sentence": "natural example showing typical usage",
  "standard_hebrew_equivalent": "what formal Hebrew would say",
  "prefer_jargon_when": "when to choose the jargon over standard",
  "prefer_standard_when": "when to choose standard over jargon",
  "source_url": "URL (web), file-path (local), or 'ah-sheli-gibor-spec-v2' (design doc)",
  "source_date": "YYYY-MM-DD",
  "cultural_note": "any context a non-native speaker would miss",
  "confidence": "high | medium | low"
}
```

### Grammar sub-schema by part of speech

**For verbs:**
```json
"grammar": {
  "part_of_speech": "verb",
  "binyan": "pi'el | hif'il | pa'al | hitpa'el | ...",
  "gender": "n/a",
  "present_ms": "...",
  "present_fs": "...",
  "present_mp": "...",
  "present_fp": "...",
  "past_3ms": "...",
  "past_1pl": "...",
  "future_1s": "...",
  "infinitive": "...",
  "construct_form": "n/a"
}
```

**For nouns:**
```json
"grammar": {
  "part_of_speech": "noun",
  "binyan": "n/a",
  "gender": "זכר | נקבה",
  "plural": "...",
  "construct_singular": "...",
  "construct_plural": "...",
  "with_definite": "...",
  "with_prefix_be": "...",
  "with_prefix_le": "..."
}
```

**For grammatical patterns** (rules, not single words):
```json
"grammar": {
  "part_of_speech": "pattern",
  "rule": "the rule statement",
  "exception_note": "edge cases"
}
```

### Provenance rules

**For web sources:**
- `source_url` = the article URL (must be publicly accessible)
- `source_date` = the article publish date (verify against the page metadata, not your retrieval date)
- The article must be in Hebrew (or have a Hebrew-language version)
- The article must be dated 2025-01-01 or later

**For local sources:**
- `source_url` = absolute file path or relative path from repo root
- `source_date` = the file's last-modified date at time of extraction
- Add a brief description in `cultural_note` of why this local source is authoritative

**For spec-derived entries:**
- `source_url` = `"ah-sheli-gibor-spec-v2"`
- `source_date` = `"2026-05-18"` (the v2 spec finalization date)

### Confidence rules

- **`high`** — appears in multiple independent 2025 sources OR is a well-established pre-existing term still in current use OR is explicitly documented in your grammar reference
- **`medium`** — appears in a single trusted 2025 source with no contradicting evidence
- **`low`** — speculative or contested. **Low-confidence entries are flagged for review and not used in active rewrites.**

---

## How to add an entry

1. Identify the term from a qualifying 2025 source (or local material with explicit provenance)
2. Look up grammar fields:
   - Verb: consult Morfix or DictaBERT for binyan and full conjugation
   - Noun: confirm gender from multiple 2025 examples (search Twitter/LinkedIn for "ה[term] הזה" vs "הזאת")
3. Test the term in 2–3 example sentences across registers
4. Compare to the standard Hebrew equivalent — confirm the jargon is genuinely preferred in tech contexts, not just lazy anglicization
5. Cross-reference with `references/grammar_layer.md` — does the term follow established patterns or does it need new pattern documentation?
6. Append the entry to `corpus/jargon.json`
7. Bump `entry_count` in the file header
8. If the term illustrates a new pattern, also update `references/grammar_layer.md`
9. Commit with message `corpus: add <term> (2025-MM source)`

---

## Academy of the Hebrew Language alignment

The Academy issues formal rulings on tech terminology. Where the Academy has an approved term **and** the anglicized loanword is also in use, the corpus entry must document both:

- `term_he` = the anglicized loanword (the one used in informal/practical writing)
- `standard_hebrew_equivalent` = the Academy term
- `prefer_jargon_when` = informal/semi-formal registers
- `prefer_standard_when` = formal/Academy-aligned content

We do not erase the Academy; we contextualize it. Both forms are real Hebrew.

---

## Anti-contributions (will be rejected)

- ❌ Entries without provenance
- ❌ Entries from pre-2025 web sources
- ❌ Made-up terms not attested in real usage
- ❌ Entries that contradict `references/grammar_layer.md` without updating the grammar layer
- ❌ Entries that promote broken grammar (anti-patterns from `references/anti_patterns.md`)
- ❌ Entries that are pure English (e.g., adding "RAG" alone as a term — it's a noun phrase needing context, not a standalone corpus entry)

---

## Where to discuss

- Open a GitHub issue for proposing a new term before adding
- Open a PR for the entry itself
- For grammar pattern disputes (e.g., "is לאופטמז really pi'el?") — cite Morfix + at least one 2025 source

---

## Roadmap participation

The corpus growth roadmap is documented in `references/sources.md`. Contributions targeting the priority source list (GeekTime, Reversim, Monday/Wix/Mobileye engineering blogs) are most welcome.
