# Using Nexus in Cowork

Cowork is the desktop app. You can run Nexus there instead of, or alongside, the terminal. This is the single source for the desktop story: how to install with no terminal, what the commands look like once installed, and how to refresh a stale plugin.

> Why this matters: running the discipline layer on top of Cowork is the point. Nexus is a harness that sits on Anthropic's own infrastructure rather than beside it. The terminal is the primary home today, but the desktop app is where an operator with no command line can still get the same rituals.

---

## What changes in the desktop app

Two things are different from the terminal:

- **Cowork loads plugin commands, not loose command files.** The `done.md`, `status.md`, and `idea.md` files copied into a project's `.claude/commands/` folder are invisible in Cowork. To get the commands in the desktop app, you install the Nexus plugin.
- **Commands appear namespaced.** Once the plugin is installed, the commands show up as `nexus:done`, `nexus:status`, `nexus:idea`, and `nexus:failure`, not as bare `/done`. They hit the same root structure (the root `failure-log.md`, the `KB/` folders) as the terminal commands do.

One thing that does not work in the desktop app:

- **`/plugin` is CLI-only.** The `/plugin` command (and `/plugin marketplace add`, `/plugin install`) works in the terminal. It does **not** work in the desktop Chat, Cowork, or Code tabs. In the desktop app, plugins are managed through the Customize panel, not by typing `/plugin`.

---

## Greenfield, no-terminal install

This is the path for an operator who has no terminal and no Git set up yet. The aim is to install and manage the plugin entirely through the desktop **Customize panel**.

> **[unverified — confirm in the clean dry-run]** The exact Customize click-path below has not yet been walked end-to-end on a clean machine. Treat the steps as the intended route, not a guarantee, until the greenfield rehearsal confirms them. Where a step is unconfirmed it is marked.

1. **Open the Customize panel** in the desktop app and find the plugin / marketplace section. **[unverified — confirm the exact menu label and location in the clean dry-run]**
2. **Add the Nexus marketplace.** This is the part that may not be possible from the GUI today. Field evidence from this week: the desktop Plugin Directory only searches the "Anthropic & Partners" catalogue plus marketplaces you have already added under "Personal", and a search for `crowcreation/nexus` returned **no match**. So a pure-GUI add of this third-party marketplace is **unconfirmed**. It may require a one-time terminal step first:
   ```
   /plugin marketplace add crowcreation/nexus
   ```
   run once in the CLI, after which the marketplace appears in the desktop Customize panel for install and updates. If you genuinely have no terminal, this is the current gap, and the clean dry-run is what will tell us whether a pure-desktop add is possible at all. We would rather say this plainly than promise a no-terminal add that does not yet exist.
3. **Install the plugin** from the Customize panel once the marketplace is visible. **[unverified — confirm the install button and confirmation in the clean dry-run]**
4. **Point Cowork at your Nexus folder.** Open the folder that holds your KB-root structure (the one with the root `failure-log.md` and the `KB/` folders).
5. **Check the commands appear.** Type `/` and look for `nexus:done` in the list. Running `nexus:done` should write to the same root `failure-log.md` and `KB/Daily/` that the terminal would.

### Refreshing a stale plugin

Desktop plugins do not auto-update, and the install can go stale or grey out. If a command stops appearing or looks greyed in Customize, **remove the plugin and re-add it** in the Customize panel. A reinstall picks up the latest version.

---

## Chris's own setup (the cockpit)

This is the maintainer's setup, useful as a worked example. Cowork runs as a desktop cockpit on top of a Nexus that is already CLI-primary:

- Point Cowork at the `knowledge-base-index` folder (the live Nexus).
- The same namespaced commands (`nexus:done`, `nexus:status`, `nexus:idea`, `nexus:failure`) are available in the desktop app.
- This gives one place to demo the plugin live to a new operator, the desktop view over a working Nexus, which pairs with the kickoff cockpit walkthrough.

The terminal stays primary; the desktop app is a window onto the same files, not a separate state.

---

## Quick reference

| Question | Answer |
|---|---|
| How do I install in the desktop app? | Through the Customize panel, not `/plugin`. A one-time CLI `/plugin marketplace add crowcreation/nexus` may be needed first (unconfirmed). |
| Why don't my `/done` files show up? | Cowork loads plugin commands, not loose `.claude/commands/` files. Install the plugin. |
| What are the commands called? | Namespaced: `nexus:done`, `nexus:status`, `nexus:idea`, `nexus:failure`. |
| Does `/plugin` work in Cowork? | No. `/plugin` is CLI-only. Use the Customize panel in the desktop app. |
| The plugin looks greyed or stale. | Remove it and re-add it in the Customize panel. |
