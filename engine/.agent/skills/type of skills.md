# Paradigms of Agent Skills in UML Diagramming

In the **UML Diagramming & Software Architecture** engineering framework, agent skills are designed as modular, autonomous capabilities connecting agentic AI models directly to authoritative modeling standards, rigorous object-oriented analysis blueprints, and structured ingestion/solution pipelines.

Following the proven architecture from `Science of Coding` and `Database Management System`, skills are categorized into two primary paradigms:
1. **Type 1: Fixed Resource Skills (`SkillsOnFixedResources`)**
2. **Type 2: Dynamic Resource Skills (`SkillsOnDynamicResources`)**

---

## 📚 Type 1: Fixed Resource Skills (`SkillsOnFixedResources`)

### 1. Concept & Purpose
A **Fixed Resource Skill** encapsulates an authoritative reference textbook, standard specification (such as the OMG Unified Modeling Language 2.5 Specification), or structured video course into an agent-executable knowledge base. Rather than dumping raw, unindexed documents into the prompt (which exhausts context and causes hallucinations), the skill organizes domain references into:
1. **Machine-Readable Routing Maps**: Fast table-of-contents files (`references/table_of_contents.md`, `references/toc.json`) allowing the agent to pinpoint clauses, diagrams, and metamodel definitions with zero token overhead.
2. **Surgical Precision CLI**: Python extraction scripts (`scripts/query_uml.py`) that search and retrieve relevant clauses, notation guidelines, or formal constraint rules on demand.
3. **Collaborative Design Protocol**: Behavioral guardrails requiring the agent to present candidate modeling options alongside trade-offs (e.g. Composition vs Aggregation, Synchronous Call vs Event-Driven Messaging) and obtain user consensus before generating final diagrams or code.

### 2. Concrete Implementations
- **`UML25Spec`**:
  - Located at: [`.agent/skills/SkillsOnFixedResources/UML25Spec/`](SkillsOnFixedResources/UML25Spec/)
  - Covers formal OMG UML 2.5 metamodels, 14 canonical diagram definitions, classifier semantics, interaction lifelines, and state transition specifications.
  - Dedicated Output Directory: [`Skills_Output/UML25Spec_output/`](../../Skills_Output/UML25Spec_output/) (stores curriculum outlines and query outputs).

---

## 🛠️ Type 2: Dynamic Resource Skills (`SkillsOnDynamicResources`)

### 1. Concept & Purpose
A **Dynamic Resource Skill** manages the dynamic intake, categorization, standardized formatting, and template-guided synthesis of real-world software architecture challenges, design pattern problems, and domain modeling specifications.

The Dynamic Resource Skill enforces:
1. **Multi-Channel Ingestion**:
   - **Document Drop Zones**: Ingestion folders ([`put the file here/`](../../Skills_Output/UMLSkill_output/Problem%20Files/Source%20of%20Problem/put%20the%20file%20here/)) for software requirement specifications (SRS), RFCs, problem briefs, and architectural challenge documents.
   - **Staging Documents**: Structured text or workbooks capturing design interview prompts and system architecture requirements.
2. **Dynamic 2-Tier Hierarchical Classification (HITL)**:
   - Reads real-time categories and subcategories from [`problem categories.md`](../../Skills_Output/UMLSkill_output/Problem%20Files/problem%20categories.md).
   - Engages the developer in an interactive Human-in-the-Loop (HITL) prompt to confirm the **Primary Category** (e.g., Structural Modeling) and **Subcategory** (e.g., Class Diagrams & Invariants) before saving entries.
3. **Non-Destructive Archival Protocol**:
   - Formats raw problem requirements into standardized Markdown schema with unique Problem IDs (e.g., `UML-1`) in [`question bank.md`](../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md).
   - Zero-data loss guarantee: raw source files are never deleted until entries are verified on disk.
4. **Mandatory 3-Tier Multi-Representation Outputs**:
   - Adheres to [`Solution formatting.md`](../../Skills_Output/UMLSkill_output/Solution%20Files/Solution%20formatting.md).
   - Generates separated, high-fidelity artifacts:
     - Standalone diagram definitions (`<ID>_diagram.puml` / `<ID>_diagram.mmd`).
     - Concrete backend OOP code implementation in Java (`<ID>_implementation.java`).
     - Comprehensive derivation and architectural trade-off manual (`<ID>_derivation.md`).

### 2. Concrete Implementations
- **`UMLSkill`**:
  - Located at: [`.agent/skills/SkillsOnDynamicResources/UMLSkill/`](SkillsOnDynamicResources/UMLSkill/)
  - Dedicated Output Directory: [`Skills_Output/UMLSkill_output/`](../../Skills_Output/UMLSkill_output/).

---

## ⚖️ Summary Comparison

| Dimension | Type 1: Fixed Resource Skill (`SkillsOnFixedResources`) | Type 2: Dynamic Resource Skill (`SkillsOnDynamicResources`) |
| :--- | :--- | :--- |
| **Primary Goal** | Grounding formal UML metamodels, semantics & standards | Ingesting, organizing, classifying, & solving modeling problems |
| **Primary Artifact** | Reference books, specifications (OMG UML 2.5) & TOC indexes | Staging requirements, question bank, & template blueprints |
| **Source Channels** | Curated textbooks, specification PDFs, and course transcripts | SRS documents, interview challenges, design RFCs, problem briefs |
| **Core Mechanism** | Zero-token TOC routing & precision CLI keyword extraction | Dynamic HITL 2-level category selection & atomic archiving |
| **Output Delivery** | Specification deep-dives, notation rules, and query manuals | 3-tier solutions: Diagram (`.puml`/`.mmd`) + Java code + Derivation |
| **Representative Skill**| [`UML25Spec`](SkillsOnFixedResources/UML25Spec/) | [`UMLSkill`](SkillsOnDynamicResources/UMLSkill/) |
| **Output Workspace** | [`Skills_Output/UML25Spec_output/`](../../Skills_Output/UML25Spec_output/) | [`Skills_Output/UMLSkill_output/`](../../Skills_Output/UMLSkill_output/) |

