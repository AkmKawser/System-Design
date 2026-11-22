# Chapter 24: Design of UML Diagrams for Online Pharmacy Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 247–264 (Total: 18 pages)  
> **Classification**: Industrial Case Study & UML Modeling Suite  
> **Navigation**: [&larr; Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP](Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP.md) | [📚 Book Index](../UML_Book.md) | [Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH &rarr;](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md)

---

## 📌 Executive Summary

Chapter 24 presents an end-to-end software engineering case study for the **Design of UML Diagrams for Online Pharmacy Management System**. This chapter demonstrates how business requirements and domain constraints are translated into formal architectural specifications through data-flow modeling and a complete suite of Unified Modeling Language (UML) structural and behavioral models.

The case study analyzes the system from multiple architectural perspectives: identifying external user and service actors, formalizing core operational capabilities, detailing procedural business workflows, specifying domain entity schemas, and architecting modular component deployment across distributed physical infrastructure.

---

## 🎯 Problem Statement & Business Context

The customer goes to the shop and purchases the medicine required. So a lot of time is wasted and the person gets tired. If he wants to exchange the product, once again he goes to the shop and replaces them. The complete process depends on the physical interactions. The Online Pharmacy is easy to use and order. The customer selects the required medicines and orders them with a single click. Before it, the customer needs to create a login account and fill all the details like name, address, any id no, etc. The client can able to view the status of the medicines. The business goal for the application is to provide the medicines to all the people and admin will provide the supplier details (Figures 24.1–24.20).

---

## ⚙️ System Architecture & Functional Capabilities

The **Design of UML Diagrams for Online Pharmacy Management System** decomposes business operations into modular functional units. These capabilities address the operational bottlenecks of manual and legacy workflows by introducing automated, role-based, and auditable software processes:

- **Login**: It allows the customer to login into the page.
- **Register**: It allows the customer to create an account.
- **Account/Profile Information**: Customer can edit their information.
- **View Orders**: Customers can view the orders they have selected.
- **Add to Wish List**: Customers can wish to list a product of their choice.
- **Add to Cart**: It displays the products added to the cart by customers.
- **Order Confirm**: It displays the confirmed orders by the customers.
- **Order Cancel**: It provides an option to delete the orders confirmed by the customers.
- **Update Delivery Info**: The customer can update the delivery address where the products are to be delivered.
- **Track Orders**: This page allows the customer to track their orders.
- **Payment**: This page allows the customer to pay for the ordered products.
- **Net Banking**: It allows to update the bank details for the payment.
- **COD**: It provides an option for the customers to pay at the time of delivery.
- **View Users**: Admin can view the users who logged in into the page.
- **Update Medicine**: Admin can view the number of medicines available and update them on the website.
- **Add/Delete Medicine**: It allows the admin to add/delete medicines based on the quantity available.
- **Maintain Orders**: It allows the admin to maintain orders.
- **View Delivery Address**: It allows the admin to view the address of the customers.
- **View Delivery Man Info**: It allows the admin to view the information about the delivery man.
- **Update Salary**: It allows the admin to update the salary for the delivery man.
- **Maintain Attendance**: It allows the admin to maintain attendance for the delivery man.
- **Check Orders**: It allows the delivery man to check orders in order to deliver them.
- **Contact Delivery Address**: It allows the delivery man to contact the address of the customers to deliver them.
- **Delivered**: Delivery mentions the status that he delivered the order to the customer.
- **Not Delivered**: It allows the delivery man to update the status of not delivered.
- **Reason for Not Delivered**: It allows the delivery man to mention why the order has not been delivered.
- **Update/View Profile**: It allows the delivery man to edit/view his profile.
- **View Attendance**: It allows the delivery man to view attendance.

---

## 📊 Complete UML Diagram Suite & Architectural Walkthrough

This chapter incorporates **21 crystal-clear, high-resolution diagram(s)** (extracted losslessly from the source edition at up to 2,000+ px) illustrating the end-to-end design from functional use cases to physical hardware deployment:

### Figure 24.1: UML Usecase Diagram

**Diagram Category**: `Use Case Diagram`  
**Architectural Role**: Specifies system boundary, primary external actors, and business use cases with include/extend relationships.

**System Design Analysis**:
Illustrates the functional boundary of the **Design of UML Diagrams for Online Pharmacy Management System**. External actors trigger core use cases, demonstrating how business transactions, authorization checkpoints, and service requests flow into the system. Relationships (`<<include>>` for mandatory sub-routines like authentication and validation, and `<<extend>>` for optional or conditional exception branches) formalize the system's external functional contract.

![Figure 24.1: UML Usecase Diagram](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_1_UML_usecase_diagram.png)

### Figure 24.2: UML Activity Diagram User

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

**System Design Analysis**:
Details the step-by-step procedural execution flow for core operations in **Design of UML Diagrams for Online Pharmacy Management System**. Begins at an initial state, navigates action states, evaluates guard conditions at decision diamonds, and models parallel execution branches using fork and join synchronizations before reaching the terminal state, ensuring business workflows are deterministic and free of race conditions.

![Figure 24.2: UML Activity Diagram User](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_2_UML_activity_diagram_User.png)

### Figure 24.3: UML Activity Diagram Admin

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

**System Design Analysis**:
Details the step-by-step procedural execution flow for core operations in **Design of UML Diagrams for Online Pharmacy Management System**. Begins at an initial state, navigates action states, evaluates guard conditions at decision diamonds, and models parallel execution branches using fork and join synchronizations before reaching the terminal state, ensuring business workflows are deterministic and free of race conditions.

![Figure 24.3: UML Activity Diagram Admin](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_3_UML_activity_diagram_Admin.png)

### Figure 24.4: UML Activity Diagram Delivery Man

**Diagram Category**: `Activity Diagram`  
**Architectural Role**: Illustrates dynamic procedural workflow, decision branching, concurrent action forks, and synchronization joins.

**System Design Analysis**:
Details the step-by-step procedural execution flow for core operations in **Design of UML Diagrams for Online Pharmacy Management System**. Begins at an initial state, navigates action states, evaluates guard conditions at decision diamonds, and models parallel execution branches using fork and join synchronizations before reaching the terminal state, ensuring business workflows are deterministic and free of race conditions.

![Figure 24.4: UML Activity Diagram Delivery Man](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_4_UML_activity_diagram_Delivery_Man.png)

### Figure 24.5: UML Sequence Diagram Customer

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

**System Design Analysis**:
Traces the time-ordered message sequence between participating objects and services in **Design of UML Diagrams for Online Pharmacy Management System**. Vertical dashed lifelines represent entity instances across time, while horizontal solid and dashed arrows show synchronous invocations, data lookups, and return values. Activation bars delineate execution duration, clarifying object collaboration during key transactional workflows.

![Figure 24.5: UML Sequence Diagram Customer](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_5_UML_sequence_diagram_Customer.png)

### Figure 24.6: UML Sequence Diagram Admin

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

**System Design Analysis**:
Traces the time-ordered message sequence between participating objects and services in **Design of UML Diagrams for Online Pharmacy Management System**. Vertical dashed lifelines represent entity instances across time, while horizontal solid and dashed arrows show synchronous invocations, data lookups, and return values. Activation bars delineate execution duration, clarifying object collaboration during key transactional workflows.

![Figure 24.6: UML Sequence Diagram Admin](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_6_UML_sequence_diagram_Admin.png)

### Figure 24.7: UML Sequence Diagram Delivery Man

**Diagram Category**: `Sequence Diagram`  
**Architectural Role**: Details chronological object interactions, synchronous message exchanges, return flows, and activation lifelines.

**System Design Analysis**:
Traces the time-ordered message sequence between participating objects and services in **Design of UML Diagrams for Online Pharmacy Management System**. Vertical dashed lifelines represent entity instances across time, while horizontal solid and dashed arrows show synchronous invocations, data lookups, and return values. Activation bars delineate execution duration, clarifying object collaboration during key transactional workflows.

![Figure 24.7: UML Sequence Diagram Delivery Man](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_7_UML_sequence_diagram_Delivery_Man.png)

### Figure 24.8: UML Collaboration Diagram Customer

**Diagram Category**: `Communication Diagram`  
**Architectural Role**: Emphasizes structural object topology and numbered sequence messaging between collaborating entities.

**System Design Analysis**:
Emphasizes the spatial and structural organization of collaborating instances in **Design of UML Diagrams for Online Pharmacy Management System**. Shows object links overlaid with numbered messages (e.g., 1.0, 1.1, 2.0), illustrating both structural connectivity and invocation hierarchy, complementing the temporal perspective of the sequence diagram.

![Figure 24.8: UML Collaboration Diagram Customer](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_8_UML_collaboration_diagram_Customer.png)

### Figure 24.9: UML Collaboration Diagram Admin

**Diagram Category**: `Communication Diagram`  
**Architectural Role**: Emphasizes structural object topology and numbered sequence messaging between collaborating entities.

**System Design Analysis**:
Emphasizes the spatial and structural organization of collaborating instances in **Design of UML Diagrams for Online Pharmacy Management System**. Shows object links overlaid with numbered messages (e.g., 1.0, 1.1, 2.0), illustrating both structural connectivity and invocation hierarchy, complementing the temporal perspective of the sequence diagram.

![Figure 24.9: UML Collaboration Diagram Admin](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_9_UML_collaboration_diagram_Admin.svg)

### Figure 24.10: UML Collaboration Diagram Delivery Man

**Diagram Category**: `Communication Diagram`  
**Architectural Role**: Emphasizes structural object topology and numbered sequence messaging between collaborating entities.

**System Design Analysis**:
Emphasizes the spatial and structural organization of collaborating instances in **Design of UML Diagrams for Online Pharmacy Management System**. Shows object links overlaid with numbered messages (e.g., 1.0, 1.1, 2.0), illustrating both structural connectivity and invocation hierarchy, complementing the temporal perspective of the sequence diagram.

![Figure 24.10: UML Collaboration Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_10_UML_collaboration_diagram_Delivery_Man.svg)

### Figure 24.11: UML State Machine Diagram Customer

**Diagram Category**: `State Machine Diagram`  
**Architectural Role**: Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions.

**System Design Analysis**:
Models the complete lifecycle state transitions for central domain entities in **Design of UML Diagrams for Online Pharmacy Management System**. Tracks transitions from initial creation through intermediate processing states to completion or cancellation. Explicit state triggers, guard expressions `[condition]`, and entry/exit actions guarantee valid business lifecycle states and eliminate invalid operational state jumps.

![Figure 24.11: UML State Machine Diagram Customer](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_11_UML_state_machine_diagram_Customer.svg)

### Figure 24.12: UML State Machine Diagram Admin

**Diagram Category**: `State Machine Diagram`  
**Architectural Role**: Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions.

**System Design Analysis**:
Models the complete lifecycle state transitions for central domain entities in **Design of UML Diagrams for Online Pharmacy Management System**. Tracks transitions from initial creation through intermediate processing states to completion or cancellation. Explicit state triggers, guard expressions `[condition]`, and entry/exit actions guarantee valid business lifecycle states and eliminate invalid operational state jumps.

![Figure 24.12: UML State Machine Diagram Admin](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_12_UML_state_machine_diagram_Admin.svg)

### Figure 24.13: UML State Machine Diagram Delivery Man

**Diagram Category**: `State Machine Diagram`  
**Architectural Role**: Captures entity lifecycle states, transition triggers, event guards, and exit/entry actions.

**System Design Analysis**:
Models the complete lifecycle state transitions for central domain entities in **Design of UML Diagrams for Online Pharmacy Management System**. Tracks transitions from initial creation through intermediate processing states to completion or cancellation. Explicit state triggers, guard expressions `[condition]`, and entry/exit actions guarantee valid business lifecycle states and eliminate invalid operational state jumps.

![Figure 24.13: UML State Machine Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_13_UML_State_machine_diagram_Delivery_Man.svg)

### Figure 24.14: UML Class Diagram Customer

**Diagram Category**: `Class Diagram`  
**Architectural Role**: Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance).

**System Design Analysis**:
Captures the static structural domain model for **Design of UML Diagrams for Online Pharmacy Management System**. Defines primary entity classes, their private/public attributes, operational methods, and relationships. It enforces structural integrity through multiplicities, composition (strong lifecycle ownership of subsidiary records), aggregation, and inheritance hierarchies, forming the foundation for the relational database schema and domain entity classes.

![Figure 24.14: UML Class Diagram Customer](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_14_UML_class_diagram_Customer.png)

### Figure 24.15: UML Class Diagram Admin

**Diagram Category**: `Class Diagram`  
**Architectural Role**: Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance).

**System Design Analysis**:
Captures the static structural domain model for **Design of UML Diagrams for Online Pharmacy Management System**. Defines primary entity classes, their private/public attributes, operational methods, and relationships. It enforces structural integrity through multiplicities, composition (strong lifecycle ownership of subsidiary records), aggregation, and inheritance hierarchies, forming the foundation for the relational database schema and domain entity classes.

![Figure 24.15: UML Class Diagram Admin](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_15_UML_class_diagram_Admin.png)

### Figure 24.16: UML Class Diagram Delivery Man

**Diagram Category**: `Class Diagram`  
**Architectural Role**: Models static structural classifiers, entity attributes, operations, and associations (composition, aggregation, inheritance).

**System Design Analysis**:
Captures the static structural domain model for **Design of UML Diagrams for Online Pharmacy Management System**. Defines primary entity classes, their private/public attributes, operational methods, and relationships. It enforces structural integrity through multiplicities, composition (strong lifecycle ownership of subsidiary records), aggregation, and inheritance hierarchies, forming the foundation for the relational database schema and domain entity classes.

![Figure 24.16: UML Class Diagram Delivery Man](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_16_UML_class_diagram_Delivery_Man.png)

### Figure 24.17: UML Component Diagram Customer

**Diagram Category**: `Component Diagram`  
**Architectural Role**: Architects physical modular software components, provided ball interfaces, and required socket dependencies.

**System Design Analysis**:
Architects the modular software organization for **Design of UML Diagrams for Online Pharmacy Management System**. Illustrates autonomous subsystems, business logic controllers, database access layers, and external service adapters. Provided interfaces (ball notation) and required dependencies (socket notation) define clear service contracts, supporting high cohesion and loose coupling.

![Figure 24.17: UML Component Diagram Customer](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_17_UML_component_diagram_Customer.svg)

### Figure 24.18: UML Component Diagram Admin

**Diagram Category**: `Component Diagram`  
**Architectural Role**: Architects physical modular software components, provided ball interfaces, and required socket dependencies.

**System Design Analysis**:
Architects the modular software organization for **Design of UML Diagrams for Online Pharmacy Management System**. Illustrates autonomous subsystems, business logic controllers, database access layers, and external service adapters. Provided interfaces (ball notation) and required dependencies (socket notation) define clear service contracts, supporting high cohesion and loose coupling.

![Figure 24.18: UML Component Diagram Admin](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_18_UML_component_diagram_Admin.png)

### Figure 24.19: UML Component Diagram Delivery Man

**Diagram Category**: `Component Diagram`  
**Architectural Role**: Architects physical modular software components, provided ball interfaces, and required socket dependencies.

**System Design Analysis**:
Architects the modular software organization for **Design of UML Diagrams for Online Pharmacy Management System**. Illustrates autonomous subsystems, business logic controllers, database access layers, and external service adapters. Provided interfaces (ball notation) and required dependencies (socket notation) define clear service contracts, supporting high cohesion and loose coupling.

![Figure 24.19: UML Component Diagram Delivery Man](../vector_images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_19_UML_component_diagram_Delivery_Man.svg)

### Figure 24.20: UML Deployment Diagram

**Diagram Category**: `Deployment Diagram`  
**Architectural Role**: Maps software execution artifacts to hardware computing nodes, client devices, application tiers, and database servers.

**System Design Analysis**:
Maps the physical runtime deployment architecture for **Design of UML Diagrams for Online Pharmacy Management System**. Depicts client hardware devices (web browsers, mobile apps), application servers, network firewalls, and persistence database nodes. Communication paths and execution environments reflect production infrastructure, scalability considerations, and network security boundaries.

![Figure 24.20: UML Deployment Diagram](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Figure_24_20_UML_deployment_diagram.png)

### Visual Artifacts & Supplementary Schematics

The following high-resolution schematics capture operational screen states, user dashboards, or notation components documented in this chapter:

#### Ch24 p264 img01

**Perspective**: `Conceptual Notation / Architecture Asset` — Supplemental conceptual illustration or notation reference from the source chapter.

![Ch24 p264 img01](../images/Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma/Ch24_p264_img01.png)

---

## 💡 Key Architectural Invariants & Domain Lessons

1. **Requirement Traceability**: Every model in the **Design of UML Diagrams for Online Pharmacy Management System** suite traces directly to business requirements and operational constraints established in the problem statement.
2. **State & Workflow Integrity**: Dynamic activity and sequence models guarantee deterministic workflow completion, enforce transactional atomicity, and prevent deadlocks.
3. **Modular Encapsulation**: Component boundaries decouple domain business logic from presentation controllers and external integration adapters, supporting high maintainability.
4. **Operational Security & RBAC**: Strict role-based authorization guards sensitive operations across external actor boundaries and administrative lifelines.
5. **High-Fidelity Deployment**: Physical node topologies reflect real-world tiered infrastructure (DMZ, application cluster, isolated persistence layer), ensuring scalability and fault tolerance.

---

## 🔗 Related Resources & Navigation

- **Navigation**: [&larr; Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP](Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP.md) | [📚 Book Index](../UML_Book.md) | [Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH &rarr;](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md)
- **Master Book Catalog**: [`UML_Book.md`](../UML_Book.md)
- **High-Resolution Images Archive**: [`images/`](../images/)