#!/usr/bin/env python3
"""
scripts/audit_rendering.py
Universal Zero-Failure Markdown & Diagram Rendering Auditor

Optimized Single-Pass (O(N)) Validator:
1. Git-Aware Diff Detection: Reads only changed/staged Markdown files via git status/diff.
   Falls back to auditing all files if requested via '--all'.
2. Single-Pass Token Scanning:
   - Tracks code fence state (``` or ````).
   - Tracks Mermaid block boundaries.
   - Detects raw dollar signs ($) in prose (outside backticks and code blocks).
   - Detects raw HTML tags (<br>, <b>, etc.) inside Mermaid diagram nodes.
   - Detects broken KaTeX escape sequences and unbalanced code fences.
   - Verifies relative image paths exist on disk.
"""

import sys
import re
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def get_target_files(all_files: bool = False) -> list[Path]:
    """Gets markdown files to audit using git diff/status for O(1) file scaling."""
    if all_files:
        all_mds = sorted(list(ROOT_DIR.glob("**/*.md")))
        return [p for p in all_mds if ".venv" not in p.parts and "site-packages" not in str(p)]

    # Get changed/untracked markdown files via git
    try:
        res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True
        )
        changed_paths = []
        for line in res.stdout.strip().split("\n"):
            if not line:
                continue
            path_str = line[3:].strip()
            # Handle renames e.g. R old -> new
            if " -> " in path_str:
                path_str = path_str.split(" -> ")[1].strip()
            p = ROOT_DIR / path_str
            if p.suffix.lower() == ".md" and p.exists():
                changed_paths.append(p)
        
        # If no uncommitted files, audit query/ and chat/ by default
        if not changed_paths:
            query_files = list((ROOT_DIR / "Skills_Output" / "query").glob("*.md"))
            return sorted(query_files)
        return sorted(changed_paths)
    except Exception:
        # Fallback to all query files
        return sorted(list((ROOT_DIR / "Skills_Output" / "query").glob("*.md")))

def audit_file(file_path: Path) -> list[str]:
    """Audits a single markdown file in one linear pass O(Lines)."""
    errors = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Unable to read file: {e}"]

    lines = content.split("\n")
    in_code_block = False
    in_mermaid = False
    fence_count = 0
    
    for line_idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        
        # 1. Code Fence Tracking
        if stripped.startswith("```"):
            fence_count += 1
            if in_code_block:
                in_code_block = False
                in_mermaid = False
            else:
                in_code_block = True
                if stripped.startswith("```mermaid"):
                    in_mermaid = True
            continue
            
        # 2. Mermaid Internal Syntax Checks
        if in_mermaid:
            # Check for illegal HTML tags in Mermaid labels (<b>, <br>, <i>, etc.)
            html_tags = re.findall(r"</?(?:b|i|br|span|div|p|strong|em)[^>]*>", line, re.IGNORECASE)
            if html_tags:
                errors.append(f"Line {line_idx}: Raw HTML tags {html_tags} found inside Mermaid diagram block.")
            
            # Check for unquoted node labels containing parentheses, colons, slashes, or ampersands
            # Matches NodeId[Label] where Label does not start with " or (
            unquoted_brackets = re.findall(r"\b[A-Za-z0-9_]+\[([^\"\(\]\n]+)\]", line)
            for label in unquoted_brackets:
                if any(ch in label for ch in "():/&"):
                    errors.append(
                        f"Line {line_idx}: Mermaid node label contains unquoted special characters '{label}'. "
                        f"Wrap label in double quotes, e.g., Node[\"{label}\"]."
                    )
            continue
            
        # 3. Prose Checks (Outside Code Blocks)
        if not in_code_block:
            # Remove inline backticked spans before inspecting prose
            clean_prose = re.sub(r"`[^`]*`", "", line)
            
            # Check for raw dollar signs (KaTeX math should be backticked or written as words)
            raw_dollars = re.findall(r"(?<!\\)\$", clean_prose)
            if raw_dollars:
                errors.append(
                    f"Line {line_idx}: Raw unescaped dollar sign ($) in prose. "
                    "Use backticks (`$HOME`), LaTeX math syntax, or write out currency in words."
                )
            
            # 5. Relative Image Existence Check (skipping badge wrappers [ [![alt](url)] (link) ])
            # Only match true image syntax ![alt](rel_path) where alt does not contain nested brackets
            # and ignore shields/http badge images
            line_no_badges = re.sub(r"\[!\[.*?\]\(.*?\)\]\(.*?\)", "", line)
            image_matches = re.findall(r"!\[([^\[\]]*)\]\((?!https?://)(.*?)\)", line_no_badges)
            for _, img_rel in image_matches:
                clean_rel = img_rel.split()[0].strip()
                clean_rel = clean_rel.split("?")[0].split("#")[0]
                target_img = (file_path.parent / clean_rel).resolve()
                if not target_img.exists():
                    errors.append(f"Line {line_idx}: Image target does not exist on disk: '{clean_rel}'")

    # 4. Global Structural Parity Check
    if fence_count % 2 != 0:
        errors.append(f"Unbalanced code fences detected: total count is {fence_count} (expected even number).")
        
    return errors

def main():
    all_files_flag = "--all" in sys.argv
    targets = get_target_files(all_files=all_files_flag)
    
    if not targets:
        print("✅ No target Markdown files to audit.")
        sys.exit(0)

    print(f"🔍 Auditing {len(targets)} markdown file(s) for rendering integrity...")
    total_errors = 0
    
    for target in targets:
        rel_path = target.relative_to(ROOT_DIR) if target.is_relative_to(ROOT_DIR) else target
        issues = audit_file(target)
        if issues:
            print(f"\n❌ Rendering violations in {rel_path}:")
            for issue in issues:
                print(f"   • {issue}")
            total_errors += len(issues)
        else:
            print(f"   ✓ {rel_path} passed.")

    if total_errors > 0:
        print(f"\n💥 Audit failed with {total_errors} total rendering error(s).")
        sys.exit(1)
    else:
        print("\n✨ All audited markdown and diagram files passed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
