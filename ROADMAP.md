# Roadmap

Nexus is an experimental, evolving field manual, not a finished product. This page is the honest map of what is real in this repo today, what is planned, and what deliberately stays a graduation step rather than a day-one cost. It will keep changing as the tooling and the practice mature.

## Built (real today)

- **The failure log** - the core primitive. Append-only record of what broke and why.
- **`/done`** - the day-one session-close command: daily note, failure-log entry with three-occurrence check, project state nudge, optional knowledge capture.
- **`/failure`** - plugin command for failure-log entries. Format-tolerant: matches the shape your log already uses, with drift categories as an optional vocabulary rather than an imposed one.
- **`/field-report`** - formats and redacts a log entry for sharing with other operators. Nothing sent automatically.
- **`/nexus-init`** - one idempotent command to bootstrap the KB-root foundations (root `failure-log.md`, the `KB/` PARA skeleton, day-one hygiene files). The one-command alternative to the setup prompt.
- **The three hooks** - session pre-flight, branch verification before commit, and session save.
- **CLAUDE-lite** - five rules and a failure log to paste into any project, no dependencies.
- **The `learn/` course** - seven modules covering the why, the substrate, the KB and `universe.md`, the disciplines, working together, and the arc.
- **The setup prompt** - interviews a new operator and scaffolds a lean Nexus around their real work.

## Planned

- **The full `/status` orchestrator** - today `/status` is a read-only scan-and-recommend surface. The plan is a richer orchestrator that reconciles across goals, projects, failures, and the idea queue.
- **`/idea`** - quick-capture to the idea queue. Shipped as a command; the triage and routing layer around it is still planned.
- **`/weekly-review` command** - the weekly review is documented as a discipline now; a command to run it is planned.
- **The cockpit** - an operations interface (Ops Center) generated from your markdown. Minimal for a new operator, vast for an experienced one.
- **Worktrees as graduation** - session isolation, pulled in when your failure log shows parallel-session pain.
- **Connected operators / agent-exchange** - the far end of the arc: linking nexus points so their agents collaborate directly. Starts through the human-and-markdown layer (weekly failure-log compare, shared field reports) and only later becomes a technical link.

## Graduation foundations (deliberately not day-one)

These exist in the maintainer's private setup. Operators adopt them as their work matures, not on day one. Day one stays tiny on purpose.

- **Full KB governance docs** - the `learn/` course is the light governance for now. The dense governance set is a later adoption.
- **The full CLAUDE.md** - day one ships a six-primitive CLAUDE.md. The full version grows through use.
- **Pre-commit hooks** - frontmatter validation, notes-index checks, and similar quality gates.
- **`.mcp.json` beyond a filesystem stub** - wiring real MCP servers is a graduation step.
- **The full 7-field frontmatter** - day one uses four fields (`title`, `status`, `tags`, `updated`). The fuller schema (owner, last_reviewed, review_every, sources) comes later.
- **Agent-register and fleet docs** - the apparatus for running a fleet of narrow agents.
- **Notes-index automation** - generating and validating the notes index automatically.

## Retired commands

- **`/nexus-status`** - an earlier failure-log summary, retired in favour of `/status`, which scans the whole system; the failure-log summary is a subset of that scan.
- **`/nexus-onboard`** - a one-shot universe-mapping interview that wrote to `.nexus/universe.md`. Retired in the 0.6.0 KB-root reconciliation: universe mapping is now seeded by the setup prompt's interview and kept living by `/done` (nudged when the world moves) and the weekly review, against a root `universe.md`. The earlier plugin also kept state under a `.nexus/` directory; that model has been replaced entirely by the KB-root structure (root `failure-log.md` and `universe.md`, session state under `.claude/session-state/`).
