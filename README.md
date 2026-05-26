<p align="center">
  <img src="./images/hero-cover-1.png" alt="Nexus" width="100%" />
</p>

# Nexus

Operational coherence for persistent AI systems.

When AI becomes a long-running operator inside your repo -- Claude Code sessions, CLAUDE.md files, Git branches, accumulated automations -- a specific class of failures emerges. Not capability failures. Coherence failures: stale state, fragmented context, instructions that decay, lessons that don't stick. Nexus documents the patterns and gives you primitives to catch this before it compounds. These are field notes from active operations, not a fixed framework -- expect them to evolve as tooling matures.

**This is for** developers running persistent AI workflows -- Claude Code, Cursor, Aider, Copilot Workspace -- where state accumulates across sessions, instructions outlive the session that wrote them, and multiple agents operate on the same repo. **Not for** one-shot prompting or stateless AI interactions. Those have different failure modes.

**Start here:** paste [CLAUDE-lite.md](./templates/CLAUDE-lite.md) into any project ([gist](https://gist.github.com/crowcreation/1809ad9f1fddbf018113b8f1712dfadb)). Five rules, one failure log, no dependencies.

---

### Install the plugin

Nexus is a Claude Code plugin. Three primitives, everything local, nothing phones home.

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
- **Session pre-flight** -- verifies your branch, checks what changed, flags stale assumptions. Runs automatically.
- **Failure log** (`/failure`) -- structured drift categories. Three occurrences of the same root cause triggers an alert.
- **Branch verification** -- warns before committing on the wrong branch.
- **Field reports** (`/field-report`) -- formats log entries for [Discussions](https://github.com/crowcreation/nexus/discussions) with redaction prompts. Nothing sent automatically.

Privacy: no telemetry, no network calls, no data leaves your machine. [Full source](./.claude-plugin/).

**Requirements**: [Claude Code](https://claude.ai/code), Python 3.8+, Git.

---

### Go deeper

- [The Coherence Problem](./docs/the-coherence-problem.md) -- the full field guide: why persistent AI systems degrade and the five drift modes
- [Patterns](./patterns/) -- five steal-this patterns with implementation details
- [Templates](./templates/) -- CLAUDE.md starter, CLAUDE-lite, failure log template
- [Principles](./PRINCIPLES.md) -- twelve lines

---

### Share what breaks

The most useful thing you can contribute is a failure you actually hit.

[Discussions](https://github.com/crowcreation/nexus/discussions) · [Contributing](./CONTRIBUTING.md) · [License](./LICENSE)
