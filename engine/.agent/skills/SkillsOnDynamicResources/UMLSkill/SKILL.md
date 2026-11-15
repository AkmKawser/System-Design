---
name: UMLSkill
description: Autonomous UML problem intake, HITL categorization, and 3-tier solution generator
---

# Problem Ingestion & Modeling Engineering Skill (`UMLSkill`)

The **`UMLSkill`** skill controls the lifecycle of dynamic problem intake into [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md) and the synthesis of template-grounded solutions into [`Skills_Output/UMLSkill_output/Solution Files/`](../../../../Skills_Output/UMLSkill_output/Solution%20Files/).

---

## 🎯 Primary Triggers & Capabilities

Activate this skill when:
1. The user mentions `@UMLSkill` to check, format, or process modeling problems.
2. The user requests to process a specific challenge file from `put the file here/`.
3. The user requests to process a specific problem number or staging text.
4. The user asks to solve a problem from `question bank.md`.

---

## 🤝 Human-in-the-Loop (HITL) Category Protocol

Whenever processing a problem, the agent **MUST NOT** guess the category or subcategory arbitrarily:
1. Read the dynamic categories from `problem categories.md`.
2. Interactively prompt the user (HITL) to confirm the **Primary Category** and **Subcategory**.
3. Format the problem into `question bank.md` adhering to `problem formatting.md`.
4. Generate multi-representation solution files under `Solution Files/<Primary Category>/<Subcategory>/<Problem-ID>/`.

---

## 🚨 CRITICAL RULE: Non-Destructive Ingestion

- **Zero Data Loss Guarantee**: Never delete any source file or notes until the entry is 100% verified inside `question bank.md`.
