# Chapter 17: Design of UML Diagrams for National Health ID 2020

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 185–190 (Total: 6 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 16: Design of UML Diagrams for Textile Management System](Chapter_16_Design_of_UML_Diagrams_for_Textile_Management_System.md) | [📚 Book Index](../Overall_Books.md) | [Chapter 18: Design of UML Diagrams for Device Handout System &rarr;](Chapter_18_Design_of_UML_Diagrams_for_Device_Handout_System.md)

---

## 📌 Chapter Overview

Chapter 17 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for National Health ID 2020**. 
This case study presents an end-to-end software engineering analysis for **National Health ID 2020**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **17.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 17

Design of UML Diagrams for

National Health ID 2020

17 .1 Problem Statement

The Prime Minister of India has announced a new scheme of National Health ID on August 15,

2020. According to this proposal, every Indian will get a unique Health ID based on their mobile

number or Aadhaar number. The National Health ID will be a repository of all health-related

information of a person. According to the National Health Authority (NHA), every patient who

wishes to have their health records available digitally must start by creating a Health ID. Each

Health ID will be linked to a health data consent manager – such as the National Digital Health

Mission (NDHM) which will be used to seek the patient’s consent and allow for seamless flow

of health information from the Personal Health Records module. This Health ID prevents various insurance frauds committed by several health agencies, hospitals including both doctors

and patients. This will reduce the paper works and help patients easily maintain their health

records. It can be used for further diagnosis. Children who are born after the implementation

of the National Health ID will have all their medications recorded including the vaccines, etc.

(Figures 17.1–17.8).

### 17.2 UML Diagrams

Usecase Specification

1. Verification

Description: People are verified for Indian citizenship through their individual identities

such as Aadhaar card or voter ID.

Flow of Events

Basic Flow: Collection of data.

Pre-Conditions: To have an Aadhaar card or voter id.

Post-Conditions: Those who don’t have unique identities will be rejected.

DOI: 10.1201/9781003287124-17

Figure 17.1 UML usecase diagram.

Figure 17.2 UML activity diagram.

Figure 17.3 UML sequence diagram.

Figure 17.4 UML collaboration diagram.

Figure 17.5 UML state machine diagram.

Figure 17.6 UML class diagram.

2. Registration

Description: People will be registered in the NHD repository to generate the unique

National Health ID for each and everyone.

Flow of Events

Basic Flow: Registration through Aadhaar.

Alternative Flow: Registration can also be done with a Phone number.

Pre-Conditions: Verification as Indian Citizen.

Post-Conditions: To activate the account.

3. Activation

Description: Everyone should activate the account with their unique Health ID.

Flow of Events

Basic Flow: To activate the account that has been created.

Pre-Conditions: To have a unique Health ID.

Post-Conditions: To use the ID during all the medical transactions to keep the record.

Figure 17.8 UML deployment diagram.

Figure 17.7 UML component diagram.

4. Add a Record

Description: Since the Health ID will start recording only after activation, old records

can be added to the repository as photocopies.

Flow of Events

Basic Flow: Adding the old records that are hard copies.

Alternative Flow: Can skip this process if they want.

Pre-Conditions: Having old records.

5. Permission

Description: A person can give access to particular doctors or agencies to view their

repository.

Flow of Events

Basic Flow: Giving access to their Medicare workers.

Alternative Flow: People can block access.

Pre-Conditions: The account must be activated.

Post-Conditions: The doctors can access the repository of the patients.

6. Health Repository

Description: The record of people is maintained by the NHD in this repository.

Flow of Events

Basic Flow: A place to store the records.

Pre-Conditions: The account must be activated.

Post-Conditions: All the medical transactions after activation will be stored in the repository.

---

## 📊 UML Modeling Suite for National Health ID 2020

The case study defines the following canonical UML models:

| Diagram Type | Perspective | Key Elements & Responsibilities |
| :--- | :--- | :--- |
| **Use Case Diagram** | Functional Scope | Primary actors, external APIs, and core business goals (`<<include>>`, `<<extend>>`). |
| **Activity Diagram** | Workflow / Process | Action states, decision diamonds, object flows, and swimlane partitions. |
| **Class Diagram** | Structural Backbone | Entity classifiers, attributes, operations, multiplicities, and relationships. |
| **Sequence Diagram** | Dynamic Interaction | Lifelines, synchronous RPCs, message returns, and execution activations. |
| **State Chart Diagram** | Lifecycle States | Discrete system states, event triggers, and boolean guard conditions. |
| **Component Diagram** | Modular Architecture | Encapsulated subsystems, provided interfaces (balls), and required interfaces (sockets). |
| **Deployment Diagram** | Physical Topology | Hardware nodes, application servers, database instances, and network links. |

---

## 🎯 Key Architectural Invariants & Modeling Lessons

1. **Requirements Grounding**: All diagrammatic artifacts trace back to functional requirements and domain constraints established in the problem statement.
2. **Structural Consistency**: Multiplicities and association lifecycles in the Class Diagram mirror the invocation sequences in the Sequence Diagram.
3. **Behavioral Invariants**: Guard conditions in State Chart and Activity models prevent invalid transitions and runtime failure modes.

---

## 🔗 Related Resources & Navigation

- **Previous Chapter**: [Design of UML Diagrams for Textile Management System](Chapter_16_Design_of_UML_Diagrams_for_Textile_Management_System.md)
- **Next Chapter**: [Design of UML Diagrams for Device Handout System](Chapter_18_Design_of_UML_Diagrams_for_Device_Handout_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/Overall_Books.md`](../Overall_Books.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
