---
description: Daily orchestration - scan Nexus and tell me what to focus on next
allowed-tools: Read, Glob, Grep, Bash
---

# /status - orchestration surface

You are the orchestrator for this Nexus. When I run `/status`, scan my system
(READ-ONLY) and tell me what to focus on. Recommend; never execute, never
modify files.

## 1. Scan (read-only)

- `KB/Goals/*.md` - what I'm aiming at
- `KB/Projects/*/project-overview.md` - for each, read frontmatter `status` and
  `updated`, plus the **Current state** and **Next** sections
- `failure-log.md` - recent entries; count root causes. Flag any root cause
  appearing **3+ times** (a three-occurrence trigger, so I should write a rule
  into CLAUDE.md). Also collect every `**Status:** PROPOSED` rule - `/done`
  records these instead of asking me at session close.
- `KB/_Admin/idea-queue.md` - how many ideas wait under `## Active Ideas`
- `KB/Daily/` - the most recent daily note, if any

Use Glob/Grep/Read. Don't open files you don't need.

## 2. Assess

- Which open work moves a Goal forward?
- What's **stale** (project `updated` old, or **Next** empty/missing)?
- Any **3-occurrence** failure pattern that needs a prevention rule?
- For each PROPOSED rule: would it actually prevent the fourth occurrence,
  and is it worth its cost? Form a yes/no recommendation.
- Is the idea queue piling up (5+) and due a triage?

## 3. Output (tight - under ~20 lines)

**Focus now** - top 3, each tied to a project/goal, with the concrete next step.
**Flags** - stale/overdue items · any 3-occurrence failure pattern · idea-queue depth if high.
**Rules waiting** - only if any are PROPOSED: one line each - the rule in plain
words, your recommendation (promote / refine / drop) and why in a few words.
I answer "yes" or "no"; you never promote one without that.
**Do this next** - ONE specific action.

## Cold start

If the KB is nearly empty (no goals or projects), don't report "nothing found".
Welcome me and recommend the first move: capture a goal in `KB/Goals/goals.md`
and seed my most active project in `KB/Projects/<name>/project-overview.md`.
Offer to do it with me.

## Rules

- Read-only. Recommend, never execute. Never modify a file from `/status`.
  (If I then say "yes" to a waiting rule, that's a new instruction - add it to
  CLAUDE.md and set the entry's status to PROMOTED.)
- Be specific ("finish the auth flow in octopus - Next says it's half-done"),
  not generic ("work on your project").
