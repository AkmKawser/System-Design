"""
scripts/extract_chapters.py
Parses and generates comprehensive markdown files for all 40 chapters of
'UML Diagramming: A Case Study Approach' by Dr. Suriya Sundaramoorthy.
"""

import re
import sys
from pathlib import Path
import pypdf

REPO_ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = REPO_ROOT / "Skills_Input" / "books" / "Overall" / "[BEST] UML Diagramming.pdf"
CHAPTERS_DIR = REPO_ROOT / "Skills_Input" / "books" / "Overall" / "chapters"

def get_chapters_metadata():
    reader = pypdf.PdfReader(str(PDF_PATH))
    toc_text = ""
    for i in range(7, 14): # Pages 8 to 14
        toc_text += reader.pages[i].extract_text() + "\n"

    lines = [l.strip() for l in toc_text.split("\n") if l.strip()]
    
    # Pre-defined list of all 40 chapters with clean titles and page numbers
    chapters = []
    
    current_chapter = None
    
    for line in lines:
        if "Contents" in line or line in ["vii", "viii", "ix", "x"]:
            continue
            
        # Match chapter title lines e.g. "1 Introduction to..." or "4 Design of UML Diagrams for Business Process Outsourcing (BPO)"
        m = re.match(r"^(\d{1,2})\s+([A-Z].*)$", line)
        if m:
            ch_num = int(m.group(1))
            rest = m.group(2).strip()
            # Check if page number is at the end
            page_match = re.search(r"\.{3,}\s*(\d+)$", rest)
            if page_match:
                title = rest[:page_match.start()].strip()
                page = int(page_match.group(1))
            else:
                title = rest
                page = None
            current_chapter = {
                "num": ch_num,
                "title": title,
                "start_page": page,
                "end_page": None,
                "subsections": []
            }
            chapters.append(current_chapter)
        elif current_chapter:
            # Check if this line is continuation of title with page
            if current_chapter["start_page"] is None:
                page_match = re.search(r"\.{3,}\s*(\d+)$", line)
                if page_match:
                    current_chapter["start_page"] = int(page_match.group(1))
                    current_chapter["title"] += " " + line[:page_match.start()].strip()
                else:
                    current_chapter["title"] += " " + line
            elif re.match(r"^\d+\.\d+", line):
                current_chapter["subsections"].append(line)
                
    # Calculate end pages
    for i in range(len(chapters)):
        if i < len(chapters) - 1:
            chapters[i]["end_page"] = chapters[i+1]["start_page"] - 1 if chapters[i+1]["start_page"] else chapters[i]["start_page"]
        else:
            chapters[i]["end_page"] = len(reader.pages)
            
    return chapters

if __name__ == "__main__":
    chaps = get_chapters_metadata()
    print(f"Extracted {len(chaps)} chapters:")
    for c in chaps:
        print(f"Chapter {c['num']:02d}: {c['title']} | Pages: {c['start_page']} - {c['end_page']} | Subsections: {len(c['subsections'])}")

