#!/usr/bin/env python3
"""
Link integrity checker and auto-fixer for epla-toc docs.

Checks each docs section independently (docs/2.9, docs/2026, etc.):
  1. Resolve every [text](link) and ![](image) relative to the source file
  2. If target missing but a file with same name exists elsewhere IN THE SAME SECTION → fix the path
  3. If target missing and not found anywhere in the section → log to broken-links.log
  4. Image links checked the same way

Cross-section links (e.g. docs/2.9 → docs/2026) are flagged as broken.

Usage:
  python3 tools/check_links.py [--fix] [section ...]

  --fix        Auto-fix wrong-path links (same filename, different dir within section)
  section      One or more section dirs to check (default: docs/2.9 docs/2026)
"""

import re
import sys
import argparse
from collections import defaultdict
from pathlib import Path

LOG_FILE   = Path("broken-links.log")
FIXED_FILE = Path("fixed-links.log")

# Matches ![](…) and [text](…), captures (bang, text, href)
LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\(([^)#\s][^)\s]*?)(?:\s+"[^"]*")?\)')


def is_external(href: str) -> bool:
    return href.startswith(("http://", "https://", "mailto:", "ftp://", "/"))


def load_section_index(section_root: Path) -> dict[str, list[Path]]:
    """Return {filename: [abs_path, ...]} for all files in section (recursive)."""
    index: dict[str, list[Path]] = defaultdict(list)
    for p in section_root.rglob("*"):
        if p.is_file():
            index[p.name].append(p)
    return index


def check_and_fix_section(section_root: Path, do_fix: bool) -> dict:
    section_root = section_root.resolve()
    md_files = sorted(section_root.rglob("*.md"))
    index = load_section_index(section_root)

    broken   = []   # {source, target, is_image, suggestion}
    fixed    = []   # {source, old_target, new_target}
    ok_count = 0
    ext_count = 0

    print(f"\n{'='*70}")
    print(f"Section: {section_root}")
    print(f"Files:   {len(md_files)}")
    print(f"{'='*70}")

    for md_path in md_files:
        content = md_path.read_text(encoding="utf-8", errors="replace")
        base_dir = md_path.parent
        new_content = content

        for m in LINK_RE.finditer(content):
            bang, _text, raw_target = m.group(1), m.group(2), m.group(3)
            is_image = bang == "!"

            if is_external(raw_target):
                ext_count += 1
                continue

            # Strip MkDocs attr suffix just in case
            target = re.sub(r'\s*\{[^}]*\}$', '', raw_target).strip()

            resolved = (base_dir / target).resolve()

            if resolved.exists():
                ok_count += 1
                continue

            # Try to find file by name within THIS section only
            fname = Path(target).name
            candidates = [
                p for p in index.get(fname, [])
                if p.resolve() != resolved
            ]

            if candidates:
                # Prefer shortest relative path from file's dir
                best = min(candidates, key=lambda p: len(p.parts))
                try:
                    new_target = str(_relpath(best, md_path.parent))
                except Exception:
                    new_target = None

                if do_fix and new_target:
                    new_content = new_content.replace(
                        m.group(0),
                        m.group(0).replace(raw_target, new_target),
                        1
                    )
                    fixed.append({
                        "source":     md_path.relative_to(section_root),
                        "old_target": target,
                        "new_target": new_target,
                    })
                    ok_count += 1
                else:
                    broken.append({
                        "source":     md_path.relative_to(section_root),
                        "target":     target,
                        "is_image":   is_image,
                        "suggestion": new_target,
                    })
            else:
                broken.append({
                    "source":   md_path.relative_to(section_root),
                    "target":   target,
                    "is_image": is_image,
                    "suggestion": None,
                })

        if do_fix and new_content != content:
            md_path.write_text(new_content, encoding="utf-8")

    return {
        "section":   str(section_root),
        "broken":    broken,
        "fixed":     fixed,
        "ok_count":  ok_count,
        "ext_count": ext_count,
        "total_files": len(md_files),
    }


def _relpath(target: Path, from_dir: Path) -> Path:
    """Return a relative path from from_dir to target."""
    target  = target.resolve()
    from_dir = from_dir.resolve()
    parts_t = target.parts
    parts_f = from_dir.parts
    # Find common prefix
    common = 0
    for a, b in zip(parts_t, parts_f):
        if a == b:
            common += 1
        else:
            break
    ups = len(parts_f) - common
    rel_parts = ['..'] * ups + list(parts_t[common:])
    return Path(*rel_parts) if rel_parts else Path('.')


def write_logs(results: list[dict], do_fix: bool) -> None:
    with LOG_FILE.open("w", encoding="utf-8") as log:
        log.write("=" * 70 + "\n")
        log.write("BROKEN LINKS REPORT\n")
        log.write("=" * 70 + "\n\n")

        total_broken = sum(len(r["broken"]) for r in results)
        total_fixed  = sum(len(r["fixed"])  for r in results)
        total_ok     = sum(r["ok_count"]    for r in results)
        total_ext    = sum(r["ext_count"]   for r in results)
        total_files  = sum(r["total_files"] for r in results)

        log.write(f"Files scanned    : {total_files}\n")
        log.write(f"Links OK         : {total_ok}\n")
        log.write(f"External (skip)  : {total_ext}\n")
        log.write(f"Fixed            : {total_fixed}\n")
        log.write(f"Broken remaining : {total_broken}\n\n")

        for r in results:
            broken = r["broken"]
            if not broken:
                continue

            found   = [b for b in broken if b["suggestion"]]
            missing = [b for b in broken if not b["suggestion"]]

            log.write("─" * 70 + "\n")
            log.write(f"SECTION: {r['section']}\n")
            log.write(f"  broken: {len(broken)}  (fixable: {len(found)}, missing: {len(missing)})\n")
            log.write("─" * 70 + "\n\n")

            if found:
                log.write(f"WRONG PATH — file exists elsewhere ({len(found)}):\n\n")
                for b in found:
                    kind = "IMG " if b["is_image"] else "LINK"
                    log.write(f"  [{kind}] {b['source']}\n")
                    log.write(f"         target    : {b['target']}\n")
                    log.write(f"         suggestion: {b['suggestion']}\n\n")

            if missing:
                log.write(f"COMPLETELY MISSING ({len(missing)}):\n\n")
                for b in missing:
                    kind = "IMG " if b["is_image"] else "LINK"
                    log.write(f"  [{kind}] {b['source']}\n")
                    log.write(f"         target: {b['target']}\n\n")

    print(f"\nBroken-links log : {LOG_FILE}")

    if do_fix:
        with FIXED_FILE.open("w", encoding="utf-8") as f:
            f.write("=" * 70 + "\n")
            f.write("FIXED LINKS\n")
            f.write("=" * 70 + "\n\n")
            for r in results:
                if not r["fixed"]:
                    continue
                f.write(f"SECTION: {r['section']}\n\n")
                for fx in r["fixed"]:
                    f.write(f"  {fx['source']}\n")
                    f.write(f"    {fx['old_target']}\n")
                    f.write(f"    → {fx['new_target']}\n\n")
        print(f"Fixed-links log  : {FIXED_FILE}")


def print_summary(results: list[dict], do_fix: bool) -> None:
    for r in results:
        broken  = r["broken"]
        fixed   = r["fixed"]
        found   = [b for b in broken if b["suggestion"]]
        missing = [b for b in broken if not b["suggestion"]]

        sec = Path(r["section"]).name
        print(f"\n  [{sec}]")
        print(f"    Files          : {r['total_files']}")
        print(f"    Links OK       : {r['ok_count']}")
        print(f"    External       : {r['ext_count']}")
        if do_fix:
            print(f"    Fixed          : {len(fixed)}")
        print(f"    Broken total   : {len(broken)}")
        print(f"      fixable      : {len(found)}")
        print(f"      missing      : {len(missing)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fix", action="store_true",
                        help="Auto-fix wrong-path links")
    parser.add_argument("sections", nargs="*",
                        default=["docs/2.9", "docs/2026"],
                        help="Section directories to check")
    args = parser.parse_args()

    results = []
    for sec in args.sections:
        p = Path(sec)
        if not p.exists():
            print(f"WARNING: section not found: {sec}")
            continue
        result = check_and_fix_section(p, args.fix)
        results.append(result)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print_summary(results, args.fix)
    write_logs(results, args.fix)

    has_broken = any(r["broken"] for r in results)
    sys.exit(1 if has_broken else 0)


if __name__ == "__main__":
    main()
