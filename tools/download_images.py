#!/usr/bin/env python3
"""Download images referenced in docs/eplan/*.md and update links."""

import re
import glob
import os
import urllib.request
import time

BASE_URL = "https://www.eplan.help/ru-ru/Infoportal/Content/Plattform/2026/Content/"
IMG_DIR = "docs/eplan/images"
os.makedirs(IMG_DIR, exist_ok=True)

# Collect all image references
pattern = re.compile(r'!\[([^\]]*)\]\(\.\./([^)]+\.png)\)')

images = set()
for path in sorted(glob.glob('docs/eplan/*.md')):
    with open(path, 'r') as f:
        for m in pattern.finditer(f.read()):
            images.add(m.group(2))  # e.g. Pictures/Gui/Lang/foo.png

print(f'Found {len(images)} unique images')

# Download
downloaded = 0
failed = []
for rel_path in sorted(images):
    filename = os.path.basename(rel_path)
    dest = os.path.join(IMG_DIR, filename)
    if os.path.exists(dest):
        print(f'  SKIP {filename} (exists)')
        downloaded += 1
        continue
    url = BASE_URL + rel_path
    try:
        urllib.request.urlretrieve(url, dest)
        print(f'  OK   {filename}')
        downloaded += 1
        time.sleep(0.2)
    except Exception as e:
        print(f'  FAIL {filename}: {e}')
        failed.append(filename)

print(f'\nDownloaded {downloaded}/{len(images)} images')
if failed:
    print(f'Failed: {failed}')

# Update links in markdown files
updated = 0
for path in sorted(glob.glob('docs/eplan/*.md')):
    with open(path, 'r') as f:
        content = f.read()
    # Replace ![alt](../Pictures/Gui/Lang/foo.png) -> ![alt](images/foo.png)
    new = pattern.sub(lambda m: f'![{m.group(1)}](images/{os.path.basename(m.group(2))})', content)
    if new != content:
        with open(path, 'w') as f:
            f.write(new)
        updated += 1

print(f'Updated links in {updated} files')
