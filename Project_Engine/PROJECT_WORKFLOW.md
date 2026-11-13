# How This Project Works (Graphical Overview)

> **Source Attribution**: Derived from `Project_Engine/chat/finalized chat.md` (Rules 1-9 and canonical folder structure), `Project_Engine/.agent/skills/` (skill typology), and the repository layout of `1.LLD/` and `2.HLD/`.

## 1. Big Picture: Engine and Topics

`Project_Engine` is the shared core. Every LLD and HLD topic follows its rules, skills and templates.

```mermaid
flowchart TD
    USER["You (the user)"] -->|"adds a topic"| TOPIC
    subgraph REPO["System-Design repository"]
        subgraph ENGINE["Project_Engine (shared core)"]
            RULES["chat/finalized chat.md - Universal Rules"]
            SKILLS[".agent/skills - Skill Generator, UMLSkill, UML25Spec"]
            TEMPL["Skills_Input/Templates - modeling blueprints"]
            TOOLS["scripts - audit_rendering.py and helpers"]
            LOG["chat/chat.md - decision log"]
        end
        subgraph LLD["1.LLD (Low-Level Design)"]
            DP["DESIGN_PATTERNS"]
            AM["ARCHITECTURE_MODELING"]
        end
        subgraph HLD["2.HLD (High-Level Design)"]
            HN["HLD topics (added over time)"]
        end
        TOPIC["New topic folder"]
    end
    RULES --> TOPIC
    SKILLS --> TOPIC
    TEMPL --> TOPIC
    TOOLS --> TOPIC
    TOPIC --> LLD
    TOPIC --> HLD
    TOPIC -->|"decisions recorded"| LOG
```

## 2. Lifecycle of One Task (Rules in Action)

```mermaid
flowchart LR
    A["1. Prompt or new topic"] --> B{"2. Trade-offs exist?"}
    B -->|"yes"| C["HITL: present options, get your confirmation (Rule 4)"]
    B -->|"no"| D
    C --> D["3. Use skills and templates to build the design"]
    D --> E["4. 3-tier mapping: Java code, UML diagram, runtime state (Rule 9)"]
    E --> F["5. Attribute sources (Rule 7)"]
    F --> G["6. Run audit_rendering.py (Rule 2)"]
    G --> H["7. Log session in chat.md (Rule 1)"]
    H --> I["8. Update folder tree (Rule 8)"]
    I --> J["9. Commit and push to origin/main (Rule 3)"]
```

## 3. Inside a Topic Folder

```mermaid
flowchart TD
    T["Topic (e.g. Observer_Pattern or URL_Shortener)"] --> D1["diagrams/ - UML, Mermaid, PlantUML, images"]
    T --> D2["code/ - Java implementation"]
    T --> D3["notes/ - trade-offs and reasoning"]
    T --> D4["resources/ - books and PDFs"]
    D2 -.->|"same concept"| D1
    D3 -.->|"explains"| D1
```

## 4. Skill System

```mermaid
flowchart TD
    SG["SkillGenerator (creates new skills with HITL)"] --> FIXED
    SG --> DYN
    FIXED["SkillsOnFixedResources - Type 1: books and specs"] --> U25["UML25Spec - OMG UML 2.5"]
    DYN["SkillsOnDynamicResources - Type 2: practice and ingestion"] --> UMLS["UMLSkill - problems to solutions"]
    U25 --> OUT["Skills_Output"]
    UMLS --> OUT
    OUT --> QH["query/ - unified manuals"]
    OUT --> SO["UMLSkill_output - question bank and solutions"]
    OUT --> SP["UML25Spec_output - spec outlines"]
```

## 5. Current Repository Map

| Path | Role |
|---|---|
| `Project_Engine/` | Shared core: rules, skills, templates, scripts, logs |
| `1.LLD/` | Low-level topics (design patterns, architecture modeling, UML) |
| `2.HLD/` | High-level topics (system architecture, scaling) |
| `README.md` | The only README in the project (Rule 10); other docs are named by topic |

