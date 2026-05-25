---
description: "Show failure log summary: category counts, three-occurrence alerts, and time since last entry."
allowed-tools: ["Read", "Grep"]
---

Display a summary of the `.nexus/failure-log.md`.

## Process

1. **Read** `.nexus/failure-log.md`. If it doesn't exist, say so and suggest `/nexus-init`.

2. **Parse** the log table. For each row with content, extract the category code and date.

3. **Output** a compact summary:

   ```
   Nexus Failure Log — [total] entries

   Category breakdown:
     SS  (State Staleness):           [N] entries [⚠ THREE-OCCURRENCE RULE if >= 3]
     CF  (Context Fragmentation):     [N] entries
     ID  (Instruction Decay):         [N] entries
     IDUP (Infrastructure Duplication): [N] entries
     FL  (Feedback Loss):             [N] entries

   Last entry: [date] ([N] days ago)
   Three-occurrence alerts: [list categories with >= 3, or "none"]
   ```

4. If any category has >= 3 entries without a corresponding preventive rule in the most recent entry for that category, flag it.
