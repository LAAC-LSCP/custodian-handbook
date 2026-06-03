#!/usr/bin/env python3
"""
Custodian Handbook Builder
===========================
Reads all markdown files from ./sections/, converts them to HTML,
injects them into template.html, and writes a single self-contained
custodian-handbook.html.

Usage:
    python build.py

Output:
    custodian-handbook.html
"""

import os
import glob
import json
import markdown
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────

SECTIONS_DIR  = "sections"
TEMPLATE_FILE = "template.html"
OUTPUT_FILE   = "custodian-handbook.html"
SITE_TITLE    = "Custodian Handbook"
FOOTER_TEXT   = "ExELang Project — Custodian Handbook"

# Sidebar labels: map filename stem → display name.
# Add or rename entries here when you add new sections.
SECTION_LABELS = {
    "00_landing":          "Introduction",
    "01_administer_elsi":  "Administer ELSI",
    "02_onboard_student":  "Onboard a New Student",
    "03_cite_data":        "Citation practices",
    "04_add_tools":        "Add Models to ELSI",
    "05_use_ExELang_data":        "Work with the data",
}

# ── Helpers ──────────────────────────────────────────────────────────────────

def slug(filepath: str) -> str:
    """Derive a stable HTML id from a filename stem."""
    return Path(filepath).stem.lstrip("0123456789_").replace("_", "-")

# ── Load & convert sections ──────────────────────────────────────────────────

def load_sections() -> list[dict]:
    files = sorted(glob.glob(os.path.join(SECTIONS_DIR, "*.md")))
    if not files:
        raise FileNotFoundError(f"No .md files found in '{SECTIONS_DIR}/'")

    md = markdown.Markdown(extensions=["extra", "toc", "fenced_code"])
    sections = []

    for f in files:
        stem = Path(f).stem
        label = SECTION_LABELS.get(stem, stem.replace("_", " ").title())
        with open(f, encoding="utf-8") as fh:
            raw = fh.read()
        md.reset()
        sections.append({
            "id":    slug(f),
            "label": label,
            "html":  md.convert(raw),
        })

    return sections

# ── Assemble HTML from template ──────────────────────────────────────────────

def build_sidebar(sections: list[dict]) -> str:
    items = []
    for i, s in enumerate(sections):
        css = "active-sidebar-btn" if i == 0 else "inactive-sidebar-btn"
        items.append(
            f'<button class="{css}" onclick="scrollToSection(\'{s["id"]}\')">'
            f'{s["label"]}</button>'
        )
    return "\n        ".join(items)

def build_content(sections: list[dict]) -> str:
    blocks = []
    for s in sections:
        blocks.append(
            f'<section id="{s["id"]}" class="docs-page-container">\n'
            f'  {s["html"]}\n'
            f'</section>'
        )
    return "\n\n      ".join(blocks)

def render(sections: list[dict]) -> str:
    with open(TEMPLATE_FILE, encoding="utf-8") as fh:
        template = fh.read()

    replacements = {
        "{{SITE_TITLE}}":     SITE_TITLE,
        "{{FOOTER_TEXT}}":    FOOTER_TEXT,
        "{{SIDEBAR_ITEMS}}":  build_sidebar(sections),
        "{{CONTENT_BLOCKS}}": build_content(sections),
        "{{SECTION_IDS}}":    json.dumps([s["id"] for s in sections]),
    }

    output = template
    for placeholder, value in replacements.items():
        output = output.replace(placeholder, value)

    return output

# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sections = load_sections()
    html     = render(sections)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✓ Built {OUTPUT_FILE} ({len(sections)} sections, {len(html):,} bytes)")
    for s in sections:
        print(f"  • [{s['id']}] {s['label']}")
