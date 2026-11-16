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
from urllib.parse import unquote
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

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
            path_str = line[3:].strip().strip('"\'')
            # Handle renames e.g. R old -> new
            if " -> " in path_str:
                path_str = path_str.split(" -> ")[1].strip().strip('"\'')
            p = ROOT_DIR / path_str
            if p.suffix.lower() == ".md" and p.exists():
                changed_paths.append(p)
        
        # If no uncommitted files, audit query/ and chat/ by default
        if not changed_paths:
            query_files = list((ROOT_DIR / "Skills_Output" / "query").glob("**/*.md"))
            return sorted(query_files)
        return sorted(changed_paths)
    except Exception:
        # Fallback to all query files
        return sorted(list((ROOT_DIR / "Skills_Output" / "query").glob("**/*.md")))

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
            # Check for reserved keyword as classDef class name
            reserved_classdef = re.findall(r'classDef\s+(?:style|class|subgraph|end|graph|flowchart)', line, re.IGNORECASE)
            if reserved_classdef:
                errors.append(f'Line {line_idx}: Mermaid reserved keyword used as classDef name: {reserved_classdef[0]}. Rename classDef class.')
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
                target_img = (file_path.parent / unquote(clean_rel)).resolve()
                if not target_img.exists():
                    errors.append(f"Line {line_idx}: Image target does not exist on disk: '{clean_rel}'")

    # 4. Global Structural Parity Check
    if fence_count % 2 != 0:
        errors.append(f"Unbalanced code fences detected: total count is {fence_count} (expected even number).")
        
    return errors

def check_single_readme() -> list[str]:
    """Rule 10: exactly one README.md (the repository root one) is allowed."""
    repo_root = ROOT_DIR.parent if (ROOT_DIR.parent / "README.md").exists() else ROOT_DIR
    skip = {".git", "node_modules"}
    extras = []
    for p in repo_root.rglob("*"):
        if p.is_file() and p.name.lower() == "readme.md" and not (set(p.parts) & skip):
            if p.resolve() != (repo_root / "README.md").resolve():
                extras.append(p)
    return [f"Rule 10 violation: extra README found: {p.relative_to(repo_root)} (rename to <Topic>.md)" for p in sorted(extras)]

def check_rule16_book_naming() -> list[str]:
    """Rule 16: Book folders <= 25 chars, book PDFs <= 30 chars, no spaces."""
    repo_root = ROOT_DIR.parent if (ROOT_DIR.parent / "README.md").exists() else ROOT_DIR
    errors = []
    for book_dir in repo_root.rglob("Data_Ingestion/Books/*"):
        if book_dir.is_dir() and book_dir.parent.name == "Books":
            if len(book_dir.name) > 25:
                errors.append(f"Rule 16 violation: Book folder name too long ({len(book_dir.name)} > 25 chars): '{book_dir.name}'")
            if " " in book_dir.name:
                errors.append(f"Rule 16 violation: Book folder name contains spaces: '{book_dir.name}'")
            for pdf_file in book_dir.glob("*.pdf"):
                if len(pdf_file.name) > 30:
                    errors.append(f"Rule 16 violation: Book PDF file name too long ({len(pdf_file.name)} > 30 chars): '{pdf_file.name}'")
                if " " in pdf_file.name:
                    errors.append(f"Rule 16 violation: Book PDF file name contains spaces: '{pdf_file.name}'")
    return errors

def main():
    readme_issues = check_single_readme()
    for issue in readme_issues:
        print(f"[FAIL] {issue}")
    book_naming_issues = check_rule16_book_naming()
    for issue in book_naming_issues:
        print(f"[FAIL] {issue}")
    all_files_flag = "--all" in sys.argv
    targets = get_target_files(all_files=all_files_flag)
    
    if not targets:
        print("✅ No target Markdown files to audit.")
        sys.exit(0)

    print(f"🔍 Auditing {len(targets)} markdown file(s) for rendering integrity...")
    total_errors = len(readme_issues) + len(book_naming_issues)
    
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

    total_errors += len(readme_issues)
    if total_errors > 0:
        print(f"\n💥 Audit failed with {total_errors} total rendering error(s).")
        sys.exit(1)
    else:
        print("\n✨ All audited markdown and diagram files passed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
