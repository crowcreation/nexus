# Gate the Chain

When your AI runs a compound command, the join between steps is the gate.

An AI session will often put several steps on one line: edit a file, run the
tests, commit, push, merge. The shell has two common ways to join them. A
semicolon means "run the next step regardless". Two ampersands mean "run the
next step only if this one succeeded". They look almost identical on screen.
Only one of them is a gate.

## What broke

Two incidents, four days apart, in the same system.

A pull request was merged while one of its automatic checks was failing. The
command waited for the checks to finish, looked at the result, and then
merged, with a semicolon between each step. The check failed, the exit code
was non-zero, and the merge ran anyway. The failure turned out to be a false
alarm, which is the only reason it cost nothing. The same line would have
merged a real failure.

Four days later a pull request went in with a failing test. One command made
an edit that asserted an exact old string, ran the tests, then committed,
pushed, opened the pull request and merged it. The edit's assertion failed
because the indentation did not match. The test run printed one failure. The
commit and merge ran anyway, because the tests were followed by a semicolon.
It was fixed two minutes later by a second pull request.

Neither was a capability failure. The AI knew the tests should pass first. The
command it wrote simply did not make that true: the join between the steps
did not stop on failure, so the step that could not be undone ran anyway.

## What changed

A reminder in an instructions file asks the AI to remember. The fix that
lasts is a check that runs before the AI's command does, and refuses.

The check splits the command into steps, respecting quotes and multi-line
text so a semicolon inside a commit message is not mistaken for a separator.
It then looks for a gated step (a commit, a merge) that is reachable from an
earlier test, check or script through anything other than a chain of
`&&`. If it finds one, it refuses and prints the safe form.

It was kept deliberately narrow, because a guard that cries wolf gets
switched off:

- Setup steps such as changing directory or listing status do not count as
  something that needs gating.
- A `set -e` prefix passes, as does a gated step inside an `if`.
- There is a documented override for the rare real case.
- It does not catch a pipe that hides the exit code of a test. That gap is
  written down, not hidden.

It also failed in its first day. It read the line breaks of a long inline
script as semicolons, and refused the safe `&&` form it was designed to
recommend. Test a new guard against the safe version of the thing it blocks
before you trust it.

## How to apply

1. Search your failure log for any case where a step ran after a step that
   had failed. Look at the characters joining the steps.
2. Pick the two or three actions you cannot take back: merge, publish, send,
   delete. Those are the gated steps.
3. Add a rule where it can actually refuse, such as a pre-command hook in
   your AI tool or a wrapper script, and not only a line in your
   instructions file.
4. Give it a safe example and an unsafe example as tests, and write down
   what it does not cover.

The rule in plain words: the step that cannot be undone should be joined to
the step that proves it is safe by something that stops when the proof fails.

Maps to: [instruction decay](../docs/the-coherence-problem.md#iv-a-taxonomy-of-drift).
