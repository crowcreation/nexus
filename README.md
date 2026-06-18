<p align="center">
  <img src="./images/hero-cover-1.png" alt="Nexus" width="100%" />
</p>

# Nexus

Operational coherence for persistent AI systems. When AI becomes a long-running operator inside your repo, a specific class of failures emerges: not capability failures, but coherence failures. Stale state, fragmented context, instructions that decay, lessons that don't stick. Nexus is an experimental, evolving field manual for catching this before it compounds.

**This is for** developers running persistent AI workflows (Claude Code, Cursor, Aider) where operational state survives across sessions, repositories evolve over time, and instructions outlive the conversation that created them. If your AI usage is mostly isolated conversations, many of these pathologies never emerge.

---

## Start here: the discipline

Two ways in, in order of commitment:

**1. The course.** [`learn/`](./learn/) is a short set of modules: why this exists, the substrate, the knowledge base and `universe.md`, the disciplines, and the arc. Read [Your First Hour](./learn/00-your-first-hour.md) first. It describes the five small things you set up on day one and the one command you actually run.

**2. CLAUDE-lite.** Paste [CLAUDE-lite.md](./templates/CLAUDE-lite.md) into any project ([gist](https://gist.github.com/crowcreation/1809ad9f1fddbf018113b8f1712dfadb)). Five rules, one failure log, no dependencies.

**3. The setup prompt.** [`setup-prompt.md`](./setup-prompt.md) interviews you, scaffolds a lean Nexus around your real work, seeds a living `universe.md`, and leaves you running `/done`.

## The disciplines

The whole system rests on one idea: discipline beats tooling. The habits are small.

- **The failure log.** When something goes wrong in your AI work, you write one plain-English line: what happened, and your best guess at the root cause. The single habit that compounds the most.
- **The session ritual.** A session has a shape: `/done` to close, every time. Two minutes to capture what happened, log anything that broke, and nudge your map if the world changed. As the rhythm earns them, `/status` joins at the start and `/idea` in the middle.
- **The three-occurrence rule.** One occurrence is an accident, two a coincidence, three a structural problem. When the same root cause shows up three times, you write a rule that prevents the next one.
- **The weekly review.** About an hour: read the failure log, count root causes, write a rule if any cause hit three, tidy each project's current state and next step, reconcile `universe.md`, and ask `/status` what the week should be.

The full treatment is in [The Disciplines](./learn/04-the-disciplines.md).

---

## Going further: the plugin

The plugin is the enforcement and graduation layer. Adopt it once the discipline is a habit. Three primitives, everything local, nothing phones home.

**1.** Add the marketplace (one-time):
```
/plugin marketplace add crowcreation/nexus
```

**2.** Install:
```
/plugin install nexus@nexus
```

**3.** In any project:
```
/nexus-init
```

**What you get:**
- **Session pre-flight** - verifies your branch, checks what changed, flags stale assumptions. Runs automatically.
- **Failure log** (`/failure`) - structured drift categories. Three occurrences of the same root cause triggers an alert.
- **Branch verification** - warns before committing on the wrong branch.
- **Universe mapping** (`/nexus-onboard`) - guided flow to document your repos, websites, tools, and projects as queryable AI context.
- **Field reports** (`/field-report`) - formats log entries for [Discussions](https://github.com/crowcreation/nexus/discussions) with redaction prompts. Nothing sent automatically.

Privacy: no telemetry, no network calls, no data leaves your machine. [Full source](./.claude-plugin/).

**Requirements**: [Claude Code](https://claude.ai/code), Python 3.8+, Git.

### Using Nexus in Cowork

Cowork (the desktop app) loads plugin commands, not the command files sitting in your project folder. So to get `/done`, `/status`, and `/idea` in Cowork, install the Nexus plugin:

1. Add the marketplace: `/plugin marketplace add crowcreation/nexus`
2. Install, or reinstall to update: `/plugin install nexus@nexus`
3. Point Cowork at your Nexus folder, type `/`, and you should see `done` in the list.

The plugin and Claude Code share the same plugin format, so the same commands work in both. If you have an older version installed, reinstall to pick up the latest.

---

## Go deeper

- [ROADMAP.md](./ROADMAP.md) - what's built today versus what's planned, honestly
- [The Coherence Problem](./docs/the-coherence-problem.md) - the full field guide: why persistent AI systems degrade and the five drift modes
- [The Operator Stack](./docs/the-operator-stack.md) - five layers, from substrate to shared intelligence
- [Patterns](./patterns/) - five steal-this patterns with implementation details
- [Templates](./templates/) - note and project templates, CLAUDE.md starter, CLAUDE-lite, failure log
- [Principles](./PRINCIPLES.md) - twelve lines

---

## Share what breaks

The most useful thing you can contribute is a failure you actually hit.

[Discussions](https://github.com/crowcreation/nexus/discussions) · [Contributing](./CONTRIBUTING.md) · [License](./LICENSE)
