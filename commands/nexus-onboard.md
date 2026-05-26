---
description: "Guided interactive flow that maps your repos, websites, tools, projects, and goals into queryable markdown context."
allowed-tools: ["Bash", "Read", "Write", "Glob", "Grep", "WebFetch"]
argument-hint: "Optional: --resume to continue a previous session"
---

Map the operator's universe into `.nexus/universe.md` — repos, websites, tools, projects, goals, working rhythm, collaborators. Each step produces visible, useful output immediately. The operator can stop anytime and pick up later.

## Tone

You are a smart colleague sitting down with someone for the first time, asking "tell me about your setup." Be conversational, not procedural. After each answer, DO something visible — scrape, list, discover — and show what you found. The operator should feel "this is already useful" at every step.

Emotional arc: curiosity → recognition ("it found my repos!") → usefulness ("my AI now knows about my world") → invitation ("you can add more anytime").

## Step 0: Pre-flight

1. Check if `.nexus/` directory exists. If not:
   - Tell the operator: "I need the .nexus/ directory first. Run `/nexus-init` to set that up — takes 30 seconds — then come back here."
   - Stop. Do not proceed.

2. Check if `.nexus/universe.md` already exists. If it does:
   - Read the `completed_steps` from its YAML frontmatter.
   - Offer three choices: "You've already mapped [list completed steps]. Want to pick up where you left off, start fresh, or update what's there?"
   - If resuming, skip to the first incomplete step.

3. If no existing universe.md, proceed to Step 1.

## Step 1: Identity & Repositories

Ask: "What's your GitHub username? (I'll go find your repos.)"

Discovery:
- Run `gh auth status` to check if GitHub CLI is authenticated.
- If authenticated, run: `gh repo list <username> --json name,description,language,updatedAt,isPrivate,isFork,url --limit 100`
- Filter out forks by default.
- Sort by `updatedAt` descending.
- Present a summary: "Found N repos. Here are the most recently active:" with a table of the top 10.
- If `gh` is not installed or not authenticated, tell the operator: "I can't reach GitHub from here. No worries — tell me about your repos and I'll document them."

Ask follow-ups:
- "Which of these do you actively work in? Or should I include all non-fork repos?"
- "Any repos not on GitHub I should know about? (GitLab, Bitbucket, local-only?)"

Write to `.nexus/universe.md`:
- Create the file with YAML frontmatter (operator_handle, github_username, timestamps, nexus_version, completed_steps: [repositories]).
- Write `# My Universe` heading and `## Repositories` section with a markdown table.

Tell the operator: "Done — your AI now knows about your repos. Even if you stop here, that's useful context."

## Step 2: Websites & Domains

Ask: "What websites or domains do you operate? (I'll take a quick look at each one.)"

Discovery — for each domain provided:
- Try `WebFetch` on the homepage URL (prepend `https://` if not provided).
- Extract: page `<title>`, `<meta name="description">` content, `<meta name="generator">` (detects WordPress, Shopify, Next.js, etc.), any prominent `<h1>`.
- From HTTP response: note the platform if detectable.
- If WebFetch is unavailable, fall back to `curl -sIL <url>` via Bash for headers, then `curl -s <url> | head -200` for meta tags.
- If both fail (proxy, firewall, etc.), ask: "I couldn't reach that domain. Can you describe what it does in one sentence?"

Present findings: "hilltop-apartments.co.uk — WordPress site, 'Luxury serviced apartments in Newcastle' — looks like a hospitality business."

Ask the operator to confirm or correct each summary.

Append `## Websites` section to `.nexus/universe.md`. Update `completed_steps` to include `websites`.

Tell the operator: "Your AI now knows what each of your sites does. When you mention 'the Hilltop site' in any session, it has context."

## Step 3: Tools & Services

Ask: "What third-party tools and services do you use regularly? Think: CRM, email, hosting, analytics, accounting, design, communication."

Auto-detect first:
- Read `.mcp.json` if it exists — extract connected MCP server names.
- Run `gh auth status` — note GitHub connection.
- Check for `.env` or `.env.local` — list variable names only (NEVER echo values). Variable names like `HUBSPOT_API_KEY` or `VERCEL_TOKEN` reveal tool connections.
- Glob for `package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml` — scan dependency names for tool SDKs (e.g., `@hubspot/api-client`, `stripe`, `@vercel/sdk`).

Present: "Based on what I can see in this repo, you're connected to: [list]. What else do you use that isn't wired up here?"

Append `## Tools & Services` section to `.nexus/universe.md`. Include both detected and manually listed tools. Update `completed_steps` to include `tools`.

## Step 4: Active Projects & Goals

Ask: "What are you actively working on right now? Not a full project list — just the things that are live and would benefit from your AI knowing about them."

For each project, capture:
- Name
- One-line description
- Current status or phase (optional)
- Which repos and/or domains it touches

Then ask: "Any goals for the next quarter that would help your AI prioritise?"

Append `## Active Projects` and `## Goals` sections to `.nexus/universe.md`. Update `completed_steps` to include `projects`.

## Step 5: Working Rhythm (optional)

Ask: "Want to tell me about your typical week? This helps your AI understand timing — like 'Mondays are for client calls, Fridays are deep work.' Totally optional."

If the operator wants to skip: "No problem — you can add this anytime by editing `.nexus/universe.md` directly."

If they share: append `## Working Rhythm` section. Keep it structured — days of week or time blocks.

Update `completed_steps` to include `rhythm` if provided.

## Step 6: Collaborators (optional)

Ask: "Who do you work with regularly? Names, roles, how they connect to your projects. Only what would help your AI understand context like 'ask Sarah about the design' or 'cc James on property emails.' Also optional."

If the operator wants to skip: acknowledge and move on.

Append `## Collaborators` section if provided. Update `completed_steps` to include `collaborators`.

## Step 7: Finalise

1. Read the complete `.nexus/universe.md` and present a summary to the operator — counts of repos, websites, tools, projects.

2. Generate the compact CLAUDE.md summary block. Format:

```markdown
## My Universe

<!-- Generated by /nexus-onboard. Full detail: .nexus/universe.md -->

**Operator**: [handle] (GitHub: [username])
**Repos**: [N] active ([top languages]) — see .nexus/universe.md
**Websites**: [domain1] ([purpose]), [domain2] ([purpose])
**Key tools**: [top 4-5 tools]
**Active projects**: [project names]
**Working rhythm**: [one-line summary, if provided]

For full detail: `Read .nexus/universe.md`
```

3. Check if CLAUDE.md exists in the project root:
   - If it exists and already has `## My Universe`: ask whether to update it.
   - If it exists without that section: append the summary block at the end.
   - If CLAUDE.md doesn't exist: create one with just the summary block.

4. Print closing message:

```
Your universe is mapped:
  .nexus/universe.md  — full detail (committable, editable)
  CLAUDE.md           — compact summary (loaded every session)

Your AI now knows about [N] repos, [N] websites, [N] tools, and [N] active projects.

To update anytime: edit .nexus/universe.md directly, or run /nexus-onboard --resume.
```

## Universe File Format

The `.nexus/universe.md` file uses this structure. YAML frontmatter fields and markdown heading anchors are stable — do not rename them.

```yaml
---
operator_handle: ""
github_username: ""
generated: "YYYY-MM-DDTHH:MM:SSZ"
last_updated: "YYYY-MM-DDTHH:MM:SSZ"
nexus_version: "0.4.0"
completed_steps: []
---
```

Heading anchors: `# My Universe`, `## Repositories`, `## Websites`, `## Tools & Services`, `## Active Projects`, `## Goals`, `## Working Rhythm`, `## Collaborators`.

Use markdown tables with consistent column headers as defined in the template at `templates/universe.md`.

## Graceful Degradation

- `gh` CLI not installed or not authenticated → ask operator to list repos manually
- `WebFetch` unavailable → fall back to `curl -sIL` + `curl -s | head -200` via Bash
- `curl` also fails → ask operator to describe each site in one sentence
- CLAUDE.md doesn't exist → create one with the summary block
- Zero repos or zero websites → handle gracefully: "Nothing found, but you can add them later by editing the file."
- Operator stops mid-flow → file is valid with whatever steps completed; resumable via `/nexus-onboard --resume`
