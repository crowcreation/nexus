# The Failure Log

Create an append-only file. Every time something goes wrong in your AI
workflows, add an entry with four fields: date, what happened, why it
happened, and what category it falls into.

Don't filter. Don't fix. Just record.

The temptation is to skip entries that feel minor or embarrassing. Resist
it. The minor failures are where patterns hide. A wrong API call, a
stale recommendation, a wasted automation run — each one alone is
forgettable. Three of them together are a signal.

Review the log weekly. Not to fix individual entries, but to look for
clusters. After a month, you'll see the same root cause appearing in
different disguises. After three months, the clusters will tell you
exactly where your system is weak — not where you think it's weak,
but where it actually fails.

The log is more valuable than any individual fix it produces. A fix
solves one problem. The log reveals which problems are structural.

## How to start

Create a file called `failure-log.md`. Add a table or list with columns
for date, description, root cause, and category. Use whatever categories
emerge naturally — common ones include state staleness, context loss,
instruction decay, infrastructure duplication, and feedback loss.

The first twenty entries will feel random. Keep going.

A starter template is available in [`/templates/failure-log.md`](../templates/failure-log.md).
