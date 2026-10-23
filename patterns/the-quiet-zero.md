# The Quiet Zero

When a reader fails and hands back an empty value, everything downstream
shows a healthy nothing.

The shape is familiar to anyone who has written defensive Python:

```python
try:
    rows = read_the_thing()
except Exception:
    rows = []
```

It is written with good intent. One flaky read should not take down the
whole report. But a status panel, a health check or a pre-flight gate that
consumes `rows` now cannot tell "nothing to report" from "could not read".
Both arrive as an empty list. The panel renders zero, and zero looks fine.

## What broke

A pre-flight check on the business's books compared two ledgers before a
session was allowed to act on them. Its fetch was wrapped in a broad `except`
that turned an attribute error into an empty result. The pre-flight said
CLEAN against books that were weeks behind.

A search of the codebase for the same shape found 436 sites: a broad
`except` whose body does nothing but pass, continue or break, or return or
assign a constant or empty value, makes no call, does not raise, and does not
use the exception it caught. Twenty-four of them fed a health check, a
liveness probe, a status panel or a session-start alert:

- a mailbox bounce-ratio check that reported OK "no outbound email or
  bounces" when every mailbox read had failed, because 0 sent and 0 bounced
  is a perfectly healthy ratio;
- a fleet traffic-light panel that showed every agent with an empty
  dead-letter queue when the queue file could not be read;
- a session-start alert that counted API failures, and printed 0 when the
  signals file was unreadable;
- an agent-map view that rendered as an empty fleet whenever its producer
  crashed.

None of these were noisy. That is the whole failure class: the instrument is
structurally incapable of failing, so it reports healthy when it is broken.

## What changed

Three things, in this order.

**A gate.** A small script walks the syntax tree of every script and refuses
the shape above. A waiver is allowed, `# swallow-ok: <reason>`, and a waiver
without a reason does not count. A `try` whose body only imports is exempt,
because an optional-dependency fallback is the one legitimate use. It runs as
a pre-commit hook, so a new quiet zero cannot land.

**A shrink-only baseline.** The 436 existing sites were listed in a fixture.
The hook fails on a new offender, and it also fails on a baseline line that
no longer offends. The list can only go down, and it is always true. A
baseline that can silently grow or go stale is itself a quiet zero.

**A burn-down, in passes.** The 24 sites feeding health signals went first.
Then the rest, in batches of twenty to thirty, each a separate change with
its own tests. Within a week the baseline read 184. Each site was fixed one
of three ways, and the return type never changed, so no caller broke:

- *log*: keep the broad `except`, write the exception to stderr, return the
  same value. The panel still shows zero, but the operator's log says why;
- *narrow*: catch only the types the body can raise, plus a log. Anything
  else now propagates;
- *surface*: put the failure into the returned value. A status line now
  carries the error text. A health result gains a `read_errors` list that is
  empty when every read worked. The bounce check returns WARN "unverified"
  instead of OK, but only when the counts are 0/0 and at least one read
  failed, so a genuinely quiet mailbox still reads OK.

Some sites were skipped on purpose and the reasons written down: a
kill-switch read that must fail open, module bootstrap blocks, and a helper
whose empty answer is its documented "cannot say" result, distinct from
`False`. Deciding that a swallow is right is fine. Not deciding is the bug.

## The test that pins it

The gate has 23 tests: eight offending shapes and eight clean ones; a
negative control at the command line where a planted swallow fails and the
same handler with one log line passes; a live-tree match against the
baseline; and a test that the pre-fix version of the health module still
contains the original offender, so the suite was red before the fix and green
after.

Each burn-down pass adds its own: dead credentials give WARN, clean reads
still give OK, an unreadable queue file sets the `dlq_unreadable` flag, a
crashed producer lands in `read_errors`. And the gate itself prints a line
that a human can read in the commit log: `OK - no new silent broad excepts,
184 baselined`.

A gap is written down rather than hidden: a handler that logs but still
returns an empty value to a pre-flight gate passes the hook. The handler
alone does not show that. That one is the next class.

## How to apply

1. Search your scripts for a broad `except` followed by `pass`, `return
   None`, `return []` or `return {}`. Count them. The number is usually
   larger than you expect.
2. For every site that feeds a health signal, a dashboard or a gate, make
   "could not read" a different value from "nothing there". A `WARN
   unverified` beats a green zero.
3. Fix the rest one of three ways: log, narrow, or surface. Keep return
   types stable so callers do not break.
4. Put the remaining count in a shrink-only baseline that a hook enforces.
   A list that can only go down is the only kind that stays honest.

The rule in plain words: an instrument that cannot fail is not an
instrument. A zero that might mean "I could not look" has to say so.

Maps to: [state staleness](../docs/the-coherence-problem.md#iv-a-taxonomy-of-drift),
and its companion note [Heartbeat Is Not Outcome](./heartbeat-is-not-outcome.md),
on the check that watches the clock instead of the work.
