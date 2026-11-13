# Software Architecture and Modeling - Outline

Formal architectural patterns, structural design principles, and model-driven system specification.

---

## 📌 Core Modules

### 1. Architectural Thinking & Invariants
- **Non-Functional Requirements (NFRs / -ilities)**: Scalability, availability, fault tolerance, maintainability, extensibility.
- **Architectural Trade-offs**: CAP Theorem, PACELC Theorem, Monolith vs Microservices.
- **Architectural Decision Records (ADRs)**: Structuring context, options, trade-offs, and consequences.

### 2. Architectural Views & Perspectives
- **Kruchten 4+1 View Model**: Logical, Development, Process, Physical, and Scenarios/Use Case views.
- **C4 Model**: Context, Container, Component, and Code diagrams.
- **Viewpoints and Perspectives Framework**: Structural, behavioral, information, security, operational.

### 3. Structural & Component Modeling
- **Component Diagrams**: Ports, provided/required interfaces, connectors, subsystems.
- **Deployment Diagrams**: Execution environments, nodes, device mapping, network communication paths.
- **Package Architecture**: Layered, Hexagonal (Ports & Adapters), Onion, Clean Architecture.

### 4. Dynamic & Behavioral Modeling
- **Sequence & Interaction Modeling**: Lifelines, message semantics (sync vs async), combined fragments (`alt`, `opt`, `loop`, `par`).
- **State Machine Modeling**: States, transitions, events, guards, internal activities, orthogonal composite states.
- **Activity & Workflow Modeling**: Control flows, decision nodes, fork/join concurrency, swimlanes.

### 5. Enterprise Architectural Patterns
- **Layered / N-Tier Architecture**: Separation of concerns, closed vs open layers.
- **Event-Driven Architecture (EDA)**: Producers, consumers, event brokers, pub/sub, event sourcing, CQRS.
- **Microservices & Service-Oriented Architecture**: Service boundaries, domain-driven design (DDD) bounded contexts, saga choreography vs orchestration.
- **Space-Based & Peer-to-Peer**: In-memory data grids, partition awareness.

