# Ah Sheli Gibor

> **אח שלי גיבור** — the affectionate Israeli startup-nation address. This skill rewrites text into the way a 2025 Israeli tech professional would actually write it.

A Claude Skill for **authentic Israeli tech Hebrew rewriting**. Receives any input text (English or formal Hebrew), comprehends it, and reconstructs it in the target Israeli tech register — with correct binyan grammar, accurate noun gender, proper smikhut, and 2025-current jargon.

---

## Installation

### One-line install (recommended)

Run from any terminal — no clone, no manual setup:

```sh
npx github:raifalex/Ah-Sheli-Gibor
```

This installs the skill into `~/.claude/skills/ah-sheli-gibor/`. Restart Claude Code afterward so it discovers the new skill.

### After publishing to npm

Once `ah-sheli-gibor` is published on the npm registry, you can run:

```sh
npx ah-sheli-gibor
```

Or install globally:

```sh
npm install -g ah-sheli-gibor
ah-sheli-gibor
```

### Installer options

```sh
npx ah-sheli-gibor                        # install to ~/.claude/skills/
npx ah-sheli-gibor --update               # git pull latest changes
npx ah-sheli-gibor --uninstall            # remove the skill
npx ah-sheli-gibor --target <path>        # install to a custom path
npx ah-sheli-gibor --dry-run              # print what would happen
npx ah-sheli-gibor --help                 # show all options
```

The installer needs Node ≥14 and `git` on your `PATH`.

### Manual install

If you prefer to clone directly:

```sh
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/raifalex/Ah-Sheli-Gibor.git ~/.claude/skills/ah-sheli-gibor
```

### Update

```sh
npx ah-sheli-gibor --update
```

Or manually:

```sh
cd ~/.claude/skills/ah-sheli-gibor && git pull
```

### Uninstall

```sh
npx ah-sheli-gibor --uninstall
```

### Verify the install

After installation and a Claude Code restart, the skill should appear in your available-skills list. Test it:

```
"rewrite the following in Israeli tech Hebrew, slack register:
We deployed the new search feature to prod last night."
```

You should see Claude pick up the `ah-sheli-gibor` skill and produce something like:

> חברה, דיפלוינו אתמול בלילה את פיצ'ר החיפוש החדש לפרוד.

---

## What this is

This is **rewriting, not translation**. A translation matches words. A rewrite reconstructs the argument from the inside out, in the voice of the target community.

If you give this skill an English blog post about deploying RAG at scale, it doesn't translate it word-by-word — it produces what an Israeli engineer at Monday/Wix/Mobileye would have written if they'd authored the same post originally. Including:

- **Correct binyan** — anglicized verbs follow pi'el patterns (לדיפלוי → מדיפלוי / דיפלוי / אדיפלוי)
- **Correct gender** — loanword nouns assigned masculine/feminine per documented Israeli usage
- **Correct plurals** — almost universally -ים for loanwords (פיצ'רים, באגים, מודלים)
- **Correct smikhut** — מנהל המוצר, not "המנהל של הפרודקט"
- **Correct code-switching** — ב-MCP with hyphen, never בMCP
- **Register-aware** — slack ≠ blog ≠ LinkedIn ≠ investor pitch ≠ PR/RFC

## The five registers

| Register | When to use |
|---|---|
| **slack / standup** | Internal chat, daily standup updates |
| **technical-blog** | Engineering blog posts, technical writeups |
| **linkedin** | Public posts from founders/engineers; story-driven |
| **investor-pitch** | Decks, investor updates, formal external comms |
| **pr-rfc** | Architecture proposals, RFCs, RFD-style documents |

## What's in this repo

```
.
├── SKILL.md                       # Operating instructions (the 5-step protocol)
├── metadata.json                  # Bilingual skill metadata
├── corpus/
│   └── jargon.json                # ~30 seed entries with full v2 schema
├── references/
│   ├── grammar_layer.md           # Binyan / gender / smikhut / prepositions
│   ├── sources.md                 # Source registry with provenance
│   └── anti_patterns.md           # Bad-output table the skill must avoid
├── tests/
│   ├── test_cases.md              # 5 test cases (one per register)
│   └── test_results_v0.md         # TC-001 dry-run results
├── examples/
│   └── rewrites/                  # Before/after examples per register
├── README.md                      # This file
└── CONTRIBUTING.md                # How to add corpus entries
```

## The 2025-only source rule

The corpus has a hard rule: **web-sourced entries must trace to a URL dated January 1, 2025 or later**.

Why: Israeli tech Hebrew evolved sharply in 2024–2025, especially in the AI/ML layer (RAG, MCP, agentic AI, fine-tuning). Pre-2025 jargon encodes outdated patterns and misses critical 2025 vocabulary.

Exempt from the date cutoff: reference grammar sources (Academy of the Hebrew Language, Morfix, Rav-Milim, MILA Corpus) describe timeless rules. Local-bootstrapped entries (author's own materials) carry explicit local provenance.

See [`references/sources.md`](references/sources.md) for the full registry.

## How to use the skill

In Claude Code (or any Claude environment with the skill installed):

```
/ah-sheli-gibor

Rewrite this in Israeli tech LinkedIn voice:
[paste English or formal-Hebrew text]
```

Or invoke naturally:

```
"Make this sound like a Tel Aviv engineer wrote it"
"Rewrite in Israeli tech Hebrew, slack register"
"Israeli LinkedIn version of this announcement"
```

The skill will identify the register (or ask if ambiguous), comprehend the source, apply the 5-step rewriting protocol, and output only the final version.

## When NOT to use this skill

- General Hebrew translation → use DeepL or DictaLM 3.0
- Formal Academy-of-Hebrew documents → use `hebrew-content-writer`
- Hebrew RTL CSS / layout → use `hebrew-rtl-best-practices`
- Hebrew PDF/DOCX/PPTX generation → use `hebrew-document-generator`
- Niqud / vowelization → use Dicta Nakdan API
- Non-tech content (legal, medical, literary) → use `hebrew-content-writer`

This skill is the **tech-jargon overlay** on top of `hebrew-content-writer`. Where they conflict on grammar fundamentals, `hebrew-content-writer` wins.

## Versioning

- **v0.1.0** (current) — scaffold + ~30 seed corpus entries + 5 test cases + full methodology
- **v0.2.0** (planned) — corpus expansion to 100 entries (70% 2025-web-dated), 4/5 tests passing as regression gate
- **v0.3.0** (planned) — 200 entries, 20 tests
- **v1.0.0** (planned) — 300+ entries with full register coverage

## License

MIT. See `LICENSE` in the repo root.

## Contributing

Open an issue or PR. Every corpus entry must conform to the [v2 schema](CONTRIBUTING.md#schema) and carry valid provenance (URL + date for web sources, file path for local sources).
