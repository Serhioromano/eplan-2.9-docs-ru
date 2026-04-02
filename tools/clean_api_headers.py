#!/usr/bin/env python3
"""Remove boilerplate headers from docs/2.9/api/*.md files.

Each file starts with:
  - Logo image link
  - "API Help"
  - Empty webindex link
  - Breadcrumb navigation
  - "Collapse All Expand All"
  - "In This Topic"
  - (blank lines)
  - Page title
  - (blank line)
  - "In This Topic"   <-- second occurrence marks end of header
  - (blank line)
  - <actual content>

This script extracts the page title and replaces everything up to and
including the second "In This Topic" with a single H1 heading.
"""

import re
import sys
from pathlib import Path

API_DIR = Path(__file__).parent.parent / "docs" / "2.9" / "api"


def clean_file(path: Path, dry_run: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Find the first line that looks like the logo/header
    if not lines or not lines[0].startswith("[![](images/"):
        return False  # already cleaned or different format

    # Find second occurrence of "In This Topic"
    in_this_topic_count = 0
    second_itp_index = None
    for i, line in enumerate(lines):
        if line.strip() == "In This Topic":
            in_this_topic_count += 1
            if in_this_topic_count == 2:
                second_itp_index = i
                break

    if second_itp_index is None:
        print(f"  WARNING: second 'In This Topic' not found in {path.name}")
        return False

    # The title is the last non-empty line before the second "In This Topic"
    title = None
    for i in range(second_itp_index - 1, -1, -1):
        if lines[i].strip():
            title = lines[i].strip()
            break

    if not title:
        print(f"  WARNING: could not extract title from {path.name}")
        return False

    # Content starts after the second "In This Topic" (skip blank lines)
    content_start = second_itp_index + 1
    while content_start < len(lines) and not lines[content_start].strip():
        content_start += 1

    new_content = f"# {title}\n\n" + "\n".join(lines[content_start:])
    # Ensure single trailing newline
    new_content = new_content.rstrip("\n") + "\n"

    if dry_run:
        print(f"  [dry-run] {path.name}: title='{title}', content from line {content_start+1}")
        return True

    path.write_text(new_content, encoding="utf-8")
    return True


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN — no files will be modified\n")

    files = sorted(API_DIR.glob("*.md"))
    if not files:
        print(f"No .md files found in {API_DIR}")
        sys.exit(1)

    changed = 0
    skipped = 0
    for f in files:
        if clean_file(f, dry_run=dry_run):
            changed += 1
            if not dry_run:
                print(f"  cleaned: {f.name}")
        else:
            skipped += 1

    print(f"\nDone. {'Would process' if dry_run else 'Processed'} {changed} files, skipped {skipped}.")


if __name__ == "__main__":
    main()