#!/usr/bin/env python3
"""
refactor_uml_chapters.py

Systematically refactors all 40 chapter markdown files in umlBook:
- Extracts original problem statements and requirements from git HEAD.
- Removes raw verbatim OCR text dumps and double-linebreak artifacts.
- Embeds ALL extracted vector SVG diagrams per chapter from vector_images/.
- Sorts figures in natural chronological order (Figure X.1 before Figure X.10).
- Synthesizes clear, comprehensive architectural summaries (Problem Statement,
  Functional Modules, DFDs, UML Diagram Suite, Architectural Invariants).
"""

import os
import re
import sys
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UML_DIR = os.path.join(
    BASE_DIR,
    "topics",
    "0.FUNDAMENTALS",
    "System Requirements",
    "UML-DIAGRAMMING",
    "Data_Ingestion",
    "Books",
    "umlBook",
)
CHAP_DIR = os.path.join(UML_DIR, "chapters")
VEC_DIR = os.path.join(UML_DIR, "vector_images")

def natural_sort_key(s):
    """Sort strings containing numbers in human/natural order."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def clean_ocr_text(text):
    """Normalize OCR whitespace and linebreaks, strip DOIs and garbage."""
    if not text:
        return ""
    text = re.sub(r'DOI:\s*10\.\d+/[^\s]+', '', text)
    text = re.sub(r's\s+m\s+a\s+r\s+a\s+g\s+D\s+i\s+L\s+M\s+U.*', '', text, flags=re.I)
    text = re.sub(r'\.\s*m\s*a\s*r\s*g\s*i\s*a\s*.*', '', text, flags=re.I)
    lines = [l.strip() for l in text.split("\n")]
    joined = " ".join([l for l in lines if l])
    return re.sub(r"\s+", " ", joined).strip()

def get_diagram_info(svg_name, chap_num):
    """Return diagram category, clean caption, and architectural role description."""
    clean_stem = svg_name.replace(".svg", "")
    lower = clean_stem.lower()

    if "usecase" in lower or "use_case" in lower:
        cat = "Use Case Diagram"
        desc = "Specifies system boundary, primary external actors, and business use cases with include/extend relationships."
    elif "class" in lower:
        cat = "Class Diagram"
        desc = "Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance)."
    elif "activity" in lower:
        cat = "Activity Diagram"
        desc = "Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins."
    elif "sequence" in lower:
        cat = "Sequence Diagram"
        desc = "Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines."
    elif "collaboration" in lower or "communication" in lower:
        cat = "Communication Diagram"
        desc = "Emphasizes structural object topology and numbered sequence messaging between collaborating entities."
    elif "state_machine" in lower or "state_chart" in lower or "state" in lower:
        cat = "State Machine Diagram"
        desc = "Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions."
    elif "component" in lower:
        cat = "Component Diagram"
        desc = "Architects physical modular software components, provided ball interfaces, and required socket dependencies."
    elif "deployment" in lower:
        cat = "Deployment Diagram"
        desc = "Maps software execution artifacts to hardware computing nodes, client devices, application tiers, and database servers."
    elif "dfd" in lower:
        cat = "Data Flow Diagram (DFD)"
        desc = "Models external entity inputs, core transformation processes, and data store read/write interactions."
    elif any(k in lower for k in ["case_", "screen", "dashboard", "popup", "login", "counter", "order", "goods", "search", "summary", "tax"]):
        cat = "System Interface & Flow Schematic"
        desc = "Depicts user interface states, administrative dashboards, or operational screen transitions."
    elif clean_stem.startswith("Ch"):
        cat = "Conceptual Notation / Architecture Asset"
        desc = "Supplemental conceptual illustration or notation reference from the source chapter."
    else:
        cat = "Architectural Figure"
        desc = "Structural schematic detailing domain requirements and workflow transitions."

    # Format human-readable caption
    caption = clean_stem.replace("_", " ")
    if caption.startswith("Figure "):
        parts = caption.split(" ", 3)
        if len(parts) >= 4 and parts[1].isdigit() and parts[2].isdigit():
            term = parts[3].title()
            term = re.sub(r'\bUml\b', 'UML', term)
            term = re.sub(r'\bDfd\b', 'DFD', term)
            caption = f"Figure {parts[1]}.{parts[2]}: {term}"
        elif len(parts) >= 3 and parts[1].isdigit():
            term = parts[2].title()
            term = re.sub(r'\bUml\b', 'UML', term)
            term = re.sub(r'\bDfd\b', 'DFD', term)
            caption = f"Figure {parts[1]}: {term}"

    return cat, caption, desc

def get_original_git_content(chap_file):
    """Retrieve original chapter text from git HEAD before refactoring."""
    git_path = f"topics/0.FUNDAMENTALS/System Requirements/UML-DIAGRAMMING/Data_Ingestion/Books/umlBook/chapters/{chap_file}"
    cmd = ["git", "show", f"HEAD:{git_path}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    return res.stdout if res.returncode == 0 else ""

def format_functional_points(body_text, chap_idx):
    """Extract and format functional modules into clean bullet points."""
    # Look for section X.2 in body
    fn_m = re.search(
        rf"###\s*{chap_idx}\s*\.?\s*2\s+(?:Major Functionalities|Functional Requirements|Software Requirements)[^\n]*\n+(.*?)(?=\n+\s*(?:###|Figure\s+{chap_idx}|System Architecture|Table\s+{chap_idx})|\Z)",
        body_text,
        re.S | re.I
    )
    if not fn_m:
        return ""
    
    raw = fn_m.group(1)
    clean = clean_ocr_text(raw)
    clean = re.sub(r'^(?:and Its Description\s*)?(?:The major functionalities of this system[^:]*:\s*)?', '', clean, flags=re.I)
    
    # Try bullet pattern 'Module – Description'
    pattern = r'([A-Za-z0-9\s/–-]+?)\s*[–—]\s*(this functionality[^.]*\.|[^.]*\.)'
    matches = re.findall(pattern, clean)
    if len(matches) >= 3:
        items = []
        for name, desc in matches:
            name_clean = re.sub(r'.*?follows:\s*', '', name).strip().rstrip('–-').strip()
            if name_clean and len(name_clean) < 35:
                items.append(f"- **{name_clean}**: {desc.strip()}")
        if items:
            return "\n".join(items)

    # If pattern didn't match cleanly, return a concise cleaned paragraph
    clean = re.sub(r'(?:Figure\s+\d+|System Architecture|Table\s+\d+).*', '', clean, flags=re.I).strip()
    return clean if len(clean) > 30 else ""

def refactor_chapter(chap_file, vec_folder, chap_idx, total_chaps, all_files):
    orig_content = get_original_git_content(chap_file)
    if not orig_content:
        chap_path = os.path.join(CHAP_DIR, chap_file)
        with open(chap_path, "r", encoding="utf-8", errors="ignore") as f:
            orig_content = f.read()

    # Locate body after 'Detailed Chapter Summary' to skip TOC collisions
    body_idx = orig_content.find("Detailed Chapter Summary")
    body_text = orig_content[body_idx:] if body_idx != -1 else orig_content

    # Extract clean chapter title from filename
    fn_parts = chap_file.replace(".md", "").split("_", 2)
    clean_title = fn_parts[2].replace("_", " ") if len(fn_parts) >= 3 else f"Case Study {chap_idx}"

    pages_m = re.search(r"> \*\*Pages\*\*:\s*([^\n]+)", orig_content)
    pages_str = pages_m.group(1).strip() if pages_m else "N/A"

    class_str = "Theoretical Foundations & UP Phases" if chap_idx == 1 else "Industrial Case Study & Diagram Suite"

    # Extract Problem Statement from body
    if chap_idx == 1:
        ps_text = "The Unified Process (UP) is an iterative, architecture-centric, and risk-driven software development process for building object-oriented systems. UP structures software lifecycles into four sequential phases: Inception (feasibility and project boundary), Elaboration (core architecture and scheduling), Construction (coding, alpha testing, and component assembly), and Transition (beta testing, deployment, and customer validation). Across these phases, the Unified Modeling Language (UML) provides the standardized graphical grammar to model structural building blocks and dynamic behavioral interactions."
    else:
        ps_m = re.search(
            rf"(?:{chap_idx}\s*\.?\s*1\s+Problem Statement\s*\n+)(.*?)(?=\n+\s*(?:###|{chap_idx}\s*\.?\s*2|Figure\s+{chap_idx}|s\s*m\s*a\s*r)|\Z)",
            body_text,
            re.S | re.I
        )
        if ps_m:
            ps_text = clean_ocr_text(ps_m.group(1))
        else:
            intro_m = re.search(r"## 📌 Chapter Overview\s*\n+(.*?)(?=\n+##|\Z)", orig_content, re.S)
            ps_text = clean_ocr_text(intro_m.group(1)) if intro_m else "This chapter provides detailed software engineering analysis and UML modeling specifications."

    # Navigation links
    prev_link = f"[&larr; {all_files[chap_idx-2].replace('.md', '')}]({all_files[chap_idx-2]})" if chap_idx > 1 else ""
    next_link = f"[{all_files[chap_idx].replace('.md', '')} &rarr;]({all_files[chap_idx]})" if chap_idx < total_chaps else ""
    nav_bar = " | ".join([p for p in [prev_link, "[📚 Book Index](../UML_Book.md)", next_link] if p])

    # SVGs for this chapter with natural sorting
    vpath = os.path.join(VEC_DIR, vec_folder)
    svgs = sorted(os.listdir(vpath), key=natural_sort_key) if os.path.exists(vpath) else []
    
    core_figures = [s for s in svgs if s.startswith("Figure_")]
    page_snippets = [s for s in svgs if not s.startswith("Figure_")]

    # Build refactored markdown
    out = []
    out.append(f"# Chapter {chap_idx:02d}: {clean_title}")
    out.append("")
    out.append(f"> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  ")
    out.append(f"> **Pages**: {pages_str}  ")
    out.append(f"> **Classification**: {class_str}  ")
    out.append(f"> **Navigation**: {nav_bar}")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 📌 Executive Summary")
    out.append("")
    if chap_idx == 1:
        out.append("Chapter 1 establishes the theoretical foundations of software engineering modeling and the **Unified Process (UP)** lifecycle. It introduces the role of the Unified Modeling Language (UML) as the international standard visual language for specifying, constructing, visualizing, and documenting software artifacts. The chapter breaks down the four UP lifecycle phases (Inception, Elaboration, Construction, Transition) and provides a comprehensive structural and behavioral taxonomy of all major UML diagrams.")
    else:
        out.append(f"Chapter {chap_idx} presents an industrial software engineering case study for **{clean_title}**. It details the transition from business requirements and domain constraints into formal software architecture specifications, leveraging data-flow modeling and a complete suite of Unified Modeling Language (UML) structural and behavioral diagrams.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 🎯 Problem Statement & System Context")
    out.append("")
    out.append(f"{ps_text}")
    out.append("")

    if chap_idx > 1:
        fn_formatted = format_functional_points(body_text, chap_idx)
        if fn_formatted:
            out.append("### Key Functional Capabilities")
            out.append("")
            out.append(f"{fn_formatted}")
            out.append("")

    out.append("---")
    out.append("")
    out.append(f"## 📊 Complete UML Diagram Suite & Architecture Specifications")
    out.append("")
    out.append(f"This chapter incorporates **{len(svgs)} standalone vector diagram(s)** illustrating the end-to-end design from functional use cases to physical hardware deployment:")
    out.append("")

    # Embed core diagrams
    if core_figures:
        for s in core_figures:
            cat, caption, desc = get_diagram_info(s, chap_idx)
            img_rel = f"../vector_images/{vec_folder}/{s}"
            out.append(f"### {caption}")
            out.append("")
            out.append(f"**Diagram Category**: `{cat}`  ")
            out.append(f"**Architectural Role**: {desc}")
            out.append("")
            out.append(f"![{caption}]({img_rel})")
            out.append("")

    # Embed page snippets / visual artifacts
    if page_snippets:
        out.append("### Visual Artifacts & Supplementary Schematics")
        out.append("")
        out.append("The following vector schematics capture operational screen states, user dashboards, or notation components documented in this chapter:")
        out.append("")
        for s in page_snippets:
            cat, caption, desc = get_diagram_info(s, chap_idx)
            img_rel = f"../vector_images/{vec_folder}/{s}"
            out.append(f"#### {caption}")
            out.append("")
            out.append(f"![{caption}]({img_rel})")
            out.append("")

    out.append("---")
    out.append("")
    out.append("## 💡 Key Architectural Invariants & Modeling Lessons")
    out.append("")
    out.append("1. **Traceability**: Every software model directly corresponds to explicit functional requirements defined during the initial domain specification.")
    out.append("2. **Separation of Concerns**: Structural models (Class, Component, Deployment) maintain clear boundaries separating business domain entities from physical infrastructure nodes.")
    out.append("3. **Behavioral Integrity**: Dynamic models (Activity, Sequence, State Machine) guarantee valid state transitions, prevent deadlocks, and verify message order consistency.")
    out.append("4. **Deployment Fidelity**: Physical nodes and execution environments accurately map runtime middleware, database engines, and client access channels.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 🔗 Related Resources & Navigation")
    out.append("")
    out.append(f"- **Navigation**: {nav_bar}")
    out.append(f"- **Master Book Catalog**: [`UML_Book.md`](../UML_Book.md)")
    out.append(f"- **Vector Images Catalog**: [`Vector_Images_Catalog.md`](../vector_images/Vector_Images_Catalog.md)")

    return "\n".join(out)

def main():
    chaps = sorted([f for f in os.listdir(CHAP_DIR) if f.endswith(".md")])
    vec_dirs = sorted([d for d in os.listdir(VEC_DIR) if os.path.isdir(os.path.join(VEC_DIR, d))])

    if len(chaps) != len(vec_dirs):
        print(f"Mismatch: {len(chaps)} chapter files vs {len(vec_dirs)} vector folders!")
        sys.exit(1)

    print(f"Refactoring all {len(chaps)} chapters using git HEAD body extraction...")
    for idx, (cf, vd) in enumerate(zip(chaps, vec_dirs), 1):
        refactored = refactor_chapter(cf, vd, idx, len(chaps), chaps)
        target_path = os.path.join(CHAP_DIR, cf)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(refactored)
        print(f"✓ [{idx:02d}/40] Refactored: {cf}")

    print("\nAll 40 chapters refactored successfully!")

if __name__ == "__main__":
    main()
