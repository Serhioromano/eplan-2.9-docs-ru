#!/usr/bin/env python3
"""Wrap dotted API identifiers in backticks in docs/2.9/api/*.md files.

Targets patterns like:
  DocumentTypeManager.DocumentType enumeration
  Eplan.EplApi.DataModel.Page class
  ProjectManager.CreateProject method
  System.GC.WaitForPendingFinalizers()
  addMenuItem, findAction  (camelCase)
  OnInitGui(), AddMenuItem()  (function calls)

Rules:
  - Only in prose lines (outside fenced code blocks)
  - Skip heading lines (starting with #)
  - Skip text already wrapped in backticks
  - Skip markdown link text AND link targets [text](url)
  - Skip content inside double quotes "..."
  - Dotted identifiers: BOTH segments must start uppercase (prevents e.g, .jpg, etc.)
  - No wrapping after backslash (prevents C:\\path\\Ident.Sub)
  - Optionally include a trailing type-descriptor word (class, method, etc.)
"""

import re
import sys
from pathlib import Path

API_DIR = Path(__file__).parent.parent / "docs" / "2.9" / "api"

# Type descriptor words that may follow the identifier (case-insensitive match)
DESCRIPTORS = (
    "class", "method", "property", "properties",
    "enumeration", "enum", "interface", "namespace",
    "object", "function", "event", "attribute",
    "struct", "type", "module", "assembly",
)
# Both-case variants so we don't need re.IGNORECASE on the whole pattern
DESCRIPTOR_RE = "|".join(f"{d}|{d.capitalize()}" for d in DESCRIPTORS)

# Dotted identifier: ALL segments must start uppercase (prevents e.g, .jpg, .Net → ok,
# .net → no). No match after a backslash (file paths).
DOTTED_IDENT = r"[A-Z][a-zA-Z0-9_]*(?:\.[A-Z][a-zA-Z0-9_]*)+(?:\(\))?"

# Pattern 1: dotted + optional descriptor, not preceded by backtick or backslash
PATTERN_DOTTED = re.compile(
    rf"(?<!`)(?<!\\)({DOTTED_IDENT})(?:\s+({DESCRIPTOR_RE}))?(?!`)"
)

# Pattern 2: function call — identifier 3+ chars followed by ()
PATTERN_FUNC = re.compile(r"(?<!`)\b([a-zA-Z][a-zA-Z0-9_]{2,})\(\)(?!`)")

# Pattern 3: camelCase — starts lowercase, contains uppercase, no dots
PATTERN_CAMEL = re.compile(r"(?<!`)\b([a-z][a-zA-Z0-9_]*[A-Z][a-zA-Z0-9_]*)(?!`)\b")

# ── protected span detectors ──────────────────────────────────────────────────
BACKTICK_SPAN = re.compile(r"`[^`]+`")
# Handles plain links [text](url), image links ![alt](url), and nested [![](img)](href)
LINK_RE = re.compile(r"!?\[(?:[^\[\]]*|\[[^\[\]]*\])*\]\([^)]*\)")
DQUOTE_RE = re.compile(r'"[^"]*"')


# ── cleanup patterns for already-wrongly-wrapped content ─────────────────────
# Fixes produced by the previous (buggy) run of this script:
CLEANUP = [
    # `e.g` or `e.g.` → e.g (abbreviation, not code)
    (re.compile(r"`(e\.g)`"), r"\1"),
    # `E.g` → E.g
    (re.compile(r"`(E\.g)`"), r"\1"),
    # Heading: # `Ident.Ident` → # Ident.Ident
    # (handled by skipping heading lines during wrapping — but fix existing ones)
    (re.compile(r"^(#{1,6}\s+)`([^`]+)`\s*$", re.MULTILINE), r"\1\2"),
    # Link target corrupted: ](`Foo.Bar` …) → ](Foo.Bar …)
    (re.compile(r"\]\(`([^`]+)`"), r"](\1"),
    # Path: \`Ident.Sub`\ → \Ident.Sub\ (backslash context)
    (re.compile(r"\\`([A-Z][a-zA-Z0-9_]*(?:\.[A-Z][a-zA-Z0-9_]*)+)`\\"), r"\\\1\\"),
    # "`onActionStart.String`.*" → `onActionStart.String.*`
    # More generally: "`partial.ident`suffix" where suffix is non-space non-quote chars
    (re.compile(r'"`([^`"]+)`([^"\s]+)"'), r'`\1\2`'),
]


def cleanup_line(line: str) -> str:
    for pattern, replacement in CLEANUP:
        line = pattern.sub(replacement, line)
    return line


def wrap_identifiers(line: str) -> str:
    """Wrap API identifiers in backticks, skipping protected spans."""

    def get_protected(text: str) -> list[tuple[int, int]]:
        spans = []
        for m in BACKTICK_SPAN.finditer(text):
            spans.append((m.start(), m.end()))
        for m in LINK_RE.finditer(text):
            spans.append((m.start(), m.end()))
        for m in DQUOTE_RE.finditer(text):
            spans.append((m.start(), m.end()))
        return spans

    def apply_pattern(text: str, pattern: re.Pattern, build_inner) -> str:
        protected = get_protected(text)

        def is_protected(start: int, end: int) -> bool:
            return any(ps <= start and end <= pe for ps, pe in protected)

        result = []
        pos = 0
        for m in pattern.finditer(text):
            if is_protected(m.start(), m.end()):
                continue
            inner = build_inner(m)
            result.append(text[pos:m.start()])
            result.append(f"`{inner}`")
            pos = m.end()
        result.append(text[pos:])
        return "".join(result)

    line = apply_pattern(
        line, PATTERN_DOTTED,
        lambda m: f"{m.group(1)} {m.group(2)}" if m.group(2) else m.group(1),
    )
    line = apply_pattern(line, PATTERN_FUNC, lambda m: f"{m.group(1)}()")
    line = apply_pattern(line, PATTERN_CAMEL, lambda m: m.group(1))
    return line


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    # Step 1: cleanup previous bad wrappings
    new_text = text
    for pattern, replacement in CLEANUP:
        new_text = pattern.sub(replacement, new_text)

    # Step 2: apply fresh wrapping line-by-line
    lines = new_text.splitlines(keepends=True)
    out = []
    in_fence = False

    for line in lines:
        stripped = line.rstrip("\n\r")

        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue

        # Skip code blocks, indented code, and heading lines
        if in_fence or stripped.startswith("    ") or stripped.startswith("#"):
            out.append(line)
            continue

        out.append(wrap_identifiers(line))

    result = "".join(out)
    if result != text:
        path.write_text(result, encoding="utf-8")
        return True
    return False


def main():
    dry_run = "--dry-run" in sys.argv
    files = sorted(API_DIR.glob("*.md"))
    changed = 0

    for f in files:
        if process_file.__name__ and not dry_run:
            if process_file(f):
                print(f"  changed: {f.name}")
                changed += 1
        else:
            # dry-run: check without writing
            text = f.read_text(encoding="utf-8")
            test_text = text
            for pattern, replacement in CLEANUP:
                test_text = pattern.sub(replacement, test_text)
            lines = test_text.splitlines(keepends=True)
            out = []
            in_fence = False
            for line in lines:
                s = line.rstrip("\n\r")
                if s.startswith("```"):
                    in_fence = not in_fence
                    out.append(line)
                    continue
                if in_fence or s.startswith("    ") or s.startswith("#"):
                    out.append(line)
                    continue
                out.append(wrap_identifiers(line))
            if "".join(out) != text:
                print(f"  would change: {f.name}")
                changed += 1

    print(f"\nDone. {'Would change' if dry_run else 'Changed'}: {changed} files.")


if __name__ == "__main__":
    main()