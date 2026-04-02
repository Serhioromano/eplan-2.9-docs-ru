#!/usr/bin/env python3
"""Ensure standalone image lines have one empty line above and below."""

import re
from pathlib import Path

STRIP_IMGS = re.compile(r'!\[[^\]]*\]\([^)]*\)(\s*\{[^}]*\})?')
MULTI_BLANK = re.compile(r'\n{3,}')


def fix_image_spacing(content):
    """Wrap each standalone image line with blank lines above and below."""
    lines = content.split('\n')
    result = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        is_standalone = bool(stripped) and '![' in line and STRIP_IMGS.sub('', stripped).strip() == ''

        if is_standalone:
            # Ensure blank line before
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            # Ensure blank line after (peek ahead)
            if i + 1 < len(lines) and lines[i + 1].strip() != '':
                result.append('')
        else:
            result.append(line)

    content = '\n'.join(result)
    # Collapse 3+ newlines to 2
    content = MULTI_BLANK.sub('\n\n', content)
    return content


if __name__ == '__main__':
    docs_dir = Path('docs/eplan')
    changed = 0

    for md_file in sorted(docs_dir.glob('**/*.md')):
        text = md_file.read_text(encoding='utf-8')
        new_text = fix_image_spacing(text)
        if new_text != text:
            md_file.write_text(new_text, encoding='utf-8')
            changed += 1

    print(f'Done. {changed} file(s) updated.')