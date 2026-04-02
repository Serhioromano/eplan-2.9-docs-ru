#!/usr/bin/env python3
"""Convert **[text]** patterns to ++"text"++ with proper spacing."""

import re
from pathlib import Path

# Match **[text]** — capture surrounding char context for spacing
PATTERN = re.compile(r'(.?)\*\*\[([^\]]+)\]\*\*(.?)', re.DOTALL)

PUNCT_AFTER = set('.,:;!?)]')

def replace(m):
    pre_char = m.group(1)
    text = m.group(2)
    post_char = m.group(3)

    key = f'++"{text}"++'

    # Space before: add if pre_char is a non-space word character
    if pre_char and pre_char not in (' ', '\t', '\n', '(', '['):
        key = ' ' + key
    # Keep pre_char as-is (re-attach)

    # Space after: add if post_char is not punctuation, space, or end
    if post_char and post_char not in PUNCT_AFTER and post_char not in (' ', '\t', '\n'):
        key = key + ' '

    return pre_char + key + post_char

docs_dir = Path('docs/eplan')
changed = 0

for md_file in sorted(docs_dir.glob('**/*.md')):
    text = md_file.read_text(encoding='utf-8')
    new_text = PATTERN.sub(replace, text)
    if new_text != text:
        md_file.write_text(new_text, encoding='utf-8')
        changed += 1

print(f'Done. {changed} file(s) updated.')