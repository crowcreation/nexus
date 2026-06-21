# Changelog

All notable changes to the Nexus plugin are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
the plugin aims to follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
The version here matches `.claude-plugin/plugin.json` and
`.claude-plugin/marketplace.json`. Every command, hook, or structure change bumps
the version and adds an entry below.

## [0.9.0] - 2026-06-21

`/nexus-init` hardening from the cold third-party walkthrough: a location guard
and a simpler branch-verification prompt.

### Changed

- `/nexus-init` pre-flight now sanity-checks the location and warns before
  scaffolding into a directory that looks like a parent/container of other
  projects (catches the common "forgot to `cd` into the new folder" mistake).
- `/nexus-init` branch-verification step now recommends Skip on a fresh setup and
  explains it in one line, instead of presenting a master-vs-main menu on day one.

## [0.8.0] - 2026-06-20

`/nexus-init` now seeds a `CLAUDE.md` of operating rules, so the quick scaffold
path is no longer rule-less. Getting Started spells out the three onboarding paths.

### Changed

- `/nexus-init` also creates a `CLAUDE.md` (from `templates/CLAUDE-lite.md`) when
  absent, alongside the failure log, KB skeleton, and hygiene files. The quick path
  now includes the operating rules; the setup-prompt remains the guided path that
  additionally seeds your goal and `universe.md`.
- `GETTING-STARTED.md` clarifies the three ways in: CLAUDE-lite paste (no install),
  plugin + `/nexus-init` (quick), plugin + setup-prompt (guided).

## [0.7.0] - 2026-06-20

Phase B: mechanical sync so the plugin cannot silently drift from its own source
again — on the plugin-to-repo axis and the plugin-to-user axis.

### Added

- `nexus.structure.json` — single machine-readable source of structural truth
  (failure-log path, session-state dir, universe path, PARA folders, frontmatter
  fields, command set, optional drift vocabulary), narrated by a thin
  `STRUCTURE.md`.
- `scripts/check_plugin_coherence.py` — zero-dependency coherence check that
  asserts every consumer agrees with `nexus.structure.json`: no stale state paths
  under an old `.nexus` directory, one failure-log path everywhere, the command
  set matching, and the drift vocabulary consistent wherever it appears.
- `.pre-commit-config.yaml` and `.github/workflows/coherence.yml` — run the
  coherence check on commit and in CI.
- `CHANGELOG.md` (this file) and a contributing rule: every command, hook, or
  structure change bumps the version and adds a changelog entry.
- `docs/updating.md` — how to keep an installed plugin current (CLI update versus
  desktop Customize panel; remove-and-re-add when greyed), linked from the README.
- Offline staleness surface: `session_preflight.py` prints the installed plugin
  version (read from the plugin manifest). No network call.

### Changed

- Drift categories are now consistently an **optional, emergent vocabulary**,
  never imposed on a day-one log. The seed template (`templates/failure-log.md`)
  is category-free; `/nexus-init` now seeds the same category-free log the setup
  prompt does; the seven codes remain only as an opt-in reference in the
  failure-logging skill, CLAUDE-lite, and `/failure`. This resolves the earlier
  inconsistency where a `/nexus-init` repo got a categorised log and a
  setup-prompt repo got a category-free one.

## [0.6.0] - 2026-06-20

Phase A: reconcile the plugin onto the KB-root state model, so install, scaffold,
and the session ritual all operate on one structure.

### Changed

- `/failure`, `/field-report`, and the three hooks now read and write the root
  `failure-log.md` and `.claude/session-state/`, replacing the old `.nexus`
  directory model. `/failure` is format-tolerant — it matches the log shape
  already in use rather than imposing one.
- `/nexus-init` repurposed to scaffold the KB-root foundations (root
  `failure-log.md`, the `KB/` PARA skeleton, day-one hygiene files), idempotently.
- README, ROADMAP, manifests, and `templates/universe.md` updated to the
  reconciled command set and KB-root framing.

### Removed

- `/nexus-onboard` — the one-shot universe-mapping interview. Universe mapping is
  now seeded by the setup prompt and kept living by `/done` and the weekly review.
- `templates/config.json` — dead under the KB-root model (nothing read it).

### Added

- `docs/cowork-setup.md` — the single desktop story (no-terminal install via the
  Customize panel, namespaced `nexus:` commands, refreshing a stale plugin).
