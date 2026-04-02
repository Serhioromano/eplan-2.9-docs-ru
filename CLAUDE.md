# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Russian-language documentation site for EPLAN 2026, built with MkDocs Material. The docs are scraped/converted from the official EPLAN help portal and served as a static site via GitHub Pages.

## Common Commands

- `make init` — install Python dependencies (mkdocs, mkdocs-material, plugins)
- `make serve` — start local dev server (`mkdocs serve`)
- `make deploy` — deploy to GitHub Pages (`mkdocs gh-deploy`)

## Architecture

- **docs/eplan/** — Markdown documentation files scraped from EPLAN help. Filenames correspond to EPLAN help URLs (`.htm` → `.md`).
- **tree/** — Scraping/parsing tooling. `db1.js`–`db9.js` contain indexed page data from EPLAN help. `root.js` has the TOC tree structure. `build-tree.js` parses these to generate `tree.json`.
- **tree.json** — Generated TOC structure mapping titles to URLs. Used to build the `nav:` section in `mkdocs.yml`.
- **mkdocs.yml** — Site config. Uses Material theme with Russian locale. Requires `GH_TOKEN` env var for git-committers plugin.
- **PROMPTS.md** — Contains the AI prompt template for rewriting docs into beginner-friendly voiceover scripts (Russian).

## Content Conventions

- Language: all docs are in Russian
- Keyboard keys use pymdownx.keys format: `++alt++`, `++ctrl+s++` (not plain text like "Alt")
- Markdown extensions in use: admonition, superfences, keys, snippets, tasklist, highlight, details
- Abbreviations are auto-appended from `docs/includes/abbreviations.md`
