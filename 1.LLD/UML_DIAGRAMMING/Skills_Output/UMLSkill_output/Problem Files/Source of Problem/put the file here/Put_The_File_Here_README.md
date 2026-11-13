# Ingestion Drop Zone (`put the file here/`)

Drop offline files, challenge PDFs, system architecture RFCs, and requirements documents directly into this directory.

---

## ⚡ Agent Ingestion Instructions

1. Use `@skill:UMLSkill` or run:
   ```bash
   python .agent/skills/SkillsOnDynamicResources/UMLSkill/scripts/ingest_manager.py --status
   ```
2. The agent will discover pending files, conduct an interactive HITL consultation to confirm Category and Subcategory, format the entry into `question bank.md`, and generate solutions.
3. **Non-Destructive Ingestion Rule**: The source file is never deleted until the parsed entry is 100% verified inside `question bank.md`.

