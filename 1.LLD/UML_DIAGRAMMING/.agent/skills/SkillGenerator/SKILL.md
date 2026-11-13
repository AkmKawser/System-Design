---
name: SkillGenerator
description: Universal skill scaffolder for UML-Diagramming. Scaffolds Type 1 (Fixed Resources) and Type 2 (Dynamic Resources) skills conforming strictly to verified repository architecture via Human-in-the-Loop dialog and scripts/generate_skill.py.
---

# Universal Skill Generator (`SkillGenerator`)

The **`SkillGenerator`** meta-skill automates the scaffolding and lifecycle provisioning of production-ready agent skills in **UML-Diagramming**, conforming strictly to the architectural standards established across the ecosystem.

---

## 🎯 Skill Paradigms Supported

1. **Type 1: Fixed Resource Skill (`SkillsOnFixedResources`)**:
   - For UML textbooks, formal OMG specifications, companion books, or video course transcripts.
   - Generates routing indexes (`table_of_contents.md`, `toc.json`), CLI search scripts (`scripts/query_<name>.py`), and output hubs (`Skills_Output/<name>_output/outline/` & `query/`).
2. **Type 2: Dynamic Resource Skill (`SkillsOnDynamicResources`)**:
   - For real-world software design problems, architecture challenges, and system modeling exercises.
   - Generates staging areas (`Source of Problem/put the file here/`), category taxonomies, `question bank.md`, formatting specifications, and multi-tier solution folders.

---

## 🛠️ Execution Protocol

When prompted to create a new skill:
1. Conduct an interactive Human-in-the-Loop (HITL) consultation to determine:
   - Skill Type: `fixed` (Type 1) or `dynamic` (Type 2).
   - Skill Name (e.g., `Fowler_UML`, `SystemDesignSkill`).
   - Source Path or Category Document.
2. Run the automated generator script:
   ```bash
   # For Fixed Resource Skill:
   python .agent/skills/SkillGenerator/scripts/generate_skill.py --type fixed --name <SkillName> --resource-type "Book" --source-path "Skills_Input/books/Structural"

   # For Dynamic Resource Skill:
   python .agent/skills/SkillGenerator/scripts/generate_skill.py --type dynamic --name <SkillName> --category-doc "problem categories.md"
   ```
3. Update `README.md`, `chat/finalized chat.md`, and log the session in `chat/chat.md`.

