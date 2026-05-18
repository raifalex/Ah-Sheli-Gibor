# Source Registry

This document tracks every source used to derive corpus entries and grammar rules. Provenance accounting is non-negotiable: every entry in `corpus/jargon.json` traces here.

## 2025-only source rule

Web-sourced entries (i.e., entries derived from third-party Hebrew tech content) must trace to a URL dated **2025-01-01 or later**. Pre-2025 Israeli tech Hebrew encodes outdated jargon — particularly missing the 2024-2025 AI/ML vocabulary explosion (RAG, MCP, agentic AI, fine-tuning workflows) and post-October-7 startup-culture shifts.

**Reference grammar sources** (Academy of the Hebrew Language, Morfix, Rav-Milim, MILA Corpus) are exempt from the date cutoff — they describe timeless rules.

**Local-bootstrapped entries** are derived from materials authored by the skill maintainer or sourced from internal/local content. They carry explicit local provenance (file path + file last-modified date).

---

## v0.1.0 source registry

### Local sources (v0 seed)

| Source | Type | Path | Date | Entries derived |
|---|---|---|---|---|
| `hebrew_style_guide.md` | Style guide (talk-specific) | `~/Documents/TechGym-Recording/Presentation md/hebrew_style_guide.md` | 2026-05-08 | 8 grammatical pattern entries: definite-article-hyphen, plural patterns, future-tense-not-going-to, partitive agreement, definite-article-after-demonstrative, approximation marker, product-names-stay-english, no-filler-words |
| `ah-sheli-gibor-spec-v2` | Skill design spec (this conversation) | conversation-internal | 2026-05-18 | 22 verb + noun + AI/ML entries + 1 smikhut pattern entry |

### Web sources (deferred to v0.2.0+)

These are the priority sources for the corpus-expansion loop. Each must yield 2025-dated content with explicit URL + date stamp on every extracted entry.

| Source | Type | URL | Status |
|---|---|---|---|
| GeekTime | Tech journalism (Hebrew) | https://www.geektime.co.il/ | Pending — fetch 2025 archive |
| Reversim Summit 2025 | Engineering conference | https://www.reversim.com/ | Pending — fetch talks + writeups |
| Monday.com Engineering | Company tech blog | https://monday.com/blog/engineering | Pending — 2025 posts only |
| Wix Engineering | Company tech blog | https://www.wix.engineering/ | Pending — 2025 posts only |
| WalkMe Blog | Product/tech blog | https://www.walkme.com/blog | Pending — 2025 posts only |
| Mobileye Tech Blog | Deep-tech | https://www.mobileye.com/blog | Pending — 2025 posts only |
| IronSource / Unity IL Engineering | AdTech/GameTech | https://engineering.is.com/ | Pending — 2025 posts only |
| LinkedIn — Israeli Tech Leaders | Social posts | linkedin.com (curated) | Pending — Hebrew posts from Israeli CTOs/VPs, 2025 only |
| Zikukim Podcast | Audio/transcript | Spotify/Apple Podcasts | Pending — 2025 episodes |
| DLD Tel Aviv 2025 | Conference | https://dld-conference.com/tel-aviv | Pending — keynote transcripts |
| Startup Nation Central | Ecosystem | https://www.startupnationcentral.org/ | Pending — 2025 reports |
| Techtalks IL | Community | https://www.techtalks.co.il/ | Pending — 2025 Hebrew dev content |
| GitHub — Israeli company README/docs | Developer content | github.com (curated) | Pending — 2025-commit Hebrew READMEs from Israeli startups |

### Hebrew grammar reference sources (timeless)

| Source | URL | Purpose |
|---|---|---|
| Academy of the Hebrew Language | https://hebrew-academy.org.il/ | Authoritative grammar rulings, new-tech terminology decisions |
| Morfix | https://www.morfix.co.il/ | Conjugation tables, gender lookup |
| Rav-Milim | https://www.ravmilim.co.il/ | Thesaurus — synonym mapping for style variation |
| MILA Corpus (Bar-Ilan University) | http://mila.cs.technion.ac.il/ | Academic Hebrew NLP reference corpus |
| DictaBERT suite | https://huggingface.co/dicta-il | Morphology, segmentation, syntax models |

---

## Provenance tagging convention

Every entry in `corpus/jargon.json` carries two provenance fields:

- `source_url` — either an actual URL (for web sources), a local file path (for local sources), or the sentinel `ah-sheli-gibor-spec-v2` (for entries derived from the skill design document)
- `source_date` — the date the source was captured/written. For web sources: the article publish date. For local files: the file's last-modified date. For spec entries: `2026-05-18` (the date the spec was finalized).

`confidence` field gates inclusion in the active corpus:
- `high` — multiple independent observations confirm the term/rule
- `medium` — single trusted source, no contradicting evidence
- `low` — speculative or contested; **flagged for follow-up verification, not used in active rewrites**

---

## Corpus growth roadmap

| Version | Entry count target | Source distribution |
|---|---|---|
| v0.1.0 (current) | 30 | 100% local-bootstrapped |
| v0.2.0 | 100 | 70% web (2025-dated), 30% local |
| v0.3.0 | 200 | 80% web (2025-dated), 20% local |
| v1.0.0 | 300+ with full register coverage | 90% web, 10% local |

Corpus expansion happens via a `/loop` task that:
1. Fetches articles from the priority web sources
2. Extracts candidate terms via DictaLM or Claude
3. Validates grammar against `grammar_layer.md`
4. Appends with full provenance to `corpus/jargon.json`
5. Updates this registry with each new source added
