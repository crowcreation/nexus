# Failure Log

Append-only record of operational friction. When something goes wrong in your
AI work — a wrong recommendation, a wasted run, a stale assumption, a duplicated
effort — write one plain-English line. Review weekly for patterns.

Record what happened and your best guess at the root cause. Keep it plain. The
labels and categories come later, if at all — let the patterns emerge from your
own entries rather than imposing a scheme on day one.

When the same root cause shows up **three times**, it is no longer a one-off. It
is structural, and the system is missing a rule. Write one preventive rule into
your `CLAUDE.md` and move on.

---

## Entries

<!-- Append new entries below. One entry per failure. Newest at the bottom.
     Shape:
     - **YYYY-MM-DD** | {what happened, one line}. Root cause: {best guess}.
-->

---

## Weekly Review

<!-- Each week, scan the entries above and count by root cause, not by symptom.
     When one root cause has appeared three or more times, write a preventive
     rule into CLAUDE.md. Tidy nothing else — the log is append-only. -->

### Week of YYYY-MM-DD

- **Entries this week**:
- **Clusters found** (root causes appearing 2+ times):
- **Rules promoted to CLAUDE.md**:
- **Open questions**:

---

<!-- Optional: a drift-category vocabulary.

     Categories are never required. Most logs never need them; a plain
     date-and-root-cause line is enough. If, after a month or two, you find the
     same kinds of failure recurring and want a shorthand to group them, the
     Nexus failure-logging skill documents an opt-in set of seven drift codes
     (SS, CF, ID, DF, CO, FL, UN). Adopt it only if your own entries ask for it.
     Do not impose it up front. -->
