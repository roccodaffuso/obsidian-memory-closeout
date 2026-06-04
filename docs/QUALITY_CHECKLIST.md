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
- Read-before-work uses dashboard/index notes, retrieval packs, optional entrypoints such as `brain_read.py "<project>"`, and coverage warnings as operational input.
- Retrieval signals cover project state, wikilink/direct link, graph relation, entity match, keyword/BM25, recency, status, confidence, and coverage.
- Archived, superseded, stale, or review-expired notes are historical context, not current truth.
- ADD-only / Proposal-first behavior avoids aggressive canonical rewrites and uses proposals for delicate edits.
- Read Before Work, Retrieval Signals, ADD-only / Proposal-first, Generated Surfaces, Retrieval Evaluation, and Final Response Contract are documented.
- Retrieval signals are advisory and generated surfaces are not the source of truth.
- Derived graph/index refreshes are optional and use documented vault commands rather than hardcoded private setup.
- Web clip guidance treats `00_Inbox/Web Clips/raw` as unreviewed source material, not canonical memory.
- Significant read receipts must close the loop with a curated update, proposal, or explicit no-durable-change marker.
- Checked memory edits use direct writes only for low-risk updates and patch proposals for risky or review-worthy canonical changes.
- No-op automation runs are silent by default. Automation hygiene uses a deterministic preflight gate and launches only when there is real work to process. Do not write ledgers for repetitive empty checks.
- Workflow outcomes distinguish status-only checks, significant reviews, and durable memory updates.
- Automations exit without side effects when `pending_count` is `0`.
- Optional maintenance loops distinguish status non-mutating, repair/generated refresh, and canonical modification.
- Do not automatically modify project notes, decision notes, preference notes, or canonical references only because a maintenance check reports warnings.
- Maintenance capability examples such as `maintenance status`, `check`, `graph refresh`, and `receipt audit` remain optional vault-documented placeholders.

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
- Significant reviews close the loop with a curated update, proposal, or explicit `no durable memory` reason.
- Git-backed maintenance stops before commit on protected deletions, raw clips/cache, Git conflicts, possible secrets, or unrelated staged files.
- Automation maintenance prefers a persistent runner or controlled heartbeat instead of continuous visible no-op threads.
- Generated surfaces include dashboards, indexes, graph JSON/report, entity registry, retrieval evaluation, and audit ledger; canonical Markdown remains source of truth.
- Retrieval evals verify expected notes are recovered and stale or forbidden notes do not rank as current truth.
- Final response contract reports changes, checks, remaining work, related updates, and `no durable memory` when nothing changed.
