# Review Notes: Core Concepts Primer v1

This is a v1 draft for review. Nothing has been committed or pushed. These notes record the decisions made while assembling the primer, the diagram choices, gaps with no existing asset, and the source files used.

## 1. Diagram map

All diagrams were copied from `C:\Users\chris\OneDrive - CrowCreation\CC\Nexus\Nexus Diagrams\` into `learn/images/` with clean lowercase-kebab-case names. Modules reference the in-repo path only, never the OneDrive path.

| Module | Concept | Original diagram filename | Copied repo filename | Reason for choice |
|--------|---------|---------------------------|----------------------|-------------------|
| 01-why-and-vision.md | Vision / cockpit / "minimal or vast, same engine, your shape" | `frame-7-generated-per-operator.png` | `learn/images/generated-per-operator.png` | Named explicitly in the experiment memory as the cockpit/vision asset that "sells universe.md directly". Chose the cleaner `frame-7` variant over `5-generated-per-operator.png` per the prefer-frame guidance. |
| 02-the-substrate.md | Substrate / markdown / own your data | `frame-2-substrate-positioning.png` | `learn/images/substrate-positioning.png` | Direct match for the substrate-positioning concept. Chose the `frame-2` variant over the plain `2-` variant per the prefer-frame guidance. |
| 03-the-kb-and-universe.md | Memory / KB / universe.md | `frame-6-memory-view.png` | `learn/images/memory-view.png` | Best fit for the operating-memory layers (map, KB, daily/failure records). Chose the `frame-6` variant over `3-memory-view.png` / `4-memory-view.png`. |
| 04-the-disciplines.md | Operational discipline flywheel | `nexus operatioal discipline flywheel agnostic.png` | `learn/images/discipline-flywheel.png` | Matches the failure-to-rule flywheel described in the module. Chose the "agnostic" variant as the more generally framed of the two flywheel diagrams for a public, multi-operator audience. Original filename contains a typo ("operatioal"); corrected in the copied name. |
| 05-working-together.md | Connected operators (the vision, human-layer-first) | `frame-3-connected-operators.png` | `learn/images/connected-operators.png` | Best fit for connecting nexus points. Chose the `frame-3` variant over `5-` / `6-connected-operators.png` and `Nexus connectedpng.png`. |
| 06-the-arc.md | Evolution arc / destination | `frame-4-evolution-arc.png` | `learn/images/evolution-arc.png` | Best fit for the graduation arc framed as destination. Chose the `frame-4` variant over `6-` / `7-evolution-arc.png` and `Nexus evolution.png`. |
| 00-your-first-hour.md | (none) | none | none | No diagram embedded by choice. The quickstart should stay text-light and fast; a `Nexus set up.png` diagram exists but risks pulling graduation/scaffolding imagery into the day-one module. Flagged below as a decision for Chris. |
| README.md (index) | (none) | none | none | Index page, no diagram needed. |

## 2. Concepts with no existing asset

- **No gap forced a fabrication.** Every module's prose is drawn from existing source files, and every embedded diagram is a confirmed file from the live directory listing. No diagram or content was invented.
- `TODO:` The quickstart module (`00-your-first-hour.md`) has no embedded diagram. A `Nexus set up.png` asset exists, but it was not used to avoid bleeding scaffolding/graduation visuals into the deliberately tiny day-one module. If Chris wants a visual there, a purpose-made "five tiny things" diagram would fit better than any current asset. Not built, flagged here.

## 3. Decisions for Chris to confirm

1. **Module split.** Kept the suggested 6-module split (00 plus 01 to 06) exactly, with no deviation. No strong reason to merge or split further surfaced.
2. **Diagrams copied into the repo, not referenced by OneDrive path.** Per the prompt, all six chosen diagrams were copied into `learn/images/` and referenced by in-repo relative path so they survive publishing to GitHub. Confirm you are happy for these PNGs to live in the public repo (they are vision/positioning diagrams, not anything sensitive).
3. **"Agnostic" flywheel variant.** Chose `nexus operatioal discipline flywheel agnostic.png` over the non-agnostic version for a public multi-operator audience. Swap if you prefer the branded one.
4. **No diagram in the quickstart.** See the TODO above. Confirm whether you want a visual on day one or prefer it kept text-light.
5. **Cockpit placement.** Per the guardrail, the cockpit appears only in the arc (06) and the vision beat of 01. The vision beat in 01 uses the generated-per-operator cockpit diagram. Confirm this is the right single place for that image rather than the arc module.
6. **Tone.** Written plain, direct, UK English, no marketing language, no em-dashes or en-dashes in prose. The "AI operatives on the front line" and "scar tissue" framings are used as narrative, drawn from the converged design notes. Confirm the level of that framing feels right for Andy and Ranj.

## 4. Source files used

nexus-public repo:
- `README.md`
- `PRINCIPLES.md`
- `docs/the-coherence-problem.md`
- `docs/the-operator-stack.md`
- `patterns/session-pre-flight.md`
- `patterns/live-state-check.md`
- `patterns/three-occurrence-rule.md`
- `patterns/narrow-contract.md`
- `patterns/failure-log.md`
- `templates/CLAUDE-lite.md`
- `templates/failure-log.md`
- `templates/universe.md`
- `commands/field-report.md`

Starter kit (read-only, not written to):
- `nexus-starter-kit/setup-prompt.md`
- `nexus-starter-kit/commands/done.md`
- `nexus-starter-kit/README.md`

Experiment framing (read-only context, distilled and paraphrased, not reproduced verbatim; no private operational detail such as Fathom IDs, commercial JV framing, or CRM notes was carried into the public modules):
- `memory/project_nexus_ranj_andy_experiment.md`

## 5. Source files not found

All Step-1 files listed as "(if present)" were present:
- `patterns/failure-log.md` exists and was used.
- `commands/field-report.md` exists and was used.

No Step-1 source file was missing at read time.
