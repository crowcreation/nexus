---
description: "Format failure-log entries or a synthesized field report for sharing to Nexus GitHub Discussions. Privacy-first: redaction prompts before output, zero-auth sharing."
allowed-tools: ["Read", "Grep"]
argument-hint: "Optional: entry number/date for single-entry mode, or --synthesis for full report"
---

Generate a contribution to the Nexus project's GitHub Discussions from your local failure log. Two modes:

## Single-entry mode

If `$ARGUMENTS` contains a date or entry number (e.g., `/field-report 2026-05-25` or `/field-report 3`):

1. **Read** `.nexus/failure-log.md` and find the matching entry.
2. **Display** the entry and ask: "Review this for anything project-specific, private, or identifying you want to redact before sharing."
3. **Walk through redaction**:
   - Project names or file paths → replace with `[project]` or `[path]`
   - Business or client names → replace with `[company]` or `[client]`
   - API endpoints or credentials → replace with `[endpoint]`
   - Specific tool configurations → generalise
4. **Pick category**: suggest the best GitHub Discussion category:
   - **Failure Patterns** — for individual failures with clear root causes
   - **Drift Incidents** — for failures caused by gradual system degradation
5. **Generate pasteable markdown**:

```markdown
## [Category code] — [anonymised description]

**What happened**: [redacted description]
**Root cause**: [redacted root cause]
**Drift mode**: [category name]
**Preventive rule**: [if written]

---
*Filed via [Nexus](https://github.com/crowcreation/nexus) failure log*
```

1. **Output** the markdown and the direct URL to create a new Discussion in the right category:
   - Failure Patterns: `https://github.com/crowcreation/nexus/discussions/new?category=failure-patterns`
   - Drift Incidents: `https://github.com/crowcreation/nexus/discussions/new?category=drift-incidents`

Tell the user: "Copy the markdown above, open the link, paste, and post. Nothing is sent automatically."

## Synthesis mode

If `$ARGUMENTS` is empty or contains `--synthesis`:

1. **Read** `.nexus/failure-log.md` and parse all entries.
2. **Analyse** for patterns:
   - Category distribution (count per drift mode)
   - Three-occurrence clusters (categories with >= 3 entries)
   - Most common root causes (group similar descriptions)
   - Preventive rules written vs. outstanding
3. **Walk through redaction** of the synthesis — same prompts as single-entry mode but applied to the aggregated patterns.
4. **Generate a field report**:

```markdown
## Field Report — [operator pseudonym or "anonymous"]

**Period**: [date of first entry] to [date of last entry]
**Entries logged**: [N]

### Pattern summary
- **[Top category]**: [N] occurrences. Common root cause: [anonymised description]
- **[Second category]**: [N] occurrences. [anonymised description]
[continue for categories with entries]

### Three-occurrence alerts triggered
- **[Category]**: [what the cluster revealed, anonymised]
[or "None yet" if no category has reached 3]

### Rules written
- [Preventive rule, anonymised]
[or "None yet"]

### Open question
[One thing the operator hasn't solved yet — invites discussion from other operators]

---
*Filed via [Nexus](https://github.com/crowcreation/nexus) failure log*
```

1. **Output** the markdown and the direct URL:
   - Field Reports: `https://github.com/crowcreation/nexus/discussions/new?category=field-reports`

Tell the user: "Copy the markdown above, open the link, paste, and post. Nothing is sent automatically."

## Privacy contract

- This command reads local files only. It makes zero network calls.
- Nothing is shared until the user manually copies and pastes the output.
- The deliberate paste IS the consent mechanism.
- All redaction happens before the output is generated, not after.
