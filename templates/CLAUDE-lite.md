# CLAUDE.md — Operational Discipline (Lite)

## How to use

Paste this into Claude Code:

> Fetch https://gist.github.com/crowcreation/1809ad9f1fddbf018113b8f1712dfadb
> and find the "Append to CLAUDE.md" section at the bottom. Append that
> block to my existing CLAUDE.md (create one if none exists). If
> failure-log.md already exists, leave it alone and tell me what's in
> it so I can decide how to proceed. If it doesn't exist, create one
> with just the heading "# Failure Log".

---

## What this is

These rules are for persistent AI systems — workflows where operational
state survives across sessions, repositories evolve over time, and
instructions outlive the conversation that created them. If your AI
usage is mostly isolated conversations, many of these pathologies
never emerge.

You are working in a system that accumulates failures silently.
These rules prevent the five most common ways persistent AI sessions
produce confident, wrong outputs. Follow them every session.

The full explanation of each rule is below. What gets appended to
your CLAUDE.md is the condensed version at the bottom — just the
operational rules, no prose.

---

## Session Pre-flight

Before doing ANY work, verify these three things:

1. **What context you're in.** Run `git status` or equivalent.
   Check the branch, the working directory, the project. Not what
   you remember — what's true right now. Other sessions, automations,
   and humans change context between sessions without telling you.

2. **What changed since last session.** Check recent commits, modified
   files, new configuration. If you skip this, you'll build on
   assumptions that no longer hold.

3. **Whether previous assumptions still hold.** The file you were
   editing — has someone else changed it? The API you were calling —
   same format? The deal you were drafting about — still open?
   Stale assumptions are invisible until they produce wrong output.

This takes sixty seconds. It prevents the worst failure mode:
doing excellent work in the wrong context.

---

## Live-State Check

Before any action whose correctness depends on external state:
**query the source. Now. Not from memory.**

Don't trust cached data. Don't trust docs. Don't trust what the
system told you yesterday. Don't trust your own prior output from
a previous session.

This applies to: CRM records, file contents, API schemas, deal
status, contact details, configuration files, deployment state,
database schemas — anything that another process can modify.

When two sources disagree, the live source wins.

The cost of checking is seconds. The cost of not checking is a
plausible-looking output built on wrong foundations, plus the
debugging time to find the discrepancy (always longer than the
check would have been).

---

## Failure Log

Maintain an append-only file called `failure-log.md`. When something
goes wrong — a wrong recommendation, a wasted run, a stale
assumption, a duplicated effort — add an entry:

```markdown
## YYYY-MM-DD — [short description]

**What happened:** [the failure, one sentence]
**Root cause:** [why it happened, one sentence]
**Category:** [SS|CF|ID|DF|FL|UN]
**Severity:** [CONTAINED|EXTERNAL]
**Status:** DETECTED
**Count:** [how many times this root cause has appeared]
**Prevention:** [what rule would prevent the next occurrence]
```

### The Five Drift Categories

| Code | Name | Signal |
|------|------|--------|
| SS | State Staleness | Acted on data that changed since you last checked |
| CF | Context Fragmentation | Lost track of what session/branch/project you're in |
| ID | Instruction Decay | Followed a rule that's outdated or contradicted |
| DF | Discovery Failure | Built something that already existed but wasn't findable |
| FL | Feedback Loss | Made the same mistake again because the lesson wasn't captured |
| UN | Uncategorised | Doesn't fit the above — review weekly for emerging patterns |

Don't filter entries. Don't fix them inline. Just record. The minor
failures are where patterns hide.

---

## Three-Occurrence Rule

When the same root cause appears **three times** in the failure log:

1. Stop treating it as a user error.
2. Start treating it as a system bug.
3. Draft a preventive rule — but don't add it to CLAUDE.md yet.

One occurrence is an accident. Two is a coincidence. Three means the
conditions that produce this failure are structural. No amount of
"being more careful" prevents the fourth — the environment makes
it likely.

When this triggers, append a **proposed rule** to the failure log
entry that triggered it:

```markdown
**Proposed rule:** [what check, gate, or instruction would prevent
the next occurrence]
**Based on:** [dates of the 3+ entries]
**Status:** PROPOSED
```

Rules stay in the failure log as proposals until the operator reviews
them. The weekly review is where proposed rules get assessed — the
operator decides whether to promote them to CLAUDE.md, refine them,
or discard them. This keeps CLAUDE.md under the operator's control
and makes the review the moment where accumulated failures become
operational intelligence.

---

## Infrastructure Check

Before proposing any new tool, integration, script, or automation:

1. Check what already exists in this repo (`scripts/`, `utils/`, config files)
2. Check what your tools provide natively (built-in commands, MCP servers, CLI flags)
3. Check connected services (existing APIs, authenticated integrations)

The most common discovery failure is building something that already
exists two directories away, or that the platform added last month.

---

## How This File Grows

This file is a living document. It grows through failure, not
through planning. The cycle:

1. Something breaks → record in failure-log.md
2. Review weekly → look for clusters by category
3. Three occurrences → write a preventive rule above
4. Rule prevents the fourth occurrence

After a month, the failure log shows your system's actual weak
points. After three months, the rules derived from those patterns
start preventing failures before they occur. After six months,
this file is meaningfully different from a fresh copy — and the
difference is entirely earned through operation.

The patterns transfer. The specific rules don't. Your failure log
will produce different rules than anyone else's, because your
system fails in ways specific to your workflows, your tools, and
your particular combination of projects.

---

## Session Close

When the session is ending — the user says "done", "let's wrap up",
"that's it", or you're about to sign off:

1. **Review what happened this session.** Scan for friction: wasted
   effort, stale assumptions, repeated work, confused context,
   misunderstood intent, or anything that felt harder than it should
   have been.

2. **If something went wrong, append to failure-log.md.** One entry
   per failure. One sentence for what happened, one for why. Pick the
   closest category. Don't overthink it.

3. **If nothing went wrong, don't write anything.** No "session
   completed successfully" entries. The log is for failures only.

This is not a chore. It takes thirty seconds. The value is in what
the log looks like after a month — patterns you didn't notice at the
time become visible in aggregate.

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

Want this automated? Install the Nexus plugin:

```
/plugin marketplace add crowcreation/nexus
```

<https://github.com/crowcreation/nexus>

---

## Append to CLAUDE.md

Everything below this heading is the condensed version your agent
appends to your existing CLAUDE.md. The full explanations are above.

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
session; (3) verify previous assumptions still hold. Sixty seconds
prevents doing excellent work in the wrong context.

### Live-State Check
Before any action depending on external state, query the source now.
Not from cache, not from docs, not from yesterday. When two sources
disagree, the live source wins.

### Failure Log
Append to failure-log.md when something goes wrong. Format: what
happened, root cause, category, count, prevention rule. Categories:
SS (State Staleness), CF (Context Fragmentation), ID (Instruction Decay),
DF (Discovery Failure), FL (Feedback Loss), UN (Uncategorised). Severity: CONTAINED
(caught internally) or EXTERNAL (affected output). Don't filter.
Just record.

### Three-Occurrence Rule
Same root cause three times = system bug, not user error. Draft a
proposed rule in the failure log entry (not in this file). The
operator reviews and promotes rules during weekly review.

### Session Close
When the session is ending, review what happened. Look for friction:
wasted effort, stale assumptions, repeated work, confused context,
misunderstood intent, or anything that felt harder than it should
have been. If anything went wrong, append to failure-log.md — one
sentence each for what happened and why. If nothing went wrong,
don't write anything.

<!-- ── end operational discipline ── -->
```
