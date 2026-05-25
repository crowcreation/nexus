# The Live-State Check

Before any action that depends on external state, query the source.

Don't trust your notes. Don't trust your memory. Don't trust cached
data. Don't trust what the system told you yesterday. Check now.

This one rule, applied consistently, prevents the single most common
coherence failure: acting on information that used to be true. The
CRM record that was updated in another session. The file that was
moved last week. The API response that changed format. The deal
that closed while you were drafting the follow-up email.

The cost of checking is seconds. The cost of not checking is a
plausible-looking output built on wrong foundations — and the
debugging time to figure out why it's wrong, which is always longer
than the check would have been.

## How to apply

Identify the actions in your workflow that depend on external state:
drafting emails (check contact/deal status first), generating reports
(check data source freshness), running automations (validate inputs
before execution), making recommendations (verify the facts they're
built on).

For each one, add a single step: query the live source before acting.
Not "check if you remember it being current" — actually query it.

The rule is simple. Applying it consistently is the hard part. Build
it into your session startup checklist or your AI's configuration so
it happens automatically rather than relying on discipline in the
moment.
