# The Three-Occurrence Rule

When the same failure appears three times, stop treating it as a user
error and start treating it as a system bug.

One occurrence is an accident. Two is a coincidence. Three means the
conditions that produce this failure are structural. The environment
makes it likely. No amount of "being more careful" will prevent the
fourth occurrence, because the problem isn't carelessness - it's that
your system creates the conditions for this failure repeatedly.

The response to three occurrences is always the same: write a rule,
a check, or a gate that prevents the fourth. If you can't prevent it
automatically, make it visible so you catch it faster next time.

This rule does two things. First, it gives you permission to ignore
one-off failures without guilt - they genuinely might not recur.
Second, it creates a hard trigger for systemic fixes, so structural
problems can't hide behind the excuse of "it was just a mistake."

## How to apply

When reviewing your failure log, count occurrences by root cause,
not by surface symptom. "Acted on stale CRM data" and "emailed a
prospect whose deal closed yesterday" are the same failure. Three
of those means you need a live-state check before CRM-dependent
actions, not three separate fixes for three separate emails.
