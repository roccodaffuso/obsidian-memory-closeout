---
id: example-retrieval-closeout
type: reference
status: complete
created: 2026-01-15
updated: 2026-01-15
confidence: high
source: synthetic-example
tags:
  - memory/example
  - workflow/read-before-work
  - workflow/retrieval-closeout
---

# Retrieval Closeout Workflow

This synthetic example shows read-before-work, retrieval signals, proposal-first updates, generated surfaces, retrieval evaluation, and final response contract behavior.

## Read Before Work

Request:

```text
Use /path/to/vault. Continue Project Alpha and inspect the current notification preference decision before changing behavior.
```

Optional entrypoint:

```text
brain_read.py "<project>"
```

Retrieved read set:

```text
Dashboard/index: Project Alpha active
Project note: current notification preference work is in review
Decision note: weekly summaries remain active
Reference note: notification defaults should be easy to override
Open loop: confirm whether daily alerts should be opt-in
Coverage: medium
```

Operational interpretation:

```text
Coverage is medium, so the agent states uncertainty and inspects source files before assuming the decision is complete.
```

## Retrieval Signals

```text
Project Alpha note: project state, wikilink/direct link, recency
Decision Notification Preference: entity match, status active, confidence high
Reference Notification Defaults: keyword/BM25, graph relation
Archived Notification Experiment: status archived, historical context only
Review-Expired Preference Draft: review expired, not current truth
Stale Preference Note: stale, historical context only
Coverage: medium
```

Signals explain why notes were retrieved. They are advisory ranking evidence, not canonical memory.

## ADD-only / Proposal-first

New observation:

```text
The code still exposes a daily alert toggle, but current memory says weekly summaries are the active default.
```

Correct memory output:

```markdown
---
id: proposal-2026-01-15-project-alpha-notification-toggle
type: memory-proposal
status: proposed
created: 2026-01-15
updated: 2026-01-15
confidence: medium
source: synthetic-agent-session
tags:
  - memory/proposal
  - project/project-alpha
---

# Project Alpha Notification Toggle Proposal

## Proposal

Review whether the daily alert toggle should remain available as opt-in while weekly summaries stay the default.

## Rationale

Existing memory says weekly summaries are active, but source inspection found a daily alert toggle.

## Links

- [[Project Alpha]]
- [[Decision Notification Preference]]
```

The agent does not rewrite the canonical decision note because placement and final content need review. It does not delete canonical memory; future replacement should use `archived`, `superseded`, or replacement links.

## Read Receipt Closeout

If a significant read receipt was created, it closes before final response:

```text
closeout: memory proposal created for Project Alpha notification toggle review.
checkpoint commit: appropriate if this vault is Git-backed and the proposal was written.
```

If no durable memory emerged:

```text
no durable memory: read set was inspected, source files matched current memory, and no project state, decision, reference, or preference changed.
```

## Generated Surfaces

After curated memory changes, regenerate documented generated surfaces when available:

```text
Dashboard: refreshed
Index: refreshed
Graph JSON/report: refreshed
Entity registry: refreshed
Retrieval evaluation: queued or run
Audit ledger: updated only for meaningful run
```

Generated surfaces are not source of truth when they conflict with canonical Markdown. Raw transcript and raw article text are not imported into public or canonical generated surfaces.

## Retrieval Evaluation

Eval case:

```text
Query: Project Alpha notification preference
Expected current notes: Project Alpha, Decision Notification Preference
Expected historical-only notes: Archived Notification Experiment
Forbidden as current truth: Review-Expired Preference Draft
```

If the eval fails, update ranking, retrieval rules, or eval expectations. Do not ignore the failure.

## Final Response Contract

```text
Changed: created one memory proposal for Project Alpha notification toggle review.
Checks: validation passed, secret scan passed, generated surfaces refreshed when documented.
Remaining: decide whether daily alerts remain opt-in.
Related updates: public skill or related tools/projects do not need changes.
Durable memory: proposal written; no raw transcript stored.
```
