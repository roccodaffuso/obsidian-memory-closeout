# Releasing

This repository can publish releases manually using the generated skill zip. The same zip can be uploaded as a Claude.ai custom skill because it contains the `obsidian-memory-closeout/` skill folder at archive root.

## Prepare

1. Update docs or examples as needed.
2. Run validation:

   ```bash
   python3 scripts/validate_skill.py --root .
   python3 skill/obsidian-memory-closeout/scripts/secret_scan.py .
   python3 scripts/package_skill.py --root . --check
   ```

3. Build the package:

   ```bash
   python3 scripts/package_skill.py --root .
   ```

## Tag

Use semantic version tags:

```bash
git tag v0.1.0
git push origin v0.1.0
```

## Release Asset

Attach `dist/obsidian-memory-closeout.zip` to the GitHub release if you want users to install from a zip instead of the GitHub directory URL.

For Claude users, mention that the release asset can be uploaded in Claude's custom Skills settings or copied into `~/.claude/skills/obsidian-memory-closeout` for Claude Code.
