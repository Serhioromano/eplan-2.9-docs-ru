#!/usr/bin/env python3
"""
Find all images smaller than 20x20 in docs/eplan/images and add { .ui-icon } class
to every image reference in markdown files.
"""

import re
from pathlib import Path
from PIL import Image

IMAGES_DIR = Path("docs/eplan/images")
DOCS_DIR = Path("docs/eplan")
MAX_SIZE = 20


def find_small_images():
    icons = set()
    for img_path in IMAGES_DIR.iterdir():
        if img_path.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"):
            try:
                with Image.open(img_path) as img:
                    w, h = img.size
                    if w < MAX_SIZE and h < MAX_SIZE:
                        icons.add(img_path.name)
            except Exception as e:
                print(f"  Skipping {img_path.name}: {e}")
    return icons


def add_class_to_md_files(icon_names):
    md_files = list(DOCS_DIR.rglob("*.md"))
    total_changes = 0

    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        new_text = text
        file_changes = 0

        for name in icon_names:
            # Match image references that use this filename but do NOT already have { .ui-icon }
            pattern = re.compile(
                r'(!\[[^\]]*\]\([^)]*' + re.escape(name) + r'\))(?!\s*\{[^}]*\.ui-icon[^}]*\})'
            )
            def replacer(m):
                nonlocal file_changes
                file_changes += 1
                return m.group(1) + "{ .ui-icon }"

            new_text = pattern.sub(replacer, new_text)

        if file_changes:
            md_file.write_text(new_text, encoding="utf-8")
            print(f"  {md_file.relative_to(DOCS_DIR)}: {file_changes} change(s)")
            total_changes += file_changes

    return total_changes


def main():
    print(f"Scanning for images smaller than {MAX_SIZE}x{MAX_SIZE}...")
    icons = find_small_images()
    print(f"Found {len(icons)} icon(s):")
    for name in sorted(icons):
        print(f"  {name}")

    if not icons:
        print("Nothing to do.")
        return

    print("\nUpdating markdown files...")
    total = add_class_to_md_files(icons)
    print(f"\nDone. Total replacements: {total}")


if __name__ == "__main__":
    main()