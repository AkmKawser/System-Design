# Chapter 20: Design of UML Diagrams for Crime Bureau

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 209–218 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 19: Design of UML Diagrams for Online College Magazine System](Chapter_19_Design_of_UML_Diagrams_for_Online_College_Magazine_System.md) | [📚 Book Index](../UML_Book.md) | [Chapter 21: Design of UML Diagrams for Smart Traffic Management System &rarr;](Chapter_21_Design_of_UML_Diagrams_for_Smart_Traffic_Management_System.md)

---

## 📌 Chapter Overview

Chapter 20 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Crime Bureau**. 
This case study presents an end-to-end software engineering analysis for **Crime Bureau**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **20.1 Problem Statement**
- **20.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 20

Design of UML Diagrams

for Crime Bureau

### 20.1 Problem Statement

Rules and regulations are paramount to all aspects of life. Certain proponents have asserted that

crime which is a violation against laws of the society, is integral to the human nature and hence

the society can never be completely free from it. In the existing system, all work is done on papers,

so it is very difficult to secure crime reports data. This system needs more manpower to track the

records of crimes and it lacks security. Modern society is characterized by increasing levels of risk

posed by internal and external security threats. This poses the importance to develop an automated crime management system to keep a record of the crime and the criminals involved. The

proposed crime bureau is a database system in which the police keeps the record of criminals who

have been arrested, to be arrested, or escaped and the complaints. This will help the police department in enhanced management of information. The main entities in the whole process include;

the petitioner (the person who files a First Incident Report (FIR)), victim, accused or criminal,

case and investigating officer. The proposed crime record management system can overcome all

the limitations of the existing system. This system provides proper security and reduces the manual work. This project helps to maintain a database through which the entire crime activities in

the state can be monitored (Figures 20.1–20.8).

### 20.2 UML Diagrams

Usecase Specification

1. Login

Description: Officials are provided with a username and password, through which they

can log into the crime bureau.

Flow of Events

Basic Flow: Opens the crime bureau website.

Alternative Flow: NIL.

DOI: 10.1201/9781003287124-20

Figure 20.1 UML usecase diagram.

Figure 20.2 UML activity diagram.

Figure 20.3 UML sequence diagram.

Figure 20.4 UML collaboration diagram.

Figure 20.5 UML state chart diagram.

Figure 20.6 UML class diagram.

Pre-Conditions: Officials should own a valid username and password.

Post-Conditions: The username and password should be correct for accessing the crime

bureau.

2. Station Details

Description: Holds all the information regarding all the police stations in the state.

Flow of Events

Basic Flow: Can add, modify and delete station details.

Alternative Flow: Can view or search station details.

Pre-Conditions: The username and password should be valid and correct.

Post-Conditions: All the updates made must be saved.

3. Crimes

Description: Lists all the criminal activities for which an FIR or complaint can be

filed.

Flow of Events

Basic Flow: Can add, update or modify crime details.

Alternative Flow: Can view and search crime details.

Pre-Conditions: The username and password of the official must be correct.

Post-Conditions: All the updates made must be saved.

Figure 20.7 UML component diagram.

4. Police Login

Description: Officials are provided with a username and password, through which they

can log into the crime bureau.

Flow of Events

Basic Flow: Opens the crime bureau website.

Alternative Flow: NIL.

Pre-Conditions: The police officers should have a valid username and login.

Post-Conditions: The username and password should be correct for accessing the crime

bureau.

5. Add Police

Description: Holds a record of all the police officers.

Flow of Events

Basic Flow: Can add, update and delete police officer details.

Alternative Flow: Can view and search the police officer details.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

Figure 20.8 UML deployment diagram.

6. Add User

Description: Holds a record of all the users who either have filed FIR or complaints.

Flow of Events

Basic Flow: Can add, update and delete user details.

Alternative Flow: Can view and search user details.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

7. FIR

Description: Holds a record of all the FIRs filed by the people.

Flow of Events

Basic Flow: Can add and update FIR.

Alternative Flow: Can view and search FIR.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

8. Complaints

Description: Holds a record of all the complaints filed by the people.

Flow of Events

Basic Flow: Can add and update complaints.

Alternative Flow: Can view and search complaints.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

9. Charge Sheet

Description: Holds a record of all the charge sheets filed by the people.

Flow of Events

Basic Flow: Can add and update complaints.

Alternative Flow: Can view and search complaints.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

10. Prisoner List

Description: Holds a list of all the prisoners.

Flow of Events

Basic Flow: Can add, update or delete prisoners.

Alternative Flow: Can view and search prisoners.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

11. Criminals

Description: Holds a list of all the criminals.

Flow of Events

Basic Flow: Can add, update or delete criminals.

Alternative Flow: Can view and search criminals.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

12. Wanted Persons

Description: Holds a list of wanted persons.

Flow of Events

Basic Flow: Can add, update or delete wanted persons.

Alternative Flow: Can view and search wanted persons.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

13. Missing Persons

Description: Holds a list of missing persons.

Flow of Events

Basic Flow: Can add, update or delete missing persons.

Alternative Flow: Can view and search missing persons.

Pre-Conditions: The username and password who tries to access the crime bureau should be

valid and correct.

Post-Conditions: All the updates made must be saved.

14. User Login

Description: Login page for the users

Flow of Events

Basic Flow: Opens the crime bureau website.

Alternative Flow: NIL.

Pre-Conditions: The user must own a valid username and password issued by the police

officers.

Post-Conditions: The username and password must be valid and correct.

---

## 📊 UML Modeling Suite for Crime Bureau

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

- **Previous Chapter**: [Design of UML Diagrams for Online College Magazine System](Chapter_19_Design_of_UML_Diagrams_for_Online_College_Magazine_System.md)
- **Next Chapter**: [Design of UML Diagrams for Smart Traffic Management System](Chapter_21_Design_of_UML_Diagrams_for_Smart_Traffic_Management_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
