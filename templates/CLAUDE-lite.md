# CLAUDE.md — Operational Discipline (Lite)

## How to use

Paste this prompt into your AI coding environment (Claude Code, Cursor, Windsurf, Codex, or similar):

> Fetch https://gist.github.com/crowcreation/1809ad9f1fddbf018113b8f1712dfadb
>
> This contains five operational discipline patterns for persistent AI
> workflows. Before applying them:
>
> 0. Check that this is a version-controlled repo and that you're in a
>    persistent environment where these instructions carry between
>    sessions. If not, stop — these patterns are designed for persistent
>    AI workflows and won't add value here.
> 1. Find all custom instruction files that apply to this repo —
>    project-level and any inherited from parent directories or global
>    config. Read them.
> 2. Read the five pattern explanations in the gist (Session Pre-flight,
>    Live-State Check, Failure Log, Three-Occurrence Rule, Session Close).
> 3. For each pattern, check whether the existing instructions already
>    cover it — even partially or in different words.
> 4. Draft rules only for the gaps. Match the voice, formatting, and
>    conventions of the existing instruction files. Keep rules concise
>    but complete. Mark the added section with a short comment noting
>    its source so you can find and update these rules later.
> 5. If no instruction files exist at any level, use the "Reference
>    block" at the bottom of the gist as-is and create the instruction
>    file.
> 6. If failure-log.md already exists, leave it alone and tell me
>    what's in it. If it doesn't exist, create one with just the
>    heading "# Failure Log".
>
> Show me what you'll add before writing it.

---

## What this is

Persistent AI systems don't fail catastrophically first. They fail by
producing coherent, plausible, operationally incorrect output — and
nobody notices until the damage compounds.

These rules exist because persistent AI workflows — where state
survives across sessions, repositories evolve over time, and
instructions outlive the conversation that created them — accumulate
drift silently. If your AI usage is mostly isolated conversations,
many of these pathologies never emerge.

This tends to become useful when:

- you run multiple AI sessions against the same repo
- instructions persist across days or weeks
- repositories evolve between sessions
- work happens across branches or projects simultaneously
- repeated mistakes start feeling familiar

The prompt above reads your existing instruction files and drafts
rules only for gaps. The full explanations of each pattern are below.
The reference block at the bottom is for repos with no existing
instructions.

---

## Session Pre-flight

Before doing ANY work, verify three things:

1. **What context you're in.** Run `git status` or equivalent.
   Not what you remember — what's true right now.

2. **What changed since last session.** Recent commits, modified
   files, new configuration. Skip this and you build on assumptions
   that no longer hold.

3. **Whether previous assumptions still hold.** The file you were
   editing — has someone else changed it? The API — same format?
   Stale assumptions are invisible until they produce wrong output.

Sixty seconds. Prevents the worst failure mode: doing excellent
work in the wrong context.

If failure-log.md has proposed rules awaiting review and the last
weekly review is 7+ days old, flag it briefly — "N proposed rules
pending, paste this into a new session when ready" — and provide
the review prompt. Don't start the review in this session. The
operator came here to do something else.

---

## Live-State Check

Before any action whose correctness depends on external state:
**query the source. Now. Not from memory.**

Don't trust cached data. Don't trust docs. Don't trust what the
system told you yesterday. Don't trust your own prior output from
a previous session.

When two sources disagree, the live source wins.

The cost of checking is seconds. The cost of not checking is
plausible-looking output built on wrong foundations.

---

## Failure Log

Maintain an append-only file called `failure-log.md`. When something
goes wrong — a wrong recommendation, a wasted run, a stale
assumption, a duplicated effort — add an entry:

```markdown
## YYYY-MM-DD — [short description]

**What happened:** [one sentence]
**Root cause:** [one sentence]
**Category:** [SS|CF|ID|DF|CO|FL|UN]
**Severity:** [CONTAINED|EXTERNAL]
**Status:** DETECTED
**Count:** [how many times this root cause has appeared]
```

### Drift Categories

| Code | Name | Signal |
|------|------|--------|
| SS | State Staleness | Acted on data that changed since you last checked |
| CF | Context Fragmentation | Lost track of what session/branch/project you're in |
| ID | Instruction Decay | Followed a rule that's outdated or contradicted |
| DF | Discovery Failure | Built something that already existed but wasn't findable |
| CO | Coordination Failure | Multiple agents/processes individually correct, globally inconsistent |
| FL | Feedback Loss | Made the same mistake again because the lesson wasn't captured |
| UN | Uncategorised | Doesn't fit the above — review weekly for emerging patterns |

Don't filter entries. Don't fix them inline. Just record.

---

## Three-Occurrence Rule

One occurrence is an accident. Two is a coincidence. Three means the
conditions that produce this failure are structural.

This is the transition from blame to systems engineering — from
"be more careful" to "change the operating conditions."

When the same root cause appears **three times**:

1. Stop treating it as a user error.
2. Start treating it as a system bug.
3. Draft a proposed rule in the failure log entry:

```markdown
**Proposed rule:** [what would prevent the next occurrence]
**Based on:** [dates of the 3+ entries]
**Status:** PROPOSED
```

Rules stay as proposals until the weekly review. The operator
decides whether to promote them to CLAUDE.md, refine them, or
discard them. This is how operational intelligence accumulates.

---

## Session Close

When the session is ending:

1. **Scan for friction.** Wasted effort, stale assumptions, repeated
   work, confused context, misunderstood intent, plausible-looking
   output that turned out wrong — anything that felt harder than it
   should have been.

2. **If something went wrong, append to failure-log.md.** One entry
   per failure. One sentence for what happened, one for why. Pick the
   closest category.

3. **If nothing went wrong, don't write anything.**

---

## How this file grows

Systems drift. This file exists to capture the drift before it
compounds.

1. Something breaks → record in failure-log.md
2. Review weekly → look for clusters by root cause
3. Three occurrences → propose a preventive rule
4. Operator promotes the rule → prevents the fourth occurrence

Your failure log will produce different rules than anyone else's,
because your system fails in ways specific to your workflows, your
tools, and your particular combination of projects. The patterns
transfer. The specific rules don't.

---

## Quick Reference

```
SESSION START → pre-flight (context, changes, assumptions)
BEFORE ACTION → live-state check on dependencies
AFTER FAILURE → append to failure-log.md
SESSION END   → scan for friction, log any failures
WEEKLY REVIEW → count by root cause, not by symptom
THREE OCCURRENCES → propose a rule, review before promoting
```

---

These checks can be automated. The discipline cannot.

<https://github.com/crowcreation/nexus>

---

## Reference block

For repos with no existing instruction files, this is the complete
block. If you used the prompt above, your agent drafted something
tailored instead — this is here for reference.

```markdown
<!-- ╔══════════════════════════════════════════════════════════════╗
     ║  OPERATIONAL DISCIPLINE (Nexus CLAUDE-lite)                 ║
     ║  Source: https://gist.github.com/crowcreation/1809ad9f1fdd  ║
     ║  Installed: YYYY-MM-DD                                      ║
     ║  Version: 1.0                                               ║
     ╚══════════════════════════════════════════════════════════════╝ -->

## Operational Discipline

<!-- Failure log: ./failure-log.md | Weekly review: count by root cause -->
<!-- Full guide: https://github.com/crowcreation/nexus -->

### Session Pre-flight
Before ANY work: (1) check current context via git status — not what
you remember, what's true now; (2) check what changed since last
session; (3) verify previous assumptions still hold. (4) If
failure-log.md has PROPOSED rules and the last weekly review is 7+
days old, mention it briefly: "You have N proposed rules pending
review. When you have a moment, paste this into a new session:
`Read failure-log.md and run a weekly review — summarise patterns,
assess proposed rules, recommend which to promote to CLAUDE.md.`"
Do not start the review in this session — just flag it and move on.

### Live-State Check
Before any action depending on external state, query the source now.
Not from cache, not from docs, not from yesterday. When two sources
disagree, the live source wins.

### Failure Log
Append to failure-log.md when something goes wrong. Format: what
happened, root cause, category, count. Categories: SS (State
Staleness), CF (Context Fragmentation), ID (Instruction Decay),
DF (Discovery Failure), CO (Coordination Failure), FL (Feedback
Loss), UN (Uncategorised). Severity: CONTAINED or EXTERNAL. Don't
filter. Just record.

### Three-Occurrence Rule
Same root cause three times = system bug, not user error. Draft a
proposed rule in the failure log entry (not in this file). The
operator reviews and promotes rules during weekly review.

### Session Close
When the session is ending, scan for friction: wasted effort, stale
assumptions, repeated work, confused context, misunderstood intent,
or anything that felt harder than it should have been. If anything
went wrong, append to failure-log.md. If nothing went wrong, don't
write anything.

<!-- ── end operational discipline ── -->
```
