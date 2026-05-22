# Output Type: Technical Documentation

Software documentation, README, API docs, operational runbooks, architecture decision records.

## When this output type is right

- **README.md** — repository or product readme
- **API documentation** — reference docs for SDK / REST API
- **Runbook** — operational procedures for on-call
- **Architecture Decision Record (ADR)** — explaining technical choice
- **Migration guide** — upgrading users from one version to another
- **Troubleshooting guide** — common issues + solutions

## Six sub-formats

### 1. README

```
# Project Name

> 1-line description

[badges]

## Quick start (5 sec)
[shortest path to value]

## Installation
[3 paths max]

## Usage
[main workflow]

## API
[link to detailed docs]

## Contributing
[link to CONTRIBUTING.md]

## License
[MIT / Apache / etc.]
```

### 2. API documentation

- Endpoint per page
- Request format (curl + multiple language snippets)
- Response format with example
- Error codes table
- Rate limits
- Authentication

### 3. Runbook

- Title + symptom that triggers it
- Severity
- Pre-conditions to check
- Step-by-step actions (numbered, executable)
- Verification of each step
- Escalation path
- Rollback procedure
- Post-incident reporting requirement

### 4. ADR (Architecture Decision Record)

- Title + status (proposed / accepted / superseded)
- Date
- Context — what problem
- Decision — what we chose
- Consequences — positive + negative + neutral
- Alternatives considered
- Reviewers + sign-off

### 5. Migration guide

- From version + to version
- Breaking changes list
- Required code changes (with examples)
- Recommended migration order
- Common issues + solutions
- Rollback plan

### 6. Troubleshooting guide

- Symptom + most likely cause
- Diagnostic commands
- Common fixes (ordered by likelihood)
- When to escalate

## Hebrew-specific conventions

- **Mix Hebrew + English freely** — tech docs are commonly bilingual
- **Code examples always English** — never translate code
- **Comments in code** can be Hebrew or English
- **Operational verbs** in Hebrew (לדפלוי / לרולבק / לסקייל) when prose context
- **Acronyms preserved English** — API / CLI / SDK / REST / gRPC / OAuth
- **Inline code formatting** for: variables, file paths, commands

## Persona pairings

- **יואל** (engineering owner — direct, practical)
- **איתמר** (depth-oriented, patient)

## Validation gates

- [ ] Format matches sub-format spec
- [ ] Code examples work (verified, not pseudocode)
- [ ] Commands include expected output
- [ ] Bilingual where audience is bilingual
- [ ] Persona voice direct + practical
- [ ] No marketing language in technical docs
