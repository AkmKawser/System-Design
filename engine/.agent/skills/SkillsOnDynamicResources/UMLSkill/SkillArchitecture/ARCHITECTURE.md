# Architecture & Operational Mechanics: `UMLSkill` Skill

## 1. System Overview & Purpose

The **`UMLSkill`** skill manages dynamic problem intake, interactive human-in-the-loop classification, non-destructive archiving, and multi-tier solution generation (Diagram + Java Code + Architectural Derivation).

---

## 2. Directory Layout

```
.agent/skills/SkillsOnDynamicResources/UMLSkill/
├── SkillArchitecture/
│   ├── ARCHITECTURE.md                  <-- Technical specifications (this file)
│   └── UMLSkill_Architecture_README.md  <-- High-level overview & agent execution rules
├── SKILL.md                             <-- Universal agent entrypoint & decision rules
└── scripts/
    └── ingest_manager.py                <-- Autonomous queue scanner & HITL parser
```
