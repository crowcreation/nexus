---
description: "Record a failure to the Nexus failure log. Captures what happened, root cause, and triggers three-occurrence alerts. Format-tolerant: matches the log shape already in use."
allowed-tools: ["Read", "Write", "Edit", "Grep", "Glob"]
argument-hint: "Optional: brief description of what went wrong"
---

Record a failure in the root `failure-log.md`. This is the same file `/done` appends to, so the three-occurrence rule sees every entry in one place.

## Process

1. **Read** the root `failure-log.md`. If it doesn't exist, create it from the plugin's `templates/failure-log.md`.

2. **Detect the existing log shape** and match it. There are two shapes in the wild:
   - **Plain-line** (what `/done` writes, and the default for a setup-prompt scaffold): one line per failure, no categories:

     ```
     - **YYYY-MM-DD** | {what happened, one line}. Root cause: {best guess}.
     ```

   - **Categorised** (the fuller `templates/failure-log.md` shape): a per-entry block with a drift-category code (SS, CF, ID, DF, CO, FL, UN), Severity, and Status.

   Read the entries already present. If the log is the plain-line form, append in the plain-line form. Do NOT impose the category table on a plain-line log. If the log is already categorised, append a categorised block. When the file is brand-new and empty, default to the plain-line form unless the operator asks for categories.

3. **Capture the failure**:
   - **Date**: today's date (YYYY-MM-DD)
   - **What happened**: if `$ARGUMENTS` is provided, use that as a starting description. Otherwise ask. Keep it concrete and specific — what went wrong, not how you felt about it.
   - **Root cause**: probe for the underlying cause, not the surface symptom. "Acted on stale CRM data" not "email was wrong."
   - **Category** (categorised logs only): offer the 7 drift codes (SS, CF, ID, DF, CO, FL, UN) with their one-line descriptions from the `failure-logging` skill. Ask Claude to pick the best fit. Use UN (Uncategorised) when the failure genuinely doesn't fit. On a plain-line log, do not ask for a category — categories are optional and emerge from the operator's own entries over time.
   - **Severity** (categorised logs only): ask whether this was CONTAINED (caught before affecting external output) or EXTERNAL (affected a client, published output, or downstream system).
   - **Status** (categorised logs only): set to DETECTED.

4. **Append** the new entry to the root `failure-log.md`, in the shape detected in step 2. Append-only — never rewrite earlier entries.

5. **Three-occurrence check**: grep the root `failure-log.md` for the same root cause (plain-line logs) or the same category (categorised logs). Count the occurrences including this one. If the count is now >= 3, output an alert:

   ```
   Three-occurrence rule triggered.
   This failure pattern is structural — the system is missing a preventive rule.
   Consider: what rule, hook, or checklist item would catch this before it happens again?
   ```

   If the operator suggests a preventive rule, offer to add it (to the entry on a categorised log, or as a one-line rule in CLAUDE.md). Let the operator approve before writing a CLAUDE.md rule.

6. **Summary**: output a one-line confirmation: "Logged failure (#[N] of this root cause). [three-occurrence alert if triggered]"
