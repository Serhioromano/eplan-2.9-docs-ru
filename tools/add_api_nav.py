#!/usr/bin/env python3
"""Convert api_tree.json into a mkdocs nav section and insert it into mkdocs.yml.

URL pattern in tree: https://www.eplan.help/en-us/Infoportal/Content/api/2.9/Actions.html
Maps to mkdocs path:  2.9/api/Actions.md

Nodes with children  → nav section (title only, no page link)
Nodes without children → nav leaf, mapped to md file (skipped if file not found)
"""

import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).parent.parent
API_DIR = ROOT / "docs" / "2.9" / "api"
TREE_JSON = ROOT / "tools" / "29" / "api_tree.json"
MKDOCS_YML = ROOT / "mkdocs.yml"

# Build set of available md filenames (without path prefix)
AVAILABLE = {p.name for p in API_DIR.glob("*.md")}


def url_to_md_path(url: str) -> str | None:
    """Convert a tree URL to a mkdocs-relative path like '2.9/api/Foo.md'."""
    filename = unquote(url.rstrip("/").split("/")[-1])
    if not filename.endswith(".html"):
        return None
    md_name = filename[:-5] + ".md"  # replace .html → .md
    if md_name in AVAILABLE:
        return f"2.9/api/{md_name}"
    return None


def build_nav(nodes: list, indent: int = 2) -> list[str]:
    """Recursively build YAML nav lines for a list of tree nodes."""
    lines = []
    pad = " " * indent

    for node in nodes:
        title = node["title"]
        children = node.get("children", [])

        if children:
            # Section: emit title header, recurse into children
            lines.append(f'{pad}- "{title}":')
            lines.extend(build_nav(children, indent + 2))
        else:
            # Leaf: map URL to md file
            md_path = url_to_md_path(node.get("link", ""))
            if md_path:
                lines.append(f'{pad}- "{title}": {md_path}')
            # else: skip — file not available

    return lines


def main():
    tree = json.loads(TREE_JSON.read_text(encoding="utf-8"))

    # tree is a list; the first item is the root "EPLAN API" node
    root = tree[0]
    assert root["title"] == "EPLAN API", f"Unexpected root title: {root['title']}"

    nav_lines = ['  - "API EPLAN":']
    nav_lines.extend(build_nav(root.get("children", []), indent=4))
    nav_block = "\n".join(nav_lines) + "\n"

    yml_text = MKDOCS_YML.read_text(encoding="utf-8")

    # Insert just before the `plugins:` top-level key
    if '"API EPLAN":' in yml_text:
        print("API EPLAN section already exists in mkdocs.yml — skipping.")
        return

    insertion_marker = "\nplugins:"
    if insertion_marker not in yml_text:
        print("ERROR: could not find 'plugins:' in mkdocs.yml")
        return

    new_yml = yml_text.replace(insertion_marker, "\n" + nav_block + "\nplugins:", 1)
    MKDOCS_YML.write_text(new_yml, encoding="utf-8")
    nav_entry_count = nav_block.count("\n- ") + nav_block.count("\n    - ") + nav_block.count("\n  - ")
    print(f"Done. Inserted {len(nav_lines)} nav lines before 'plugins:'.")


if __name__ == "__main__":
    main()