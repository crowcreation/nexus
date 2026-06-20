# Keeping Nexus updated

The plugin gets better over time. Unlike the paste layer (CLAUDE-lite and the
setup prompt, which you own outright once copied), an installed plugin can fall
behind its source. This is how you pull the latest version. Nothing here phones
home — updating is always something you do, never something that happens to you.

> First install is a different thing and lives elsewhere. The terminal install is
> in the [README](../README.md#going-further-the-plugin); the desktop, no-terminal
> install is in [Using Nexus in Cowork](./cowork-setup.md). This page is only
> about moving an already-installed plugin to a newer version.

## Am I behind?

At session start the pre-flight prints the installed version, for example
`Nexus plugin v0.7.0`. Compare it against the latest entry in
[CHANGELOG.md](../CHANGELOG.md). If yours is older, update with one of the routes
below. The check is deliberately offline — the plugin does not reach out to a
marketplace to compare, so this manual glance is the surface.

## Terminal (CLI)

Two steps, because refreshing the marketplace listing and reinstalling the plugin
are separate:

```
/plugin marketplace update
/plugin install nexus@nexus
```

The first pulls the latest marketplace metadata for `crowcreation/nexus`; the
second reinstalls the plugin at the version the marketplace now points to. Run
both. Updating the marketplace alone does not move an installed plugin.

## Desktop app (Cowork)

The desktop app has no `/plugin` command — it is CLI-only and does nothing in the
Chat, Cowork, or Code tabs. Plugins are managed through the **Customize panel**.

- Open the Customize panel and find the Nexus plugin under its plugins or
  marketplace section.
- If an update control is offered, use it.
- **If the plugin looks greyed out or stale, or an update control is missing,
  remove the plugin and re-add it.** A clean remove-and-re-add picks up the latest
  version. This is the reliable desktop refresh today.

Remember the desktop commands are namespaced: `nexus:done`, `nexus:status`,
`nexus:idea`, `nexus:failure`. After an update, type `/` and confirm they still
appear before relying on them.

## A note on the two layers

If update friction ever gets in your way, remember the discipline does not depend
on the plugin. The five patterns live in [CLAUDE-lite](../templates/CLAUDE-lite.md),
which you paste and own — it never goes stale on you because nothing of ours sits
in your repo. The plugin is the enforcement and graduation layer on top. Keep the
discipline in the paste layer; treat the plugin update as the cost of the
automation it buys you. See [STRUCTURE.md](../STRUCTURE.md#two-layers-two-sync-stories)
for the full trade-off.
