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

**3.** In any project, bootstrap the KB-root foundations in one command:
```
/nexus-init
```
This ensures the root `failure-log.md`, the `KB/` PARA skeleton, and day-one hygiene files (`.gitignore`, `.env.example`). It is idempotent — it only creates what's missing and never overwrites. It is the one-command alternative to pasting the full setup prompt.

**What you get:**
- **Session pre-flight** - verifies your branch, checks what changed, flags stale assumptions. Runs automatically.
- **Failure log** (`/failure`) - appends to the same root `failure-log.md` that `/done` writes, so the three-occurrence rule sees every entry. Format-tolerant: matches the log shape you already use, categories optional.
- **Branch verification** - warns before committing on the wrong branch.
- **Foundations bootstrap** (`/nexus-init`) - one idempotent command to scaffold the KB-root structure.
- **Field reports** (`/field-report`) - formats log entries for [Discussions](https://github.com/crowcreation/nexus/discussions) with redaction prompts. Nothing sent automatically.

Privacy: no telemetry, no network calls, no data leaves your machine. [Full source](./.claude-plugin/).

**Requirements**: [Claude Code](https://claude.ai/code), Python 3.8+, Git.

**Keeping it current**: the plugin gets updates; an installed copy can fall behind. [Keeping Nexus updated](./docs/updating.md) covers the CLI and desktop routes. (The paste layer above never has this problem — you own your copy.)

### Using Nexus in Cowork

Cowork (the desktop app) loads plugin commands, not the command files sitting in your project folder, and the commands appear namespaced (`nexus:done`, `nexus:status`). The full desktop story — installing with no terminal, the namespaced commands, and refreshing a stale plugin — lives in one place: [Using Nexus in Cowork](./docs/cowork-setup.md).

---

## Go deeper

- [ROADMAP.md](./ROADMAP.md) - what's built today versus what's planned, honestly
- [STRUCTURE.md](./STRUCTURE.md) - the one structural shape, the coherence check that keeps the plugin honest with itself, and the two-layer sync trade-off
- [The Coherence Problem](./docs/the-coherence-problem.md) - the full field guide: why persistent AI systems degrade and the five drift modes
- [The Operator Stack](./docs/the-operator-stack.md) - five layers, from substrate to shared intelligence
- [Patterns](./patterns/) - five steal-this patterns with implementation details
- [Templates](./templates/) - note and project templates, CLAUDE.md starter, CLAUDE-lite, failure log
- [Principles](./PRINCIPLES.md) - twelve lines

---

## Share what breaks

The most useful thing you can contribute is a failure you actually hit.

[Discussions](https://github.com/crowcreation/nexus/discussions) · [Contributing](./CONTRIBUTING.md) · [License](./LICENSE)
