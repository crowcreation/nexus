# Nexus setup prompt

Paste everything in the code block below into Claude Code, running inside a
**fresh empty git repo**. It interviews you, scaffolds a lean Nexus around your
real work, seeds a living `universe.md`, and ends by running `/done` so the one
day-one habit is real from minute one.

**Before pasting:** copy this repo's `commands/` folder into your repo's
`.claude/commands/` so `done.md`, `status.md` and `idea.md` already exist. The
prompt is written to leave them alone, not recreate them. (`/done` is the one
command you run on day one. `/status` and `/idea` are copied in too, but you
graduate into them once the daily rhythm has earned them, not on day one.)

```
You are bootstrapping "Nexus" for me, and I want you to understand the spirit
of it before you build anything.

THE SPIRIT: This is an experiment in building a persistent AI operating
system, not a product install. Nexus is a harness for you, Claude: I bring
the structured memory, the rules, and the guardrails; you bring the
intelligence. It is plain markdown in a git repo I own, model-agnostic by
design, so the harness outlives any one model. It starts deliberately small
and grows ONLY through use: every failure logged, every rule earned, every
file justified by a real session. Day one it will be modest. That is expected
and fine. The experiment is what it becomes by month three, and that depends
on a weekly discipline, not on cleverness at setup time. Do not over-build.
Do not pre-fill. Seed intent, not snapshots.

Three things anchor day one: a real BUSINESS goal (the actual outcome I am
working towards, not a Nexus goal); the disciplines (the failure log, the
session ritual, the weekly review); and a LIVING universe.md (a map of my
world, seeded from this interview, kept alive by being nudged as things
change, never a one-shot snapshot).

Work in two stages.

STAGE 1 - INTERVIEW ME. Ask these ONE AT A TIME, wait for each answer, keep it
conversational, don't lecture:
  1. In one or two sentences, what real business outcome are you working
     towards right now?
  2. What's your single most active project? Short name, one line on what it is,
     and where the code/files live.
  3. What ongoing areas of responsibility do you carry that aren't projects?
     (e.g. a product's support, finances, a client) - list a few.
  4. What tools and services do you use day to day? (GitHub, Sentry, email
     provider, host, etc.)
  5. What's the most annoying recurring thing about how you work with AI right
     now - what keeps going wrong or getting lost?
  6. Any rules for how you want me (Claude) to behave in this repo?

STAGE 2 - SCAFFOLD. After the interview, build all of this, then stop:

Foundations (lean, day-one hygiene):
  - .gitignore - with these entries:
      .env
      .env.*
      !.env.example
      .auth/
      state/
      .claude/session-state/
      .claude/worktrees/
      __pycache__/
      *.pyc
      .obsidian/workspace*
      .DS_Store
      .tmp/
  - .env.example - placeholder keys only (NEVER a committed .env):
      ANTHROPIC_API_KEY=
      OPENAI_API_KEY=
      HF_TOKEN=
      GITHUB_TOKEN=
    with a comment noting these are filled when wiring real tools, not day-one.
  - .obsidian/ - a minimal Obsidian config so the vault opens cleanly:
      .obsidian/core-plugins.json = ["file-explorer","global-search","backlink","templates","daily-notes"]
      .obsidian/community-plugins.json = ["obsidian-git","dataview"]

Folders (PARA), each with a one-line README.md explaining what lives there:
  KB/Projects/ KB/Areas/ KB/Knowledge/ KB/Goals/ KB/Daily/ KB/Archive/
  KB/_Admin/

Light frontmatter - use these FOUR fields on every note and overview, no more:
  title, status, tags, updated. (Keep it light. A fuller schema is a
  graduation step, not a day-one cost.)

Seed from my answers:
  - KB/Goals/goals.md            <- my Q1 business goal, as a short list
  - KB/Projects/<kebab-name>/project-overview.md  <- my Q2 project, with the
    4-field frontmatter (title, status: active, tags, updated) and sections:
    Overview / Current state / Next
  - KB/Areas/<area>.md           <- one per Q3 area
  - KB/Knowledge/ stays empty - it fills through use, never pre-filled
  - universe.md (repo root) - a LIVING map seeded from Q2/Q3/Q4: my
    repositories, the sites I run, the tools I use, the projects I'm on.
    Mark it clearly as living, not a one-shot snapshot: a header note saying
    it is nudged by /done when the world moves and reconciled in the weekly
    review. Use the universe.md template shape if one is present.

CLAUDE.md (repo root) - my operating rules:
  - Six primitives, one short section each: (1) Session pre-flight; (2) Branch
    check before every commit; (3) Live-state check - query the source, not
    memory; (4) Failure log - append after any failure; (5) Three-occurrence
    rule - 3x same root cause = write a rule here; (6) Infrastructure check -
    read "Available Infrastructure" before building anything new.
  - "Available Infrastructure" section - list my Q4 tools as stubs to wire up.
  - "The discipline" section, verbatim:
      * A session has a shape: /done to close, every time. As the rhythm
        earns them, /status to start and /idea as you go join in.
      * Once a week (the weekly review, about an hour): read the failure log,
        count root causes, write one rule if any cause hit three, tidy each
        project's Current state and Next, reconcile universe.md against
        reality, and ask /status what the week should be.
      * Once a month: step above the system - map it, diagram it, explain it -
        then refine it from that altitude. This Nexus should evolve to mirror
        MY internal model, not anyone else's.
      * The contract: this system gives back what I put in, with interest.
        Skipping the ritual doesn't pause the experiment - it ends it.
  - "How I want Claude to work" - my Q6 rules.

failure-log.md (repo root) - append-only. Header explains: record what
  happened and the root cause, in plain English (entry shape:
  "- **YYYY-MM-DD** | what happened. Root cause: best guess."), and that 3 of
  the same root cause = write a rule into CLAUDE.md. No categories - patterns
  and labels should emerge from MY entries over time, not be imposed up front.
  Seed ONE entry from my Q5 annoyance, framed as the first pattern to watch.

KB/_Admin/notes-index.md - empty index stub.

KB/_Admin/kb-style.md - how knowledge gets written here. Content, verbatim:
    * One topic per file, lowercase-kebab-case, in KB/Knowledge/<domain>/.
    * Write for the model AND the human: self-contained pages, plain
      markdown, no jargon that isn't defined on the page.
    * Lead with a 2-3 line summary; details after.
    * Link related pages liberally with vault-relative paths.
    * Distinguish RAW captures (transcripts, clips - save as-is, never edit)
      from COMPILED pages (synthesised knowledge - keep current, bump
      updated). When in doubt, save raw now, compile later.
    * Every new page gets one line in KB/_Admin/notes-index.md.
    * The KB grows through use - /done offers to capture durable knowledge
      at session close. Never bulk-import or pre-fill; stale knowledge is
      worse than absent knowledge.

Commands: three already exist in .claude/commands/ (done.md, status.md,
  idea.md). Leave them as-is - do NOT recreate them.

CONVENTIONS - keep these EXACT (they let my Nexus connect to my brother's
  later): lowercase-kebab-case filenames; 4-field frontmatter on every
  project-overview.md; the failure-log entry shape above (date | what
  happened | root cause); any future agent gets a contract block (inputs /
  outputs / constraints / forbidden).

Init git, commit "chore: bootstrap Nexus foundation". Then set up the GitHub
remote, handling sign-in explicitly because this is where people get stuck:
  1. Check GitHub auth FIRST: run `gh auth status`. If it is not signed in,
     stop and tell me to run `gh auth login` (GitHub.com, HTTPS, log in via
     browser), and wait until I confirm before continuing.
  2. Then create and push the private remote: `gh repo create <name>
     --private --source=. --push`. If `gh` is not installed, give me the
     manual steps.
  3. If a push fails with `permission denied` or an SSH-key error, that is a
     sign-in problem, not a code problem. Point me back to `gh auth login` (or
     setting up an SSH key) and retry. Do not move on until the push works.
A git-backed, remotely-stored KB is part of the deal: it is how version
control works, and later the basis for connecting to other operators' Nexus.

FINISH: summarise what you built in 5 lines, remind me that /done is the one
command I run on day one (and that /status and /idea graduate in once the
rhythm earns them), point me at the weekly review, then RUN /done so the
closing ritual is real from the first session.
```

## After setup

- **Day one:** run `/done` at the end of every session. That one habit keeps
  the rest alive.
- **Graduation:** once the daily rhythm is automatic, add `/status` at the
  start of a session and `/idea` in the middle. They are already copied in;
  use them when the rhythm has earned them.
- **Sharing what breaks:** the failure log is also the channel. Use
  [`/field-report`](./commands/field-report.md) to redact and share an entry
  with other operators.
- **The course:** [`learn/`](./learn/) walks through the why, the substrate,
  the KB and `universe.md`, the disciplines, and the arc.
- **Public repo:** <https://github.com/crowcreation/nexus>
