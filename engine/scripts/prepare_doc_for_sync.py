#!/usr/bin/env python3
"""
engine/scripts/prepare_doc_for_sync.py
Automated Document Preparation & Diagram Compiler Engine

Enforces Universal Rule 18 & Rule 19:
1. Compiles all raw Mermaid code blocks (```mermaid ... ```) into 2x high-resolution PNGs
   using Playwright Chromium and offline cached mermaid.min.js.
2. Formats all diagram filenames with strict HYPHENS ('-'), never underscores ('_'),
   preventing Markdown emphasis/italics URL parsing collisions.
3. Isolates every diagram image on its own dedicated paragraph followed by a clean
   divider ('---'), preventing image-text paragraph merging and wrapping in Google Docs.
4. Strips any bare '---' lines that directly precede '#' headings, eliminating all
   empty Setext heading artifacts (HEADING_2/3 "") in Google Docs.
5. Enforces strict LF ('\n') line endings, preventing Google Drive API UTF-16 character offset drift.

Usage:
  python engine/scripts/prepare_doc_for_sync.py <path/to/markdown.md>
  python engine/scripts/prepare_doc_for_sync.py --all
"""

import os
import re
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CACHE_DIR = ROOT_DIR / "engine" / "scripts" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
MERMAID_JS = CACHE_DIR / "mermaid.min.js"

def ensure_mermaid_js():
    """Ensures mermaid.min.js is cached locally for fast, offline rendering."""
    if not MERMAID_JS.exists():
        import urllib.request
        print("Downloading mermaid.min.js for offline renderer...")
        url = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            MERMAID_JS.write_bytes(resp.read())
        print(f"Cached mermaid.min.js ({MERMAID_JS.stat().st_size} bytes)")

def clean_slug(text: str) -> str:
    """Converts a title or text into a clean hyphenated filename slug."""
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    slug = re.sub(r"[\s_]+", "-", slug_candidate := text)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug[:40] if slug else "diagram"

def prepare_markdown_file(md_path: Path):
    """Processes a single markdown file for Google Docs sync."""
    md_path = md_path.resolve()
    if not md_path.exists():
        print(f"Error: file not found: {md_path}")
        return False

    print(f"\n=======================================================")
    print(f"Processing: {md_path.relative_to(ROOT_DIR) if md_path.is_relative_to(ROOT_DIR) else md_path}")
    print(f"=======================================================")

    images_dir = md_path.parent / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    ensure_mermaid_js()
    mermaid_js_code = MERMAID_JS.read_text(encoding="utf-8")

    content = md_path.read_text(encoding="utf-8")
    mermaid_matches = list(re.finditer(r"```mermaid\n([\s\S]*?)\n```", content))

    if mermaid_matches:
        print(f"Found {len(mermaid_matches)} raw Mermaid diagram block(s) to compile.")

        render_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
{mermaid_js_code}
</script>
<style>
  body {{
    margin: 0;
    padding: 20px;
    background-color: white;
    display: inline-block;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}
  #graph {{
    background-color: white;
    max-width: 860px;
  }}
</style>
</head>
<body>
<div id="graph"></div>
<script>
  mermaid.initialize({{
    startOnLoad: false,
    theme: 'default',
    flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'basis' }},
    themeVariables: {{
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
      fontSize: '14px'
    }}
  }});
  async function renderMermaid(code) {{
    try {{
      document.getElementById('graph').innerHTML = '';
      const id = 'svg_' + Math.random().toString(36).substring(2, 9);
      const {{ svg }} = await mermaid.render(id, code);
      document.getElementById('graph').innerHTML = svg;
      return {{ success: true }};
    }} catch (err) {{
      return {{ success: false, error: err.toString() }};
    }}
  }}
</script>
</body>
</html>"""

        html_runner = CACHE_DIR / "render_runner.html"
        html_runner.write_text(render_html, encoding="utf-8")

        rendered_replacements = []

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(device_scale_factor=2)
            page.goto(f"file:///{html_runner.resolve().as_posix()}")

            for i, match in enumerate(mermaid_matches):
                code = match.group(1).strip()
                # Find preceding heading for diagram title
                preceding_text = content[:match.start()]
                headings = [h.group(1).strip() for h in re.finditer(r"#{1,4}\s+([^\n]+)", preceding_text)]
                title = headings[-1] if headings else f"diagram-{i+1}"
                # Clean title if it contains generic diagram label
                if "diagram" in title.lower() and len(headings) > 1:
                    title = headings[-2]
                
                slug = f"{i+1:02d}-{clean_slug(title)}.png"
                target_png = images_dir / slug

                res = page.evaluate("renderMermaid", code)
                if not res.get("success"):
                    print(f"  [WARN] Failed to render diagram {i+1} ({slug}): {res.get('error')}")
                    continue

                page.wait_for_selector("#graph svg")
                svg_locator = page.locator("#graph svg")
                svg_locator.screenshot(path=str(target_png))
                print(f"  [OK] Rendered {slug} ({target_png.stat().st_size} bytes)")

                replacement = f"![{title} Architecture Diagram](images/{slug})"
                rendered_replacements.append((match.start(), match.end(), replacement))

            browser.close()

        # Clean up runner HTML
        if html_runner.exists():
            html_runner.unlink()

        # Replace Mermaid blocks from end to start
        for start, end, repl in reversed(rendered_replacements):
            content = content[:start] + repl + content[end:]

    # 2. Structural Layout Hygiene:
    # A. Strip any '---' that directly precedes an ATX heading (#)
    content = re.sub(r"---\s*\n+(\#{1,4}\s+[^\n]+)", r"\1", content)

    # B. Ensure every image is followed by a dedicated divider '---'
    # This prevents image-text paragraph concatenation in Google Docs
    def format_image_node(match):
        img_line = match.group(1).strip()
        return f"\n\n{img_line}\n\n---\n\n"

    content = re.sub(r"(!\[[^\]]+\]\(images/[^\)]+\))\s*\n*(?:---\s*\n*)?", format_image_node, content)

    # C. Normalize multiple blank lines to double newlines
    content = re.sub(r"\n{3,}", "\n\n", content)

    # D. Write back with strict LF newlines
    md_path.write_text(content, encoding="utf-8", newline="\n")
    print(f"  ✓ Layout polished with clean image dividers & zero empty Setext headings.")
    return True

def main():
    if len(sys.argv) < 2:
        # Default to the complete architectural patterns catalog if no argument
        default_file = ROOT_DIR / "topics" / "0.FUNDAMENTALS" / "Software Architecture and Modeling" / "1.ARCHITECTURE" / "2. Architecture Patterns" / "output" / "query_Architecture_Patterns" / "003_complete_architectural_patterns_catalog.md"
        if default_file.exists():
            prepare_markdown_file(default_file)
        else:
            print("Usage: python engine/scripts/prepare_doc_for_sync.py <path_to_markdown_file>")
        sys.exit(0)

    target_arg = sys.argv[1]
    if target_arg == "--all":
        query_files = list(ROOT_DIR.glob("topics/**/output/**/*.md"))
        for f in sorted(query_files):
            prepare_markdown_file(f)
    else:
        prepare_markdown_file(Path(target_arg))

if __name__ == "__main__":
    main()
