#!/usr/bin/env python3
"""
Fix pymdownx.keys formatting (++text++) in markdown files.

Rules:
1. No space inside after opening ++ or before closing ++
2. Space before opening ++ (unless start of line or preceded by space/opening bracket)
3. Space after closing ++ unless followed by punctuation (. , ; : ! ? ) ] })
"""

import re
import sys
import glob
import os

DRY_RUN = "--dry-run" in sys.argv or "-n" in sys.argv


def fix_keys(content: str) -> str:
    # Single-pass: find all ++...++ patterns and fix them + surrounding context
    def fix_match(m):
        before_char = m.group(1)  # character before ++
        inner = m.group(2).strip()  # content inside, stripped
        after_char = m.group(3)  # character after ++

        # Build replacement
        result = ""

        # Add space before if needed
        if before_char and before_char not in (" ", "\t", "(", "\n", ""):
            result = before_char + " "
        else:
            result = before_char

        result += f"++{inner}++"

        # Add space after if needed
        if after_char and after_char not in (" ", "\t", ".", ",", ";", ":", "!", "?", ")", "]", "}", "\n", ""):
            result += " " + after_char
        else:
            result += after_char

        return result

    # Match: (char before)(++ content ++)(char after)
    # Use lookbehind alternative: capture one char before, the ++...++, and one char after
    result = re.sub(
        r'(^|.)\+\+(\s*[^+]+?\s*)\+\+(.|$)',
        fix_match,
        content,
        flags=re.MULTILINE,
    )

    return result


def main():
    docs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "eplan")
    files = glob.glob(os.path.join(docs_dir, "**", "*.md"), recursive=True)

    total_fixed = 0
    for filepath in sorted(files):
        with open(filepath, "r", encoding="utf-8") as f:
            original = f.read()

        fixed = fix_keys(original)

        if fixed != original:
            rel = os.path.relpath(filepath)
            total_fixed += 1

            # Show diff lines
            orig_lines = original.splitlines()
            fixed_lines = fixed.splitlines()
            for i, (ol, fl) in enumerate(zip(orig_lines, fixed_lines), 1):
                if ol != fl:
                    print(f"{rel}:{i}")
                    print(f"  - {ol.strip()}")
                    print(f"  + {fl.strip()}")

            if not DRY_RUN:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(fixed)

    print(f"\n{'[DRY RUN] ' if DRY_RUN else ''}Fixed {total_fixed} files")


if __name__ == "__main__":
    main()