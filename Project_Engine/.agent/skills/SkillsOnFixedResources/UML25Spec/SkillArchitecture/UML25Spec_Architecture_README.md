# Skill Architecture & Usage Instructions: `UML25Spec`

This document defines the technical architecture, execution pipeline, and usage guidelines for the **`UML25Spec`** skill.

---

## 🏛️ System Architecture

The `UML25Spec` skill connects any agentic AI system to formal domain knowledge without suffering from context exhaustion, token window degradation, or hallucinations.

## 📖 Operational Instructions for Agents

1. **Surgical Search First**: Never answer from memory alone. Run `scripts/query_uml25spec.py "<topic>"` to retrieve verified citations.
2. **Deep Outline Verification**: Check `Skills_Output/UML25Spec_output/outline/` for exact section and topic matches.
3. **Standardized Manual Output**: Output all requested topics into `Skills_Output/UML25Spec_output/query/<NNN>_<topic>.md`.
