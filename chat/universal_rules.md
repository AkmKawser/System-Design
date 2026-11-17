# Finalized Operational Rules & Architectural Directives

This document stores all **Universal Rules** and **Finalized Operational Guidelines** that the AI Agent **must always follow** across every interaction, prompt, code change, and session in this repository.

Whenever the user provides an instruction that is later modified or refined, only the **most up-to-date, finalized version** is recorded here to maintain a clear single source of truth.

---

## 🎯 0. Project Scope

This repository (**System-Design**) holds all **LLD** (`1.LLD/`) and **HLD** (`2.HLD/`) study topics. **`engine/`** is the shared computational core: every LLD and HLD topic must follow the Universal Rules below and use the templates, scripts, and logs inside it. Paths in the rules (`chat/`, `engine/scripts/`, `engine/Skills_Output/`) are relative to the repository root.

---

## 🌐 1. Universal Rules (Mandatory for Every Prompt & Action)

These rules are permanent operational constraints. The agent must enforce them proactively on every step:

### Rule 1: Continuous Conversation Logging (Exhaustive Full-Transcript Protocol)
- **Directive**: Every single interaction without exception must be systematically recorded in [chat/chatLog.md](chatLog.md) in chronological session format **immediately after the agent finishes formulating the response**.
- **Mandatory Contents for Every Session Entry**:
  1. **User Request / Prompt**: The exact user prompt or question in full.
  2. **Agentic Log**: Key internal actions, decisions made, tools invoked, file modifications, and verification steps executed.
  3. **Agent Response**: The complete response, solution, or guidance delivered to the user.
- **Enforcement**: By default, automatically update chat/chatLog.md on every turn before finalizing the Git commit and push (Rule 3). Never conclude an exchange without an exhaustive log entry in chat/chatLog.md.

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
- **Directive**: The agent must maintain and continuously update the **latest, complete folder structure tree** inside this document (`chat/universal_rules.md`). Whenever directories are moved, added, or restructured, the canonical architecture diagram in Section 2 must be refreshed immediately to reflect the exact state of the project.

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

### Rule 11: Continuous Output and Query Manual Indexing in Root `README.md`
- **Directive**: The root `README.md` must continuously and dynamically feature an exhaustive, dedicated **Master Output & Query Catalog** table indexing **every single output, query manual, and architectural deliverable** created in this repository (such as files under `topics/<topic>/output/query_<topic>/` and topic-level guides).
- **Required Metadata in Root `README.md` for Each Output**:
  1. **Output ID / Scope**: Serialized identifier (e.g. `QUERY-001`, `QUERY-002`, `LLD-DP-001`, `ARCH-001`).
  2. **Topic / Category**: Target category or query subfolder (e.g. `UML_Metamodels`, `DESIGN_PATTERNS`, `1.ARCHITECTURE`).
  3. **Output Title / Name**: Human-readable, descriptive topic title.
  4. **Core Focus / Description**: Summary of core invariants, 3-tier models, or design analysis covered.
  5. **Direct Clickable Link**: Direct file link to the output artifact.
- **Enforcement**:
  - Whenever any query manual, design pattern guide, or topic output is produced or updated, the agent **MUST immediately add or refresh its entry in the root `README.md` catalog** before concluding the turn.
  - The rendering audit script (`audit_rendering.py`) and agent verification steps must ensure all links in this catalog resolve cleanly.

### Rule 12: Continuous Synchronization of `index.md` (Master Navigation Catalog)
- **Directive**: Whenever a new topic, subtopic, query manual, versioned study note, or roadmap deliverable is created, modified, or relocated anywhere in the repository, the agent **MUST immediately update the master navigation catalog**:
  - **Root Master Catalog ([`index.md`](../index.md))**: The primary navigation catalog at the repository root must always index the topic name, category/scope, terminal subfolder path, active query manuals, and versioned notes.
- **Enforcement**:
  - The turn is considered incomplete if changes were made to topics or outputs without updating `index.md`.
  - All relative links inside `index.md` must resolve cleanly to existing files and directories on disk.

### Rule 13: No `.gitignore` Without Explicit User Instruction
- **Directive**: The agent must **never create, add, or modify any `.gitignore` file** (at the repository root or in any subfolder) unless the user explicitly tells it to.
- **Enforcement**:
  1. Do not use `.gitignore` to hide, exclude, or untrack files (including large files, build output, or private folders) on your own initiative.
  2. If a file or folder seems like it should be ignored, ask the user first instead of adding a `.gitignore` entry.
  3. Existing `.gitignore` files inside the project may only be edited when the user explicitly requests it.

### Rule 14: Comprehensive Resource Image Ingestion for Queries (Book & Course Visual Grounding)
- **Directive**: Whenever the user poses an analytical query or request referencing an ingested resource (book PDF, video course, documentation, or technical slide deck), the agent **MUST** extract, preserve, and integrate all pertinent visual assets (diagrams, architecture topologies, workflow schematics, taxonomy charts, and scorecard ratings) into the generated query manual.
- **Enforcement & Operational Protocol**:
  1. **Source Asset Extraction**: Locate the underlying book or course artifact within `Data_Ingestion/Books/` or `Data_Ingestion/Courses/`. Programmatically extract all relevant figures, diagrams, and scorecards associated with the queried topic into a localized asset repository (`Data_Ingestion/Books/images/` or topic-specific asset directories).
  2. **In-Prose Visual Embedding**: Directly embed each extracted figure in the corresponding section of the generated `.md` file using clean markdown image syntax with backticks or relative path syntax.
  3. **Multi-Modal Synchronization**: Every embedded diagram must be paired with precise source attribution (Figure number, chapter, page number) alongside the agent's autonomous architectural explanation, failure mode analysis, and trade-off evaluation.
  4. **Disk Existence & Integrity Verification**: The agent must verify that every embedded image path physically resolves on disk (audited via `scripts/audit_rendering.py`). Broken or non-existent image paths are strictly forbidden.

### Rule 15: Single `outline.md` Policy (Universal Master Topic Outline Protocol)
- **Directive**: There must be **strictly one `outline.md` file in the entire repository**, located at the repository root (`System-Design/outline.md`). **Only topic outlines from all over the project are kept in this file**.
- **Mandatory Principles & Invariants**:
  1. **Strictly Topic Outline Content**: Unlike `index.md` (which maps filesystem navigation, terminal folders, query outputs, and versioned notes) and `README.md` (which provides the project landing overview and output catalog), `outline.md` is **strictly reserved for holding the comprehensive pedagogical curriculum and topic syllabus breakdown** across all domains (`0.FUNDAMENTALS`, `1.LLD`, `2.HLD`).
  2. **Zero Scattered Outlines in Subfolders**: No individual or redundant `outline.md`, `Outline.md`, or `outline_<topic>.md` files may exist in subdirectories or topic folders. All topic-level and subtopic-level learning outlines must be consolidated and maintained exclusively inside root `outline.md`.
  3. **Continuous Synchronization**: Whenever a new topic, subtopic, or curriculum module is created, modified, or reorganized, the agent **MUST** update root `outline.md` to reflect the complete project-wide curriculum.

### Rule 16: Isolated Book Encapsulation & Concise Naming Protocol (Max Length Limits)
- **Directive**: Every PDF book in the repository **MUST** reside inside its own dedicated subfolder under `Data_Ingestion/Books/<Book_Folder_Name>/`. Loose PDF book files directly under `Data_Ingestion/Books/` are strictly prohibited. Both the folder name and the PDF file name **MUST adhere to strict character length limits and clean slug conventions** to prevent Windows OS MAX_PATH (260 characters) violations and ensure desktop accessibility.
- **Strict Character Length & Slug Limits**:
  1. **Folder Name Character Limit**: **Maximum 25 characters** (`len(folder_name) <= 25`). Must use clean, concise kebab-case or snake_case slugs without spaces, subtitles, authors, or special punctuation (e.g., `fund-soft-arch/`, `arch-patterns/`, `arch-viewpoints/`, `headfirst/`, `umlBook/`).
  2. **PDF File Name Character Limit**: **Maximum 30 characters** (`len(file_name) <= 30`, including the `.pdf` extension). Must be concise, matching the folder slug (e.g., `fund-soft-arch.pdf`, `arch-patterns.pdf`, `arch-viewpoints.pdf`, `uml-diagramming.pdf`).
  3. **Zero Whitespace & URL Safety**: No spaces or special characters (`[]`, `()`, `&`, `+`) are permitted in book folder or file names. This eliminates URL-encoding artifacts (`%20`) in markdown image links and guarantees cross-platform compatibility across Windows Explorer, macOS, Linux, and terminal CLIs.
- **Mandatory Principles & Invariants**:
  1. **Automated Folder Creation by Agent**: Whenever the user supplies, drops, or requests the ingestion of a book PDF, the agent **MUST automatically create** a dedicated concise subfolder obeying the maximum 25-character limit inside `Data_Ingestion/Books/`.
  2. **Complete Book Asset Co-location**: All data, assets, extracted figures, vector diagrams, chapter breakdowns, and indices derived from that book **MUST** be placed and preserved exclusively inside that specific book's dedicated folder:
     - Source PDF: `Data_Ingestion/Books/<short_slug>/<short_slug>.pdf`
     - Extracted figures/images: `Data_Ingestion/Books/<short_slug>/images/` (or `vector_images/`)
     - Extracted chapters: `Data_Ingestion/Books/<short_slug>/chapters/`
     - Book documentation and guides: `Data_Ingestion/Books/<short_slug>/<short_slug>.md`
  3. **Strict Inter-Book Isolation**: No book assets or images may spill into the parent `Data_Ingestion/Books/` directory or mix with assets belonging to another book. Every book folder forms an isolated, self-contained knowledge package.

### Rule 17: Standalone Animated SVG & Diagram Style Guide (Vector & Animation Standards)
- **Directive**: All standalone animated vector diagrams created or embedded across the repository **MUST strictly adhere to the Canonical Animated Diagram Style Guide** ([`architecture/diagram_style_guide.md`](../architecture/diagram_style_guide.md)), using [`animated_images/ui-api-backend-flow.svg`](../animated_images/ui-api-backend-flow.svg) as the reference standard.
- **Mandatory Specifications & Invariants**:
  1. **Format & Sizing**:
     - Standalone SVG file with an embedded `<style>` block.
     - Strictly no HTML tags, no `<foreignObject>`, no JavaScript, no external files, and no CSS variables.
     - Fixed width: `width="680"`, viewport: `viewBox="0 0 680 H"`, with exactly 20px bottom padding below the lowest element.
     - Root element must define `role="img"`, `<title>`, and `<desc>` for accessibility.
  2. **Typography**:
     - System font stack: `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`.
     - Exactly two font sizes: `14px` (font-weight 500 for titles) and `12px` (subtitles and labels).
     - Sentence case capitalization only; subtitles must contain 5 words or fewer.
     - Centered text alignment: `text-anchor="middle"` and `dominant-baseline="central"` inside all boxes.
  3. **Boxes, Colors & Arrows**:
     - Primary concept boxes: Rounded rectangles (`rx="8"`), `120px` width, `20px` inter-box gap, `0.5px` stroke.
     - Analogy boxes: Matching rounded shape with dashed stroke (`stroke-dasharray="4 3"`), `36px` height.
     - Palette: 2 to 3 cohesive families (Gray, Teal, Purple). Light fill, darker border, darkest text of that family.
     - Theme Adaptability: Dedicated `@media (prefers-color-scheme: dark)` block with dark fills, light borders, and light text ensuring 100% legibility in both Light and Dark modes.
     - Arrows: `1.5px` stroke with small open arrowheads, `16px` span between boxes.
     - Traffic Lanes: Dashed `1px` lines above (Request lane) and below (Response lane) the boxes.
  4. **CSS Animation Loop**:
     - Pure CSS `@keyframes` animating only `opacity` and `transform`.
     - Continuous loop: Exactly one `12s` linear infinite cycle.
     - Request packet: Amber circle traveling along the top lane, stopping at the center of each box.
     - Response packet: Green circle returning along the bottom lane.
     - Box highlight: `2.5px` amber outline fading in when the packet arrives at the active box.
     - Dynamic caption: Step-by-step explanatory caption below the diagram synchronized with packet arrival.
     - Accessibility: Keyframe animations must be wrapped inside `@media (prefers-reduced-motion: no-preference)`, displaying static captions when motion is reduced.
  5. **Embedding Protocol**:
     - Must be saved in `animated_images/<name>.svg` (or topic-specific subfolder).
     - Must be embedded in Markdown exclusively via image syntax:
       ```markdown
       ![Alt Text](relative/path/to/diagram.svg)
       ```
     - **NEVER** paste raw SVG XML code directly into Markdown files, as GitHub and GitBook will strip the CSS animations.
  6. **Sequence Diagram Animation Protocol**:
     - Participants are boxes across the top (120px wide, 20px gaps, centers at `x = 160 + 140 * i`), each with a dashed vertical lifeline running down (`stroke-dasharray="4 4"`).
     - Messages are horizontal arrows between lifelines, spaced exactly `40px` apart vertically, in chronological time order from top to bottom.
     - Requests use solid 1.5px arrows. Responses use dashed 1.5px arrows pointing back.
     - Message labels are 12px text centered directly above each arrow.
     - One single amber dot follows the full message path as a continuous line, dropping down lifelines between message steps. Each arrow and label fades in (`opacity: 1`) when the dot reaches it.
     - The caption at the bottom changes dynamically at each message step.
     - Dot keyframe positions (`translate(x, y)`), arrow fade-in times, and caption transition times must be strictly synchronized.
  7. **Universal Diagram Archetype Policy (Mandatory Claude Animated SVG)**:
     - Moving forward, **ALL diagrams created across the repository MUST use this Canonical Claude Animated SVG format** adhering to the respective archetype in [`architecture/diagram_style_guide.md`](../architecture/diagram_style_guide.md) (Horizontal Pipeline, Sequence Diagram, Topology, or State Machine).
     - Static Mermaid diagrams are preserved as companion text-mode code representations, but the primary pedagogical visualization asset must always be the theme-adaptive, animated standalone SVG.

---

## 🏛️ 2. Finalized Repository Architecture & Output Guidelines (Learning-Roadmap Architecture)

### Canonical Repository Folder Structure (Always Kept Up to Date)

```
System-Design/
├── README.md                                 # Single root project overview & Master Output Catalog
├── index.md                                  # Master Navigation Catalog: Topics, Queries & Notes
├── outline.md                                # Single Master Topic Outline (consolidating all curricula)
├── .gitbook.yaml                             # GitBook Space & Root Configuration
├── gitbook-docs.yaml                         # GitBook Site-Wide Git Sync Architecture
├── animated_images/                          # Standalone Animated Vector SVGs
│   └── ui-api-backend-flow.svg               # Canonical reference animated diagram
│
├── architecture/                             # Architectural Specifications Subsystem
│   ├── architecture.md                       # Comprehensive Project Architecture & Sequence Lifecycles
│   ├── folderstructure.md                    # Canonical Filesystem Topology Specification
│   └── diagram_style_guide.md                # Standalone Animated SVG & Diagram Standards
│
├── engine/                                   # Computational & Agentic Engine Subsystem
│   ├── engine.md                             # Scaffolding logic, Two-Tier ingestion & verification
│   ├── scripts/                              # audit_rendering.py, extract_chapters.py, etc.
│   └── Skills_Output/                        # Universal query hub & output staging
│
├── chat/                                     # Governance, Logging & Rules Subsystem
│   ├── universal_rules.md                    # Permanent Operational Invariants (HITL Git confirmation, etc.)
│   └── chatLog.md                            # Full-fidelity chronological activity transcript
│
├── Upcoming Updates/                         # Strategic Roadmaps & Forward-Looking Blueprints
│   └── Upcoming Updates.md                   # Shared Agent Memory roadmap & implementation plan
│
└── topics/                                   # Domain Knowledge & Learning Roadmaps Root
    ├── 0.FUNDAMENTALS/                       # Core Software Engineering Foundations
    │   ├── outline_0.FUNDAMENTALS.md         # Topic Manifest
    │   ├── System Requirements/
    │   ├── Software Development Lifecycle/
    │   ├── Software Architecture and Modeling/
    │   │   ├── 1.ARCHITECTURE/               # Terminal Leaf: template/, Data_Ingestion/, output/
    │   │   └── 2.ARCHITECTURE_MODELING/      # Viewpoints & Perspectives reference
    │   ├── Science of Language Frameworks [Backend]/
    │   ├── Design System [Front End]/
    │   ├── Select Technology Stack/
    │   ├── API Architecture and Design/      # Terminal Leaf: template/, Data_Ingestion/Courses/, output/
    │   └── Networking/                       # Terminal Leaf: template/, Data_Ingestion/Courses/, output/
    │
    ├── 1.LLD/                                # Low-Level Design Root
    │   ├── outline_1.LLD.md                  # LLD Manifest
    │   ├── DESIGN_PATTERNS/                  # Terminal Leaf: template/, Data_Ingestion/, output/
    │   └── UML-DIAGRAMMING/                  # Terminal Leaf: template/, Data_Ingestion/, output/
    │
    └── 2.HLD/                                # High-Level Design Root
        ├── outline_2.HLD.md                  # HLD Manifest
        └── HLD_Overview/                     # Terminal Leaf: template/, Data_Ingestion/, output/
```
