#!/usr/bin/env python3
"""Install study-flow skill + commands into a course folder.

Usage:
    python3 scripts/install.py /path/to/course-folder [--force]

Creates:
    <course>/.opencode/skills/study-flow/SKILL.md
    <course>/.opencode/commands/*.md

Idempotent: existing files are skipped unless --force is given.
Works on macOS, Linux and Windows (needs python3 only).
"""
import argparse
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL_SRC = REPO / "skills" / "study-flow" / "SKILL.md"
COMMAND_SRCS = sorted((REPO / "commands").glob("*.md"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Install study-flow skill and commands into a course folder."
    )
    parser.add_argument("target", help="course folder to install into")
    parser.add_argument(
        "--force", action="store_true", help="overwrite existing files"
    )
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    if not SKILL_SRC.is_file():
        sys.exit(f"error: skill file missing in repo: {SKILL_SRC}")

    installs = [(SKILL_SRC, target / ".opencode" / "skills" / "study-flow" / "SKILL.md")]
    installs += [(src, target / ".opencode" / "commands" / src.name) for src in COMMAND_SRCS]

    done: list[Path] = []
    skipped: list[Path] = []
    for src, dst in installs:
        if dst.exists() and not args.force:
            skipped.append(dst)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        done.append(dst)

    for path in done:
        print(f"installed: {path.relative_to(target)}")
    for path in skipped:
        print(f"skipped (exists, use --force): {path.relative_to(target)}")

    print()
    print("Next steps:")
    print("  1. Restart OpenCode inside the course folder.")
    print("  2. Optional, only for embedding slide figures as images:")
    print("     macOS:         brew install poppler")
    print("     Debian/Ubuntu: sudo apt install poppler-utils")
    print("     Windows:       choco install poppler")
    print("     Without poppler the skill still works; figures fall back to")
    print("     a 'see slide p.N' note instead of an embedded image.")


if __name__ == "__main__":
    main()
