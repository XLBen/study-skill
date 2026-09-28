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
SKILL_DIR_SRC = REPO / "skills" / "study-flow"
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
    if not SKILL_DIR_SRC.is_dir():
        sys.exit(f"error: skill folder missing in repo: {SKILL_DIR_SRC}")

    installs = []
    skill_dst_dir = target / ".opencode" / "skills" / "study-flow"
    for src in sorted(SKILL_DIR_SRC.rglob("*")):
        if src.is_file():
            installs.append((src, skill_dst_dir / src.relative_to(SKILL_DIR_SRC)))
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
    print("  2. Optional, only for embedding slide/book figures as images:")
    print("     pip3 install pymupdf   (Homebrew python: add --break-system-packages)")
    print("     or install poppler: brew install poppler / apt install poppler-utils")
    print("     Without a renderer the skill still works; figures fall back to")
    print("     a 'see slide p.N' note instead of an embedded image.")


if __name__ == "__main__":
    main()
