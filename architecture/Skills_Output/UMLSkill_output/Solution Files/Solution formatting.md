# Solution Output Formatting Specification (`Solution formatting.md`)

Every solved modeling challenge or system architecture problem must strictly produce this multi-representation artifact set.

---

## 🏛️ Artifact Set & Naming Conventions

For a problem with ID `UML-1`:

| Artifact | File Naming Pattern | Concrete Example (`UML-1`) |
| :--- | :--- | :--- |
| **PlantUML Model** | `<ID>_diagram.puml` | `UML-1_diagram.puml` |
| **Mermaid Model** | `<ID>_diagram.mmd` | `UML-1_diagram.mmd` |
| **OOP Code Implementation** | `<ID>_implementation.java` | `UML-1_implementation.java` |
| **Derivation & Trade-off Manual** | `<ID>_derivation.md` | `UML-1_derivation.md` |

---

## 📋 Derivation Document Schema (`<ID>_derivation.md`)

```markdown
# Architectural Derivation: [ID] - [Problem Title]

## 📌 Metadata
- **Problem ID**: [e.g., UML-1]
- **Category**: [Primary Category]
- **Subcategory**: [Subcategory]
- **Applied Template**: [`Skills_Input/Templates/<Template Name>.md`](../../../Skills_Input/Templates/)
- **Problem Reference**: [`question bank.md#<id-lowercase>`](../../Problem%20Files/question%20bank.md#uml-1)

---

## 1. Domain Modeling & Invariant Formulation
- Core entities, classifiers, operations, and multiplicity proofs.
- Invariant analysis (e.g. why Composition is required over Aggregation).

---

## 2. Collaborative Design Trade-offs
- **Option A**: [e.g. Synchronous HTTP vs Asynchronous Event Broker]
- **Option B**: [e.g. State Pattern vs Strategy Pattern]
- **Decision Rationale**: Why Option A or B was chosen given system requirements.

---

## 3. Formal UML Diagram Specification
- Complete diagram specifications with visibilities, stereotypes, and multiplicities.

---

## 4. End-to-End Concrete Java Implementation
- Production-ready Java code implementing classes, interfaces, and relationship bindings.

---

## 5. Runtime Architecture & Memory State Analysis
- JVM heap graph, stack frames, or distributed network event sequencing.

---

## 6. Anti-Pattern & Edge Case Audit
- Circular dependencies, God Classes, tight coupling, or deadlock hazards.
```

