# How This Project Works (Graphical Overview)

> **Source Attribution**: Derived from `chat/universal_rules.md` (Universal Rules and canonical folder structure), `engine/` computational core, and the repository layout of `0.FUNDAMENTALS/`, `1.LLD/`, and `2.HLD/`.

## 1. Big Picture: Engine and Topics

`engine/` is the shared computational core. Every LLD and HLD topic follows its operational rules, templates, scripts, and logs.

```mermaid
flowchart TD
    USER["You (the user)"] -->|"adds a topic"| TOPIC
    subgraph REPO["System-Design repository"]
        subgraph ENGINE["engine (shared computational core)"]
            RULES["chat/universal_rules.md - Universal Rules"]
            TEMPL["Templates - modeling blueprints"]
            TOOLS["engine/scripts - audit_rendering.py and helpers"]
            LOG["chat/chatLog.md - decision log"]
        end
        subgraph FUND["0.FUNDAMENTALS"]
            FD["Architecture Styles & SDLC"]
        end
        subgraph LLD["1.LLD (Low-Level Design)"]
            DP["DESIGN_PATTERNS"]
            UML["UML-DIAGRAMMING"]
        end
        subgraph HLD["2.HLD (High-Level Design)"]
            HN["HLD topics (added over time)"]
        end
        TOPIC["New topic folder"]
    end
    RULES --> TOPIC
    TEMPL --> TOPIC
    TOOLS --> TOPIC
    TOPIC --> FUND
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
    C --> D["3. Use templates to build the design"]
    D --> E["4. 3-tier mapping: Java code, UML diagram, runtime state (Rule 9)"]
    E --> F["5. Attribute sources (Rule 7)"]
    F --> G["6. Run audit_rendering.py (Rule 2)"]
    G --> H["7. Log session in chatLog.md (Rule 1)"]
    H --> I["8. Update folder tree (Rule 8)"]
    I --> J["9. Commit and push to origin/main (Rule 3)"]
```

## 3. Inside a Topic Folder

Every topic workspace contains its own dedicated template, data ingestion resources, and structured outputs:

```mermaid
flowchart TD
    T["Topic (e.g. DESIGN_PATTERNS or HLD_Overview)"] --> TMP["template/ - topic-specific output template"]
    T --> DI["Data_Ingestion/ - books, source PDFs, and references"]
    T --> OUT["output/ - query manuals and versioned notes"]
    OUT --> QM["query_<topic>/ - targeted query deep dives"]
    OUT --> VN["Note_version-#_<topic>/ - comprehensive versioned notes"]
```

## 4. Current Repository Map

| Path | Role |
|---|---|
| `engine/` | Shared computational core: scripts, tools, and query hubs |
| `chat/` | Operational rules (`universal_rules.md`) and session history (`chatLog.md`) |
| `architecture/` | System architecture models and canonical folder structure |
| `topics/0.FUNDAMENTALS/` | Core architecture fundamentals, SDLC, tech stack selection |
| `topics/1.LLD/` | Low-level design: Design Patterns, UML Diagramming |
| `topics/2.HLD/` | High-level design: System architecture, scaling |
| `README.md` | Single root project overview and master output catalog |
| `index.md` | Master Navigation Catalog indexing all topics, queries, and notes |
| `outline.md` | Single Master Topic Outline consolidating all curricula |

