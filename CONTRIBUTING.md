# Contributing

Nexus is currently a collection of operational patterns, failure records,
and coordination heuristics extracted from real daily use.

The most valuable contributions are not features. They are lessons earned
through operation.

## What belongs here

- Failure patterns with clear root causes
- Drift incidents and coherence failures
- Operational heuristics that survived repeated use
- CLAUDE.md patterns that prevented coordination problems
- Narrow-contract examples
- Session pre-flight checklists
- Improvements to clarity, diagnosis, and operational discipline

When possible, include:
- what broke
- why it broke
- how it was detected
- what changed afterward
- which drift mode it maps to

Concrete incidents are more valuable than abstract opinions.

## What does not belong here (yet)

- Large architectural rewrites
- Framework proposals
- General-purpose AI tooling
- Feature requests without operational grounding
- Abstractions disconnected from real use

Nexus is intentionally narrow.

## Keeping the plugin coherent

Two rules keep the plugin honest with itself and current for the people who
install it:

- **Structure lives in one place.** Paths, the command set, and the drift
  vocabulary are declared once in [`nexus.structure.json`](./nexus.structure.json).
  Every consumer restates them in its own prose or code, so when you change one,
  change it everywhere and run `python scripts/check_plugin_coherence.py`. The
  check runs on commit (pre-commit) and in CI; it fails with a precise diff if a
  consumer drifts.
- **Every command, hook, or structure change bumps the version and adds a
  changelog entry.** Update `version` in both `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and add an entry to
  [`CHANGELOG.md`](./CHANGELOG.md). This is how an installed plugin can tell it is
  behind its source.

---

The goal is not to build the biggest system.
The goal is to understand how coherence degrades in real workflows,
and which disciplines prevent it.

Restraint is part of the project.
