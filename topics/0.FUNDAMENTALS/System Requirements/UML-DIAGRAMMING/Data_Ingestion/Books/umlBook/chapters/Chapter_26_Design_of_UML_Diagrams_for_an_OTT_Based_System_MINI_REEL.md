# Chapter 26: Design of UML Diagrams for an OTT Based System MINI REEL

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 279–286 (Total: 8 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md) | [📚 Book Index](../UML_Book.md) | [Chapter_27_Design_of_UML_Diagrams_for_e_Med_Medical_Assistance_Tool &rarr;](Chapter_27_Design_of_UML_Diagrams_for_e_Med_Medical_Assistance_Tool.md)

---

## 📌 Executive Summary

Chapter 26 presents an industrial software engineering case study for **Design of UML Diagrams for an OTT Based System MINI REEL**. It details the transition from business requirements and domain constraints into formal software architecture specifications, leveraging data-flow modeling and a complete suite of Unified Modeling Language (UML) structural and behavioral diagrams.

---

## 🎯 Problem Statement & System Context

An over-the-top (OTT) media service is a streaming media service offered directly to viewers via the internet. The OTT media can be streamed anywhere with just the use of an internet connection. The scope of this project lies in the maximised use of the internet by the current generation. The system aims at providing a fun-filled and informative services that they would be able to access easily from their place. This system includes streaming of shows and movies that could be viewed by the users and an administrator governing the updates in the OTT based on the schedule of the show or movie release. Users can have a trial package of the services offered for 1 month and further subscriptions are based on the amount paid categorised as normal users and premium users. Creating an account involves payment to the services provided. Hence the trial users could use the trial package for a month and create an account for them maintaining a secret password that makes their account safe from other people accessing it. The premium users have the privilege of providing suggestions of the shows in the discussion room. All the users should be provided with the facility of a chat room where the users can chat and express their views and comments. The administrator will have control over the shows broadcasted and maintain a proper timeline of the shows, movies and live shows. News feeds highlighting the recent updates in the world will also be available in MINIREELS in a brief format. Users can also add their favourite videos to LIKES list and watch them whenever needed (Figures 26.1–26.8).

---

## 📊 Complete UML Diagram Suite & Architecture Specifications

This chapter incorporates **8 standalone vector diagram(s)** illustrating the end-to-end design from functional use cases to physical hardware deployment:

### Figure 26.1: UML Usecase Diagram

**Diagram Category**: `Use Case Diagram`  
**Architectural Role**: Specifies system boundary, primary external actors, and business use cases with include/extend relationships.

![Figure 26.1: UML Usecase Diagram](../vector_images/Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_/Figure_26_1_UML_usecase_diagram.svg)

### Figure 26.2: UML Activity Diagram

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

![Figure 26.2: UML Activity Diagram](../vector_images/Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_/Figure_26_2_UML_activity_diagram.svg)

### Figure 26.3: UML Sequence Diagram

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

![Figure 26.3: UML Sequence Diagram](../vector_images/Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_/Figure_26_3_UML_sequence_diagram.svg)

### Figure 26.4: UML Collaboration Diagram

**Diagram Category**: `Communication Diagram`  
**Architectural Role**: Emphasizes structural object topology and numbered sequence messaging between collaborating entities.

![Figure 26.4: UML Collaboration Diagram](../vector_images/Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_/Figure_26_4_UML_collaboration_diagram.svg)

### Figure 26.5: UML State Chart Diagram

**Diagram Category**: `State Machine Diagram`  
**Architectural Role**: Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions.

![Figure 26.5: UML State Chart Diagram](../vector_images/Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_/Figure_26_5_UML_state_chart_diagram.svg)

### Figure 26.6: UML Class Diagram

**Diagram Category**: `Class Diagram`  
**Architectural Role**: Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance).

![Figure 26.6: UML Class Diagram](../vector_images/Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_/Figure_26_6_UML_class_diagram.svg)

### Figure 26.7: UML Component Diagram

**Diagram Category**: `Component Diagram`  
**Architectural Role**: Architects physical modular software components, provided ball interfaces, and required socket dependencies.

![Figure 26.7: UML Component Diagram](../vector_images/Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_/Figure_26_7_UML_component_diagram.svg)

### Figure 26.8: UML Deployment Diagram

**Diagram Category**: `Deployment Diagram`  
**Architectural Role**: Maps software execution artifacts to hardware computing nodes, client devices, application tiers, and database servers.

![Figure 26.8: UML Deployment Diagram](../vector_images/Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_/Figure_26_8_UML_deployment_diagram.svg)

---

## 💡 Key Architectural Invariants & Modeling Lessons

1. **Traceability**: Every software model directly corresponds to explicit functional requirements defined during the initial domain specification.
2. **Separation of Concerns**: Structural models (Class, Component, Deployment) maintain clear boundaries separating business domain entities from physical infrastructure nodes.
3. **Behavioral Integrity**: Dynamic models (Activity, Sequence, State Machine) guarantee valid state transitions, prevent deadlocks, and verify message order consistency.
4. **Deployment Fidelity**: Physical nodes and execution environments accurately map runtime middleware, database engines, and client access channels.

---

## 🔗 Related Resources & Navigation

- **Navigation**: [&larr; Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md) | [📚 Book Index](../UML_Book.md) | [Chapter_27_Design_of_UML_Diagrams_for_e_Med_Medical_Assistance_Tool &rarr;](Chapter_27_Design_of_UML_Diagrams_for_e_Med_Medical_Assistance_Tool.md)
- **Master Book Catalog**: [`UML_Book.md`](../UML_Book.md)
- **Vector Images Catalog**: [`Vector_Images_Catalog.md`](../vector_images/Vector_Images_Catalog.md)