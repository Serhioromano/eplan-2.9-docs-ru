#!/usr/bin/env python3
"""
Fix broken bold markers left after **[text]** → ++"text"++ conversion.

Pattern: **Title ++"..."++ ** → **Title** ++"..."++
Also handle: **Title ++"key"++ ** text  (trailing orphaned **)
"""

import re
from pathlib import Path

# Fix: **<word(s)> ++"key"++ ** → **<word(s)>** ++"key"++
# The leading ** was the bold-open for the dialog name,
# the trailing ** was the bold-close that got separated from its content.
FIX_BOLD = re.compile(r'\*\*([^*\n]+?) (\+\+"[^"]+"\+\+) \*\*')

docs_dir = Path('docs/eplan')
changed = 0

for md_file in sorted(docs_dir.glob('**/*.md')):
    text = md_file.read_text(encoding='utf-8')
    new_text = FIX_BOLD.sub(r'**\1** \2', text)
    if new_text != text:
        md_file.write_text(new_text, encoding='utf-8')
        changed += 1

print(f'Done. {changed} file(s) fixed.')
