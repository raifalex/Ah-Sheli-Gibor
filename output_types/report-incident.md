# Output Type: Incident Report

Post-incident write-up. Used after cyber incidents, system outages, safety events, or process failures. Timeline + root cause + remediation + lessons.

## When this output type is right

- **Cybersecurity incident post-mortem** — after a security breach or attack
- **System outage post-mortem** — production system failure
- **Safety incident report** — workplace / customer / regulatory safety event
- **Process failure analysis** — operational / supply chain incident
- **Compliance violation report** — regulatory event with required disclosure
- **Customer-facing incident summary** — communication to affected customers

## Length

3–15 pages depending on severity. Most cyber incidents: 6–10. Brief outages: 2–4.

## Structural template

### Header
- Incident ID + classification (P1/P2/P3 or severity level)
- Date / time discovered, contained, resolved (Israeli ISO timestamps)
- Affected systems / customers / regions
- Authors + reviewers + sign-off

### Executive summary (~200–500 words)
- What happened
- Impact (customers affected, downtime, data exposure)
- Status (resolved / contained / ongoing)
- Top 3 lessons

### Timeline (chronological)
Minute-by-minute or hour-by-hour reconstruction:
- T+0:00 — initial detection
- T+0:05 — escalation
- T+0:30 — containment action
- T+2:00 — partial recovery
- T+8:00 — full recovery
- T+24:00 — confirmed clean

### Root cause analysis
- Immediate cause (proximate)
- Contributing factors (process, people, technology)
- Underlying systemic cause (5 Whys)
- Why monitoring / controls failed to detect/prevent

### Impact assessment
- Customers / users affected
- Data exposure (records, types of data)
- Financial impact (revenue, SLA penalties, response cost)
- Reputational impact
- Regulatory implications

### Response actions taken
- Detection and triage
- Containment
- Eradication
- Recovery
- Communication (internal, customer, regulator)

### Remediation
- Short-term fixes (already done)
- Medium-term improvements (in progress)
- Long-term structural changes (planned)
- Owners + deadlines per item

### Lessons learned
- What we did well
- What we did poorly
- Process changes
- Technical changes
- Cultural changes

### Disclosure / compliance section
- Regulatory notifications required (GDPR 72h / Tikun 13 / FedRAMP / HIPAA)
- Customer communications sent
- Public disclosure status

### Sign-off
- IR lead + CISO + Legal + Compliance signatures

## Hebrew-specific conventions

- **Cyber acronyms** preserved English (IR / DFIR / SIEM / EDR / IOC / TTP)
- **Israeli regulatory references** (Tikun 13 / INCD reporting / NIS)
- **Timeline in Israeli local time + UTC**
- **Numbers digital** with currency markers
- **No filler / no minimization** — incident reports require honest, direct language
- **Smikhut for compound terms** (תקיפת RANSOMWARE / מערך הסייבר / צוות התגובה)

## Persona pairings

| Incident type | Best persona |
|---|---|
| Cyber incident (CISO-led) | **דנה** (sharp, debate-tested) or **יואל** (assertive ownership) |
| Customer-facing summary | **נועה** (honest, accountable) or **שירה** (dignified) |
| Regulatory filing | **שירה** (formal-classical) |
| Internal eng-led post-mortem | **יואל** (founder-owner) |

## Special validation gates for incident reports

- [ ] No-blame framing in language (focus on systems, not individuals)
- [ ] Timeline precise (timestamps to the minute)
- [ ] Impact quantified
- [ ] Root cause goes deeper than proximate (5 Whys reasoning)
- [ ] Remediation has owners + deadlines
- [ ] Regulatory disclosure status explicit
- [ ] Lessons learned section is honest (not PR-spin)
- [ ] Sign-off chain present
- [ ] Persona voice accountable, not defensive
- [ ] Hebrew grammar clean

## Related output types

- For external communication: `press-release`
- For board notification: `report-executive`
- For technical depth: `report-whitepaper`
