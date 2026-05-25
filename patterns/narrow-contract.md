# The Narrow Contract

Before delegating a task to an AI session, write down four things:

**What it needs.** Not "access to the codebase" but "the contents of
these three files and the output of this API call." Name the specific
inputs.

**What it produces.** Not "improvements" but "a modified version of
this file, or a written explanation of why no modification is needed."
Define a concrete, verifiable output.

**What it must not do.** Not assumed boundaries but explicit ones.
"Do not modify files outside this directory. Do not make API calls.
Do not create new files without approval." Constraints that are
checkable.

**What counts as failure.** Not "something went wrong" but "if the
input file doesn't exist, stop and report rather than improvising."
Defined abort conditions that prevent silent degradation.

This takes sixty seconds. It saves hours of debugging.

## Why it matters

An AI with ambient access that produces good results is
indistinguishable from an AI with ambient access that produces
plausible-looking wrong results. You can't tell the difference
without boundaries to check against.

When a task with explicit boundaries fails, you know exactly which
boundary was violated. Was the input wrong? The output unexpected?
Did it exceed its constraints? Each answer points to a different
fix. Compare this to "the AI did something weird" as a failure
report.

The narrow contract doesn't reduce what AI can do. It makes what
AI does visible.
