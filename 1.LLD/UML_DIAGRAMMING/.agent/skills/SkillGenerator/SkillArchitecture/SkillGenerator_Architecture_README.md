# Skill Architecture & Usage Guide: `SkillGenerator`

This document details the usage directives for the **`SkillGenerator`** meta-skill in `UML-Diagramming`.

---

## 📖 Operational Instructions

1. **Invoke via HITL Prompt**: Prompt `@SkillGenerator create a new skill for <Resource/Topic>`.
2. **Execute Automation**: Run `scripts/generate_skill.py` with appropriate parameters.
3. **Validate Rendering**: Run `python scripts/audit_rendering.py` immediately following scaffolding.
4. **Synchronize Hubs**: Add navigation buttons to `README.md` and update `chat/finalized chat.md`.

