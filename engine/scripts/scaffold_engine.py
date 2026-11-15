#!/usr/bin/env python3
"""
scripts/scaffold_engine.py
Automated Query Subfolder Creator & Real-Time Directory Watcher

Specification:
When a folder is created in '0.FUNDAMENTALS', '1.LLD', or '2.HLD' (e.g. named "Topic"),
the engine automatically creates a corresponding subfolder inside 'Project_Engine/Skills_Output/query/'
named 'query_<Topic>'.

Usage:
1. CLI Mode:
   python Project_Engine/scripts/scaffold_engine.py "1.LLD/Topic"
   Creates 'Topic' (if not already created) and automatically creates 'query/query_Topic/'.

2. Watcher Daemon Mode:
   python Project_Engine/scripts/scaffold_engine.py --watch
   Monitors '0.FUNDAMENTALS', '1.LLD', and '2.HLD' in real time.
   Whenever a new folder is created, it automatically generates 'query/query_<Folder_Name>/'.
"""

import sys
import os
import time
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
QUERY_DIR = REPO_ROOT / "Project_Engine" / "Skills_Output" / "query"
TOPIC_ROOTS = [
    REPO_ROOT / "0.FUNDAMENTALS",
    REPO_ROOT / "1.LLD",
    REPO_ROOT / "2.HLD"
]

def create_query_dependency(folder_name: str, verbose: bool = True) -> Path:
    """Creates the corresponding query_<folder_name> subfolder inside query/."""
    query_subfolder_name = f"query_{folder_name}"
    target_query_dir = QUERY_DIR / query_subfolder_name
    target_query_dir.mkdir(parents=True, exist_ok=True)

    gitkeep = target_query_dir / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")

    if verbose:
        print(f"✨ Auto-created query dependency folder:")
        print(f"   Project_Engine/Skills_Output/query/{query_subfolder_name}/")

    return target_query_dir

def handle_folder_creation(target_path: Path, verbose: bool = True) -> Path:
    """Handles the creation of a folder under LLD/HLD/FUNDAMENTALS."""
    target_path = target_path.resolve()
    if not target_path.exists():
        target_path.mkdir(parents=True, exist_ok=True)

    folder_name = target_path.name
    query_dep = create_query_dependency(folder_name, verbose=verbose)
    return query_dep

def is_watched_topic_folder(path: Path) -> bool:
    """Checks whether a folder was created under 0.FUNDAMENTALS, 1.LLD, or 2.HLD."""
    if not path.is_dir():
        return False
    
    # Ignore hidden folders (.git, .agent, etc.)
    if path.name.startswith("."):
        return False

    try:
        rel = path.relative_to(REPO_ROOT)
        top_part = rel.parts[0]
        if top_part in ["0.FUNDAMENTALS", "1.LLD", "2.HLD"]:
            # Must be a child under one of the topic roots
            return len(rel.parts) >= 2
    except Exception:
        return False
    return False

def run_watcher(interval_seconds: float = 1.0):
    """Real-time directory watcher monitoring LLD/HLD/FUNDAMENTALS."""
    print("👀 Project Engine Query Scaffolder Watcher is ACTIVE.")
    print("   Watching topic roots for folder creation:")
    for root in TOPIC_ROOTS:
        if root.exists():
            print(f"   - {root.relative_to(REPO_ROOT)}")
    print(f"   Destination: Project_Engine/Skills_Output/query/query_<Folder_Name>/")
    print(f"   Polling every {interval_seconds} second(s). Press Ctrl+C to terminate.\n")

    # Snapshot existing directories
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
                for d in root.glob("**/*"):
                    if not d.is_dir():
                        continue
                    d_resolved = d.resolve()
                    if d_resolved not in known_dirs:
                        known_dirs.add(d_resolved)
                        if is_watched_topic_folder(d_resolved):
                            print(f"\n⚡ New folder detected: {d_resolved.relative_to(REPO_ROOT)}")
                            create_query_dependency(d_resolved.name)
    except KeyboardInterrupt:
        print("\n🛑 Watcher stopped by user.")

def main():
    parser = argparse.ArgumentParser(
        description="Project Engine Query Dependency Scaffolder & Watcher"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help="Path or relative directory created (e.g. '1.LLD/Topic' or 'Topic')"
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
        handle_folder_creation(target_path)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
