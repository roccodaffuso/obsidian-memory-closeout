# Web Clips And Inbox Review

Browser and web clippings are useful sources, but they are not canonical memory. Treat them as unreviewed inbox material until they are summarized, checked, and linked to a durable destination note.

## Folder Convention

When a vault has no existing convention, use:

```text
00_Inbox/Web Clips/raw/
```

Raw clips should be excluded from Git and derived indexes by default.

Recommended `.gitignore` and `.graphifyignore` entries:

```gitignore
00_Inbox/Web Clips/raw/
```

## Optional Extraction

If the vault documents a web extraction tool such as Defuddle, use it only as pre-processing to reduce page clutter before review. Clean extracted Markdown can make summarization easier, but it remains source material.

Do not treat extracted Markdown or raw article text as canonical memory. Promote only durable summaries with source URL, context, links, and a clear destination note.

## Promotion Criteria

Promote a web clip only when it:

- Is durable beyond the moment.
- Has a clear source URL and context.
- Is privacy-safe.
- Can be summarized without storing the full raw content.
- Has a clear destination note, such as a project, decision, reference, or proposal.

## Rejection Criteria

Reject or delete a raw clip when it is:

- One-off reading with no durable value.
- A full article dump.
- Private or account-specific data.
- A secret, credential, token, or key.
- A low-quality or duplicate source.

## Review Workflow

1. Inspect the raw clip only long enough to decide whether it has durable value.
2. Optionally run a documented extraction tool to remove navigation, ads, and page chrome.
3. Capture source URL, title, author or publisher when available, and retrieval context.
4. Summarize the reusable idea in your own words.
5. Link the summary to a destination note.
6. Remove or leave ignored the raw clip according to the vault's retention policy.
7. Lint for privacy, links, duplicates, and coverage gaps.

## Example

Raw source:

```text
00_Inbox/Web Clips/raw/example-app-notification-patterns.md
Source URL: https://example.org/articles/notification-patterns
Context: Research for Project Alpha notification settings.
```

Promoted destination:

```text
06_References/Notification Patterns.md
```

The promoted note should summarize durable guidance and link to `[[Project Alpha]]` or `[[Decision Notification Cadence]]`. It should not store the full article body.
