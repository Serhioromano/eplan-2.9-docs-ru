#!/usr/bin/env python3
"""Convert standalone 'Example' labels + indented code blocks into proper MkDocs format.

Before:
    Example


        m_EventHandler = new EventHandler("Ged.Redraw");
        m_EventHandler.EplanEvent += delegate { ... };

After:
    **Example**

    ```csharp
    m_EventHandler = new EventHandler("Ged.Redraw");
    m_EventHandler.EplanEvent += delegate { ... };
    ```
"""

import re
import sys
from pathlib import Path

API_DIR = Path(__file__).parent.parent / "docs" / "2.9" / "api"

# A standalone Example label: "Example" (or "Example Title", etc.) alone on a line
EXAMPLE_LABEL_RE = re.compile(r"^Example\s*$")


def detect_lang(code_lines: list[str]) -> str:
    """Guess language from code content."""
    text = "\n".join(code_lines)
    if re.search(r"'''|Public |Dim |End |Implements ", text):
        return "vb"
    if re.search(r"///|new [A-Z]|\bdelegate\b|;\s*$|\{|\}", text):
        return "csharp"
    return ""  # plain / command-line


def strip_indent(lines: list[str]) -> list[str]:
    """Remove common leading whitespace from non-blank lines."""
    non_blank = [l for l in lines if l.strip()]
    if not non_blank:
        return lines
    min_indent = min(len(l) - len(l.lstrip()) for l in non_blank)
    result = []
    for line in lines:
        if line.strip():
            result.append(line[min_indent:])
        else:
            result.append("")
    return result


def process_file(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=False)
    out: list[str] = []
    i = 0
    changed = False
    in_fence = False

    while i < len(lines):
        line = lines[i]

        # Track fenced code blocks
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue

        # Inside a code fence — pass through unchanged
        if in_fence:
            out.append(line)
            i += 1
            continue

        # Check for standalone Example label
        if not in_fence and EXAMPLE_LABEL_RE.match(line):
            j = i + 1

            # Skip blank / whitespace-only lines (these are the "header blanks")
            while j < len(lines) and not lines[j].strip():
                j += 1

            # Check that what follows is indented code
            if j < len(lines) and lines[j].startswith(" "):
                # Collect the code block: indented lines OR blank lines
                # Stop at the first non-indented, non-blank line
                code_raw: list[str] = []
                while j < len(lines):
                    l = lines[j]
                    if l.strip() == "":
                        # blank line: peek ahead — if next non-blank is indented, keep it
                        # otherwise end the block
                        k = j + 1
                        while k < len(lines) and not lines[k].strip():
                            k += 1
                        if k < len(lines) and lines[k].startswith(" "):
                            code_raw.append(l)  # blank within block
                            j += 1
                        else:
                            break  # end of block
                    elif l.startswith(" "):
                        code_raw.append(l)
                        j += 1
                    else:
                        break  # non-indented content ends block

                code_lines = strip_indent(code_raw)
                # Trim leading/trailing blank lines
                while code_lines and not code_lines[0].strip():
                    code_lines.pop(0)
                while code_lines and not code_lines[-1].strip():
                    code_lines.pop()

                if code_lines:
                    lang = detect_lang(code_lines)
                    fence = f"```{lang}" if lang else "```"
                    out.append("**Example**")
                    out.append("")
                    out.append(fence)
                    out.extend(code_lines)
                    out.append("```")
                    i = j
                    changed = True
                    continue

        out.append(line)
        i += 1

    if changed:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main():
    dry_run = "--dry-run" in sys.argv
    files = sorted(API_DIR.glob("*.md"))
    changed = 0

    for f in files:
        if dry_run:
            # Preview: just detect without writing
            lines = f.read_text(encoding="utf-8").splitlines()
            for line in lines:
                if EXAMPLE_LABEL_RE.match(line):
                    print(f"  {f.name}")
                    changed += 1
                    break
        else:
            if process_file(f):
                print(f"  changed: {f.name}")
                changed += 1

    print(f"\nDone. {'Would change' if dry_run else 'Changed'}: {changed} files.")


if __name__ == "__main__":
    main()