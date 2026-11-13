# Problem Formatting Schema (`problem formatting.md`)

All software design challenges, architectural specifications, and modeling problems ingested into `question bank.md` must adhere strictly to this schema.

---

## 📋 Markdown Entry Schema

```markdown
---

<a id="[problem-id-lowercase]"></a>
# Problem [ID]: [Problem Title]

## 📌 Metadata & Source Attribution
- **Problem ID**: [Unique ID, e.g., UML-1, UML-2]
- **Problem Title**: [Exact title of the modeling challenge]
- **Primary Category**: [Primary Domain from problem categories.md]
- **Subcategory**: [Subcategory from problem categories.md]
- **Difficulty**: [Easy / Medium / Hard]
- **Source**: [Source Name, Company, Book, or RFC]
- **Target Template**: [Matching template from Skills_Input/Templates/]

---

## 📝 Problem Statement & System Requirements
[Detailed functional description of the system or business domain to be modeled.]

---

## 🎯 Modeling Objectives & Deliverables
1. **Structural / Behavioral Model**: Primary UML diagram requirement.
2. **Key Invariants**: Business rules, multiplicity constraints, or state rules.
3. **Target Code Mapping**: Expected OOP Java interfaces and classes.

---

## 🧪 Scenarios & Test Cases
### Scenario 1: [Normal Flow / Success Path]
- **Trigger**: [User action / Event]
- **Expected Sequence / State**: [Resulting behavior]

### Scenario 2: [Failure / Edge Case]
- **Trigger**: [Constraint violation / Error event]
- **Expected Handling**: [Exception / Error state transition]

---
```
