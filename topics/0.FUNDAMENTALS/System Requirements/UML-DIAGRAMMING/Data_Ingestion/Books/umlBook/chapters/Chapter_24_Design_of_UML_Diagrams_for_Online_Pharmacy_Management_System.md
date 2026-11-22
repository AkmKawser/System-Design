# Chapter 24: Design of UML Diagrams for Online Pharmacy Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 247–264 (Total: 18 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP](Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP.md) | [📚 Book Index](../UML_Book.md) | [Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH &rarr;](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md)

---

## 📌 Executive Summary

Chapter 24 presents an industrial software engineering case study for **Design of UML Diagrams for Online Pharmacy Management System**. It details the transition from business requirements and domain constraints into formal software architecture specifications, leveraging data-flow modeling and a complete suite of Unified Modeling Language (UML) structural and behavioral diagrams.

---

## 🎯 Problem Statement & System Context

The customer goes to the shop and purchases the medicine required. So a lot of time is wasted and the person gets tired. If he wants to exchange the product, once again he goes to the shop and replaces them. The complete process depends on the physical interactions. The Online Pharmacy is easy to use and order. The customer selects the required medicines and orders them with a single click. Before it, the customer needs to create a login account and fill all the details like name, address, any id no, etc. The client can able to view the status of the medicines. The business goal for the application is to provide the medicines to all the people and admin will provide the supplier details (Figures 24.1–24.20).

---

## 📊 Complete UML Diagram Suite & Architecture Specifications

This chapter incorporates **21 standalone vector diagram(s)** illustrating the end-to-end design from functional use cases to physical hardware deployment:

### Figure 24.1: UML Usecase Diagram

**Diagram Category**: `Use Case Diagram`  
**Architectural Role**: Specifies system boundary, primary external actors, and business use cases with include/extend relationships.

![Figure 24.1: UML Usecase Diagram](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_1_UML_usecase_diagram.svg)

### Figure 24.2: UML Activity Diagram User

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

![Figure 24.2: UML Activity Diagram User](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_2_UML_activity_diagram_User.svg)

### Figure 24.3: UML Activity Diagram Admin

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

![Figure 24.3: UML Activity Diagram Admin](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_3_UML_activity_diagram_Admin.svg)

### Figure 24.4: UML Activity Diagram Delivery Man

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

![Figure 24.4: UML Activity Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_4_UML_activity_diagram_Delivery_Man.svg)

### Figure 24.5: UML Sequence Diagram Customer

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

![Figure 24.5: UML Sequence Diagram Customer](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_5_UML_sequence_diagram_Customer.svg)

### Figure 24.6: UML Sequence Diagram Admin

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

![Figure 24.6: UML Sequence Diagram Admin](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_6_UML_sequence_diagram_Admin.svg)

### Figure 24.7: UML Sequence Diagram Delivery Man

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

![Figure 24.7: UML Sequence Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_7_UML_sequence_diagram_Delivery_Man.svg)

### Figure 24.8: UML Collaboration Diagram Customer

**Diagram Category**: `Communication Diagram`  
**Architectural Role**: Emphasizes structural object topology and numbered sequence messaging between collaborating entities.

![Figure 24.8: UML Collaboration Diagram Customer](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_8_UML_collaboration_diagram_Customer.svg)

### Figure 24.9: UML Collaboration Diagram Admin

**Diagram Category**: `Communication Diagram`  
**Architectural Role**: Emphasizes structural object topology and numbered sequence messaging between collaborating entities.

![Figure 24.9: UML Collaboration Diagram Admin](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_9_UML_collaboration_diagram_Admin.svg)

### Figure 24.10: UML Collaboration Diagram Delivery Man

**Diagram Category**: `Communication Diagram`  
**Architectural Role**: Emphasizes structural object topology and numbered sequence messaging between collaborating entities.

![Figure 24.10: UML Collaboration Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_10_UML_collaboration_diagram_Delivery_Man.svg)

### Figure 24.11: UML State Machine Diagram Customer

**Diagram Category**: `State Machine Diagram`  
**Architectural Role**: Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions.

![Figure 24.11: UML State Machine Diagram Customer](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_11_UML_state_machine_diagram_Customer.svg)

### Figure 24.12: UML State Machine Diagram Admin

**Diagram Category**: `State Machine Diagram`  
**Architectural Role**: Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions.

![Figure 24.12: UML State Machine Diagram Admin](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_12_UML_state_machine_diagram_Admin.svg)

### Figure 24.13: UML State Machine Diagram Delivery Man

**Diagram Category**: `State Machine Diagram`  
**Architectural Role**: Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions.

![Figure 24.13: UML State Machine Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_13_UML_State_machine_diagram_Delivery_Man.svg)

### Figure 24.14: UML Class Diagram Customer

**Diagram Category**: `Class Diagram`  
**Architectural Role**: Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance).

![Figure 24.14: UML Class Diagram Customer](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_14_UML_class_diagram_Customer.svg)

### Figure 24.15: UML Class Diagram Admin

**Diagram Category**: `Class Diagram`  
**Architectural Role**: Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance).

![Figure 24.15: UML Class Diagram Admin](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_15_UML_class_diagram_Admin.svg)

### Figure 24.16: UML Class Diagram Delivery Man

**Diagram Category**: `Class Diagram`  
**Architectural Role**: Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance).

![Figure 24.16: UML Class Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_16_UML_class_diagram_Delivery_Man.svg)

### Figure 24.17: UML Component Diagram Customer

**Diagram Category**: `Component Diagram`  
**Architectural Role**: Architects physical modular software components, provided ball interfaces, and required socket dependencies.

![Figure 24.17: UML Component Diagram Customer](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_17_UML_component_diagram_Customer.svg)

### Figure 24.18: UML Component Diagram Admin

**Diagram Category**: `Component Diagram`  
**Architectural Role**: Architects physical modular software components, provided ball interfaces, and required socket dependencies.

![Figure 24.18: UML Component Diagram Admin](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_18_UML_component_diagram_Admin.svg)

### Figure 24.19: UML Component Diagram Delivery Man

**Diagram Category**: `Component Diagram`  
**Architectural Role**: Architects physical modular software components, provided ball interfaces, and required socket dependencies.

![Figure 24.19: UML Component Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_19_UML_component_diagram_Delivery_Man.svg)

### Figure 24.20: UML Deployment Diagram

**Diagram Category**: `Deployment Diagram`  
**Architectural Role**: Maps software execution artifacts to hardware computing nodes, client devices, application tiers, and database servers.

![Figure 24.20: UML Deployment Diagram](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_20_UML_deployment_diagram.svg)

### Visual Artifacts & Supplementary Schematics

The following vector schematics capture operational screen states, user dashboards, or notation components documented in this chapter:

#### Ch24 p264 img01

![Ch24 p264 img01](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Ch24_p264_img01.svg)

---

## 💡 Key Architectural Invariants & Modeling Lessons

1. **Traceability**: Every software model directly corresponds to explicit functional requirements defined during the initial domain specification.
2. **Separation of Concerns**: Structural models (Class, Component, Deployment) maintain clear boundaries separating business domain entities from physical infrastructure nodes.
3. **Behavioral Integrity**: Dynamic models (Activity, Sequence, State Machine) guarantee valid state transitions, prevent deadlocks, and verify message order consistency.
4. **Deployment Fidelity**: Physical nodes and execution environments accurately map runtime middleware, database engines, and client access channels.

---

## 🔗 Related Resources & Navigation

- **Navigation**: [&larr; Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP](Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP.md) | [📚 Book Index](../UML_Book.md) | [Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH &rarr;](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md)
- **Master Book Catalog**: [`UML_Book.md`](../UML_Book.md)
- **Vector Images Catalog**: [`Vector_Images_Catalog.md`](../vector_images/Vector_Images_Catalog.md)