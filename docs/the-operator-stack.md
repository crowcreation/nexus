# The Operator Stack

How operational discipline builds up in persistent AI systems.

> The [field guide](./the-coherence-problem.md) describes what breaks and why.
> This document describes the layers that form when you start fixing it.

---

Nobody designs these layers. They emerge. Something goes wrong, you
write it down, patterns appear, rules follow, enforcement automates
the rules, and eventually the interesting part is what you've
learned -- not the tools.

Five layers. Not architecture to adopt, but a map of what
accumulates when persistent AI workflows run long enough to fail in
structural ways.

## Layer 0 -- Substrate

The operational environment where persistent state lives.

This means Git, markdown files that survive between sessions,
terminal access, local-first tooling, and repositories that evolve
over time. It means workflows where the AI reads instructions
someone wrote last week, checks state that another session modified
yesterday, and commits to a branch that three other processes also
touch.

Without persistent state, the coherence problem doesn't emerge.
Without version control, you can't track what drifted. Without
markdown, you don't have a format that both humans and AI can read
and write without friction.

Nexus doesn't provide the substrate. It assumes it. Operators
converge on their own combinations -- worktrees for session
isolation, tmux for persistence, Obsidian or plain directories for
knowledge, local search for discoverability. These are
coherence-supporting patterns from mature engineering, not inventions
of any particular project. Use what works. The substrate exists
independently of everything above it.

## Layer 1 -- Operational Memory

The record of what happened and what was learned.

A failure log. Notes on recurring friction. Rules that accumulated
from past incidents. Persistent state about what broke, why, and
what prevents it next time. This is the layer where a system starts
to know itself -- not through model training, but through append-only
records that survive across sessions.

This is likely the real primitive. Not the plugin. Not the
discipline habits. The durable, transmissible record of operational
experience. A failure log with a hundred entries is more valuable
than any configuration, because it contains information that doesn't
exist anywhere else: the specific ways this system, with this
operator, running these workflows, actually fails.

The failure log format, drift categories, and three-occurrence rule
all live here. They're mechanisms for turning incidents into memory.

## Layer 2 -- Operational Discipline

The habits that prevent known failure modes.

Live-state checks before acting on cached data. Branch verification
before committing. Pre-flight checks at session start. Explicit
contracts before delegating work. Reflection at session close. Weekly
review of the failure log for patterns.

These are not tools. They're behaviours. They work when followed and
fail when skipped, regardless of what enforcement exists above them.
Someone who checks live state before every recommendation prevents
staleness failures whether or not a hook reminds them to.

[CLAUDE-lite](../templates/CLAUDE-lite.md) lives at this layer. Five
rules, one failure log, no dependencies. Paste it in, follow it,
see what accumulates. The discipline exists before the enforcement,
and creates value without it.

## Layer 3 -- Enforcement

Automation that reinforces the habits.

Hooks that check your branch before a commit. Pre-flight scripts
that run at session start. Compliance gates that block publishing
until content passes validation. Structured commands that make the
right behaviour the easy behaviour.

The [Nexus plugin](../README.md#install-the-plugin) lives here. It
automates what Layer 2 describes. Session pre-flight becomes a hook
instead of a habit. Branch verification becomes a check instead of
a reminder. Failure logging gets a structured command instead of
manual file edits.

Enforcement reinforces discipline. It does not create discipline
from zero. An operator who installs the plugin without understanding
the habits it automates will find it annoying rather than useful.
The layers build upward for a reason.

## Layer 4 -- Shared Intelligence

What emerges when operational memory crosses operator boundaries.

Field reports from different operators. Drift patterns that recur
across unrelated systems. Heuristics that one operator discovered
and another recognises. A shared vocabulary for failure modes that
previously had no name.

This layer doesn't exist yet in any meaningful way. It's the
long-term hypothesis: that persistent AI systems fail in structurally
similar ways regardless of operator, domain, or tooling -- and that
sharing those patterns accelerates everyone's learning.

[Discussions](https://github.com/crowcreation/nexus/discussions)
and [field reports](../commands/field-report.md) are the current
mechanism. Whether shared intelligence becomes the most valuable
layer depends on whether the failure patterns turn out to be
universal or idiosyncratic. The data doesn't exist yet to know.

---

## Where things live

| Layer | In the repo | Outside the repo |
|-------|-------------|------------------|
| Substrate | -- | Git, terminal, markdown tools, worktrees |
| Operational memory | `templates/failure-log.md`, drift categories | Your `failure-log.md`, your accumulated entries |
| Discipline | `templates/CLAUDE-lite.md`, `patterns/` | Your CLAUDE.md rules, your review habits |
| Enforcement | `hooks/`, `commands/`, `skills/` | Your installed plugin instance |
| Shared intelligence | `CONTRIBUTING.md`, Discussions | Your field reports, your shared learnings |

The [gist](https://gist.github.com/crowcreation/1809ad9f1fddbf018113b8f1712dfadb)
covers Layer 2. It hints at Layer 1. It doesn't touch the rest.
That compression is deliberate. The gist works because it's a
practical artifact, not a systems document.

---

## What Nexus assumes but does not own

The substrate matters. These tools exist independently, predate this
project, and will outlast it:

- **Version control** -- Git, branches, commit history as audit trail
- **Persistent operational memory** -- markdown files, knowledge bases, accumulated notes
- **Session persistence** -- AI environments that carry instructions between conversations
- **Local-first tooling** -- search, editing, scripting without network dependencies
- **Process isolation** -- worktrees, terminals, containers for parallel work

Operators converge on these because persistent AI workflows need
them, not because any project prescribes them.

---

[Field guide](./the-coherence-problem.md) · [Patterns](../patterns/) · [Templates](../templates/) · [Back to README](../README.md)
