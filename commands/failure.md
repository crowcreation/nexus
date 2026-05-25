---
description: "Record a failure to the Nexus failure log. Captures what happened, root cause, drift category, and triggers three-occurrence alerts."
allowed-tools: ["Read", "Write", "Edit", "Grep", "Glob"]
argument-hint: "Optional: brief description of what went wrong"
---

Record a failure in the `.nexus/failure-log.md`. Load the `failure-logging` skill for category reference.

## Process

1. **Read** `.nexus/failure-log.md`. If it doesn't exist, create it from the plugin's template (the one with category codes and empty table).

2. **Capture the failure**:
   - **Date**: today's date (YYYY-MM-DD)
   - **What happened**: if `$ARGUMENTS` is provided, use that as a starting description. Otherwise ask. Keep it concrete and specific — what went wrong, not how you felt about it.
   - **Root cause**: probe for the underlying cause, not the surface symptom. "Acted on stale CRM data" not "email was wrong."
   - **Category**: present the 5 drift codes (SS, CF, ID, IDUP, FL) with their one-line descriptions from the skill. Ask Claude to pick the best fit. If genuinely unclear, default to SS (state staleness) — it's the most common.
   - **Occurrences**: search the existing failure-log table for entries with the same category. Count them. This new entry makes occurrences = previous count + 1.

3. **Append** a new row to the log table in `.nexus/failure-log.md`.

4. **Three-occurrence check**: if the occurrence count for this category is now >= 3, output an alert:

   ```
   Three-occurrence rule triggered for [CATEGORY].
   This failure pattern is structural — the system is missing a preventive rule.
   Consider: what rule, hook, or checklist item would catch this before it happens again?
   ```

   If the user suggests a preventive rule, add it to the "Preventive rule" column of the most recent entry.

5. **Summary**: output a one-line confirmation: "Logged [CATEGORY] failure (#[N] in this category). [three-occurrence alert if triggered]"
