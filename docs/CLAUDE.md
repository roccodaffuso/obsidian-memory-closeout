# Claude Support

`obsidian-memory-closeout` is packaged as a standard `SKILL.md` directory, so the same installable skill folder can be used by Codex, Claude Code, and Claude custom skills.

## Claude Code

Claude Code discovers personal skills from:

```text
~/.claude/skills/<skill-name>/SKILL.md
```

Install this skill for Claude Code with:

```bash
git clone https://github.com/Nova1390/obsidian-memory-closeout.git
cd obsidian-memory-closeout
./scripts/install_claude.sh
```

This copies:

```text
skill/obsidian-memory-closeout/
```

to:

```text
~/.claude/skills/obsidian-memory-closeout/
```

You can also install it as a project-local Claude Code skill:

```bash
mkdir -p .claude/skills
cp -R skill/obsidian-memory-closeout .claude/skills/obsidian-memory-closeout
```

Then start Claude Code in that project and ask:

```text
Use the Obsidian Memory Closeout skill. Read relevant memory before work, then close out any durable memory changes.
```

## Claude.ai Custom Skills

Claude.ai custom skills can be uploaded as a ZIP containing the skill folder as the archive root.

Build the package:

```bash
python3 scripts/package_skill.py --root .
```

Upload:

```text
dist/obsidian-memory-closeout.zip
```

The ZIP contains:

```text
obsidian-memory-closeout/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
```

After upload, enable the skill in Claude's Skills settings and test with a prompt such as:

```text
Use my Obsidian memory closeout skill. Query memory before work, use retrieval signals when available, and write only curated durable updates.
```

## Compatibility Notes

- `SKILL.md` is the source instruction file.
- The directory name `obsidian-memory-closeout` is the command/skill identifier in Claude Code.
- `agents/openai.yaml` is included for Codex/OpenAI-compatible agents and is harmless for Claude.
- Scripts are optional helpers; the skill should still work as instructions when a host cannot run scripts.
- Vault-specific commands such as `brain_read.py`, `graph refresh`, `maintenance status`, or `retrieval eval` are examples of documented local capabilities, not hard requirements.

## Safety

Before publishing or uploading the skill package, run:

```bash
python3 scripts/validate_skill.py --root .
python3 skill/obsidian-memory-closeout/scripts/secret_scan.py .
python3 scripts/package_skill.py --root . --check
```

Review the package before enabling it in Claude, especially scripts and references.
