#!/usr/bin/env python3
"""
scripts/scaffold_engine.py
Universal Event-Driven Topic Scaffolder & Real-Time Directory Watcher

Modes:
1. CLI Mode:
   python Project_Engine/scripts/scaffold_engine.py "1.LLD/DESIGN_PATTERNS/Chapter-6-Command_Pattern"
   Directly creates the topic folder and hydrates all dependency files.

2. Watcher Daemon Mode:
   python Project_Engine/scripts/scaffold_engine.py --watch
   Monitors '0.FUNDAMENTALS', '1.LLD', and '2.HLD' in real time.
   Automatically hydrates any newly created empty folder with the complete topic dependency suite.
"""

import sys
import os
import re
import time
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TOPIC_ROOTS = [
    REPO_ROOT / "0.FUNDAMENTALS",
    REPO_ROOT / "1.LLD",
    REPO_ROOT / "2.HLD"
]

def clean_identifier(name: str) -> str:
    """Converts a folder name into a valid Java/Mermaid identifier."""
    # Strip prefix like Chapter-6- or 01_
    cleaned = re.sub(r"^(?:Chapter-\d+-|\d+[\._-])", "", name)
    cleaned = re.sub(r"[^A-Za-z0-9_]", "", cleaned.replace(" ", "_").replace("-", "_"))
    return cleaned or "Topic"

def to_camel_case(name: str) -> str:
    """Converts a snake_case/kebab-case name to CamelCase."""
    ident = clean_identifier(name)
    parts = ident.split("_")
    return "".join(p.capitalize() for p in parts if p) or "TopicDemo"

def determine_domain(target_path: Path) -> str:
    """Identifies whether the topic belongs to FUNDAMENTALS, LLD, or HLD."""
    try:
        rel = target_path.relative_to(REPO_ROOT)
        top_part = rel.parts[0]
        if "FUNDAMENTALS" in top_part:
            return "0.FUNDAMENTALS"
        elif "LLD" in top_part:
            return "1.LLD"
        elif "HLD" in top_part:
            return "2.HLD"
    except Exception:
        pass
    return "1.LLD"

def scaffold_topic(target_dir: Path, verbose: bool = True) -> bool:
    """Hydrates a target directory with the standard topic dependency suite."""
    target_dir = target_dir.resolve()
    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)

    topic_name = target_dir.name
    class_name = to_camel_case(topic_name)
    domain = determine_domain(target_dir)

    # Subdirectories
    code_dir = target_dir / "code"
    diagrams_dir = target_dir / "diagrams"
    notes_dir = target_dir / "notes"
    resources_dir = target_dir / "resources"

    code_dir.mkdir(exist_ok=True)
    diagrams_dir.mkdir(exist_ok=True)
    notes_dir.mkdir(exist_ok=True)
    resources_dir.mkdir(exist_ok=True)

    # 1. Topic Skill (SKILL.md)
    skill_file = target_dir / "SKILL.md"
    if not skill_file.exists():
        skill_content = f"""# Topic Skill: {topic_name}

> **Domain**: `{domain}`
> **Parent Engine**: `Project_Engine` (Inherits Generic Ingestion & 3-Tier Output Standard)
> **Reference Guide**: [Rule 9 (3-Tier Modeling Mapping)](file:///Project_Engine/chat/finalized%20chat.md#L68-L74)

---

## 1. Topic-Specific Scope & Objectives
Define the core design challenge, invariants, and architectural domain for **{topic_name}**.

- **Primary Responsibility**: 
- **Core Dilemma / Trade-off**: 
- **Key Invariants**: 

---

## 2. Topic-Specific Invariants & Rules
Instructions and constraints unique to this topic:
1. **Domain Boundary**: What logic belongs strictly inside this topic vs outside.
2. **Edge Cases**: Common race conditions, lifecycle pitfalls, or memory leak traps.
3. **Design Trade-offs**: When to use this pattern/architecture vs alternative approaches.

---

## 3. Mandatory 3-Tier Deliverable Checklist
Every solution produced under this topic must deliver:
- [ ] **Tier 1 (OOP Code)**: Strict Java 21 implementation in [`code/`](code/) with clean OOP principles.
- [ ] **Tier 2 (UML Diagrams)**: Formal Mermaid and/or PlantUML diagrams in [`diagrams/`](diagrams/).
- [ ] **Tier 3 (Runtime Memory State)**: JVM heap object graph and stack activation traces in [`notes/`](notes/).
"""
        skill_file.write_text(skill_content, encoding="utf-8")

    # 2. Starter Java Code
    java_file = code_dir / f"{class_name}Demo.java"
    if not java_file.exists():
        pkg_suffix = clean_identifier(topic_name).lower()
        java_content = f"""package com.systemdesign.{domain.lower().replace('.', '_')}.{pkg_suffix};

/**
 * 3-Tier Modeling Demonstration for {topic_name}
 * Layer 1: Concrete Object-Oriented Implementation (Strictly Java 21)
 */
public class {class_name}Demo {{

    public static void main(String[] args) {{
        System.out.println("Executing {topic_name} demonstration...");
        // TODO: Implement domain classes and interaction logic
    }}
}}
"""
        java_file.write_text(java_content, encoding="utf-8")

    # 3. Starter Mermaid Diagram
    mmd_file = diagrams_dir / f"{clean_identifier(topic_name)}_architecture.mmd"
    if not mmd_file.exists():
        mmd_content = f"""```mermaid
classDiagram
    class {class_name}Demo {{
        +main(args: String[]) void
    }}

    class Context {{
        -state: String
        +executeOperation() void
    }}

    {class_name}Demo --> Context : "invokes"
```
"""
        mmd_file.write_text(mmd_content, encoding="utf-8")

    # 4. Starter Notes & Trade-offs Document
    notes_file = notes_dir / f"{clean_identifier(topic_name)}_Tradeoffs.md"
    if not notes_file.exists():
        notes_content = f"""# Architectural Notes & Trade-offs: {topic_name}

> **Source Attribution**: Managed by `Project_Engine` standard templates.

---

## 1. Core Problem Statement & Motivation
Describe why **{topic_name}** is needed and what anti-patterns arise without it.

---

## 2. Architectural Trade-offs Matrix

| Evaluation Dimension | This Approach | Alternative Approach | Trade-off Analysis |
| :--- | :--- | :--- | :--- |
| **Complexity** | Moderate | High | Simplified maintenance at slight abstraction cost. |
| **Performance** | High | Moderate | Direct in-memory dispatch. |
| **Extensibility** | High | Low | Open-Closed Principle adhered. |

---

## 3. Architecture Decision Record (ADR)

- **Context**: 
- **Decision**: 
- **Consequences**: 
  - *Positive*: 
  - *Negative*: 

---

## 4. Layer 3 Runtime Memory State Analysis
Illustrate JVM heap object graphs, call stack frames, or thread execution lifelines here.
"""
        notes_file.write_text(notes_content, encoding="utf-8")

    # 5. Resources Staging .gitkeep
    gitkeep_file = resources_dir / ".gitkeep"
    if not gitkeep_file.exists():
        gitkeep_file.write_text("", encoding="utf-8")

    if verbose:
        print(f"✨ Successfully scaffolded topic: {topic_name}")
        print(f"   ├── SKILL.md")
        print(f"   ├── code/{class_name}Demo.java")
        print(f"   ├── diagrams/{clean_identifier(topic_name)}_architecture.mmd")
        print(f"   ├── notes/{clean_identifier(topic_name)}_Tradeoffs.md")
        print(f"   └── resources/.gitkeep")

    return True

def is_topic_dir(path: Path) -> bool:
    """Checks whether a folder qualifies as a topic directory requiring scaffolding."""
    if not path.is_dir():
        return False
    name = path.name
    # Ignore internal/meta folders
    if name.startswith(".") or name in ["code", "diagrams", "notes", "resources", "chapters", "vector_images", "Books", "put the file here", "Source of Problem", "Problem Files", "Solution Files", "outline"]:
        return False
    
    # Must be at least 2 levels deep from REPO_ROOT (e.g. 1.LLD/DESIGN_PATTERNS/Topic)
    try:
        rel = path.relative_to(REPO_ROOT)
        return len(rel.parts) >= 2
    except Exception:
        return False

def run_watcher(interval_seconds: float = 1.0):
    """Watches topic roots and auto-scaffolds newly created empty directories."""
    print("👀 Project Engine Directory Watcher is ACTIVE.")
    print("   Monitoring topic roots:")
    for root in TOPIC_ROOTS:
        if root.exists():
            print(f"   - {root.relative_to(REPO_ROOT)}")
    print(f"   Polling every {interval_seconds} second(s). Press Ctrl+C to terminate.\n")

    # Keep track of known directories
    known_dirs = set()
    for root in TOPIC_ROOTS:
        if root.exists():
            for p in root.glob("**/*"):
                if p.is_dir():
                    known_dirs.add(p.resolve())

    try:
        while True:
            time.sleep(interval_seconds)
            for root in TOPIC_ROOTS:
                if not root.exists():
                    continue
                current_dirs = [p for p in root.glob("**/*") if p.is_dir()]
                for d in current_dirs:
                    d_resolved = d.resolve()
                    if d_resolved not in known_dirs:
                        known_dirs.add(d_resolved)
                        if is_topic_dir(d_resolved):
                            # Check if SKILL.md already exists
                            if not (d_resolved / "SKILL.md").exists():
                                print(f"\n⚡ New topic folder detected: {d_resolved.relative_to(REPO_ROOT)}")
                                scaffold_topic(d_resolved)
    except KeyboardInterrupt:
        print("\n🛑 Watcher stopped by user.")

def main():
    parser = argparse.ArgumentParser(
        description="Project Engine Automated Topic Scaffolder & Watcher Daemon"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help="Path or relative directory of the new topic to scaffold (e.g. '1.LLD/DESIGN_PATTERNS/Chapter-6-Command_Pattern')"
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Run as a real-time background watcher daemon detecting new folders"
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Polling interval in seconds for watcher mode (default: 1.0s)"
    )

    args = parser.parse_args()

    if args.watch:
        run_watcher(interval_seconds=args.interval)
    elif args.target:
        target_path = Path(args.target)
        if not target_path.is_absolute():
            target_path = REPO_ROOT / target_path
        scaffold_topic(target_path)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
