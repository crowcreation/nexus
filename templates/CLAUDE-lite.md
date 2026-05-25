# CLAUDE.md — Operational Discipline (Lite)

You are working in a system that accumulates failures silently.
These rules prevent the five most common ways AI sessions produce
confident, wrong outputs. Follow them every session.

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

## Branch Verification Before Commits

**Re-check the branch immediately before every `git commit`.**

Do not trust the branch you saw at session start. Parallel sessions,
automated merges, and other operators can move HEAD between your first
read and your commit. Run `git rev-parse --abbrev-ref HEAD` right
before staging.

If the branch differs from what you expected: STOP. Tell the user.
Do not auto-switch, auto-revert, or assume it's fine.

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
**Category:** [SS|CF|ID|IDUP|FL]
**Count:** [how many times this root cause has appeared]
**Prevention:** [what rule would prevent the next occurrence]
```

### The Five Drift Categories

| Code | Name | Signal |
|------|------|--------|
| SS | State Staleness | Acted on data that changed since you last checked |
| CF | Context Failure | Lost track of what session/branch/project you're in |
| ID | Instruction Decay | Followed a rule that's outdated or contradicted |
| IDUP | Infrastructure Duplication | Built something that already existed |
| FL | Feedback Loss | Made the same mistake again because the lesson wasn't captured |

Don't filter entries. Don't fix them inline. Just record. The minor
failures are where patterns hide.

---

## Three-Occurrence Rule

When the same root cause appears **three times** in the failure log:

1. Stop treating it as a user error.
2. Start treating it as a system bug.
3. Write a preventive rule in this file.

One occurrence is an accident. Two is a coincidence. Three means the
conditions that produce this failure are structural. No amount of
"being more careful" prevents the fourth — the environment makes
it likely.

The response is always: write a rule, a check, or a gate that
prevents the next occurrence. Add it to the relevant section of
this file. If you can't prevent it automatically, make it visible
so you catch it faster.

Rules written from three-occurrence patterns go here:

```markdown
<!-- SYSTEM RULES (derived from failure patterns) -->
<!-- Each rule traces to 3+ entries in failure-log.md -->
```

---

## Infrastructure Check

Before proposing any new tool, integration, script, or automation:

1. Check what already exists in this repo (`scripts/`, `utils/`, config files)
2. Check what your tools provide natively (built-in commands, MCP servers, CLI flags)
3. Check connected services (existing APIs, authenticated integrations)

The most common IDUP failure is building something that already
exists two directories away, or that the platform added last month.

---

## Post-Compaction Recovery

When context is compressed during long sessions:

1. Re-read any active plan file before continuing work
2. Verify phase status — "started" does not mean "completed"
3. Confirm with user before any phase transition

Context compaction preserves what was done but may lose what
remained to do.

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

## Quick Reference

```
SESSION START → pre-flight (context, changes, assumptions)
BEFORE COMMIT → verify branch matches expectation
BEFORE ACTION → live-state check on dependencies
AFTER FAILURE → append to failure-log.md
WEEKLY REVIEW → count by root cause, not by symptom
THREE OCCURRENCES → write a rule, don't just "be careful"
BEFORE BUILDING → check what exists first
```

---

Want this automated? Install the Nexus plugin:

```
/plugin marketplace add crowcreation/nexus
```

<https://github.com/crowcreation/nexus>
