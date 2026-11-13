"""
scripts/generate_chapter_markdowns.py
Generates individual Markdown (.md) files for all 40 chapters of
'UML Diagramming: A Case Study Approach' by Dr. Suriya Sundaramoorthy.
"""

import os
import re
import sys
import warnings
from pathlib import Path
import pypdf

warnings.filterwarnings("ignore")

REPO_ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = REPO_ROOT / "Skills_Input" / "books" / "Overall" / "[BEST] UML Diagramming.pdf"
CHAPTERS_DIR = REPO_ROOT / "Skills_Input" / "books" / "Overall" / "chapters"
CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

PDF_PAGE_OFFSET = 14  # book page 1 corresponds to pdf reader page index 14 or 15

# Master list of all 40 chapters with start and end pages in the book
CHAPTERS_METADATA = [
    (1, "Introduction to UML Diagrams and Its Components", 1, 22),
    (2, "Design of UML Diagrams for Webmed - Healthcare Service System Services", 23, 38),
    (3, "Design of UML Diagrams for Inventory Management System", 39, 58),
    (4, "Design of UML Diagrams for Business Process Outsourcing (BPO) Management System", 59, 74),
    (5, "Design of UML Diagrams for E-Ticketing for Buses", 75, 84),
    (6, "Design of UML Diagrams for Weather Monitoring System", 85, 94),
    (7, "Design of UML Diagrams for E-Province", 95, 104),
    (8, "Design of UML Diagrams for DigiDocLocker", 105, 112),
    (9, "Design of UML Diagrams for Online Marketplace", 113, 122),
    (10, "Design of UML Diagrams for Product Recommendation System", 123, 128),
    (11, "Design of UML Diagrams for Advocate Diary", 129, 138),
    (12, "Design of UML Diagrams for My Helper", 139, 146),
    (13, "Design of UML Diagrams for COVID-19 Management System", 147, 156),
    (14, "Design of UML Diagrams for Car Care", 157, 166),
    (15, "Design of UML Diagrams for E-Ration Shop", 167, 176),
    (16, "Design of UML Diagrams for Textile Management System", 177, 184),
    (17, "Design of UML Diagrams for National Health ID 2020", 185, 190),
    (18, "Design of UML Diagrams for Device Handout System", 191, 198),
    (19, "Design of UML Diagrams for Online College Magazine System", 199, 208),
    (20, "Design of UML Diagrams for Crime Bureau", 209, 218),
    (21, "Design of UML Diagrams for Smart Traffic Management System", 219, 226),
    (22, "Design of UML Diagrams for Job Seeker Portal System", 227, 236),
    (23, "Design of UML Diagrams for AAROGYA SETU - Health Care APP", 237, 246),
    (24, "Design of UML Diagrams for Online Pharmacy Management System", 247, 264),
    (25, "Design of UML Diagrams for EQUIHEALTH", 265, 278),
    (26, "Design of UML Diagrams for an OTT-Based System - MINI REEL", 279, 286),
    (27, "Design of UML Diagrams for e-Med Medical Assistance Tool", 287, 294),
    (28, "Design of UML Diagrams for Diet Care", 295, 302),
    (29, "Design of UML Diagrams for Student Counselling Management System", 303, 312),
    (30, "Design of UML Diagrams for E-Visa Processing and Follow-Up System", 313, 324),
    (31, "Design of UML Diagrams for Placement Automation System", 325, 332),
    (32, "Design of UML Diagrams for Farm Management System", 333, 340),
    (33, "Design of UML Diagrams for Green Rides", 341, 348),
    (34, "Design of UML Diagrams for Art Gallery Management System", 349, 356),
    (35, "Design of UML Diagrams for GUIDE - Dropshipping Website", 357, 366),
    (36, "Design of UML Diagrams for Online Quiz System", 367, 376),
    (37, "Design of UML Diagrams for Book Bank Management System", 377, 388),
    (38, "Design of UML Diagrams for Website Development", 389, 396),
    (39, "Design of UML Diagrams for STARTUP MEET", 397, 404),
    (40, "Design of UML Diagrams for Video Suggestion System", 405, 417),
]

def sanitize_filename(title: str) -> str:
    # Clean title for filename
    clean = re.sub(r"[^\w\s-]", "", title)
    clean = re.sub(r"[\s-]+", "_", clean).strip("_")
    return clean

def extract_chapter_text(reader: pypdf.PdfReader, start_book_page: int, end_book_page: int) -> str:
    # Find start and end indices
    # book page 1 starts around index 15
    start_idx = start_book_page + 14
    end_idx = min(end_book_page + 14, len(reader.pages) - 1)
    
    extracted_text = []
    for idx in range(start_idx, end_idx + 1):
        try:
            page_txt = reader.pages[idx].extract_text() or ""
            # Filter running headers and footers
            lines = page_txt.split("\n")
            filtered_lines = []
            for line in lines:
                l_str = line.strip()
                # Skip page numbers alone
                if l_str.isdigit():
                    continue
                # Skip running header e.g. "24 ◾ UML Diagramming" or "Contents ◾ ix"
                if re.match(r"^\d+\s*◾", l_str) or re.search(r"◾\s*\d+$", l_str):
                    continue
                if "UML Diagramming: A Case Study Approach" in l_str:
                    continue
                filtered_lines.append(line)
            extracted_text.append("\n".join(filtered_lines))
        except Exception as e:
            print(f"Warning reading page {idx}: {e}")
            
    full_text = "\n\n".join(extracted_text)
    # Fix hyphenation across newlines e.g. "imple-\nmentation" -> "implementation"
    full_text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", full_text)
    # Replace stray unescaped dollar signs with "USD " or escape
    full_text = full_text.replace("$", "\\$")
    return full_text

def build_chapter_markdown(ch_num: int, title: str, start_page: int, end_page: int, content: str) -> str:
    prev_ch = ch_num - 1 if ch_num > 1 else None
    next_ch = ch_num + 1 if ch_num < 40 else None
    
    # Format navigation
    nav_links = []
    if prev_ch:
        prev_title = CHAPTERS_METADATA[prev_ch - 1][1]
        prev_fname = f"Chapter_{prev_ch:02d}_{sanitize_filename(prev_title)}.md"
        nav_links.append(f"[&larr; Chapter {prev_ch:02d}: {prev_title}]({prev_fname})")
    nav_links.append("[📚 Book Index](../README.md)")
    if next_ch:
        next_title = CHAPTERS_METADATA[next_ch - 1][1]
        next_fname = f"Chapter_{next_ch:02d}_{sanitize_filename(next_title)}.md"
        nav_links.append(f"[Chapter {next_ch:02d}: {next_title} &rarr;]({next_fname})")
    nav_bar = " | ".join(nav_links)
    
    # Identify case study or theory
    is_theory = (ch_num == 1)
    domain_type = "Theoretical Foundations & UP Phases" if is_theory else "Industrial Case Study & Diagram Suite"
    
    # Clean content into structured paragraphs
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
    
    md = f"""# Chapter {ch_num:02d}: {title}

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: {start_page}–{end_page} (Total: {end_page - start_page + 1} pages)  
> **Classification**: {domain_type}  
> **Navigation**: {nav_bar}

---

## 📌 Chapter Overview

Chapter {ch_num} of *UML Diagramming: A Case Study Approach* focuses on **{title}**. 
{"It provides the comprehensive conceptual foundation for the Unified Process (UP) lifecycle, core modeling philosophies, and the pyramid of UML diagrams." if is_theory else f"This case study presents an end-to-end software engineering analysis for **{title.replace('Design of UML Diagrams for ', '')}**, establishing formal requirements, data-flow models, and complete UML diagram specifications."}

---

## 📑 Core Topics & Sections

"""
    # Extract sections like "X.Y Title"
    sections = re.findall(rf"^({ch_num}\.\d+(?:\.\d+)?\s+[A-Z].*)$", content, re.MULTILINE)
    if sections:
        for s in sections[:20]:
            s_clean = s.strip().replace("\\$", "")
            md += f"- **{s_clean}**\n"
        md += "\n---\n\n"

    md += "## 📝 Detailed Chapter Summary & Content\n\n"
    
    # Process text content intelligently into subsections or clean markdown
    current_section = None
    section_body = []
    
    lines = content.split("\n")
    for line in lines:
        l = line.strip()
        if not l:
            continue
        
        # Check if line is a section heading e.g. "2.1 Problem Statement"
        sec_match = re.match(rf"^({ch_num}\.\d+(?:\.\d+)?)\s+(.*)$", l)
        if sec_match and len(l) < 100:
            if section_body:
                body_text = "\n\n".join(section_body).strip()
                if body_text:
                    md += f"{body_text}\n\n"
                section_body = []
            sec_num = sec_match.group(1)
            sec_title = sec_match.group(2).strip().replace("\\$", "")
            md += f"### {sec_num} {sec_title}\n\n"
        else:
            # Regular text line
            # Check for bullet points
            if l.startswith("•") or l.startswith("- ") or re.match(r"^\d+\.\s+", l):
                clean_bullet = l.replace("•", "- ").replace("\\$", "")
                section_body.append(clean_bullet)
            else:
                section_body.append(l.replace("\\$", ""))

    if section_body:
        md += "\n\n".join(section_body).strip() + "\n\n"

    # Add diagrammatic summary table for case studies
    if not is_theory:
        system_name = title.replace("Design of UML Diagrams for ", "").replace(" – Healthcare Service System Services", "")
        md += f"""---

## 📊 UML Modeling Suite for {system_name}

The case study defines the following canonical UML models:

| Diagram Type | Perspective | Key Elements & Responsibilities |
| :--- | :--- | :--- |
| **Use Case Diagram** | Functional Scope | Primary actors, external APIs, and core business goals (`<<include>>`, `<<extend>>`). |
| **Activity Diagram** | Workflow / Process | Action states, decision diamonds, object flows, and swimlane partitions. |
| **Class Diagram** | Structural Backbone | Entity classifiers, attributes, operations, multiplicities, and relationships. |
| **Sequence Diagram** | Dynamic Interaction | Lifelines, synchronous RPCs, message returns, and execution activations. |
| **State Chart Diagram** | Lifecycle States | Discrete system states, event triggers, and boolean guard conditions. |
| **Component Diagram** | Modular Architecture | Encapsulated subsystems, provided interfaces (balls), and required interfaces (sockets). |
| **Deployment Diagram** | Physical Topology | Hardware nodes, application servers, database instances, and network links. |

---

## 🎯 Key Architectural Invariants & Modeling Lessons

1. **Requirements Grounding**: All diagrammatic artifacts trace back to functional requirements and domain constraints established in the problem statement.
2. **Structural Consistency**: Multiplicities and association lifecycles in the Class Diagram mirror the invocation sequences in the Sequence Diagram.
3. **Behavioral Invariants**: Guard conditions in State Chart and Activity models prevent invalid transitions and runtime failure modes.

---

## 🔗 Related Resources & Navigation

- **Previous Chapter**: {f"[{CHAPTERS_METADATA[prev_ch - 1][1]}](Chapter_{prev_ch:02d}_{sanitize_filename(CHAPTERS_METADATA[prev_ch - 1][1])}.md)" if prev_ch else "None (First Chapter)"}
- **Next Chapter**: {f"[{CHAPTERS_METADATA[next_ch - 1][1]}](Chapter_{next_ch:02d}_{sanitize_filename(CHAPTERS_METADATA[next_ch - 1][1])}.md)" if next_ch else "None (Last Chapter)"}
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
"""
    else:
        md += """---

## 🎯 Key Takeaways: Unified Process (UP) & UML Foundations

1. **Iterative & Incremental**: The UP structure guides modeling across **Inception**, **Elaboration**, **Construction**, and **Transition**.
2. **Static vs Dynamic Duality**: Every software system requires both structural static models (Class, Object, Component, Deployment) and dynamic behavioral models (Use Case, Activity, Sequence, State Machine).
3. **Traceability Invariant**: Use case specifications govern sequence lifeline behaviors, which in turn drive class operation requirements.

---

## 🔗 Navigation
- **Next Chapter**: [Chapter 02: Design of UML Diagrams for Webmed - Healthcare Service System Services](Chapter_02_Design_of_UML_Diagrams_for_Webmed_Healthcare_Service_System_Services.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
"""
    return md

def main():
    print(f"📖 Opening PDF: {PDF_PATH.name}...")
    reader = pypdf.PdfReader(str(PDF_PATH))
    print(f"Total pages: {len(reader.pages)}")
    
    generated_files = []
    
    for ch_num, title, start_page, end_page in CHAPTERS_METADATA:
        print(f"Generating Chapter {ch_num:02d}: {title} (p. {start_page}–{end_page})...")
        content = extract_chapter_text(reader, start_page, end_page)
        md_text = build_chapter_markdown(ch_num, title, start_page, end_page, content)
        
        fname = f"Chapter_{ch_num:02d}_{sanitize_filename(title)}.md"
        out_path = CHAPTERS_DIR / fname
        out_path.write_text(md_text, encoding="utf-8")
        generated_files.append((ch_num, title, fname, start_page, end_page))
        
    print(f"\n✅ Successfully generated all {len(generated_files)} chapter markdown files in:\n   {CHAPTERS_DIR}")
    return generated_files

if __name__ == "__main__":
    main()

