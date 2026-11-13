# Finalized Operational Rules & Architectural Directives

This document stores all **Universal Rules** and **Finalized Operational Guidelines** that the AI Agent **must always follow** across every interaction, prompt, code change, and session in this repository.

Whenever the user provides an instruction that is later modified or refined, only the **most up-to-date, finalized version** is recorded here to maintain a clear single source of truth.

---

## 🌐 1. Universal Rules (Mandatory for Every Prompt & Action)

These rules are permanent operational constraints. The agent must enforce them proactively on every step:

### Rule 1: Continuous Conversation Logging
- **Directive**: Every interaction, prompt, architectural decision, and action must be systematically recorded in [`chat/chat.md`](chat.md) in chronological session format.
- **Enforcement**: Never complete a turn involving project updates without appending the session details to `chat/chat.md`.

### Rule 2: Strict Rendering & Formatting Audit (Zero-Failure Policy via Optimized Algorithm)
- **Directive**: Always run or invoke the **Optimized Single-Pass Rendering Auditor** ([`scripts/audit_rendering.py`](../scripts/audit_rendering.py)) before finalizing any prompt or task.
- **The Optimized Verification Algorithm**:
  Rather than sequentially reading all files in the repository, the agent uses an **event-driven diff-scoped linear algorithm**:
  1. **Git-Aware Diff Scoping**: Inspects `git status --porcelain` to identify only the subset of files modified, added, or staged in the current conversation (`O(1)` file selection instead of `O(TotalFiles)`).
  2. **Single-Pass Stream Tokenizer**: Evaluates each targeted file in a single linear pass (`O(Lines)`) tracking code fences, Mermaid block contexts, and prose tokens simultaneously.
  3. **Zero Dollar Signs in Prose**: Enforces that no raw dollar symbols appear in prose text (uses explicit words like "dollars" or backticked expressions).
  4. **Pure Mermaid Syntax & Mandatory Double-Quoted Node Labels**:
     - Verifies that no raw HTML tags (`<b>`, `<br/>`, `<span>`, `<div>`) are present inside Mermaid node labels.
     - **CRITICAL**: Every Mermaid node label (`Node["Label"]`) and edge label (`-->|"Label"|`) that contains parentheses `()`, colons `:`, slashes `/`, or ampersands `&` **MUST** be wrapped in double quotes. Unquoted parentheses inside `Node[Label (Info)]` trigger GitHub's Mermaid lexer crash (`Expecting 'SQE' ... got 'PS'`).
  5. **Standardized Table Cells**: Enforces clean textual markers (`PREVENTED`, `ALLOWED`) instead of multi-byte emoji symbols that misalign column borders.
  6. **Parity Check**: Asserts that all markdown code fences (```` ``` ````) are strictly balanced (total fence count is even).
  7. **Asset Reference Validation**: Verifies that every local image reference (`!` `[alt](path)`) exists on physical disk.
- **CLI Command**: Run `python scripts/audit_rendering.py` (audits active modified/query files) or `python scripts/audit_rendering.py --all` (full repo audit).

### Rule 3: Global Rule on Mandatory Automated Git Commit & Push (Every Prompt Guarantee)
- **Directive**: The agent must **automatically commit and push to GitHub (`origin/main`)** on every single task, user prompt, or repository modification without ever requiring the user to prompt for it.
- **Enforcement & Operational Protocol**:
  1. Inspect `git status --porcelain` before completing any response.
  2. If any tracked or untracked changes exist, stage them with `git add <files>`.
  3. Craft a clean semantic Git commit message conforming to Conventional Commits (`feat:`, `docs:`, `fix:`, `refactor:`, `chore:`).
  4. Immediately execute `git push origin main` to synchronize the remote repository.
  5. The turn is only complete when the local workspace and remote `origin/main` are 100% in sync.

### Rule 4: Human-in-the-Loop (HITL) for Architectural Choices
- **Directive**: The agent must never unilaterally guess diagram categories or pick arbitrary designs when trade-offs exist (e.g. Composition vs Aggregation, Synchronous Call vs Asynchronous Event, State Machine vs Strategy Pattern, Microservice Component Boundary). Present options with trade-offs and seek explicit user confirmation.

### Rule 5: Non-Destructive Ingestion & Zero Data Loss
- **Directive**: Raw source files, staging workbooks, or challenge documents dropped into `put the file here/` or staging documents must **never** be deleted or cleared until the extracted entry is 100% verified inside `question bank.md`.

### Rule 6: Global Rule on Autonomous Reasoning & Pedagogical Simplification
- **Directive**: Using skills as reference **never** restricts the agent from thinking independently. The agent **MUST** inject its own reasoning, analogies, state machine breakdowns, and step-by-step simplifications so that any reader can understand complex UML metamodels, design patterns, and distributed system architectures effortlessly.
- **Enforcement**: Every manual must blend canonical standards (OMG UML 2.5, Fowler, Booch) with the agent's own intuitive explanations, real-world engineering metaphors, and practical runtime insights.

### Rule 7: Global Rule on Mandatory Skill & Concept Source Attribution
- **Directive**: Whenever any concept, quote, diagram, or explanation is generated from a skill, the agent **MUST explicitly state the exact skill name, specification clause, or reference source** where that particular concept or text was taken from (e.g. `> **Source Attribution**: Derived from @UML25Spec (Section 11: Structured Classifiers) and Fowler UML Distilled (Chapter 3: Class Diagrams)`).
- **Enforcement**: Every major section of a generated manual must include a clear source attribution callout alongside a dedicated synthesis table mapping which skill contributed which concept.

### Rule 8: Continuous Synchronization of the Canonical Folder Structure
- **Directive**: The agent must maintain and continuously update the **latest, complete folder structure tree** inside this document (`chat/finalized chat.md`). Whenever directories are moved, added, or restructured, the canonical architecture diagram in Section 2 must be refreshed immediately to reflect the exact state of the project.

### Rule 9: Mandatory 3-Tier Modeling Mapping (OOP Code -> UML Diagram -> Runtime Architecture)
- **Directive**: For **EVERY single modeling concept** discussed, documented, or solved in this repository (e.g., in query manuals, design patterns, architectural syntheses, and problem solutions), the agent **MUST** provide an end-to-end multi-tier demonstration detailing what happens at three distinct layers:
  1. **Coding Level (Strictly Java / OOP Application Logic)**: Show the concrete backend object-oriented implementation in **Java** (e.g., classes, interfaces, abstract classes, field references, method signatures, dependency injection, concurrency primitives, or design pattern wiring).
  2. **UML Diagram Level**: Show the exact formal diagram specification in **Mermaid** and/or **PlantUML** (e.g., Class diagram with multiplicities and visibility, Sequence diagram with lifelines and activation boxes, State Machine with guards/triggers, or Component diagram with ports and interfaces).
  3. **Runtime Architecture / Memory State Level**: Show the concrete physical execution state at runtime. Illustrate the JVM heap object graph, pointer references, stack frames during execution, event queue delivery, or distributed microservice network payloads using structured ASCII state maps or data flow diagrams.
- **Enforcement**: No theoretical concept or operational query manual can be considered complete without this explicit **OOP Code -> UML Diagram -> Runtime State** breakdown.

---

## 🏛️ 2. Finalized Repository Architecture & Output Guidelines

### Canonical Repository Folder Structure (Always Kept Up to Date)

```
UML-Diagramming/
├── .agent/
│   └── skills/
│       ├── SkillGenerator/                         # Universal HITL Skill Scaffolder (scripts/, SKILL.md, SkillArchitecture/)
│       ├── SkillsOnFixedResources/                 # Type 1: Textbooks, Specifications & Course Skills
│       │   └── UML25Spec/                          # Formal OMG UML 2.5 Specification & Reference Skill
│       ├── SkillsOnDynamicResources/               # Type 2: Dynamic Practice & Ingestion Skills
│       │   └── UMLSkill/                           # Dynamic intake, HITL categorization, and solution generator
│       └── type of skills.md                       # Skill Typology Specification (Fixed vs Dynamic)
├── chat/
│   ├── chat.md                                     # Chronological Session & Decision Log
│   └── finalized chat.md                           # Single Source of Truth for Governance Rules
├── scripts/
│   └── audit_rendering.py                          # Single-Pass O(N) Git-Aware Markdown/Diagram Auditor
├── Skills_Input/
│   ├── books/                                      # Curated Textbooks & Specifications
│   │   ├── Overall/                                # Comprehensive Case Studies ([BEST] UML Diagramming.pdf)
│   │   │   ├── chapters/                           # 40 individual Chapter Markdown summaries
│   │   │   └── vector_images/                      # 477 Scalable Vector Graphics (.svg) diagrams by chapter
│   │   ├── Structural/                             # Class, Object, Package, Component, Deployment
│   │   ├── Behavioral/                             # Use Case, Activity, State Machine
│   │   └── Architectural/                          # Interaction, Sequence, Communication, Timing
│   ├── Templates/                                  # Formal Step-by-Step Modeling Blueprints
│   │   ├── Class_and_Object_Diagram_Template.md    # Multiplicities, associations, invariants, OOP mapping
│   │   ├── Sequence_and_Interaction_Diagram_Template.md # Lifelines, synch/asynch, loops, alt/opt fragments
│   │   ├── State_Machine_and_Activity_Diagram_Template.md # States, triggers, guards, actions, fork/join
│   │   └── Use_Case_and_Component_Diagram_Template.md # Actors, boundaries, include/extend, ports/interfaces
│   └── TopicsOutline/                              # Master Domain Outlines
│       └── UML_2.5_Diagrams_Master_Outline.md      # Taxonomy of all 14 UML 2.5 diagrams
├── Skills_Output/
│   ├── Skills_Output_README.md                     # Centralized Output Protocol & Hub Guide
│   ├── query/                                      # 🌟 UNIFIED QUERY HUB (All Single & Combined Syntheses)
│   │   ├── Query_Hub_README.md                     # Master Index of all generated manuals
│   │   └── 001_uml_2_5_taxonomy_structural_vs_behavioral.md # Inaugural reference manual
│   ├── UMLSkill_output/                            # Dynamic Problem Ingestion & Modeling Solutions
│   │   ├── Problem Files/                          # Ingested challenges, question bank & formatting specs
│   │   │   ├── Problem_Files_README.md             # Registry instructions
│   │   │   ├── problem formatting.md               # Standardized problem schema
│   │   │   ├── problem categories.md               # 2-Tier category & subcategory taxonomy
│   │   │   ├── question bank.md                    # Master problem archive table
│   │   │   └── Source of Problem/                  # Ingestion drop zones
│   │   │       ├── Source_Of_Problem_README.md     # Ingestion workflow guide
│   │   │       └── put the file here/              # PDF / raw file staging drop zone
│   │   │           └── Put_The_File_Here_README.md
│   │   ├── Solution Files/                         # Multi-representation solutions
│   │   │   ├── Solution_Files_README.md            # Solution archive directory guide
│   │   │   └── Solution formatting.md              # Diagram (.puml/.mmd) + Java + Derivation spec
│   │   └── UMLSkill_Output_README.md               # Dynamic Skill Output Hub
│   └── UML25Spec_output/                           # Fixed Resource Output Workspace
│       ├── outline/                                # Complete specification outlines
│       │   └── UML25Spec_Complete_Outline.md       # Comprehensive 22-clause specification map
│       └── UML25Spec_Output_README.md              # Reference Skill Output Hub
├── Upcoming Updates/
│   └── Upcoming Updates.md                         # Serialized Milestone & Feature Tracking
├── .gitattributes                                  # Line normalization rules
├── .gitignore                                      # Standard repository exclusions
└── README.md                                       # Repository Overview & Public Portal
```
