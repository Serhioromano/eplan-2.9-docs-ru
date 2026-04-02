#!/usr/bin/env python3
"""Convert legacy EPLAN API code blocks to proper MkDocs markdown.

Two patterns are handled:

1. TAB BLOCKS (C# / VB tabs)
   Before:
       * C#
       * VB

       code for C# ...


       code for VB ...

   After:
       === "C#"

           ```csharp
           code for C# ...
           ```

       === "VB"

           ```vb
           code for VB ...
           ```

2. TABLE BLOCKS (single-language Copy Code tables)
   Before:
       C# |  Copy Code
       ---|---

       code ...

   After:
       ```csharp
       code ...
       ```
"""

import re
import sys
from pathlib import Path

API_DIR = Path(__file__).parent.parent / "docs" / "2.9" / "api"

LANG_MAP = {
    "C#": "csharp",
    "VB": "vb",
    "XML": "xml",
}

# Marker lines inside indented blocks to strip entirely
STRIP_LINE_RE = re.compile(r"^\s*\[C#\]\s*$|^\s*\[VB\]\s*$", re.IGNORECASE)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def strip_indent(lines: list[str], spaces: int = 4) -> list[str]:
    """Remove up to `spaces` leading spaces from each line."""
    result = []
    for line in lines:
        if line.startswith(" " * spaces):
            result.append(line[spaces:])
        elif line.strip() == "":
            result.append("")
        else:
            result.append(line)
    return result


def split_code_sections(lines: list[str]) -> list[list[str]]:
    """Split a list of stripped lines into code sections at 2+ blank-line runs."""
    sections: list[list[str]] = []
    current: list[str] = []
    blank_run = 0

    for line in lines:
        if line.strip() == "":
            blank_run += 1
        else:
            if blank_run >= 2 and current:
                # End of a section, start a new one
                sections.append(current)
                current = []
            elif blank_run == 1 and current:
                current.append("")  # keep single blank lines within code
            blank_run = 0
            current.append(line)

    if current:
        sections.append(current)

    return sections


def trim_code(lines: list[str]) -> list[str]:
    """Strip leading/trailing blank lines from a code section."""
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return lines


def build_tabbed(tab_names: list[str], sections: list[list[str]]) -> str:
    """Build a pymdownx.tabbed block."""
    out = []
    for name, code_lines in zip(tab_names, sections):
        lang = LANG_MAP.get(name, "")
        fence = f"```{lang}" if lang else "```"
        out.append(f'=== "{name}"\n')
        out.append("\n")
        out.append(f"    {fence}\n")
        for line in code_lines:
            out.append(f"    {line}\n" if line else "\n")
        out.append(f"    ```\n")
        out.append("\n")
    return "".join(out).rstrip("\n")


def build_fenced(lang_key: str, code_lines: list[str]) -> str:
    """Build a single fenced code block."""
    lang = LANG_MAP.get(lang_key, lang_key.lower() if lang_key else "")
    fence = f"```{lang}" if lang else "```"
    lines = [f"{fence}\n"]
    for line in code_lines:
        lines.append(f"{line}\n" if line else "\n")
    lines.append("```\n")
    return "".join(lines)


# ---------------------------------------------------------------------------
# Pattern 1: tab blocks  `  * C#\n  * VB\n`
# ---------------------------------------------------------------------------

TAB_HEADER_RE = re.compile(
    r"(?m)^((?:  \* .+\n)+)"   # one or more `  * TabName` lines
    r"((?:[ \t]*\n|    .+\n)*)" # indented block (blank lines or 4-space lines)
)


def replace_tab_block(m: re.Match) -> str:
    header_block = m.group(1)
    body_block = m.group(2)

    tab_names = [line[4:].rstrip() for line in header_block.splitlines(keepends=True)]

    # Only act if ALL tab names look like language markers (not URL lists)
    for name in tab_names:
        if "[" in name or "(" in name:
            return m.group(0)  # it's a regular bullet list, leave it alone

    body_lines = body_block.splitlines()
    stripped = strip_indent(body_lines, 4)
    # Remove [C#] / [VB] marker lines
    stripped = [line for line in stripped if not STRIP_LINE_RE.match(line)]
    sections = split_code_sections(stripped)
    sections = [trim_code(s) for s in sections if any(l.strip() for l in s)]

    n = len(tab_names)
    if len(sections) < n:
        # Not enough sections — can't transform reliably
        return m.group(0)
    if len(sections) > n:
        # More sections than tabs: merge extras into the last tab
        merged_last = []
        for s in sections[n - 1:]:
            if merged_last:
                merged_last.append("")  # blank line between merged sections
            merged_last.extend(s)
        sections = sections[:n - 1] + [merged_last]

    return build_tabbed(tab_names, sections) + "\n\n"


# ---------------------------------------------------------------------------
# Pattern 2: table blocks  `LANG |  Copy Code\n---|---\n`
# ---------------------------------------------------------------------------

TABLE_HEADER_RE = re.compile(
    r"(?m)^([^\n]*)\|  Copy Code[ \t]*\n"    # language line
    r"\|?-+\|?-+[ \t]*\n"                     # ---|--- separator
    r"((?:[ \t]*\n|    .+\n|      .+\n)*)"    # indented block
)


def replace_table_block(m: re.Match) -> str:
    lang_raw = m.group(1).strip().rstrip("|").strip()
    body_block = m.group(2)

    body_lines = body_block.splitlines()
    stripped = strip_indent(body_lines, 4)
    # Also strip 2-space prefix (some lines have 6 leading spaces → 2 remain)
    stripped = [line[2:] if line.startswith("  ") and not line.startswith("   ") else line
                for line in stripped]
    stripped = [line for line in stripped if not STRIP_LINE_RE.match(line)]
    # Collapse into one section
    all_code = trim_code([l for l in stripped if l.strip() or stripped])
    # Clean trailing blanks
    while all_code and all_code[-1].strip() == "":
        all_code.pop()

    if not any(l.strip() for l in all_code):
        return m.group(0)  # empty block, leave it

    return build_fenced(lang_raw, all_code) + "\n"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original

    text = TABLE_HEADER_RE.sub(replace_table_block, text)
    text = TAB_HEADER_RE.sub(replace_tab_block, text)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    dry_run = "--dry-run" in sys.argv
    files = sorted(API_DIR.glob("*.md"))

    changed = skipped = 0
    for f in files:
        if dry_run:
            original = f.read_text(encoding="utf-8")
            # just detect
            if TABLE_HEADER_RE.search(original) or TAB_HEADER_RE.search(original):
                print(f"  would change: {f.name}")
                changed += 1
            else:
                skipped += 1
        else:
            if process_file(f):
                print(f"  changed: {f.name}")
                changed += 1
            else:
                skipped += 1

    print(f"\nDone. {'Would change' if dry_run else 'Changed'}: {changed}, unchanged: {skipped}.")


if __name__ == "__main__":
    main()