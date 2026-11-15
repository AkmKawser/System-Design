# Finalized Operational Rules & Architectural Directives

This document stores all **Universal Rules** and **Finalized Operational Guidelines** that the AI Agent **must always follow** across every interaction, prompt, code change, and session in this repository.

Whenever the user provides an instruction that is later modified or refined, only the **most up-to-date, finalized version** is recorded here to maintain a clear single source of truth.

---

## 🎯 0. Project Scope

This repository (**System-Design**) holds all **LLD** (`1.LLD/`) and **HLD** (`2.HLD/`) study topics. **`Project_Engine/`** is the shared core: every LLD and HLD topic must follow the Universal Rules below and use the skills, templates, scripts and logs inside it. Paths in the rules (`chat/`, `scripts/`, `Skills_Input/`, `Skills_Output/`) are relative to `Project_Engine/`.

---

## 🌐 1. Universal Rules (Mandatory for Every Prompt & Action)

These rules are permanent operational constraints. The agent must enforce them proactively on every step:

### Rule 1: Continuous Conversation Logging (Exhaustive Full-Transcript Protocol)
- **Directive**: Every single interaction without exception must be systematically recorded in [chat/chat.md](chat.md) in chronological session format **immediately after the agent finishes formulating the response**.
- **Mandatory Contents for Every Session Entry**:
  1. **User Request / Prompt**: The exact user prompt or question in full.
  2. **Agentic Log**: Key internal actions, decisions made, tools invoked, file modifications, and verification steps executed.
  3. **Agent Response**: The complete response, solution, or guidance delivered to the user.
- **Enforcement**: By default, automatically update chat/chat.md on every turn before finalizing the Git commit and push (Rule 3). Never conclude an exchange without an exhaustive log entry in chat/chat.md.

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

### Rule 10: Single README Policy (One `README.md` Per Project)
- **Directive**: There must be **exactly one `README.md` in the entire project**, located at the repository root (`System-Design/README.md`). Every other readme-style or guide file must be named after its topic as `<Topic>.md` (e.g. `Observer_Pattern.md`, `Query_Hub.md`, `Skills_Output_Guide.md`), never `README.md` or `HLD_Overview.md`.
- **Enforcement**:
  1. Before creating any new documentation file, confirm it is not named `README.md` (case-insensitive) unless it is the root file.
  2. When renaming a file under this rule, update every markdown link and reference that points to the old name.
  3. The final rendering audit must flag any extra `README.md` found outside the repository root.
### Rule 11: No `.gitignore` Without Explicit User Instruction
- **Directive**: The agent must **never create, add, or modify any `.gitignore` file** (at the repository root or in any subfolder) unless the user explicitly tells it to.
- **Enforcement**:
  1. Do not use `.gitignore` to hide, exclude, or untrack files (including large files, build output, or private folders) on your own initiative.
  2. If a file or folder seems like it should be ignored, ask the user first instead of adding a `.gitignore` entry.
  3. Existing `.gitignore` files inside the project may only be edited when the user explicitly requests it.
---

## 🏛️ 2. Finalized Repository Architecture & Output Guidelines (System-Design: LLD + HLD powered by Project_Engine)

### Canonical Repository Folder Structure (Always Kept Up to Date)

```
System-Design/
├── Project_Engine/                                 # SHARED CORE: tooling, skills, scripts, and logs
│   ├── .agent/
│   │   └── skills/
│   │       ├── SkillGenerator/                     # Universal HITL Skill Scaffolder (scripts/, SKILL.md, SkillArchitecture/)
│   │       ├── SkillsOnFixedResources/             # Type 1: Textbooks, Specifications & Course Skills
│   │       │   └── UML25Spec/                      # Formal OMG UML 2.5 Specification & Reference Skill
│   │       ├── SkillsOnDynamicResources/           # Type 2: Dynamic Practice & Ingestion Skills
│   │       │   └── UMLSkill/                       # Dynamic intake, HITL categorization, and solution generator
│   │       └── type of skills.md                   # Skill Typology Specification (Fixed vs Dynamic)
│   ├── chat/
│   │   ├── chat.md                                 # Chronological Session & Decision Log
│   │   └── finalized chat.md                       # Single Source of Truth for Governance Rules
│   ├── scripts/                                    # audit_rendering.py (Single-Pass O(N) Git-Aware Auditor) + tooling
│   ├── Skills_Output/
│   │   ├── Skills_Output.md                        # Centralized Output Protocol & Hub Guide
│   │   └── query/                                  # UNIFIED QUERY HUB (Topic-Centric Multi-Skill Syntheses)
│   │       ├── Query_Hub.md                        # Master Index of all generated manuals (Rule 10 compliant)
│   │       ├── UML_Metamodels/                     # UML 2.5 standards & metamodel taxonomy
│   │       │   └── 001_uml_2_5_taxonomy_structural_vs_behavioral.md
│   │       ├── Design_Patterns/                    # GoF, enterprise & cloud patterns
│   │       ├── Distributed_Systems/                # Microservices, consensus, replication & caching
│   │       ├── Concurrency_and_Runtimes/           # JVM memory model, threads, locks
│   │       └── System_Requirements/                # Capacity planning, FR/NFR analysis
│   ├── Upcoming Updates/
│   │   └── Upcoming Updates.md                     # Serialized Milestone & Feature Tracking
│   ├── PROJECT_WORKFLOW.md                         # Graphical overview of how the project runs
│   └── Project_Engine.md                           # Engine Overview (topic-named, Rule 10)
├── 0.FUNDAMENTALS/                                 # Core Software Engineering Foundations
│   ├── System Requirements/                        # Requirements taxonomies, FRs, NFRs, templates
│   ├── Software Development Lifecycle/             # Methodologies, SDLC phases, testing, CI/CD (Outline.md)
│   ├── Software Architecture and Modeling/         # Views, patterns, ADRs, modeling (Outline.md)
│   │   ├── 1.ARCHITECTURE/                         # Architecture principles and documentation
│   │   └── 2.ARCHITECTURE_MODELING/                # Viewpoints & perspectives textbook and guides
│   ├── Science of Language Frameworks [Backend]/   # Runtimes, threading, frameworks, protocols (Outline.md)
│   ├── Design System [Front End]/                  # Design tokens, components, state, a11y (Outline.md)
│   └── Select Technology Stack/                    # Framework and technology selection matrices
├── 1.LLD/                                          # Low-Level Design topics (use Project_Engine)
│   ├── DESIGN_PATTERNS/                            # Chapter-1 Strategy ... Chapter-5 Singleton
│   └── UML-DIAGRAMMING/                            # UML case studies, specs, vector diagrams (Books/umlBook)
├── 2.HLD/                                          # High-Level Design topics (use Project_Engine)
│   └── HLD_Overview.md
└── README.md                                       # THE ONLY README.md in the project (Rule 10)
```
