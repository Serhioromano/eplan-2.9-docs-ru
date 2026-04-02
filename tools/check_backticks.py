#!/usr/bin/env python3
"""
Check that all inline code spans (`...`) have a space before and after,
unless the closing backtick is followed by: . , ) ; : ! ? or end of line.
"""

import re
import sys
from pathlib import Path

# Characters that are allowed directly after a closing backtick (no space needed)
ALLOWED_AFTER = set('.,);:!?')


def check_file(path: Path) -> list[tuple]:
    issues = []
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()

    in_code_block = False
    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Find all single-backtick spans (not double-backtick)
        for m in re.finditer(r'(?<!`)`([^`\n]+?)`(?!`)', line):
            start, end = m.start(), m.end()

            # --- check BEFORE opening backtick ---
            before_ok = start == 0 or line[start - 1] == ' '

            # --- check AFTER closing backtick ---
            if end >= len(line):
                after_ok = True  # end of line
            else:
                after_char = line[end]
                after_ok = after_char == ' ' or after_char in ALLOWED_AFTER

            if not before_ok or not after_ok:
                reason_parts = []
                if not before_ok:
                    reason_parts.append(f"no space before (char before: {line[start-1]!r})")
                if not after_ok:
                    reason_parts.append(f"no space after (char after: {line[end]!r})")
                issues.append({
                    'file': path,
                    'line': lineno,
                    'col': start + 1,
                    'span': m.group(),
                    'reason': ', '.join(reason_parts),
                    'context': line,
                })

    return issues


def main():
    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
    else:
        paths = sorted(Path('docs').rglob('*.md'))

    all_issues = []
    for p in paths:
        all_issues.extend(check_file(p))

    if not all_issues:
        print("No issues found.")
        return 0

    for issue in all_issues:
        print(f"{issue['file']}:{issue['line']}:{issue['col']}: {issue['span']!r}  [{issue['reason']}]")
        print(f"  {issue['context']}")
        print()

    print(f"Total: {len(all_issues)} issue(s) found.")
    return 1


if __name__ == '__main__':
    sys.exit(main())