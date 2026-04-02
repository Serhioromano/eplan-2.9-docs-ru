#!/usr/bin/env python3
"""Convert ![](images/arrow*.png) lines to !!! info admonition blocks in docs/eplan/."""

import re
from pathlib import Path

ARROW = re.compile(r'^!\[[^\]]*\]\(images/arrow[^)]*\)\s*(.+)$', re.MULTILINE)
MULTI_BLANK = re.compile(r'\n{3,}')

def replace(m):
    text = m.group(1).strip()
    return f'\n\n!!! info "Для сведения:"\n\n    {text}\n'

docs_dir = Path('docs/eplan')
changed = 0

for md_file in sorted(docs_dir.glob('**/*.md')):
    text = md_file.read_text(encoding='utf-8')
    new_text = ARROW.sub(replace, text)
    new_text = MULTI_BLANK.sub('\n\n', new_text)
    if new_text != text:
        md_file.write_text(new_text, encoding='utf-8')
        changed += 1

print(f'Done. {changed} file(s) updated.')