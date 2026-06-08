---
id: example-web-clip-review
type: reference
status: complete
created: 2026-01-15
updated: 2026-01-15
confidence: high
source: synthetic-example
tags:
  - memory/example
  - workflow/web-clips
---

# Web Clip Inbox Review

This synthetic example shows how to review browser/web clippings without turning raw source dumps into canonical memory.

## Raw Inbox Item

```text
Path: 00_Inbox/Web Clips/raw/example-app-notification-patterns.md
Source URL: https://example.org/articles/notification-patterns
Context: Research for Project Alpha notification settings.
Content: Full copied article body omitted from canonical memory.
```

The raw clip is ignored by Git and indexing by default.

Recommended ignore entry:

```gitignore
00_Inbox/Web Clips/raw/
```

## Optional Extraction Step

If the vault documents an extraction tool such as Defuddle, the agent may use it as pre-processing to create cleaner source material before review. The extracted Markdown is still not canonical memory.

Example extracted summary:

```markdown
Source URL: https://example.org/articles/notification-patterns
Title: Notification Patterns For Example Apps
Extraction: cleaned Markdown summary, not a full article dump

- The source compares weekly summaries, daily alerts, and event-triggered notifications.
- It recommends clear defaults and user-controlled cadence for routine updates.
- It warns against making high-frequency alerts the default for low-urgency events.
```

The extracted summary helps review the source without committing raw article text.

## Review

Promotion criteria:

- Durable beyond the moment: yes, it affects notification design references.
- Clear source URL/context: yes, source URL and Project Alpha context are present.
- Privacy-safe: yes, no account data or secrets.
- Summarizable without full raw content: yes.
- Clear destination note: `06_References/Notification Patterns.md`.

Rejection criteria:

- Not one-off reading.
- Not saved as a full article dump.
- No private/account data.
- No secrets or credentials.
- Not a duplicate source.

## Promoted Note

```markdown
---
id: reference-notification-patterns
type: reference
status: active
created: 2026-01-15
updated: 2026-01-15
confidence: medium
source: https://example.org/articles/notification-patterns
tags:
  - memory/reference
  - project/project-alpha
---

# Notification Patterns

## Summary

The source describes notification settings patterns that favor user-controlled cadence and clear default behavior. For Project Alpha, it supports keeping weekly summaries as the default and considering daily alerts only as an opt-in.

## Source Context

- Source URL: https://example.org/articles/notification-patterns
- Review context: Example App notification settings research.

## Links

- [[Project Alpha]]
- [[Decision Notification Cadence]]
```

## What Was Not Saved

- Full article body.
- Raw browser clipping dump.
- Account-specific page data.
- Secrets, credentials, or private details.
