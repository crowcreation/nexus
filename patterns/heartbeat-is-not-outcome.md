# Heartbeat Is Not Outcome

A check that proves a job ran is not a check that the job did its work.

Most health checks on scheduled AI agents start as liveness checks: did the
timer fire, did the process exit cleanly, is the last run recent. They are
cheap to write and they are green almost all the time. That is the problem.
A job can run on schedule, exit cleanly and do nothing, and a liveness check
cannot tell the difference.

## What broke

An agent reads a mailbox folder of forwarded emails, works out what each one
is about, and files it. It runs on a timer. Its health check asked one
question: has the scheduled task run recently?

One afternoon in August it skipped five forwards. It did not crash. It ran,
on time, every time, for the next seventeen days, and the check stayed green
throughout. The five emails sat untouched until a person noticed.

The cause was found weeks later, from the agent's own state file. It keeps a
cursor: a record of which messages it has already seen, each with a status.
Five entries carried a status the agent never writes, all stamped the same
second. Something else, most likely an interactive session, had marked those
five as handled. From then on the agent counted them as already seen and
skipped them, which it reported honestly as "skipped by cursor". Nothing read
that number.

The same week, in the same system, a second check turned out to have the
same shape. A mailbox bounce-ratio check read sent items and bounces, and
when every read failed it got zero of each and reported OK: "no outbound
email or bounces". That one is the subject of its own note, [The Quiet
Zero](./the-quiet-zero.md).

## What changed

A new check reads the agent's own run reports and never calls the mailbox.
For each live run it compares two numbers the agent already records:
forwards received (messages polled, minus those the cursor skipped) and
forwards handled (the sum of the terminal outcomes). It:

- fails when a gap between the two lasts through two live runs in a row,
  and says how many are unhandled and when the oldest was first seen;
- fails when the last two runs ended before they polled anything. A run
  that never got far enough to have an outcome cannot make the check green;
- warns when there is no live run at all, when the latest run was a
  kill-switch run, when the poll page came back full so older forwards may
  never have been seen, and when the cursor holds a recent entry with a
  status the agent never writes. That last rule exists because the original
  incident is invisible in the run reports; only the state file shows it;
- ignores dry runs, and returns OK on a machine that does not own the job,
  because the owning machine runs the check.

The old liveness check was kept. It answers a different question.

## The test that pins it

The reports fed to the check in its tests are written by the agent's own
report builder, not by hand, so the reader is tested against what the writer
really emits. Two live runs that each received five forwards and handled
none fail with "5 forward(s) unhandled, oldest since <time>". Before this
check existed, the only signal on this agent was liveness, and it would have
stayed green.

Two further tests assert that the constants the check relies on, the page
size and the list of statuses the agent writes, are read from the agent's
module rather than copied. If the agent changes them, the check's tests fail
instead of drifting quietly.

## How to apply

1. For each scheduled agent, write down what "did its work" means as two
   counts: received and handled. If the agent does not record them, that is
   the first fix.
2. Write the check against the agent's own report. Refuse to be green when a
   run never got far enough to have an outcome.
3. Name the states the agent can write. Anything else found in its state
   file is a finding, not noise.
4. Test the reader with the writer's real output, and read shared constants
   from the writer's module instead of copying them.

The rule in plain words: a heartbeat proves the clock, not the work. A check
is only as honest as the thing it reads.

Maps to: [state staleness](../docs/the-coherence-problem.md#iv-a-taxonomy-of-drift),
a green status that had stopped being true. Quiet wrongness is more dangerous
than obvious failure.
