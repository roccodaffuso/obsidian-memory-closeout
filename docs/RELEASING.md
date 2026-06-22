# Releasing

This repository publishes GitHub Releases automatically when a semantic version tag is pushed. The generated skill zip can still be built manually and uploaded as a Claude.ai custom skill because it contains the `obsidian-memory-closeout/` skill folder at archive root.

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
git tag -a v0.3.3 -m "v0.3.3"
git push origin v0.3.3
```

Pushing the tag triggers `.github/workflows/release.yml`, which creates the GitHub Release with generated notes.

## Release Asset

Attach `dist/obsidian-memory-closeout.zip` to the GitHub release only if you want users to install from a zip instead of the GitHub directory URL.

For Claude users, mention that the release asset can be uploaded in Claude's custom Skills settings or copied into `~/.claude/skills/obsidian-memory-closeout` for Claude Code.
