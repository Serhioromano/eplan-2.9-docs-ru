#!/usr/bin/env python3
"""Wrap patterns like Создать(<текущий_номер>) in backticks in all docs markdown files."""

import re
import sys
from pathlib import Path

# Match word(<...>) not already wrapped in backticks
PATTERN = re.compile(r'(?<!`)(\b[\w_]+\(<[^>]+>\))(?!`)')

docs_dir = Path("docs/eplan")
changed = 0

for md_file in sorted(docs_dir.glob("*.md")):
    text = md_file.read_text(encoding="utf-8")
    new_text = PATTERN.sub(r'`\1`', text)
    if new_text != text:
        md_file.write_text(new_text, encoding="utf-8")
        # Count replacements
        n = len(PATTERN.findall(text))
        print(f"{md_file.name}: {n} replacement(s)")
        changed += 1

print(f"\nDone. {changed} file(s) updated.")