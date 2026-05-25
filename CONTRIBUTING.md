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

The goal is not to build the biggest AI operating system.
The goal is to understand how coherence degrades in real workflows,
and which disciplines prevent it.

Restraint is part of the project.
