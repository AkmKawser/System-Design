# Canonical Folder Structure Blueprint

This document details the complete canonical filesystem topology, file naming conventions, and directory hierarchy of the **Learning & Roadmap Project**.

---

## 1. High-Level Repository Tree

```
Learning-Roadmap_Project-Structure/
├── README.md                                 # Single root project overview & entry point
├── index.md                                  # Master Navigation Catalog: Topics, Queries & Notes
├── outline.md                                # Single Master Topic Outline: Consolidated Curriculum
│
├── architecture/                             # Architectural Specifications Subsystem
│   ├── architecture.md                       # Comprehensive Project Architecture & Subsystems
│   └── folderstructure.md                    # Canonical Filesystem Topology (This Document)
│
├── engine/                                   # Computational & Agentic Engine Subsystem
│   └── engine.md                             # Scaffolding logic, 3-tier ingestion, RAG & STT rules
│
├── chat/                                     # Governance, Logging & Rules Subsystem
│   ├── universal_rules.md                    # 15 Permanent Operational Invariants (HITL, Audits, etc.)
│   └── chatLog.md                            # Full-fidelity chronological transcript of all turns
│
├── Upcoming Updates/                         # Strategic Roadmaps & Forward-Looking Blueprints
│   └── Upcoming Updates.md                   # Shared Agent Memory roadmap & implementation plan
│
└── topics/                                   # Domain Knowledge & Learning Roadmaps Root
    └── <topic_name>/                         # Immediate Topic Subfolder (e.g. 0.FUNDAMENTALS/)
        └── [Intermediate Subfolders...]/     # Arbitrary nesting (e.g., LLD/, Design_Patterns/)
            └── <last_subfolder>/             # Terminal Leaf Node (Identified via index.md)
                ├── template/                 # Custom Template Blueprint Directory
                │   └── template.md           # User custom template specification
                │
                ├── Data_Ingestion/           # Multi-Source Knowledge Ingestion Gateway
                │   ├── Books/                # Two-Tier Book Extraction Pipeline
                │   │   ├── raw_books/        # Original PDFs / EPUBs / DOCX files
                │   │   ├── indices/          # TOC JSON & markdown structural indices
                │   │   │   ├── toc_book1.json
                │   │   │   └── table_of_contents.md
                │   │   └── scripts/          # Surgical extraction CLI tooling
                │   │       └── query_book.py # pypdf CLI for surgical page slicing
                │   │
                │   ├── Courses/              # Web & Course Scraped Content (Playwright)
                │   │   └── <course_name>/    # Syllabi, transcripts & lecture outlines
                │   │
                │   └── Random/               # Isolated Resources Gateway
                │       ├── docs/             # Ad-hoc PDFs, text notes & articles (RAG indexed)
                │       └── transcripts/      # Audio-to-text transcripts (Whisper/Gemini STT)
                │
                └── output/                   # Topic Deliverables & Knowledge Outputs
                    ├── query_<topic_name>/   # Answers, Q&A manuals, surgical problem breakdowns
                    └── Note_version-#_<topic_name>/ # Versioned study roadmaps & synthesized notes
```

---

## 2. Directory & File Breakdown

| Path | Type | Owner | Role & Operational Purpose |
| :--- | :--- | :--- | :--- |
| `README.md` | File | Agent / User | Single root documentation file providing high-level repository summary. |
| `outline.md` | File | Agent | Master Navigation Catalog table indexing all topics, queries, and versioned notes. |
| `architecture/architecture.md` | File | Agent | Detailed system design, subsystem blueprints, data flow diagrams, and lifecycle. |
| `architecture/folderstructure.md` | File | Agent | Canonical filesystem tree and directory naming conventions (this file). |
| `engine/engine.md` | File | Agent | Autonomous engine rules: leaf discovery, automated scaffolding, Two-Tier RAG, Playwright, STT. |
| `chat/universal_rules.md` | File | Agent / User | 11 permanent operational invariants (HITL Git confirmation, rendering audits, logging). |
| `chat/chatLog.md` | File | Agent | Full-fidelity chronological conversation and background action transcript. |
| `topics/` | Directory | User / Agent | Root container hosting all learning topics and roadmaps. |
| `topics/<topic>/outline_<topic>.md` | File | User | Topic manifest specifying which subfolder is the terminal leaf node. |
| `<last_subfolder>/template/template.md` | File | User / Agent | Houses user custom templates. If defined, the agent structures all outputs according to it. |
| `<last_subfolder>/Data_Ingestion/Books/` | Directory | Engine | Contains `raw_books/`, `indices/`, and `query_book.py` for deterministic retrieval. |
| `<last_subfolder>/Data_Ingestion/Courses/`| Directory | Engine | Scraped course syllabi and video lecture transcripts via Playwright automation. |
| `<last_subfolder>/Data_Ingestion/Random/` | Directory | Engine | Ad-hoc PDFs/docs and Speech-to-Text transcripts (`.md` / `.json`) from audio files. |
| `<last_subfolder>/output/query_<topic>/` | Directory | Agent | On-demand query manuals, question breakdowns, and technical solutions. |
| `<last_subfolder>/output/Note_version-#_<topic>/` | Directory | Agent | Structured versioned knowledge notes, roadmaps, and syntheses. |
