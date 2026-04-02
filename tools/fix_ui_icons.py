#!/usr/bin/env python3
"""
Add { .ui-icon } to inline image references where image is < 22x22 px.
Skips images that are alone on a line (standalone).
"""

import re
import struct
from pathlib import Path


def get_png_size(path):
    try:
        with open(path, 'rb') as f:
            h = f.read(24)
            if h[:8] == b'\x89PNG\r\n\x1a\n' and h[12:16] == b'IHDR':
                w = struct.unpack('>I', h[16:20])[0]
                h2 = struct.unpack('>I', h[20:24])[0]
                return w, h2
    except Exception:
        pass
    return None


# Build set of small image filenames
images_dir = Path('docs/eplan/images')
small_images = set()
for img_path in images_dir.glob('*.png'):
    size = get_png_size(img_path)
    if size and size[0] < 22 and size[1] < 22:
        small_images.add(img_path.name)

print(f'Small images (<22x22): {len(small_images)}')

# Match image not already followed by { .ui-icon } or any { }
IMG_RE = re.compile(r'!\[([^\]]*)\]\((images/([^)]+\.png))\)(?!\s*\{)')

# Strip all image refs (with optional attr) to detect standalone lines
STRIP_IMGS = re.compile(r'!\[[^\]]*\]\([^)]*\)(\s*\{[^}]*\})?')


def is_standalone(line):
    """True if the line contains only image(s) and whitespace (no other text)."""
    remainder = STRIP_IMGS.sub('', line).strip()
    return remainder == ''


def process_line(line):
    def replace(m):
        img_name = m.group(3)
        if img_name in small_images:
            return m.group(0) + '{ .ui-icon }'
        return m.group(0)
    return IMG_RE.sub(replace, line)


docs_dir = Path('docs/eplan')
changed = 0

for md_file in sorted(docs_dir.glob('**/*.md')):
    text = md_file.read_text(encoding='utf-8')
    lines = text.split('\n')
    new_lines = []
    file_changed = False

    for line in lines:
        if not is_standalone(line):
            new_line = process_line(line)
            if new_line != line:
                file_changed = True
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if file_changed:
        md_file.write_text('\n'.join(new_lines), encoding='utf-8')
        changed += 1

print(f'Updated {changed} files.')