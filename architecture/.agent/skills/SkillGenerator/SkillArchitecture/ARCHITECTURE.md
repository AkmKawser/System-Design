# Architecture & Operational Mechanics: `SkillGenerator` Meta-Skill

## 1. System Overview & Purpose

The **`SkillGenerator`** meta-skill provides automated, deterministic scaffolding of new agent skills. It ensures that every new skill added to the repository strictly respects the dual-paradigm architecture:
- Type 1: Fixed Resource Skill (`SkillsOnFixedResources`)
- Type 2: Dynamic Resource Skill (`SkillsOnDynamicResources`)

---

## 2. Scaffolding Pipeline

```mermaid
flowchart TD
    User["Developer: 'Create new skill'"] --> HITL{"Human-in-the-Loop Dialog: Choose Paradigm"}
    HITL -->|"Type 1: Fixed Resource"| T1["Fixed Resource (Books / Specs / Courses)"]
    HITL -->|"Type 2: Dynamic Resource"| T2["Dynamic Resource (Problems / Challenges)"]
    
    T1 --> Script["scripts/generate_skill.py"]
    T2 --> Script

    Script --> Scaffold["Scaffold Directory Tree & Files"]
    Scaffold --> Sync["Synchronize README.md & chat.md"]
```
