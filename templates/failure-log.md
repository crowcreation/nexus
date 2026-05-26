# Failure Log

Append-only record of operational friction. Review weekly for patterns.

<!-- ┌─────────────────────────────────────────────────────────┐
     │  Categories                                             │
     │  SS  State Staleness      — acted on stale data         │
     │  CF  Context Fragmentation — lost track of context      │
     │  ID  Instruction Decay    — followed outdated rules     │
     │  DF  Discovery Failure    — rebuilt what already existed │
     │  FL  Feedback Loss        — repeated a known mistake    │
     │  UN  Uncategorised        — review weekly for patterns  │
     │                                                         │
     │  Severity                                               │
     │  CONTAINED — caught before external impact              │
     │  EXTERNAL  — affected output, client, or downstream     │
     │                                                         │
     │  Status                                                 │
     │  DETECTED → PROPOSED → RULE WRITTEN → ENFORCED          │
     └─────────────────────────────────────────────────────────┘ -->

---

## Entries

<!-- Append new entries below. One entry per failure. -->
<!-- Format:
### YYYY-MM-DD — [short description]
**Session**: [what you were working on] | **ID**: [session ID if available]
**What happened**: [one sentence]
**Why**: [root cause, one sentence]
**Category**: [SS|CF|ID|DF|FL|UN] | **Severity**: [CONTAINED|EXTERNAL]
**Occurrences**: [Nth time this root cause has appeared]
**Proposed rule**: [if 3+ occurrences — what would prevent the next one?]
**Status**: DETECTED
-->

---

## Weekly Review

<!-- Each week, scan entries above for clusters by root cause.
     When a root cause appears 3+ times, assess the proposed rule.
     Promote to CLAUDE.md if it earns its place. -->

### Week of YYYY-MM-DD

- **Entries this week**:
- **Clusters found**:
- **Rules proposed**:
- **Rules promoted to CLAUDE.md**:
- **Open questions**:
