"""
Precision Query CLI for UML25Spec
"""
import sys
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[4]
SOURCE_DIR = BASE_DIR / "Skills_Input/books"

def search_resource(keyword):
    print(f"🔍 Searching UML25Spec for keyword: '{keyword}'...")
    matches = []
    if not SOURCE_DIR.exists():
        print(f"⚠️ Source directory does not exist yet: {SOURCE_DIR}")
        return
    for file in SOURCE_DIR.rglob("*.*"):
        if file.suffix.lower() in [".md", ".txt", ".puml", ".java", ".json", ".pdf"]:
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if keyword.lower() in content.lower():
                        matches.append(file)
            except:
                pass
    print(f"Found {len(matches)} matching files:")
    for m in matches[:10]:
        print(f"  📄 {m.relative_to(BASE_DIR)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query UML25Spec resources")
    parser.add_argument("keyword", help="Keyword to search")
    args = parser.parse_args()
    search_resource(args.keyword)
