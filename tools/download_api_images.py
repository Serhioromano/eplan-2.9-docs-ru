#!/usr/bin/env python3
"""Download missing images from EPLAN API HTML files.

Scans all *.html files in docs/2.9/api/, collects every <img src="...">
reference, and downloads each image (once) from:
  https://www.eplan.help/en-us/Infoportal/Content/api/2.9/<src>

Images are saved to docs/2.9/api/images/, preserving any subdirectory
structure but stripping a leading "images/" prefix from the src path.

Skips files that already exist locally.
"""

import re
import sys
import time
import urllib.request
from pathlib import Path
from urllib.parse import unquote

BASE_URL = "https://www.eplan.help/en-us/Infoportal/Content/api/2.9/"
API_DIR = Path(__file__).parent.parent / "docs" / "2.9" / "api"
IMAGES_DIR = API_DIR / "images"

# Ignore these — they are scripts/stylesheets, not images
SKIP_EXTENSIONS = {".js", ".css"}


def collect_srcs(html_dir: Path) -> set[str]:
    """Return the set of unique src values from all <img> tags in *.html files."""
    srcs: set[str] = set()
    pattern = re.compile(r'<img\b[^>]+\bsrc="([^"]+)"', re.IGNORECASE)
    for html_file in sorted(html_dir.glob("*.html")):
        text = html_file.read_text(encoding="utf-8", errors="replace")
        for match in pattern.finditer(text):
            src = match.group(1).strip()
            ext = Path(src.split("?")[0]).suffix.lower()
            if ext not in SKIP_EXTENSIONS and src:
                srcs.add(src)
    return srcs


def src_to_local(src: str) -> Path:
    """Map an src value to a local path under IMAGES_DIR.

    Rules:
      - Strip a leading "images/" prefix (those files already live under images/)
      - Preserve any other subdirectory structure (graphs/, Addons_files/, …)
    """
    rel = unquote(src)
    if rel.startswith("images/"):
        rel = rel[len("images/"):]
    return IMAGES_DIR / rel


def download(src: str, dest: Path) -> bool:
    """Download src from BASE_URL to dest. Returns True on success."""
    url = BASE_URL + src
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status != 200:
                print(f"  SKIP {resp.status}: {src}")
                return False
            dest.write_bytes(resp.read())
        return True
    except Exception as e:
        print(f"  ERROR {src}: {e}")
        return False


def main():
    dry_run = "--dry-run" in sys.argv
    srcs = collect_srcs(API_DIR)
    print(f"Found {len(srcs)} unique image references in HTML files.")

    to_download = []
    for src in sorted(srcs):
        local = src_to_local(src)
        if local.exists():
            continue
        to_download.append((src, local))

    print(f"{len(to_download)} images need downloading ({len(srcs) - len(to_download)} already present).\n")

    if dry_run:
        for src, local in to_download:
            print(f"  would download: {src}  →  {local.relative_to(API_DIR.parent.parent)}")
        return

    ok = fail = 0
    for src, local in to_download:
        print(f"  downloading: {src}")
        if download(src, local):
            ok += 1
        else:
            fail += 1
        time.sleep(0.1)  # be polite

    print(f"\nDone. Downloaded: {ok}, Failed: {fail}.")


if __name__ == "__main__":
    main()