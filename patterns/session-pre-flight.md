# The Session Pre-flight

At the start of every AI session, verify three things before doing
any work:

**What context you're in.** Which branch, which project, which
workspace. Not what you remember from last time - what's true right
now. Parallel sessions, overnight automations, and other operators
can change the context between sessions without you noticing.

**What changed since last session.** New commits, modified files,
updated configurations, closed deals, sent emails. Anything that
happened between the end of the last session and the start of this
one. If you skip this step, you'll build on assumptions that may no
longer hold.

**Whether previous assumptions are still valid.** The prospect you
were drafting an email to - is the deal still open? The file you
were modifying - has someone else changed it? The API endpoint you
were calling - does it still return the same format? Stale
assumptions are invisible until they produce wrong outputs.

## Why this prevents the worst failures

The most disorienting coherence failure is doing excellent work in
the wrong context. Everything runs perfectly. The output is high
quality. And it's all pointed in the wrong direction because the
starting assumptions were stale.

A sixty-second pre-flight catches this before any work begins. It's
the cheapest insurance in the entire system.

## How to implement

Add a checklist to your AI's configuration file that runs at session
start. Three items: verify context, check for changes, validate
assumptions. Make it automatic so it doesn't depend on you
remembering to do it.
