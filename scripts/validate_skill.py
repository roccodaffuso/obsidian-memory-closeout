#!/usr/bin/env python3
"""Validate the public skill package without external dependencies."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


SKILL_NAME = "obsidian-memory-closeout"
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
PRIVATE_PATH_PATTERNS = [
    re.compile("/" + "Users" + r"/[^/\s]+"),
    re.compile("/" + "home" + r"/[^/\s]+"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+"),
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
]
PUBLIC_SAFETY_PATTERNS = {
    "raw transcript marker": re.compile(r"(?m)^(User|Assistant|Human|Agent|System):\s+"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "openai key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    "github token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}"),
    "aws access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}
REQUIRED_ROOT_FILES = (
    "README.md",
    "PRIVACY.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "AGENTS.md",
    "LICENSE",
    "docs/GRAPHIFY.md",
    "docs/QUALITY_CHECKLIST.md",
    "docs/WEB_CLIPS.md",
    ".github/workflows/validate.yml",
)
REQUIRED_SKILL_FILES = (
    "SKILL.md",
    "LICENSE.txt",
    "agents/openai.yaml",
    "references/checked-memory-edits.md",
    "references/graphify.md",
    "references/memory-note-schema.md",
    "references/transcript-processing.md",
    "references/web-clips.md",
    "scripts/refresh_graphify.py",
    "scripts/secret_scan.py",
)


def parse_simple_yaml(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def validate_frontmatter_file(path: pathlib.Path, required_keys: tuple[str, ...]) -> str | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return f"{path} must start with YAML frontmatter"
    metadata = parse_simple_yaml(match.group("body"))
    for key in required_keys:
        if key not in metadata:
            return f"{path} frontmatter missing {key}"
    return None


def iter_public_text_files(root: pathlib.Path) -> list[pathlib.Path]:
    suffixes = {".md", ".txt", ".yaml", ".yml", ".py", ".sh"}
    skipped = {".git", "dist", "__pycache__"}
    files: list[pathlib.Path] = []
    for path in sorted(root.rglob("*")):
        if any(part in skipped for part in path.parts):
            continue
        if path.is_file() and (path.suffix.lower() in suffixes or path.name in {"LICENSE", ".gitignore"}):
            files.append(path)
    return files


def require_terms(root: pathlib.Path, rel: str, terms: tuple[str, ...]) -> int | None:
    text = (root / rel).read_text(encoding="utf-8").lower()
    for term in terms:
        if term.lower() not in text:
            return fail(f"{rel} missing required term: {term}")
    return None


def validate_public_safety(root: pathlib.Path) -> int | None:
    detector_files = {
        pathlib.Path("scripts/validate_skill.py"),
        pathlib.Path("skill/obsidian-memory-closeout/scripts/secret_scan.py"),
    }
    for path in iter_public_text_files(root):
        rel = path.relative_to(root)
        if rel in detector_files:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in PUBLIC_SAFETY_PATTERNS.items():
            if pattern.search(text):
                return fail(f"{rel} contains public-safety finding: {name}")
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    skill_dir = root / "skill" / SKILL_NAME
    skill_md = skill_dir / "SKILL.md"
    agents_yaml = skill_dir / "agents" / "openai.yaml"

    for rel in REQUIRED_ROOT_FILES:
        if not (root / rel).is_file():
            return fail(f"missing required repository file: {rel}")

    if not skill_md.is_file():
        return fail(f"missing {skill_md}")

    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return fail("SKILL.md must start with YAML frontmatter")

    metadata = parse_simple_yaml(match.group("body"))
    if metadata.get("name") != SKILL_NAME:
        return fail("SKILL.md frontmatter name does not match package name")
    if len(metadata.get("description", "")) < 80:
        return fail("SKILL.md description should be specific enough to trigger reliably")

    frontmatter_keys = set(parse_simple_yaml(match.group("body")).keys())
    if frontmatter_keys != {"name", "description"}:
        return fail("SKILL.md frontmatter should contain only name and description")

    for path in iter_public_text_files(root):
        file_text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in PRIVATE_PATH_PATTERNS:
            if pattern.search(file_text):
                rel = path.relative_to(root)
                return fail(f"{rel} contains private-looking text matching {pattern.pattern}")

    result = validate_public_safety(root)
    if result is not None:
        return result

    if not agents_yaml.is_file():
        return fail("missing agents/openai.yaml")
    agents_text = agents_yaml.read_text(encoding="utf-8")
    for required in ("display_name:", "short_description:", "default_prompt:"):
        if required not in agents_text:
            return fail(f"agents/openai.yaml missing {required}")

    referenced = re.findall(r"`(references/[^`]+|scripts/[^`]+)`", text)
    for rel in referenced:
        if not (skill_dir / rel).is_file():
            return fail(f"SKILL.md references missing file: {rel}")

    for rel in REQUIRED_SKILL_FILES:
        if not (skill_dir / rel).is_file():
            return fail(f"missing required file: {rel}")

    graphify_docs = (
        root / "README.md",
        root / "docs" / "GRAPHIFY.md",
        skill_dir / "references" / "graphify.md",
    )
    for path in graphify_docs:
        content = path.read_text(encoding="utf-8")
        if "Graphify" not in content or ".graphifyignore" not in content:
            return fail(f"{path.relative_to(root)} should document Graphify and .graphifyignore")

    operating_model_terms = ("Ingest", "Query", "Lint")
    for rel in (
        "README.md",
        "skill/obsidian-memory-closeout/SKILL.md",
        "docs/QUALITY_CHECKLIST.md",
        "examples/ingest-query-lint.md",
    ):
        result = require_terms(root, rel, operating_model_terms)
        if result is not None:
            return result

    result = require_terms(
        root,
        "skill/obsidian-memory-closeout/SKILL.md",
        (
            "Before Work / During Work / Closeout",
            "Before Work / Query",
            "During Work",
            "Closeout",
            "proactively decide",
            "Retrieval Signals",
            "retrieval packs",
            "brain_read.py",
            "operational input",
            "coverage is low or medium",
            "schema",
            "links",
            "privacy",
            "stale decisions",
            "coverage gaps",
        ),
    )
    if result is not None:
        return result

    retrieval_workflow_terms = (
        "Read Before Work",
        "Retrieval Signals",
        "ADD-only / Proposal-first",
        "Generated Surfaces",
        "Retrieval Evaluation",
        "Final Response Contract",
        "project state",
        "wikilink/direct link",
        "graph relation",
        "entity match",
        "keyword/BM25",
        "recency",
        "status",
        "confidence",
        "coverage",
        "archived",
        "superseded",
        "stale",
        "review-expired",
        "advisory",
        "source of truth",
        "no durable memory",
    )
    for rel in (
        "README.md",
        "skill/obsidian-memory-closeout/SKILL.md",
        "docs/QUALITY_CHECKLIST.md",
        "examples/retrieval-closeout.md",
    ):
        result = require_terms(root, rel, retrieval_workflow_terms)
        if result is not None:
            return result

    result = require_terms(
        root,
        "skill/obsidian-memory-closeout/SKILL.md",
        (
            "session summaries",
            "reference summaries",
            "decision proposals",
            "memory proposals",
            "Do not delete canonical memory",
            "replacement links",
            "Significant receipts must not remain orphaned",
            "Do not create read receipts for noisy micro-tasks",
            "dashboards, indexes, graph JSON/report, entity registry, retrieval evaluation, and audit ledger",
            "raw article text",
            "If evals fail, correct ranking",
            "Do not ignore failures",
        ),
    )
    if result is not None:
        return result

    result = require_terms(
        root,
        "examples/retrieval-closeout.md",
        (
            "brain_read.py \"<project>\"",
            "Coverage is medium",
            "Archived Notification Experiment",
            "Review-Expired Preference Draft",
            "memory proposal",
            "checkpoint commit",
            "Generated surfaces are not source of truth",
            "Forbidden as current truth",
            "Related updates",
        ),
    )
    if result is not None:
        return result

    checked_edit_terms = (
        "Checked Memory Edits",
        "Obsidian Markdown remains the canonical source of truth",
        "patch proposal",
        "Target content hash",
        "Append to an existing section",
        "Update one existing frontmatter field",
        "Add one wikilink to `Links`",
        "Excluded operations",
        "Safe apply",
    )
    for rel in (
        "skill/obsidian-memory-closeout/SKILL.md",
        "skill/obsidian-memory-closeout/references/checked-memory-edits.md",
    ):
        result = require_terms(root, rel, checked_edit_terms)
        if result is not None:
            return result

    result = require_terms(
        root,
        "docs/QUALITY_CHECKLIST.md",
        ("Checked memory edits", "patch proposals", "content hash freshness", "safe apply"),
    )
    if result is not None:
        return result

    result = require_terms(
        root,
        "README.md",
        (
            "Checked Memory Edits",
            "Obsidian Markdown remains the canonical source of truth",
            "patch proposal",
            "Allowed v1 operations",
            "whole-note replacements are excluded",
        ),
    )
    if result is not None:
        return result

    result = require_terms(
        root,
        "CONTRIBUTING.md",
        ("Update public documentation whenever behavior changes", "README.md", "docs/", "examples", "validation"),
    )
    if result is not None:
        return result

    result = require_terms(
        root,
        "skill/obsidian-memory-closeout/SKILL.md",
        (
            "Outcome Classification",
            "Status-only",
            "Significant review",
            "Durable memory update",
            "Read Receipt Closeout Rule",
            "process a significant review",
            "modify memory",
            "no durable memory",
            "Stage only files belonging to the closeout",
            "Consolidate repeated micro-receipts",
            "update the classifier or rules",
            "Do not leave significant read receipts untracked, uncommitted, or unlinked to a closeout",
        ),
    )
    if result is not None:
        return result

    automation_hygiene_terms = (
        "Automation Hygiene",
        "No-op automation runs are silent by default",
        "deterministic preflight gate",
        "Do not write ledgers for repetitive empty checks",
        "real work to process",
        "pending_count",
        "exit without side effects",
    )
    for rel in (
        "README.md",
        "skill/obsidian-memory-closeout/SKILL.md",
        "docs/QUALITY_CHECKLIST.md",
        "examples/automation-hygiene.md",
    ):
        result = require_terms(root, rel, automation_hygiene_terms)
        if result is not None:
            return result

    result = require_terms(
        root,
        "examples/automation-hygiene.md",
        (
            "Outcome Types",
            "Status-only",
            "Significant Review With No Durable Memory",
            "no durable memory",
            "Empty Scheduled Run",
            "Meaningful Scheduled Run",
            "Risky Edit Becomes Patch Proposal",
            "pending_count: 0",
            "Durable memory written",
            "Automation ledger",
            "target_hash",
            "append-to-existing-section",
        ),
    )
    if result is not None:
        return result

    maintenance_loop_terms = (
        "Optional Maintenance Loop",
        "maintenance status",
        "check",
        "graph refresh",
        "receipt audit",
        "Status non-mutating",
        "Repair/generated refresh",
        "Canonical modification",
        "Do not automatically modify project notes",
        "Git-backed",
        "protected deletions",
        "raw clips/cache",
        "Git conflicts",
        "possible secrets",
        "persistent runner",
        "controlled heartbeat",
    )
    for rel in (
        "README.md",
        "skill/obsidian-memory-closeout/SKILL.md",
        "docs/QUALITY_CHECKLIST.md",
        "examples/maintenance-loop.md",
    ):
        result = require_terms(root, rel, maintenance_loop_terms)
        if result is not None:
            return result

    result = require_terms(
        root,
        "docs/QUALITY_CHECKLIST.md",
        (
            "Significant read receipts",
            "no-durable-change marker",
            "checkpoint commits",
        ),
    )
    if result is not None:
        return result

    result = require_terms(
        root,
        "skill/obsidian-memory-closeout/SKILL.md",
        (
            "Derived Graph Outputs",
            "documented refresh command",
            "Do not invent graph/index commands",
            "verify they were regenerated",
            "not treat Graphify",
        ),
    )
    if result is not None:
        return result

    result = require_terms(
        root,
        "skill/obsidian-memory-closeout/SKILL.md",
        (
            "Safety and Deletion Guardrails",
            "Never perform mass deletion",
            "Never delete raw sources",
            "unexpected deletions are staged",
            "raw transcripts, caches, secrets, credentials, or unrelated files are staged",
        ),
    )
    if result is not None:
        return result

    web_clip_terms = (
        "00_Inbox/Web Clips/raw",
        "promotion criteria",
        "rejection criteria",
        "full article dump",
        "clear source URL",
    )
    for rel in (
        "README.md",
        "docs/WEB_CLIPS.md",
        "skill/obsidian-memory-closeout/references/web-clips.md",
        "examples/web-clip-review.md",
    ):
        result = require_terms(root, rel, web_clip_terms)
        if result is not None:
            return result

    result = require_terms(
        root,
        "skill/obsidian-memory-closeout/SKILL.md",
        (
            "Promote only durable summaries",
            "Leave ambiguous clips pending with a reason",
            "Do not commit full clipped articles",
        ),
    )
    if result is not None:
        return result

    example_memory_terms = (
        "Agent First Reads Existing Memory",
        "Relevant existing project note",
        "Relevant decision",
        "Relevant reference",
        "Relevant open loop",
        "Work Performed",
        "Session Closeout",
        "Only durable state is updated",
    )
    result = require_terms(root, "examples/before-after.md", example_memory_terms)
    if result is not None:
        return result

    result = require_terms(
        root,
        "examples/ingest-query-lint.md",
        ("Read receipt closeout", "Local checks", "Derived indexes", "Git status", "Checkpoint commit"),
    )
    if result is not None:
        return result

    result = require_terms(
        root,
        "CONTRIBUTING.md",
        (
            "public safety audit",
            "synthetic and privacy-safe",
            "Personal names",
            "private filesystem paths",
            "Raw transcript-like content",
            "committing sensitive memory",
        ),
    )
    if result is not None:
        return result

    for example in sorted((root / "examples").glob("*.md")):
        error = validate_frontmatter_file(
            example,
            ("id", "type", "status", "created", "updated", "confidence", "source", "tags"),
        )
        if error:
            return fail(error)

    print(f"validated {SKILL_NAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
