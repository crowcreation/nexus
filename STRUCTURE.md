# Structure

Nexus has one structural shape, and it is written down once, in
[`nexus.structure.json`](./nexus.structure.json). That file is the single source
of truth for where state lives and what the plugin ships:

- the failure log is the root `failure-log.md`
- session state lives under `.claude/session-state/`
- the living map is the root `universe.md`
- the knowledge base is PARA: `KB/Projects`, `KB/Areas`, `KB/Knowledge`,
  `KB/Goals`, `KB/Daily`, `KB/Archive`, `KB/_Admin`
- day-one frontmatter is four fields: `title`, `status`, `tags`, `updated`
- the commands are `done`, `status`, `idea`, `failure`, `field-report`,
  `nexus-init`
- drift categories are an optional, emergent vocabulary, never imposed on a
  day-one log

## Why a JSON file nothing imports

The markdown commands and the Python hooks each restate these paths in their own
prose and code. Editing `nexus.structure.json` does not magically rewrite them —
there is no build step, and a markdown command cannot import a JSON value.

So the JSON is canonical for a different reason: a check makes deviation fail.
[`scripts/check_plugin_coherence.py`](./scripts/check_plugin_coherence.py) loads
`nexus.structure.json` and asserts that every consumer agrees with it — the same
failure-log path everywhere, the command set matching, no stale state paths under
an old `.nexus` directory left behind, the drift vocabulary consistent wherever
it appears. The check
runs as a pre-commit hook and a GitHub Action. If a command drifts from the
declared structure, the commit fails with a precise diff.

This is the plugin practising what Nexus preaches. The whole project exists
because a distribution artefact can silently drift from its own source. The
0.5.0 to 0.6.0 reconciliation happened because two state models (an old `.nexus`
directory and KB-root) had been living in one plugin for weeks without anyone
noticing. The
check is the rule written so it cannot happen a third time.

## The two scaffolders are thin emitters of one structure

`/nexus-init` and the setup prompt both build the same KB-root foundations. They
are two ways to emit the one structure in `nexus.structure.json`, kept in
agreement by the check. `/field-report` is the human backstop for the drift a
check cannot see — the semantic, "this got sloppy" kind — by formatting failure
entries for sharing with other operators.

## Two layers, two sync stories

Nexus ships its discipline on two layers, and they trade off differently:

- **The paste layer** — [CLAUDE-lite](./templates/CLAUDE-lite.md) and the
  [setup prompt](./setup-prompt.md). You copy it into your own repo and own the
  copy outright. There is **no user-sync problem**: nothing of ours sits in your
  repo waiting to go stale. The cost is the other side of the same coin — you get
  no automatic updates. When the patterns improve, your pasted copy does not.

- **The plugin** — installed from the marketplace. It **does** get updates: a new
  version is one `/plugin marketplace update` (or a Customize-panel reinstall)
  away. The cost is update friction — the plugin can fall behind its source, and
  keeping it current is a real step (see [docs/updating.md](./docs/updating.md)).

The conclusion we build around, on purpose: the **discipline** lives in the paste
layer, where it can never go stale on the user, and the **enforcement
automation** lives in the plugin, where the update cost buys you hooks and checks
that a paste cannot provide. Discipline first; the plugin is the graduation step,
not the entry point.
