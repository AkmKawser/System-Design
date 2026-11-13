"""
Ingestion & Category Manager Script for UMLSkill
Supports:
  - Checking pending items in 'Skills_Output/UMLSkill_output/Problem Files/Source of Problem/'
  - Inspecting files in 'put the file here/'
  - Reading dynamic categories and nested subcategories from 'problem categories.md'
  - Formatting entries into 'question bank.md' with chosen Category & Subcategory
  - Safe, non-destructive atomic cleanup ONLY after verified writes
"""

import os
import sys
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
PROBLEMS_DIR = REPO_ROOT / "Skills_Output" / "UMLSkill_output" / "Problem Files"
SOURCE_DIR = PROBLEMS_DIR / "Source of Problem"
PUT_DIR = SOURCE_DIR / "put the file here"
CATEGORIES_FILE = PROBLEMS_DIR / "problem categories.md"
QUESTION_BANK = PROBLEMS_DIR / "question bank.md"

def load_categories():
    """Dynamically loads categories from problem categories.md."""
    if not CATEGORIES_FILE.exists():
        return {
            "Structural Modeling": [("Class Diagrams & Domain Models", "Multiplicities, attributes, and relationships")],
            "Behavioral Modeling": [("State Machine & Lifecycle Transitions", "States, transitions, and guards")],
            "Interaction Dynamics": [("Sequence Diagrams & Synchronicity", "Lifelines, sync/async messages, and fragments")]
        }
    
    hierarchy = {}
    content = CATEGORIES_FILE.read_text(encoding="utf-8")
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("|") and not line.startswith("| #") and not line.startswith("| :---"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 4:
                primary = parts[1].replace("**", "").strip()
                subcat = parts[2].strip()
                desc = parts[3].strip()
                if primary not in hierarchy:
                    hierarchy[primary] = []
                if (subcat, desc) not in hierarchy[primary]:
                    hierarchy[primary].append((subcat, desc))
    return hierarchy

def list_categories():
    hierarchy = load_categories()
    print("=== Dynamic UML Problem Categories & Subcategories (from problem categories.md) ===")
    for idx, (primary, subcats) in enumerate(hierarchy.items(), 1):
        print(f"[{idx:02d}] 📁 {primary}")
        for s_idx, (sub_name, desc) in enumerate(subcats, 1):
            print(f"      ↳ [{idx}.{s_idx}] {sub_name} - {desc}")
    return hierarchy

def get_pending_files():
    if not PUT_DIR.exists():
        return []
    files = []
    for f in PUT_DIR.iterdir():
        if f.is_file() and not f.name.lower().startswith("readme") and not f.name.lower().startswith("."):
            files.append(f)
    return files

def show_status():
    files = get_pending_files()
    print("=== UML Problem Intake Queue Status ===")
    print(f"📁 Drop Zone ('put the file here/'): {len(files)} pending file(s)")
    for idx, f in enumerate(files, 1):
        print(f"   [{idx:02d}] 📄 {f.name} ({f.stat().st_size} bytes)")
    if not files:
        print("   (Queue is currently empty. Drop challenge files into 'put the file here/')")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UMLSkill Ingest Manager")
    parser.add_argument("--status", action="store_true", help="Display queue status")
    parser.add_argument("--categories", action="store_true", help="List dynamic categories")
    args = parser.parse_args()

    if args.categories:
        list_categories()
    else:
        show_status()

