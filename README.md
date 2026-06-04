# Obsidian Memory Closeout

![Obsidian Memory Closeout social preview](assets/social-preview.png)

[![Validate](https://github.com/Nova1390/obsidian-memory-closeout/actions/workflows/validate.yml/badge.svg)](https://github.com/Nova1390/obsidian-memory-closeout/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Turn meaningful work into curated Obsidian memory, and read that memory before acting.

`obsidian-memory-closeout` is a privacy-first skill for using an Obsidian-compatible vault as both input and output. It helps agents query existing memory before work, ingest durable updates afterward, and keep the vault useful without storing raw transcripts, secrets, credentials, or noisy logs.

## What It Does

- Queries relevant existing notes, decisions, open loops, and references before work.
- Uses retrieval signals and coverage warnings to make read-before-work more reliable.
- Ingests durable updates from a session, transcript, web clip, or completed task.
- Writes concise session summaries, decisions, project updates, references, or inbox proposals.
- Lints memory quality for schema, links, privacy, stale decisions, duplication, noise, and coverage gaps.
- Reviews web clips as unreviewed inbox material before promoting them into canonical notes.
- Distinguishes status-only checks, significant reviews, and durable memory updates.
- Uses checked patch proposals when a canonical memory edit is clear but direct writing is risky or review-worthy.
- Keeps scheduled automation runs quiet when there is no real memory work to process.
- Supports optional vault maintenance loops for health checks and generated refreshes.
- Evaluates retrieval changes when a vault provides eval cases.
- Works as a standard `SKILL.md` package for Codex, Claude Code, and Claude custom skills.
- Finds or asks for the target Obsidian vault and follows existing vault conventions first.
- Runs a local secret scan before committing or handing off.
- Refreshes Graphify or other derived indexes without treating them as the source of truth.

## What's New In v0.3.1

- Claude support: installable in Claude Code at `~/.claude/skills/obsidian-memory-closeout/SKILL.md`.
- Claude.ai custom skill support via `dist/obsidian-memory-closeout.zip`.
- Claude-compatible skill metadata with a concise `description` under the custom skill limit.
- Claude install docs, release notes, validation coverage, and `scripts/install_claude.sh`.
- Retrieval-aware read-before-work: agents treat read sets as operational input and use coverage warnings before assuming completeness.
- Retrieval signals: project state, wikilinks, graph relations, entity matches, keyword/BM25, recency, status, confidence, and coverage.
- Proposal-first memory updates, read receipt closeouts, automation hygiene, maintenance loops, generated surfaces, and retrieval eval guidance.

## Checked Memory Edits

Obsidian Markdown remains the canonical source of truth. Direct edits are best for small, obvious, low-risk canonical updates.

When the target note is clear but the edit is risky, concurrent, stale-prone, or review-worthy, the skill uses a patch proposal instead of editing directly. Patch proposals include the target note/path, target content hash, operation, metadata, and proposed change.

Allowed v1 operations are intentionally small: append to an existing section, update one existing frontmatter field, or add one wikilink to `Links`. Deletions, renames, multi-file rewrites, and whole-note replacements are excluded. See [skill/obsidian-memory-closeout/references/checked-memory-edits.md](skill/obsidian-memory-closeout/references/checked-memory-edits.md).

## Automation Hygiene

Scheduled memory automations should preserve signal. No-op automation runs are silent by default: when there is no new input, durable change, or actionable blocker, the run should not create a session note, read receipt, ledger, commit, or visible thread summary.

Every automation should start with a deterministic preflight gate. If `pending_count` is `0`, exit without side effects and report only a brief status if requested. If the host app creates a visible conversation for every scheduled run, use this preflight gate before invoking the full closeout workflow.

Only launch when there is real work to process. Meaningful runs can write ledgers for promoted memory, processed source material, canonical note changes, actionable blockers, or significant maintenance. Do not write ledgers for repetitive empty checks.

Read receipts, significant reviews, and memory edits must close the loop before the final response. Valid closeouts are a session summary, project/update note, decision, reference/proposal, or explicit `no durable memory` reason. See [examples/automation-hygiene.md](examples/automation-hygiene.md).

## Workflow Outcomes

- **Status-only**: a preflight or review found nothing new or durable. Return a short status only when requested; do not create notes, ledgers, commits, threads, or read receipts.
- **Significant review**: memory or inbox material was meaningfully reviewed. Close with a curated update, proposal, or `no durable memory` reason.
- **Durable memory update**: canonical notes changed. Run local checks, refresh documented indexes/graphs when supported, inspect Git status, and checkpoint meaningful changes.

## Read Before Work And Retrieval

Before meaningful work on an existing project, decision, preference, or open loop, read relevant memory first. Use dashboard/index notes, retrieval packs, project notes, decision notes, references, open loops, and optional entrypoints such as `brain_read.py "<project>"` when the vault documents them.

Treat the read set as operational input. If coverage is low or medium, state uncertainty and inspect sources before assuming completeness.

When available, briefly report retrieval signals that explain relevance: project state, wikilink/direct link, graph relation, entity match, keyword/BM25, recency, status, confidence, and coverage. Archived, superseded, stale, or review-expired notes are historical context, not current truth. Signals are advisory, not canonical memory.

## ADD-only / Proposal-first

Default to adding curated memory instead of aggressively rewriting canonical notes. New observations should become session summaries, reference summaries, decision proposals, memory proposals, or ledgers.

Update canonical notes only when placement and content are clear. For delicate or review-worthy edits, create a patch/proposal instead of editing directly. Do not delete canonical memory; use `archived`, `superseded`, or replacement links.

## Optional Maintenance Loop

Some vaults expose health or maintenance capabilities. Treat names like `maintenance status`, `check`, `graph refresh`, and `receipt audit` as placeholder examples of vault-provided capabilities, not required commands.

For significant closeouts, run documented health or maintenance checks before and after the curated update when available. Keep the outcomes separate:

- **Status non-mutating**: inspect health, pending work, stale generated outputs, receipts, or blockers without writing notes, ledgers, commits, or threads for empty status.
- **Repair/generated refresh**: regenerate only derived surfaces such as indexes, graphs, reports, search data, or receipt audits.
- **Canonical modification**: update project notes, decision notes, preference notes, or references only as a separate judged task.

Do not automatically modify project notes, decision notes, preference notes, or canonical references only because a check reports warnings. For Git-backed vaults, after curated memory changes run available checks, run available generated refreshes, inspect status, create a meaningful commit, and push when appropriate. Stop before committing if protected deletions, raw clips/cache, Git conflicts, possible secrets, or unrelated staged files appear.

For automations, prefer a persistent runner or controlled heartbeat when available, and avoid continuous new visible threads for no-op checks. See [examples/maintenance-loop.md](examples/maintenance-loop.md).

## Generated Surfaces And Retrieval Eval

Dashboards, indexes, graph JSON/report, entity registry, retrieval evaluation, and audit ledger are generated surfaces. Regenerate them after curated changes when the vault documents that workflow, but do not treat them as source of truth if they conflict with canonical Markdown.

Do not import raw transcript or raw article text into public or canonical generated surfaces. If retrieval eval cases exist, run them after changes to ranking or read flow. Evals should verify that the right notes are retrieved and that stale, forbidden, or review-expired notes do not rank as current truth.

## Final Response Contract

At the end of a significant task, report what changed, which checks ran, what remains to do, whether the public skill or related tools/projects should be updated, and why there was `no durable memory` if nothing was updated.

## Why This Exists

Raw transcripts are bad long-term memory. They are noisy, often mix durable decisions with drafting chatter, and can accidentally contain secrets or sensitive details. They are also hard to maintain because context, uncertainty, and outdated statements are difficult to separate later.

Memory also needs to be queried before work. A vault that is only written after the fact becomes an archive. A useful memory vault should inform the next action by surfacing project state, decisions, open loops, and references before the agent acts.

This skill prefers curated closeouts: decisions, session summaries, project updates, references, and proposals that preserve useful context without storing unnecessary raw material.

## Ingest / Query / Lint

The skill follows a compact operating model for LLM-readable memory vaults:

1. **Query**: read relevant notes, decisions, open loops, and references before acting.
2. **Work**: use current task context plus retrieved memory.
3. **Ingest**: convert useful sources into curated notes such as decisions, session summaries, project updates, references, or proposals.
4. **Lint**: check schema, links, privacy, stale decisions, duplicated or noisy notes, and coverage gaps.

Definitions:

- **Query**: read relevant existing memory before work.
- **Ingest**: convert useful sources into curated Obsidian notes.
- **Lint**: validate that memory remains useful, private, linked, current, and non-duplicative.

## Web Clips And Inbox Review

Browser and web clippings are source material, not canonical memory. A generic inbox convention is:

```text
00_Inbox/Web Clips/raw/
```

Raw clips should be ignored by Git and indexing by default, then reviewed for promotion into curated notes. Promote a clip only when it is durable beyond the moment, has a clear source URL/context, is privacy-safe, can be summarized without storing the full raw content, and has a clear destination note. Reject one-off reading, full article dumps, private/account data, secrets or credentials, and low-quality or duplicate sources.

Promotion criteria: durable beyond the moment, clear source URL/context, privacy-safe, summarizable without full raw content, and clear destination note.

Rejection criteria: one-off reading, full article dumps, private/account data, secrets or credentials, and low-quality or duplicate sources.

See [docs/WEB_CLIPS.md](docs/WEB_CLIPS.md) and [examples/web-clip-review.md](examples/web-clip-review.md).

## Derived Indexes And Graphify

Markdown notes remain the source of truth. Graphify or other derived indexes can be refreshed after curated notes are written, but generated graph data should not replace canonical notes.

When using Graphify, keep `.graphifyignore` privacy-aware and avoid indexing raw transcripts, private dumps, caches, and unreviewed web clips. See [docs/GRAPHIFY.md](docs/GRAPHIFY.md).

## Repository Layout

```text
.
├── skill/obsidian-memory-closeout/    # Installable agent skill package
├── examples/                          # Synthetic, privacy-safe examples
├── assets/                            # Public repository images
├── docs/                              # Claude, Graphify, web clip, release, and quality docs
├── scripts/                           # Install, validation, and packaging helpers
├── .github/workflows/validate.yml      # CI validation workflow
├── AGENTS.md                          # Guidance for agents editing this repo
├── CONTRIBUTING.md                    # Contribution and public-safety rules
├── PRIVACY.md                         # Privacy model and boundaries
├── SECURITY.md                        # Security reporting policy
├── LICENSE                            # MIT license
└── README.md
```

## Install

### Option A: Codex Skill Installer

Ask Codex to install the skill from this GitHub directory:

```text
$skill-installer install https://github.com/Nova1390/obsidian-memory-closeout/tree/main/skill/obsidian-memory-closeout
```

Restart Codex after installation so the skill is discovered.

### Option B: Local Clone

Clone the repository, then install the skill into your local Codex skills directory:

```bash
git clone https://github.com/Nova1390/obsidian-memory-closeout.git
cd obsidian-memory-closeout
./scripts/install_local.sh
```

By default, the installer copies the skill to:

```text
~/.codex/skills/obsidian-memory-closeout
```

To install somewhere else:

```bash
CODEX_HOME=/path/to/codex ./scripts/install_local.sh
```

### Option C: Claude Code

Clone the repository, then install the same skill folder into your Claude Code skills directory:

```bash
git clone https://github.com/Nova1390/obsidian-memory-closeout.git
cd obsidian-memory-closeout
./scripts/install_claude.sh
```

By default, the installer copies the skill to:

```text
~/.claude/skills/obsidian-memory-closeout
```

To install somewhere else:

```bash
CLAUDE_HOME=/path/to/claude ./scripts/install_claude.sh
```

For project-local Claude Code use, copy the skill folder to:

```text
.claude/skills/obsidian-memory-closeout
```

See [docs/CLAUDE.md](docs/CLAUDE.md).

### Option D: Claude.ai Custom Skill

Build a ZIP package:

```bash
python3 scripts/package_skill.py --root .
```

Upload `dist/obsidian-memory-closeout.zip` in Claude's custom Skills settings. The ZIP contains the `obsidian-memory-closeout/` skill folder at archive root, which is the structure Claude expects.

### Option E: Manual Copy

Copy the installable skill folder to your Codex skills directory:

```bash
cp -R skill/obsidian-memory-closeout ~/.codex/skills/obsidian-memory-closeout
```

For Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R skill/obsidian-memory-closeout ~/.claude/skills/obsidian-memory-closeout
```

Restart Codex after copying. Claude Code detects edits to existing skill folders during a session, but starting a fresh session is the simplest verification path.

## Graphify Integration

Graphify support is optional and privacy-aware. The skill integrates with [safishamsi/graphify](https://github.com/safishamsi/graphify), treating Markdown notes as the source of truth and Graphify output as a derived index that can be refreshed after curated notes are written.

When `graphify` is installed, agents can run the bundled helper from the installed skill folder. For Codex:

```bash
python3 ~/.codex/skills/obsidian-memory-closeout/scripts/refresh_graphify.py /path/to/vault
```

For Claude Code:

```bash
python3 ~/.claude/skills/obsidian-memory-closeout/scripts/refresh_graphify.py /path/to/vault
```

Use `--html` if you also want a visual graph artifact:

```bash
python3 /path/to/installed/obsidian-memory-closeout/scripts/refresh_graphify.py /path/to/vault --html
```

The skill checks `.graphifyignore` before treating a vault as ready for indexing and should avoid indexing raw transcripts, private dumps, cache folders, and other sensitive source material. See [docs/GRAPHIFY.md](docs/GRAPHIFY.md) for setup, expected outputs, and privacy guardrails.

## Package

Create a distributable zip in `dist/` for Claude custom skills or manual distribution:

```bash
python3 scripts/package_skill.py
```

The package contains only the installable skill folder, not the repository docs or examples.

## Validate

Run the same checks used by CI:

```bash
python3 scripts/validate_skill.py --root .
python3 skill/obsidian-memory-closeout/scripts/secret_scan.py .
python3 scripts/package_skill.py --root . --check
```

The validation checks that:

- `SKILL.md` has valid frontmatter.
- `agents/openai.yaml` exists and matches the skill metadata shape.
- Referenced files exist.
- Graphify runtime guidance is packaged with the skill.
- Claude install and packaging guidance is documented.
- Checked memory edit guidance is packaged with the skill.
- Automation hygiene and workflow outcome guidance are covered.
- Optional maintenance loop guidance is covered.
- Read-before-work, retrieval signals, generated surfaces, retrieval eval, and final response contract guidance are covered.
- Sanitized examples contain expected frontmatter.
- Packaging produces a zip with the expected skill files.
- The repository does not contain common secret-like patterns.

## Usage Prompt

After installing in Codex, ask:

```text
Create a curated memory closeout for this session in my Obsidian vault.
```

In Claude Code or Claude.ai, use the same intent:

```text
Use the Obsidian Memory Closeout skill. Query relevant memory before work, then write only curated durable updates.
```

For before-work memory lookup:

```text
Use /path/to/vault. Before working on Project Alpha, query relevant memory notes, decisions, open loops, and references. After the work, ingest durable updates and lint memory quality.
```

You can also provide a vault path explicitly:

```text
Use /path/to/vault and create a memory closeout for this transcript.
```

## Examples

See [examples/before-after.md](examples/before-after.md) for a minimal synthetic before/after showing how a noisy AI session input becomes curated Obsidian notes without storing the raw transcript.

See [examples/ingest-query-lint.md](examples/ingest-query-lint.md) for the full generic workflow: query existing memory, do the work, ingest durable updates, then lint memory quality.

See [examples/automation-hygiene.md](examples/automation-hygiene.md) for scheduled run behavior: silent empty checks, meaningful closeouts with ledgers, and risky edits converted into patch proposals.

See [examples/maintenance-loop.md](examples/maintenance-loop.md) for optional vault health checks, generated refreshes, and canonical-change guardrails.

See [examples/retrieval-closeout.md](examples/retrieval-closeout.md) for read-before-work, retrieval signals, proposal-first updates, and final response contract behavior.

## Privacy

This repository does not include private vault content. The included examples are synthetic and sanitized. See [PRIVACY.md](PRIVACY.md) for the intended privacy boundaries and review checklist.

## Contributing

Issues and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and keep all examples synthetic. Security or privacy concerns should follow [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
