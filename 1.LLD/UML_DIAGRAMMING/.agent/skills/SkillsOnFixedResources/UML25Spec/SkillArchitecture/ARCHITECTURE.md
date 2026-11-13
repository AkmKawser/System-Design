# Architecture & Operational Mechanics: `UML25Spec` Skill

## 1. System Overview & Purpose

The **`UML25Spec`** skill is a portable, self-contained, agent-agnostic knowledge and retrieval module encapsulating:
* **Resource Type**: Specification
* **Source Path**: `Skills_Input/books`
* **Architecture Standard**: SkillsOnFixedResources (Type 1)

---

## 2. Directory Layout

```
.agent/skills/SkillsOnFixedResources/UML25Spec/
├── SkillArchitecture/
│   ├── ARCHITECTURE.md                  <-- Technical specifications (this file)
│   └── UML25Spec_Architecture_README.md  <-- High-level overview & agent execution rules
├── SKILL.md                             <-- Universal agent entrypoint & query decision rules
├── references/
│   ├── table_of_contents.md             <-- Fast human & agent topic index
│   └── toc.json                         <-- Machine-readable outline tree
└── scripts/
    └── query_uml25spec.py    <-- Precision CLI search & extraction
```
