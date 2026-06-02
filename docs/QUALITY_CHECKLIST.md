# Quality Checklist

Use this checklist when reviewing the repository or preparing a release.

## Skill Quality

- `SKILL.md` frontmatter contains only `name` and `description`.
- Description explains both what the skill does and when to use it.
- Runtime instructions are concise and action-oriented.
- Longer optional workflows live in `references/`.
- Every referenced file exists.
- Scripts are deterministic and have been run locally.
- Graphify guidance explains derived-index behavior and privacy boundaries.
- The skill treats memory as both input and output: Query before work, Ingest durable updates, and Lint quality before handoff.
- The skill has a generic Before Work / During Work / Closeout workflow.
- Derived graph/index refreshes are optional and use documented vault commands rather than hardcoded private setup.
- Web clip guidance treats `00_Inbox/Web Clips/raw` as unreviewed source material, not canonical memory.
- Significant read receipts must close the loop with a curated update, proposal, or explicit no-durable-change marker.
- Checked memory edits use direct writes only for low-risk updates and patch proposals for risky or review-worthy canonical changes.
- No-op automation runs are silent by default. Automation hygiene uses a deterministic preflight gate and launches only when there is real work to process. Do not write ledgers for repetitive empty checks.

## Repository Quality

- README has install, validate, package, usage, privacy, and license sections.
- `AGENTS.md` tells future agents how to avoid privacy mistakes.
- `CONTRIBUTING.md` and `SECURITY.md` exist.
- CI runs validation, secret scan, and packaging checks.
- Release documentation explains how to build and attach the package.
- Graphify setup and refresh behavior are documented in `docs/GRAPHIFY.md`.
- Web clip inbox review is documented in `docs/WEB_CLIPS.md`.
- README documents the `Ingest / Query / Lint` operating model with neutral placeholders.

## Privacy Quality

- No private vault content.
- No raw transcripts.
- No credentials or tokens.
- No personal absolute paths.
- Examples are synthetic.
- Lint guidance covers schema, links, privacy, stale decisions, duplication/noise, and coverage gaps.
- Raw web clips are ignored by Git/indexing by default and promoted only after review.
- Deletion and staging guardrails stop commits with unexpected deletions, raw transcripts, caches, secrets, or unrelated files.
- Verification guidance includes local checks, supported graph/index refresh, Git status inspection, focused staging, and checkpoint commits when appropriate.
- Patch proposals validate target existence, content hash freshness, required structure, and privacy before safe apply.
- Empty automation checks do not create durable no-op notes, read receipts, ledgers, commits, or user-visible thread summaries.
