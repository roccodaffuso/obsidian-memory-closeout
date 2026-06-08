---
name: obsidian-memory-closeout
description: Query Obsidian memory before work and write privacy-safe closeouts, proposals, decisions, web clip reviews, automation hygiene, maintenance checks, retrieval evals, and generated refreshes.
---

# Obsidian Memory Closeout

## Principle

Memory is both input and output. Query relevant existing notes before acting, then write durable, curated updates into an Obsidian-compatible Markdown vault after useful work happens.

Do not wait for the user to explicitly ask for memory updates when durable information emerges and a vault path or memory contract is available. Proactively decide whether to update an existing note, write a curated note, create a decision, create a session summary, or leave a proposal.

Do not store raw transcripts, secrets, credentials, sensitive claims, unnecessary personal details, or noisy command logs. Prefer explicit notes, traceable sources, and small updates over archival dumps.

## Locate The Vault

Use the first available source:

1. A vault path explicitly provided by the user.
2. `OBSIDIAN_VAULT_PATH`, `MEMORY_VAULT_PATH`, or a similar environment variable.
3. The current working directory, if it looks like an Obsidian vault or memory repo.
4. Ask the user for the vault path when none can be inferred safely.

Before querying or writing, inspect local conventions: `AGENTS.md`, `.gitignore`, `.graphifyignore`, templates, and existing note structure.

## Before Work / During Work / Closeout

### Before Work / Query

Read Before Work is mandatory before meaningful work on an existing project, decision, preference, or open loop when relevant memory is available.

When a vault path or memory contract is available before meaningful work, read relevant existing memory before acting. Search or inspect:

- Dashboard or index notes for orientation and active areas.
- Retrieval packs or read sets when the vault exposes them.
- Project and area notes for current state, goals, constraints, and next actions.
- Decision notes for active choices, rejected alternatives, and revisit dates.
- Session notes for recent changes and unresolved open loops.
- Reference notes for reusable technical or domain context.
- Reviewed web clip proposals or inbox items, but not raw clipping dumps.
- Proposal notes when canonical memory placement is still unresolved.

If the vault documents an entrypoint such as `brain_read.py "<project>"`, use it as an optional read-before-work entrypoint, not as a required command.

Treat the read set as operational input, not background reading. Use it to constrain assumptions, choose next steps, and avoid repeating stale decisions.

Use the smallest useful context set. If no relevant memory exists, continue with the current task and note the coverage gap during linting. If coverage is low or medium, state uncertainty and inspect sources before assuming completeness.

### Retrieval Signals

When available, read and briefly report why retrieved notes are relevant. Generic signals include:

- Project state.
- Wikilink/direct link.
- Graph relation.
- Entity match.
- Keyword/BM25 match.
- Recency.
- Status.
- Confidence.
- Coverage.

Archived, superseded, stale, or review-expired notes are historical context, not current truth. Retrieval signals are advisory ranking evidence, not canonical memory.

### During Work

Track durable candidates as they emerge:

- Facts that will matter later.
- Decisions and rejected alternatives.
- Project state changes.
- Resolved or new open loops.
- Stable user/team preferences.
- Reusable references and source URLs.

Keep this as working context. Do not save noisy intermediate reasoning, raw transcripts, secrets, credentials, or unnecessary sensitive details.

### Closeout

At natural stopping points, write only curated durable summaries:

- Update existing notes when the canonical destination is clear.
- Create a decision note for a durable choice.
- Create a session summary for what changed.
- Create a project or area update for durable state.
- Create a reference note for reusable source material.
- Create a patch proposal when the canonical target note is clear but direct writing is risky or review-worthy.
- Leave a proposal when placement or confidence is unclear.

Then lint memory quality, run configured checks, and refresh documented derived indexes or graphs when available.

### ADD-only / Proposal-first

Default to adding curated memory instead of aggressively rewriting canonical notes.

- New observations become session summaries, reference summaries, decision proposals, memory proposals, or ledgers.
- Update canonical notes only when placement and content are clear.
- For delicate, stale-prone, concurrent, or review-worthy edits, create a patch/proposal instead of editing directly.
- Do not delete canonical memory. Use `archived`, `superseded`, or replacement links when memory is no longer current.

### Outcome Classification

Classify each memory workflow before writing:

- **Status-only**: preflight or review found no new input, durable change, or actionable blocker. Return a brief status only when requested. Do not create durable memory artifacts.
- **Significant review**: the agent read meaningful memory, reviewed inbox/source material, or investigated an open loop. Close the loop with a curated update, proposal, or explicit `no durable memory` reason.
- **Durable memory update**: project state, decisions, references, preferences, open loops, or canonical notes changed. Write the smallest useful curated update and verify it.

### Read Receipt Closeout Rule

Close the loop before the final response when you create a read receipt, process a significant review, or modify memory. The closeout must be one of:

- Session summary.
- Project/update note.
- Decision.
- Reference or proposal.
- Explicit `no durable memory` reason for status-only, read-only advisory, or tiny tasks.
- Explicit `no durable change` reason when the read receipt led to no durable update.
- Checkpoint commit when the repository or vault uses Git and meaningful files changed.

If memory files changed:

- Run local quality checks documented by the vault.
- Refresh generated indexes or graphs when supported.
- Inspect Git status before staging.
- Stage only files belonging to the closeout when unrelated user edits exist.
- Create a checkpoint commit when appropriate.

Consolidate repeated micro-receipts from the same work stream into one closeout note. If receipt classification is wrong for a repeated pattern, update the classifier or rules instead of only patching the individual receipt.

Do not create read receipts for noisy micro-tasks. Significant receipts must not remain orphaned.

### Automation Hygiene

For scheduled or background runs, preserve signal and avoid visible thread clutter.

- No-op automation runs are silent by default. If there is no new input, no durable change, and no actionable blocker, do not create a session note, read receipt, ledger, commit, or user-visible thread summary.
- A concise `no changes` result is acceptable, but do not store it as durable memory unless it resolves a real open loop.
- Every automation starts with a deterministic preflight gate before invoking the full agent workflow.
- Preflight should check `pending_count`, pending inputs, unreviewed source material, expected maintenance work, and actionable blockers.
- If `pending_count` is `0`, exit without side effects.
- Launch the full closeout workflow only when there is real work to process.
- If content is processed, produce curated, verifiable output. Never store raw transcripts, full logs, or copied source material.
- Write automation ledgers only for meaningful runs: promoted memory, archived or processed source material, canonical note changes, actionable blockers, or significant maintenance.
- Do not write ledgers for repetitive empty checks.

### Optional Maintenance Loop

If the vault documents health or maintenance capabilities, use them before and after a significant closeout. Treat names like `maintenance status`, `check`, `graph refresh`, and `receipt audit` as placeholder examples of vault-provided capabilities, not required commands.

Distinguish maintenance outcomes:

- **Status non-mutating**: inspect health, pending work, stale generated outputs, receipts, or blockers. Do not write notes, ledgers, commits, or threads for empty status.
- **Repair/generated refresh**: regenerate only derived surfaces such as indexes, graphs, reports, search data, or receipt audits. Canonical Markdown stays unchanged unless separately chosen.
- **Canonical modification**: project notes, decision notes, preference notes, and reference notes change. Keep this as a separate judged task with a closeout.

Maintenance rules:

- Do not automatically modify project notes, decision notes, preference notes, or canonical references only because a check reports warnings.
- If a read receipt or equivalent is written, close the loop before the final response with a session/project/decision/reference update, memory proposal, or explicit `no durable memory` reason.
- For Git-backed vaults, after curated memory changes run available checks, run available generated refreshes, inspect status, create a meaningful commit, and push when appropriate.
- Stop and report before committing if protected deletions, raw clips/cache, Git conflicts, possible secrets, or unrelated staged files appear.
- For automations, prefer a persistent runner or controlled heartbeat when available. Do not create continuous new visible threads for no-op checks.

## Operating Model

Follow this loop:

1. **Query existing memory**: read relevant notes, decisions, open loops, and references before work.
2. **Do the work**: use current task context plus retrieved memory.
3. **Ingest durable updates**: convert useful sources into curated notes.
4. **Lint memory quality**: validate that the vault remains useful, private, linked, current, and non-duplicative.

### Query

Query means reading relevant existing memory before acting. Prefer precise notes over broad folder scans. Capture any relevant constraints, decisions, open loops, stale assumptions, or missing coverage in the working context.

### Ingest

Ingest means converting useful sources into curated notes. Identify durable memory candidates: decisions, project state changes, resolved open loops, stable preferences, reusable references, and session summaries.

Exclude raw transcripts, secrets, credentials, private keys, tokens, full logs, and unnecessary sensitive details.

Choose the smallest useful write:

- Session summary.
- Decision note.
- Project or area update.
- Reference note.
- Memory proposal when canonical placement is unclear.

Use Obsidian links between related notes.

### Checked Memory Edits

Obsidian Markdown remains the canonical source of truth. Prefer direct edits only for small, obvious, low-risk canonical updates.

When the target note is clear but the edit is risky, concurrent, stale-prone, or review-worthy, create a patch proposal instead of editing directly. Read `references/checked-memory-edits.md`.

Patch proposal fields:

- `type` and `status`.
- Target note/path.
- Target content hash.
- Operation.
- `created`, `updated`, and `source`.
- Proposed change.

Allowed v1 operations:

- Append to an existing section.
- Update one existing frontmatter field.
- Add one wikilink to `Links`.

Excluded operations:

- Delete.
- Rename.
- Multi-file rewrite.
- Whole-note replacement.

Validate target existence, hash freshness, required section/frontmatter presence, and absence of secrets/raw transcripts. Safe apply only validated small patches and mark the proposal applied/closed.

Example CLI names such as `memory-patch validate` or `memory-patch apply` are placeholders, not required implementations.

### Web Clips

Browser and web clippings are unreviewed source material, not canonical memory. Use this generic inbox convention when the vault has no existing one:

```text
00_Inbox/Web Clips/raw/
```

Raw clips should be ignored by Git and indexing by default. Promote only durable summaries. Leave ambiguous clips pending with a reason. Do not commit full clipped articles unless the user explicitly wants that and copyright/privacy policy allows it. Read `references/web-clips.md` for promotion and rejection criteria.

If available, use a documented extraction tool to reduce clutter before summarizing; never store full raw article text as canonical memory.

### Lint

Lint means validating memory quality before handoff. Check:

- Schema: required frontmatter exists and matches local templates.
- Links: related notes are connected and broken links are avoided.
- Privacy: no raw transcripts, secrets, credentials, or unnecessary sensitive details.
- Web clips: raw clips are not treated as canonical notes and are excluded from Git/indexing when possible.
- Stale decisions: active decisions with revisit dates or outdated assumptions are called out.
- Duplication/noise: repeated, low-value, or overly broad notes are avoided.
- Coverage gaps: missing project state, open loops, or references are noted.

Run a privacy scan before commit or handoff. Use `scripts/secret_scan.py` if helpful. If the vault is a Git repo, checkpoint meaningful memory changes only after staging is reviewed.

## Transcript Handling

When given a transcript, chat log, meeting notes, audio transcript, or exported conversation:

- Extract durable facts and decisions only.
- Preserve source traceability at the summary level.
- Do not copy long raw passages.
- Split very long transcripts into chunks, then merge only stable outcomes.
- Mark uncertain claims with lower confidence.

Read `references/transcript-processing.md` for the detailed transcript workflow.

## Note Schema

Follow the vault's existing schema first. If none exists, use the generic schema in `references/memory-note-schema.md`.

Every canonical note should have enough metadata to answer:

- What type of memory is this?
- Where did it come from?
- How confident is it?
- When was it last updated?
- What notes does it connect to?

## Derived Graph Outputs

Some vaults maintain derived graph, search, or index artifacts. Markdown notes remain canonical.

- Run the vault's documented refresh command if one exists.
- Do not invent graph/index commands when the vault has no documented workflow.
- If derived outputs are expected, verify they were regenerated and include them in quality checks.
- Do not treat Graphify, any knowledge graph tool, or any private output path as mandatory for every vault.
- Treat dashboards, indexes, graph JSON/report, entity registry, retrieval evaluation, and audit ledger as generated surfaces.
- Do not index raw transcript folders, unreviewed web clips, caches, secrets, or private dumps unless the documented workflow explicitly allows it.
- Do not import raw transcript or raw article text into public or canonical generated surfaces.
- If generated surfaces conflict with canonical Markdown, treat canonical Markdown as the source of truth and report the mismatch.

Read `references/graphify.md` only when the vault documents Graphify or the user asks for it.

## Retrieval Evaluation

If the project has retrieval eval cases, run them after changes to ranking, read-before-work flow, retrieval packs, or generated retrieval surfaces.

Eval cases should check:

- The right notes are retrieved for representative tasks.
- Stale, archived, superseded, forbidden, or review-expired notes do not rank as current truth.
- Coverage, confidence, status, and recency signals are interpreted as advisory.

If evals fail, correct ranking, retrieval rules, or eval expectations. Do not ignore failures.

## Final Response Contract

At the end of each significant task, report:

- What changed.
- Which checks ran.
- What remains to do.
- Whether the public skill or related tools/projects should be updated.
- If nothing was updated, why there was `no durable memory`.

## Safety and Deletion Guardrails

- Never perform mass deletion of memory vault content.
- Never delete raw sources unless the vault's documented workflow explicitly says to archive or move them.
- Stop before committing if unexpected deletions are staged.
- Stop before committing if raw transcripts, caches, secrets, credentials, or unrelated files are staged.
- Report uncertain staging state instead of guessing.

## Failure Modes

- If the vault path is unknown, ask instead of guessing.
- If the write would require storing sensitive material, summarize at a safer abstraction or refuse that part.
- If a derived graph/index refresh is unavailable, leave notes updated and mention that derived outputs were not refreshed.
- If direct canonical writing is risky, create a memory proposal in the inbox or provide the proposal text to the user.
- Do not leave significant read receipts untracked, uncommitted, or unlinked to a closeout.
