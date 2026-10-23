# Patterns

Two kinds of file live here.

**The five patterns.** Each one is something you can start on Monday with a
text file. The short versions are in [section X of the field
guide](../docs/the-coherence-problem.md#x-patterns-you-can-steal); these
files carry the implementation detail.

- [The failure log](./failure-log.md)
- [The three-occurrence rule](./three-occurrence-rule.md)
- [The live-state check](./live-state-check.md)
- [The narrow contract](./narrow-contract.md)
- [The session pre-flight](./session-pre-flight.md)

**Field notes.** One specific failure class each, taken from a real incident
in a system that has run persistent AI sessions daily for over a year. Each
note says what broke in plain words, the mechanism that ended it, and the
test that pins it so it stays ended. Names, figures and credentials from the
operating business are removed; the numbers that remain are the system's own.

- [Gate the Chain](./gate-the-chain.md): the commit or merge that ran after
  the test that failed, because a semicolon joined them.
- [Heartbeat Is Not Outcome](./heartbeat-is-not-outcome.md): the health
  check that stayed green for seventeen days while an agent skipped its work,
  because it watched the clock instead of the outcome.
- [The Quiet Zero](./the-quiet-zero.md): 436 places where a failed read
  became an empty value, and the shrink-only gate that is working the number
  down.

A field note is the right size for a contribution. If you have one, see
[Contributing](../CONTRIBUTING.md): what broke, why, how it was detected, what
changed, and which drift mode it maps to.
