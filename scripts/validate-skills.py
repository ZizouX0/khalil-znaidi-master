#!/usr/bin/env python3
"""
Validate every skill in .claude/skills against the Agent Skills spec.

Checks the frontmatter rules that both Claude Code's loader and the packaging
format care about:

  - SKILL.md exists and starts with parseable YAML frontmatter
  - `name` is kebab-case, <= 64 chars, and matches the directory name
  - `description` is present, <= 1024 chars, and free of angle brackets
  - no keys outside the spec's allowed set

Exits non-zero if any skill fails.

Usage: scripts/validate-skills.py [skills_dir]
"""
import re
import sys
from pathlib import Path

import yaml

ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def validate(skill_dir: Path) -> list[str]:
    errors = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return ["SKILL.md not found"]

    match = FRONTMATTER_RE.match(skill_md.read_text(encoding="utf-8"))
    if not match:
        return ["no YAML frontmatter"]

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f"invalid YAML: {exc}"]

    if not isinstance(frontmatter, dict):
        return ["frontmatter is not a YAML mapping"]

    unexpected = sorted(set(frontmatter) - ALLOWED)
    if unexpected:
        errors.append(f"unexpected key(s): {', '.join(unexpected)}")

    name = frontmatter.get("name")
    if not isinstance(name, str) or not name.strip():
        errors.append("missing 'name'")
    else:
        name = name.strip()
        if not NAME_RE.match(name):
            errors.append(f"name {name!r} is not kebab-case")
        elif name != skill_dir.name:
            errors.append(f"name {name!r} != directory {skill_dir.name!r}")
        if len(name) > 64:
            errors.append(f"name is {len(name)} chars (max 64)")

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("missing 'description'")
    else:
        if len(description) > 1024:
            errors.append(f"description is {len(description)} chars (max 1024)")
        if "<" in description or ">" in description:
            errors.append("description contains angle brackets")

    return errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else
                Path(__file__).resolve().parent.parent / ".claude" / "skills")
    if not root.is_dir():
        print(f"skills directory not found: {root}")
        return 1

    skills = sorted(d for d in root.iterdir() if d.is_dir())
    failed = 0
    for skill in skills:
        errors = validate(skill)
        if errors:
            failed += 1
            print(f"FAIL {skill.name}")
            for error in errors:
                print(f"       {error}")

    print(f"\n{len(skills) - failed}/{len(skills)} skills valid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
