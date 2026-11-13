# UML 2.5 Master Diagrams & Concepts Taxonomy Outline

This document provides a canonical, high-level taxonomy of the **14 official diagrams of the OMG Unified Modeling Language (UML) 2.5 standard**, organized into structural and behavioral dimensions.

---

## 🏛️ The 14 UML 2.5 Diagrams Taxonomy

```
                                  UML 2.5 Diagrams
                                         │
        ┌────────────────────────────────┴────────────────────────────────┐
        ▼                                                                 ▼
Structure Diagrams (7)                                          Behavior Diagrams (7)
  ├── Class Diagram                                               ├── Use Case Diagram
  ├── Object Diagram                                              ├── Activity Diagram
  ├── Package Diagram                                             ├── State Machine Diagram
  ├── Component Diagram                                           └── Interaction Diagrams (4)
  ├── Composite Structure Diagram                                       ├── Sequence Diagram
  ├── Deployment Diagram                                                ├── Communication Diagram
  └── Profile Diagram                                                   ├── Interaction Overview Diagram
                                                                        └── Timing Diagram
```

---

## 📐 Detailed Breakdown

### 1. Structure Diagrams (Static Architecture)
1. **Class Diagram**: Static structure, classifiers, features, associations, aggregations, compositions, multiplicities, generalizations, and dependencies.
2. **Object Diagram**: Snapshot of runtime object instances, field values, and active links at a single point in time.
3. **Package Diagram**: High-level organization of models, classes, and namespaces with dependencies, imports, and merges.
4. **Component Diagram**: Autonomous software units, provided and required interfaces (lollipop and socket notations), ports, and wiring.
5. **Composite Structure Diagram**: Internal classifier structure, collaborating parts, ports, and connectors.
6. **Deployment Diagram**: Physical deployment topology, execution environment nodes, devices, communication paths, and artifact manifestations.
7. **Profile Diagram**: Metamodel extensions, stereotypes, tagged values, and domain-specific customization profiles.

### 2. Behavior Diagrams (Dynamic Dynamics)
1. **Use Case Diagram**: System boundaries, primary/secondary actors, use case relationships (`<<include>>`, `<<extend>>`), and functional scope.
2. **Activity Diagram**: Procedural business logic, control flows, data object flows, fork/join synchronization, decisions, and swimlanes.
3. **State Machine Diagram**: Discrete state lifecycles, event triggers, boolean guards, actions, composite/submachine states, and pseudostates.
4. **Sequence Diagram**: Chronological message exchange between lifelines, synchronous/asynchronous messaging, reply flows, and combined fragments (`alt`, `opt`, `loop`, `par`).
5. **Communication Diagram**: Interaction topology focusing on object relationships with numbered sequential messages.
6. **Interaction Overview Diagram**: Variant of an activity diagram where nodes encapsulate sequence or interaction diagrams.
7. **Timing Diagram**: Interaction dynamics emphasizing continuous time constraints and state transitions along an explicit time axis.

