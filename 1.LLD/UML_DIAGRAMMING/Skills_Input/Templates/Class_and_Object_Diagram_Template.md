# Class & Object Diagram Engineering Template

This template instructs the agent on the rigorous, step-by-step methodology required to model structural domains, object relationships, and object-oriented class hierarchies from first principles.

---

## 🎯 Conceptual Foundations & Invariants

A formal UML Class Diagram models the static structural backbone of a software system. Every class model must define:
1. **Attributes & Visibilities**:
   - `+` Public
   - `-` Private
   - `#` Protected
   - `~` Package-private
2. **Operations & Method Signatures**: Return types, parameters, and exception specifications.
3. **Formal Relationship Semantics**:
   - **Generalization (`--|>`)**: Inheritance (`is-a` relationship, Liskov Substitution Principle).
   - **Realization (`..|>`)**: Interface implementation contract.
   - **Composition (`*--`)**: Strong `has-a` relationship where parts cannot exist independently of the whole (cascade delete semantics).
   - **Aggregation (`o--`)**: Weak `has-a` shared relationship where parts have independent lifecycles.
   - **Association (`-->`)**: Navigable structural reference.
   - **Dependency (`..>`)**: Transient usage relationship (e.g. method parameter or local variable).
4. **Multiplicities**: Exact lower and upper bounds (`1`, `0..1`, `1..*`, `*`).

---

## 📋 Step-by-Step Problem-Solving Recipe

### Phase 1: Entity & Boundary Extraction
1. Identify all core business entities from the problem description.
2. Determine attribute types and operations for each classifier.
3. Assign strict visibility rules (encapsulate all mutable fields as private `-`).

### Phase 2: Relationship & Multiplicity Derivation
1. Map all inter-entity associations.
2. Apply the **Composition vs Aggregation Rule**:
   - If the child object's lifecycle is bound strictly to the parent &rarr; Use Composition (`*--`).
   - If the child object exists independently or can be shared &rarr; Use Aggregation (`o--`) or Association (`-->`).
3. Formulate exact multiplicity bounds on both ends of every relationship.

### Phase 3: Formal Diagram Synthesis (PlantUML / Mermaid)
Generate clean, syntax-compliant diagram definitions.

### Phase 4: Concrete OOP Code Mapping (Strictly Java)
Provide side-by-side production Java code illustrating:
- Fields, getters/setters, constructors, collections with generic bounds (e.g. `List<OrderItem>`).
- Defensive copying and lifecycle management matching composition constraints.

### Phase 5: Runtime Heap Memory State
Illustrate JVM heap object graphs showing references, nullability, and pointer collections.
