#!/usr/bin/env python3
"""Clean up markdown files in docs/new/:
1. Reformat 'См. также' section (bold, colon, list, no blank lines between links)
2. Collapse multiple blank lines into one
3. Remove leading whitespace from list items (* and 1., 2., etc.)
4. Delete everything before the first ## heading
5. Change .htm to .md in markdown links
6. Convert javascript: links to plain text
7. Convert button references [Text] to ++Text++ (pymdownx.keys format)
8. Delete transparent.gif / javascript:void lines (collapsed section headers)
9. Convert arrow.png lines to admonition info blocks
10. Add { .ui-icon } to inline images smaller than 20x20 px (via Pillow)
11. Unwrap clickable thumbnails [![](thumb)](../Pictures/.../full.png) → ![](images/full.png),
    downloading the full image to images/ if not already present.
"""

import re
import glob
import urllib.request
from pathlib import Path

try:
    from PIL import Image as _PILImage
    _USE_PIL = True
except ImportError:
    import struct
    _USE_PIL = False

def fix_see_also(content):
    """Reformat 'См. также' sections."""
    pattern = re.compile(
        r'^См\. также\s*\n'
        r'((?:\s*\n)*'
        r'(?:\[.+?\]\(.+?\)\s*\n(?:\s*\n)*)+)',
        re.MULTILINE
    )
    def reformat(match):
        block = match.group(1)
        links = re.findall(r'(\[.+?\]\(.+?\))', block)
        result = '**См. также:**\n\n'
        result += '\n'.join(f'* {link}' for link in links) + '\n'
        return result
    return pattern.sub(reformat, content)

def collapse_blank_lines(content):
    """Replace multiple consecutive blank lines (including whitespace-only lines) with a single blank line."""
    # First, strip trailing whitespace from every line so whitespace-only lines become truly empty
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    # Then collapse runs of 2+ empty lines into one
    return re.sub(r'\n{3,}', '\n\n', content)

def strip_list_indent(content):
    """Remove leading whitespace from list items (* and numbered),
    but preserve indent inside admonition blocks."""
    ADM_RE = re.compile(r'^(!{3}|\?{3})')
    lines = content.splitlines(keepends=True)
    in_admonition = False
    body_started = False
    result = []
    for line in lines:
        stripped = line.rstrip('\n\r')
        if ADM_RE.match(stripped):
            in_admonition = True
            body_started = False
            result.append(line)
            continue
        if in_admonition:
            if stripped == '':
                # Empty line: end admonition only after body has started
                if body_started:
                    in_admonition = False
                result.append(line)
                continue
            if stripped.startswith('    '):
                # Admonition content — keep as-is
                body_started = True
                result.append(line)
                continue
            # Non-indented non-empty line ends admonition
            in_admonition = False
        # Strip excess indent from list items
        line = re.sub(r'^[ \t]+(\* )', r'\1', line)
        line = re.sub(r'^[ \t]+(\d+\. )', r'\1', line)
        result.append(line)
    return ''.join(result)

def delete_before_first_heading(content):
    """Delete everything before the first ## heading and make it level 1."""
    match = re.search(r'^## ', content, re.MULTILINE)
    if match:
        content = content[match.start():]
        # Change first ## to #
        content = '# ' + content[3:]
    return content

def fix_glossary_links(content):
    """Convert [text](Glossary_o_*.md) links to plain text."""
    return re.sub(r'\[([^\]]+)\]\(Glossary_o_[^)]+\.md\)', r'\1', content)

def fix_javascript_links(content):
    """Convert [text](javascript:...) links to plain text, remove empty ones."""
    content = re.sub(r'\[([^\]]+)\]\(javascript:[^)]*\);?\)?', r'\1', content)
    content = re.sub(r'\[\]\(javascript:[^)]*\);?\)?', '', content)
    return content

def fix_stray_semicolon_paren(content):
    """Remove leftover ;) artifacts from escaped javascript links."""
    return re.sub(r';\)', '', content)

def fix_htm_links(content):
    """Change .htm to .md in internal markdown links and remove #fragment anchors."""
    content = re.sub(r'\]\((?!https?://)([^)]+)\.htm(#[^)]*)?\)', r'](\1.md)', content)
    return content

def fix_arrow_admonitions(content):
    """Convert ![](images/arrow*.png) lines to !!! info admonition blocks."""
    pattern = re.compile(r'^!\[[^\]]*\]\(images/arrow[^)]*\)\s*(.+)$', re.MULTILINE)
    def replace(m):
        text = m.group(1).strip()
        return f'\n\n!!! info "Для сведения:"\n\n    {text}\n'
    content = pattern.sub(replace, content)
    return content

def delete_transparent_gif_lines(content):
    """Delete lines with transparent.gif + javascript:void (collapsed section headers from EPLAN help)."""
    content = re.sub(r'^.*\[!\[[^\]]*\]\([^)]*transparent\.gif\)[^\]]*\]\(javascript:void\\\(0\\\).*\n?', '', content, flags=re.MULTILINE)
    return content

def _load_small_images(images_dir='docs/eplan/images'):
    """Return set of image filenames that are smaller than 20x20 px."""
    small = set()
    exts = ('*.png', '*.jpg', '*.jpeg', '*.gif', '*.webp')
    paths = []
    for ext in exts:
        paths.extend(Path(images_dir).glob(ext))
    for p in paths:
        try:
            if _USE_PIL:
                with _PILImage.open(p) as img:
                    w, h = img.size
            else:
                with open(p, 'rb') as f:
                    raw = f.read(24)
                if raw[:8] == b'\x89PNG\r\n\x1a\n' and raw[12:16] == b'IHDR':
                    w = struct.unpack('>I', raw[16:20])[0]
                    h = struct.unpack('>I', raw[20:24])[0]
                else:
                    continue
            if w < 20 and h < 20:
                small.add(p.name)
        except Exception:
            pass
    return small

_SMALL_IMAGES = set()

def fix_ui_icons(content):
    """Add { .ui-icon } to inline image refs where image is < 20x20 px."""
    img_re = re.compile(r'!\[([^\]]*)\]\((images/([^)]+\.(png|jpg|jpeg|gif|webp)))\)(?!\s*\{)')
    strip_re = re.compile(r'!\[[^\]]*\]\([^)]*\)(\s*\{[^}]*\})?')

    def process_line(line):
        remainder = strip_re.sub('', line).strip()
        if remainder == '':
            return line  # standalone image line — skip
        def replace(m):
            if m.group(3) in _SMALL_IMAGES:
                return m.group(0) + '{: .ui-icon }'
            return m.group(0)
        return img_re.sub(replace, line)

    return '\n'.join(process_line(l) for l in content.split('\n'))

def fix_image_spacing(content):
    """Ensure standalone image lines have one empty line above and below."""
    strip_re = re.compile(r'!\[[^\]]*\]\([^)]*\)(\s*\{[^}]*\})?')
    lines = content.split('\n')
    result = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        is_standalone = bool(stripped) and '![' in line and strip_re.sub('', stripped).strip() == ''
        if is_standalone:
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            if i + 1 < len(lines) and lines[i + 1].strip() != '':
                result.append('')
        else:
            result.append(line)
    return '\n'.join(result)

def fix_merged_words(content):
    """Insert space between a lowercase Cyrillic letter and an uppercase one (merged words)."""
    return re.sub(r'([а-яё])([А-ЯЁ])', r'\1 \2', content)

def fix_button_brackets(content):
    """Convert button references like кнопке [OK] to кнопке ++OK++ (pymdownx.keys format)."""
    def replace_btn(m):
        prefix = m.group(1).rstrip()
        text = m.group(2).strip()
        return f'{prefix} ++{text}++'
    content = re.sub(
        r'((?:кнопк[еуиойам]|нажмите|клавиш[еуиой]|нажав|щелкните|нажатием|помощи|выберите|меню|на|по|или)\s?)\[([^\]]+)\](?!\()',
        replace_btn,
        content,
        flags=re.IGNORECASE
    )
    # Replace "F1"-"F12" with ++F1++-++F12++
    content = re.sub(r'"(F\d{1,2})"', r'++\1++', content)
    # Replace literal <...> with ++...++
    content = content.replace('<...>', '++...++')
    # Fix spacing around ++key++ blocks
    def fix_keys(m):
        pre = m.group(1)
        key = m.group(2).strip()
        post = m.group(3)
        if pre and pre not in (' ', '\t', '\n'):
            pre = pre + ' '
        if post and post not in (' ', '\t', '\n', '.', ',', ';', ':', '!', '?', ')', ']', '\r'):
            post = ' ' + post
        return f'{pre}++{key}++{post}'
    content = re.sub(r'(.|^)\s*\+\+\s*([^+]+?)\s*\+\+\s?(.?)', fix_keys, content)
    return content

_HTML_TAGS = {
    'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
    'b', 'base', 'bdi', 'bdo', 'blockquote', 'body', 'br', 'button',
    'canvas', 'caption', 'cite', 'code', 'col', 'colgroup',
    'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'div', 'dl', 'dt',
    'em', 'embed',
    'fieldset', 'figcaption', 'figure', 'footer', 'form',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hr', 'html',
    'i', 'iframe', 'img', 'input', 'ins',
    'kbd', 'label', 'legend', 'li', 'link',
    'main', 'map', 'mark', 'menu', 'meta', 'meter',
    'nav', 'noscript',
    'object', 'ol', 'optgroup', 'option', 'output',
    'p', 'param', 'picture', 'pre', 'progress',
    'q', 'rp', 'rt', 'ruby',
    's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span',
    'strong', 'style', 'sub', 'summary', 'sup',
    'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead',
    'time', 'title', 'tr', 'track',
    'u', 'ul', 'var', 'video', 'wbr',
}

_PLACEHOLDER_TAG_RE = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)(/?)>')

def escape_placeholder_tags(content):
    """Escape <x>, <y> etc. (non-HTML placeholder tags with only ASCII letters) as \\<x\\>."""
    # Process line by line, skip code blocks and inline code
    lines = content.split('\n')
    in_fence = False
    result = []
    for line in lines:
        if re.match(r'^```', line):
            in_fence = not in_fence
        if in_fence or line.startswith('    '):
            result.append(line)
            continue
        # Skip inline code spans before replacing
        def replace_tag(m):
            slash = m.group(1)
            tag = m.group(2).lower()
            self_close = m.group(3)
            if tag in _HTML_TAGS:
                return m.group(0)
            inner = f'{slash}{m.group(2)}{self_close}'
            return f'\\<{inner}\\>'
        # Protect inline code, process rest
        parts = re.split(r'(`[^`]*`)', line)
        new_parts = []
        for part in parts:
            if part.startswith('`') and part.endswith('`'):
                new_parts.append(part)
            else:
                new_parts.append(_PLACEHOLDER_TAG_RE.sub(replace_tag, part))
        result.append(''.join(new_parts))
    return '\n'.join(result)


# ── Clickable thumbnail unwrapper ────────────────────────────────────────────
# Matches: [![](images/NAME_thumb_0_60.png)](../Pictures/Sub/Dir/NAME.png)
_THUMB_RE = re.compile(
    r'\[!\[([^\]]*)\]\(images/[^)]+\)\]'   # [![](images/thumb.png)]
    r'\((\.\./[^)]+\.png)\)'               # (../Pictures/.../real.png)
)
_EPLAN_PICS_BASE = "https://eplan.help/ru-ru/Infoportal/Content/Plattform/2.9/Content/"

def fix_thumbnails(content, images_dir):
    """Replace [![](thumb)](../Pictures/.../full.png) with ![](images/full.png),
    downloading full.png to images_dir if not already present."""
    images_dir = Path(images_dir)

    def replace(m):
        alt = m.group(1)
        rel_path = m.group(2)       # ../Pictures/Gui/Lang/foo.png
        fname = Path(rel_path).name # foo.png
        dest = images_dir / fname

        if not dest.exists():
            clean = re.sub(r'^(\.\./)+', '', rel_path)
            url = _EPLAN_PICS_BASE + clean
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                data = urllib.request.urlopen(req, timeout=20).read()
                dest.write_bytes(data)
            except Exception as e:
                print(f"  WARN: could not download {url}: {e}")
                return m.group(0)

        return f'![{alt}](images/{fname})'

    return _THUMB_RE.sub(replace, content)


def process_file(path, images_dir=None):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    _idir = images_dir or str(Path(path).parent / 'images')
    original = content
    content = fix_thumbnails(content, _idir)
    content = delete_before_first_heading(content)
    content = delete_transparent_gif_lines(content)
    content = fix_see_also(content)
    content = strip_list_indent(content)
    content = fix_glossary_links(content)
    content = fix_javascript_links(content)
    content = fix_stray_semicolon_paren(content)
    content = fix_htm_links(content)
    content = fix_merged_words(content)
    content = fix_button_brackets(content)
    content = escape_placeholder_tags(content)
    content = fix_arrow_admonitions(content)
    content = fix_ui_icons(content)
    content = fix_image_spacing(content)
    content = collapse_blank_lines(content)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

import sys

docs_dir = sys.argv[1] if len(sys.argv) > 1 else 'docs/new'
images_dir = sys.argv[2] if len(sys.argv) > 2 else f'{docs_dir}/images'

_SMALL_IMAGES = _load_small_images(images_dir)

count = 0
for path in sorted(glob.glob(f'{docs_dir}/*.md') + glob.glob(f'{docs_dir}/**/*.md')):
    if process_file(path, images_dir):
        count += 1

print(f'Updated {count} files')
