# Chapter 36: Design of UML Diagrams for Online Quiz System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 367–376 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter_35_Design_of_UML_Diagrams_for_GUIDE_Dropshipping_Website](Chapter_35_Design_of_UML_Diagrams_for_GUIDE_Dropshipping_Website.md) | [📚 Book Index](../UML_Book.md) | [Chapter_37_Design_of_UML_Diagrams_for_Book_Bank_Management_System &rarr;](Chapter_37_Design_of_UML_Diagrams_for_Book_Bank_Management_System.md)

---

## 📌 Executive Summary

Chapter 36 presents an industrial software engineering case study for **Design of UML Diagrams for Online Quiz System**. It details the transition from business requirements and domain constraints into formal software architecture specifications, leveraging data-flow modeling and a complete suite of Unified Modeling Language (UML) structural and behavioral diagrams.

---

## 🎯 Problem Statement & System Context

Online learning is a part of many institution’s course offerings around the world. The scope of online quiz systems increased in this pandemic situation. The objective of the system is to maintain and improve the education rate by conducting quizzes (exams). The system acts as a bridge between student and teacher to gain knowledge and monitor it by the institution (admin). This system provides teachers to know about the students in remote education. The delightful features of the system are online teachers, remote tests, auto evaluation and feedback from students. Admin is responsible for the registration of both teachers and students. Teachers define the number of questions, time of the quiz, schedule for the quiz and they can edit it. At the end of a quiz, students can see the correct answers and their performance (Figures 36.1–36.10).

---

## 📊 Complete UML Diagram Suite & Architecture Specifications

This chapter incorporates **11 standalone vector diagram(s)** illustrating the end-to-end design from functional use cases to physical hardware deployment:

### Figure 36.1: UML Usecase Diagram

**Diagram Category**: `Use Case Diagram`  
**Architectural Role**: Specifies system boundary, primary external actors, and business use cases with include/extend relationships.

![Figure 36.1: UML Usecase Diagram](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_1_UML_usecase_diagram.svg)

### Figure 36.2: UML Activity Diagram Scenario 1

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

![Figure 36.2: UML Activity Diagram Scenario 1](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_2_UML_activity_diagram_Scenario_1.svg)

### Figure 36.3: UML Activity Diagram Scenario 2

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

![Figure 36.3: UML Activity Diagram Scenario 2](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_3_UML_activity_diagram_Scenario_2.svg)

### Figure 36.4: UML Sequence Diagram Scenario 1

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

![Figure 36.4: UML Sequence Diagram Scenario 1](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_4_UML_sequence_diagram_Scenario_1.svg)

### Figure 36.5: UML Sequence Diagram Scenario 2

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

![Figure 36.5: UML Sequence Diagram Scenario 2](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_5_UML_sequence_diagram_Scenario_2.svg)

### Figure 36.6: UML Collaboration Diagram

**Diagram Category**: `Communication Diagram`  
**Architectural Role**: Emphasizes structural object topology and numbered sequence messaging between collaborating entities.

![Figure 36.6: UML Collaboration Diagram](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_6_UML_collaboration_diagram.svg)

### Figure 36.7: UML State Chart Diagram

**Diagram Category**: `State Machine Diagram`  
**Architectural Role**: Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions.

![Figure 36.7: UML State Chart Diagram](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_7_UML_state_chart_diagram.svg)

### Figure 36.8: UML Class Diagram

**Diagram Category**: `Class Diagram`  
**Architectural Role**: Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance).

![Figure 36.8: UML Class Diagram](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_8_UML_class_diagram.svg)

### Figure 36.9: UML Component Diagram

**Diagram Category**: `Component Diagram`  
**Architectural Role**: Architects physical modular software components, provided ball interfaces, and required socket dependencies.

![Figure 36.9: UML Component Diagram](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_9_UML_component_diagram.svg)

### Figure 36.10: UML Deployment Diagram

**Diagram Category**: `Deployment Diagram`  
**Architectural Role**: Maps software execution artifacts to hardware computing nodes, client devices, application tiers, and database servers.

![Figure 36.10: UML Deployment Diagram](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Figure_36_10_UML_deployment_diagram.svg)

### Visual Artifacts & Supplementary Schematics

The following vector schematics capture operational screen states, user dashboards, or notation components documented in this chapter:

#### Ch36 p376 img01

![Ch36 p376 img01](../vector_images/Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S/Ch36_p376_img01.svg)

---

## 💡 Key Architectural Invariants & Modeling Lessons

1. **Traceability**: Every software model directly corresponds to explicit functional requirements defined during the initial domain specification.
2. **Separation of Concerns**: Structural models (Class, Component, Deployment) maintain clear boundaries separating business domain entities from physical infrastructure nodes.
3. **Behavioral Integrity**: Dynamic models (Activity, Sequence, State Machine) guarantee valid state transitions, prevent deadlocks, and verify message order consistency.
4. **Deployment Fidelity**: Physical nodes and execution environments accurately map runtime middleware, database engines, and client access channels.

---

## 🔗 Related Resources & Navigation

- **Navigation**: [&larr; Chapter_35_Design_of_UML_Diagrams_for_GUIDE_Dropshipping_Website](Chapter_35_Design_of_UML_Diagrams_for_GUIDE_Dropshipping_Website.md) | [📚 Book Index](../UML_Book.md) | [Chapter_37_Design_of_UML_Diagrams_for_Book_Bank_Management_System &rarr;](Chapter_37_Design_of_UML_Diagrams_for_Book_Bank_Management_System.md)
- **Master Book Catalog**: [`UML_Book.md`](../UML_Book.md)
- **Vector Images Catalog**: [`Vector_Images_Catalog.md`](../vector_images/Vector_Images_Catalog.md)