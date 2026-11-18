# Chapter 27: Design of UML Diagrams for e-Med Medical Assistance Tool

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 287–294 (Total: 8 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 26: Design of UML Diagrams for an OTT-Based System - MINI REEL](Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_System_MINI_REEL.md) | [📚 Book Index](../UML_Book.md) | [Chapter 28: Design of UML Diagrams for Diet Care &rarr;](Chapter_28_Design_of_UML_Diagrams_for_Diet_Care.md)

---

## 📌 Chapter Overview

Chapter 27 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for e-Med Medical Assistance Tool**. 
This case study presents an end-to-end software engineering analysis for **e-Med Medical Assistance Tool**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **27.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 27

Design of UML Diagrams

for e-Med Medical

Assistance Tool

27 .1 Problem Statement

e-Med is your perfect medical friend. We often see our grandparents forgetting to take their

medicines or getting tensed when they run out of medical supplies. In this fast-paced world with

unhealthy lifestyles, a number of young people also have some medical issues. e-Med is a tool that

helps keep track of and address all your personal medical needs. Once the data is fed regarding

the schedule of intake of medicines, this tool will provide reminders for taking the medicines. It

will also send notifications to restock the medicines. It is also programmed to schedule monthly

or yearly appointments regularly with the family doctor. Another interesting feature of this tool is

that during critical situations, pressing the emergency button will automatically contact your near

and dear ones whose contacts are in your emergency contact list. The tool helps in keeping a record

of your medical history such as your blood sugar levels, pressure levels, etc. by using the Medical

Notes feature. e-Med is an indispensable tool for people of all ages with medical issues to help

maintain a good health routine (Figures 27.1–27.8).

### 27.2 UML Diagrams

Actor Specification

1. Customers/Users – The users of this tool are people of all ages with chronic health issues

who need to take medicines regularly to keep themselves healthy. Users must record their

medical history and update medical history whenever required. The users can schedule

appointments regularly with their doctor. They can press the emergency button when a critical situation arises. They can also write and update medical notes.

DOI: 10.1201/9781003287124-27

2. Admin (Database) – The database stores all the information about the users, their medical

history, notes, etc. It initiates operations like sending notifications when it is time for the

users to take their medicine or restock medicines. It also sends a message to the receptionist

to schedule an appointment and calls the emergency contacts as soon as the emergency button is pressed.

Figure 27.1 UML usecase diagram.

Figure 27.2 UML activity diagram.

Figure 27.3 UML sequence diagram.

Usecase Specification

1. Fill Personal Medical History

Description: The users can fill in the details of the frequency of medicine intake, the

stock of monthly medicines, the contact number of the doctor/receptionist for scheduling

regular appointments and the emergency contact numbers of close relatives and neighbours.

Flow of Events

Basic Flow: The users are asked to fill in their medical history.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The details entered by the user must be validated.

Figure 27.4 UML collaboration diagram.

Figure 27.5 UML state chart diagram.

2. Validate and Store

Description: The personal medical history of the user is validated and stored in the

database.

Flow of Events

Basic Flow: The details entered by the user in their personal medical history are validated

and stored in the database.

Alternative Flow: If the details are incorrect, the user has to re-enter the data in the fields

with incorrect data.

Pre-Conditions: All the required details must be filled and verified before storing them in

the database.

Post-Conditions: Nil.

Figure 27.6 UML class diagram.

Figure 27.7 UML component diagram.

3. View Medical History

Description: This allows the user to view the medical data entered by him/her.

Flow of Events

Basic Flow: The user can view the details that he/she filled in their medical history.

Alternative Flow: Nil.

Pre-Conditions: All the details must be filled and stored in the database.

Post-Conditions: Nil.

4. Update Medical History

Description: The users should update the medical history when there is a change in the

dosage or frequency of medication.

Flow of Events

Basic Flow: The data in the personal medical history are updated whenever the user changes

any field in that form.

Alternative Flow: Nil.

Pre-Conditions: All the details must be filled and stored in the database.

Post-Conditions: The details must be updated in the database.

5. Reminder to Have Medicines on Time

Description: The app gives notifications for timely intake of medicines.

Flow of Events

Basic Flow: The users are reminded to have their medicines on time.

Alternative Flow: Nil.

Pre-Conditions: The user must have filled the details regarding the schedule of intake of

medicines in his/her personal medical history.

Post-Conditions: Nil.

6. Reminder to Buy Medicines When Not in Stock

Description: The app tracks the stock of medicines and reminds the user to restock the

medicines that would not last for more than a few days.

Flow of Events

Basic Flow: The users are reminded to buy medicines when they are out of stock.

Alternative Flow: Nil.

Figure 27.8 UML deployment diagram.

Pre-Conditions: The user must have filled in the details regarding the stock of medicines at

the moment and the number of medicines he/she takes daily in his/her personal medical

history.

Post-Conditions: Nil.

7. Schedule Appointments Regularly

Description: e-Med schedules appointment regularly with the doctor.

Flow of Events

Basic Flow: The app schedules appointments after a fixed period of time by sending a message to the doctor/receptionist.

Alternative Flow: Nil.

Pre-Conditions: The number of appointments with the doctor in a year (like once in

6 months, once a month, etc.) must be stored

Post-Conditions: Message should be sent to the doctor/receptionist to book an appointment.

8. Send Messages to Receptionist

Description: It regularly sends a message to the receptionist for the booking of

appointments.

Flow of Events

Basic Flow: The app sends a message to the receptionist/doctor to book appointments.

Alternative Flow: Nil.

Pre-Conditions: The receptionist/doctor’s contact number must be saved in the app.

Post-Conditions: Nil.

9. Press Emergency Button

Description: The users can press the emergency button when in serious condition.

Flow of Events

Basic Flow: When an emergency situation arises, the users can press this button to call for

help immediately.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The app should call the emergency contacts right after the button is pressed.

10. Call Emergency Contacts

Description: As soon as the emergency button is pressed, the app calls all the emergency

contacts.

Flow of Events

Basic Flow: The emergency contacts are called after the emergency button is pressed.

Alternative Flow: Nil.

Pre-Conditions: The contact numbers of close relatives and neighbours must be saved as

emergency contacts.

Post-Conditions: Nil.

11. Write Medical Notes for Reference

Description: Medical notes such as sugar levels, pressure levels etc. can be recorded here.

Flow of Events

Basic Flow: Users can write any medical details that they wish to keep track of in the

medical notes.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: It must be stored in the database as soon as the notes are saved.

12. View Medical Notes

Description: Users can view the medical notes to monitor sugar or pressure levels.

Flow of Events

Basic Flow: The user can view the details that he/she wrote in their medical notes.

Alternative Flow: Nil.

Pre-Conditions: All the details written by the user in the medical notes must be stored in

the database.

Post-Conditions: Nil.

13. Update Medical Notes

Description: Users may update medical notes after taking another sugar level or pressure

level reading.

Flow of Events

Basic Flow: The data in the medical notes are updated whenever the user changes it.

Alternative Flow: Nil.

Pre-Conditions: All the details written by the user in the medical notes must be stored in

the database.

Post-Conditions: The updated notes must be stored in the database.

---

## 📊 UML Modeling Suite for e-Med Medical Assistance Tool

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

- **Previous Chapter**: [Design of UML Diagrams for an OTT-Based System - MINI REEL](Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_System_MINI_REEL.md)
- **Next Chapter**: [Design of UML Diagrams for Diet Care](Chapter_28_Design_of_UML_Diagrams_for_Diet_Care.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
