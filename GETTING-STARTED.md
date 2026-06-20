# Getting started

A greenfield setup, from an empty terminal to a running Nexus, in about ten minutes. This is the terminal path, which is the reliable one today. Prefer the desktop app? See [Using Nexus in Cowork](./docs/cowork-setup.md).

Everything here works the same on **macOS, Windows, and Linux**: the commands are identical. "Open a terminal" means Terminal on macOS or Linux, or PowerShell (or Windows Terminal) on Windows.

> Just want the discipline in an *existing* project, with no install and no new structure? Paste [CLAUDE-lite](./templates/CLAUDE-lite.md) instead. This guide is the full greenfield build.

## What you need first

- **Git** - version control ([install](https://git-scm.com/downloads)).
- **Claude Code** - the AI tool that runs in your terminal ([install](https://claude.ai/code)).
- A **GitHub account** - so your work is backed up ([sign up](https://github.com)).

## Steps

1. **Open a terminal.**

2. **Make a folder for your Nexus and go into it.**
   ```
   mkdir my-nexus
   cd my-nexus
   ```

3. **Turn it into a Git repository.**
   ```
   git init
   ```

4. **Start Claude Code.**
   ```
   claude
   ```

5. **Install the Nexus plugin** (this is what gives you the commands). Type these in the Claude session:
   ```
   /plugin marketplace add https://github.com/crowcreation/nexus
   /plugin install nexus@nexus
   ```

6. **Scaffold your Nexus.** Two ways, pick one:
   - **Quick (`/nexus-init`):** creates your `CLAUDE.md` (the operating rules), `failure-log.md`, the `KB/` folders, and the hygiene files. Idempotent and fast. You then add your goal and `universe.md` as you go (`/status` will prompt you).
   - **Guided (the setup prompt, recommended for a first Nexus):** instead of `/nexus-init`, paste the [setup prompt](./setup-prompt.md) and answer a few questions. It does everything `/nexus-init` does, and also interviews you to seed your goal and a living `universe.md` up front, so there is nothing to fill in afterwards.

7. **Back it up to GitHub.** Ask Claude: *"back this up to a new private GitHub repo"*. It will run the steps for you. The first time, it may ask you to sign in once with `gh auth login` (choose GitHub.com and log in through the browser).

8. **You are running.** From now on a session has a shape:
   - `/status` to start - what should I focus on?
   - `/idea` as you go - capture a thought.
   - `/done` to close - every time. Two minutes: what happened, what broke.

   Once a week, take about an hour for the weekly review: read your failure log, look for anything that has happened three times, and tidy your projects.

> The commands may show in the menu with a `nexus:` prefix (for example `nexus:done`). That is the same command.

## Where next

- [Your First Hour](./learn/00-your-first-hour.md) - what these five things are, and why.
- [The Disciplines](./learn/04-the-disciplines.md) - the habits that make it compound.
- [The course](./learn/) - the full picture.
