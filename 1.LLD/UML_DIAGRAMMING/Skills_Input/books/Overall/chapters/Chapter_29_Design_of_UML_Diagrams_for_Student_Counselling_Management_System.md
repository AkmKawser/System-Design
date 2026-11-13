# Chapter 29: Design of UML Diagrams for Student Counselling Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 303–312 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 28: Design of UML Diagrams for Diet Care](Chapter_28_Design_of_UML_Diagrams_for_Diet_Care.md) | [📚 Book Index](../README.md) | [Chapter 30: Design of UML Diagrams for E-Visa Processing and Follow-Up System &rarr;](Chapter_30_Design_of_UML_Diagrams_for_E_Visa_Processing_and_Follow_Up_System.md)

---

## 📌 Chapter Overview

Chapter 29 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Student Counselling Management System**. 
This case study presents an end-to-end software engineering analysis for **Student Counselling Management System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **29.1 Problem Statement**
- **29.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 29

Design of UML Diagrams

for Student Counselling

Management System

### 29.1 Problem Statement

The first phase of a person’s life is confined mainly by education and training. Hence, counselling is an important aspect for the students of the current technological generation as an individual counsellor may remain in contact with all individual students as well as parents. Student

Counselling Management System will simplify the process and reduce the manual paperwork.

It is used to smoothen the work of each counsellor who is facing problems currently, and making complete atomization of manual process to computerized system. The main objective of the

Student Counselling Management System is to design a system to rationalize the admission to

particular courses in a university/institution. Through this system, the student will be able to

register for counselling if he is eligible. If the student is qualifying the criteria then he will get the

information regarding the colleges and the universities in which he can apply. The main features

are online admission, report generation based on student’s merit list and keeping track of counselling procedures and finally publishing results. A student can also get the information regarding

how many seats have been booked and vacant seats available in the institution (Figures 29.1–29.8).

### 29.2 UML Diagrams

Actor Specification

1. Student – Student is the one who initiates the process by registering and filling choices.

2. Admin Team – Admin Team is the one that responds to students’ submissions of forms and

choice sheets and is also responsible for seat allotment.

3. College – College is the one that collects admit letters from admin team and decides whether

or not to accept the student.

DOI: 10.1201/9781003287124-29

Figure 29.1 UML usecase diagram.

Figure 29.2 UML activity diagram.

Figure 29.3 UML sequence diagram.

Usecase Specification

1. Login

Description: Functionality involves the student logging into our website.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Should have passed Higher Secondary Board Examinations.

Post-Conditions: Nil.

2. Password Verification

Description: Functionality involves verifying the username and password the student

entered.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Password should be entered in order to verify.

Post-Conditions: Nil.

3. Display Login Error

Description: Functionality involves throwing an error if the username or password

doesn’t match.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The student is prompted to enter username and password again.

4. Registration Form

Description: Functionality involves filling up of registration form.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: All the details specified in the registration form must be entered.

Figure 29.4 UML collaboration diagram.

Figure 29.5 UML state chart diagram.

5. Enrolment Fees

Description: Functionality involves filling the form agreeing to pay the enrolment fees

in advance.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: The student should have an account in a bank.

Post-Conditions: Nil.

Figure 29.6 UML class diagram.

Figure 29.7 UML component diagram.

6. Make Payment

Description: Functionality involves making payment for registration and enrolment

forms.

Flow of Events

Alternative Flow: If the payment failed, make another payment.

Pre-Conditions: Nil.

Post-Conditions: The student is eligible to fill the choice sheet.

7. Payment through Debit Card

Description: Functionality involves paying registration and enrolment fees through

Debit Card.

Flow of Events

Alternative Flow: If the student doesn’t want this option he can go with the net banking

option.

Pre-Conditions: The student must specify the Debit Card details correctly.

Post-Conditions: Nil.

Figure 29.8 UML deployment diagram.

8. Net Banking

Description: Functionality involves paying registration and enrolment fees online

through UPI.

Flow of Events

Alternative Flow: If the student doesn’t want this option he/she can go with payment through

the Debit Card option.

Pre-Conditions: The student should have a UPI account.

Post-Conditions: Nil.

9. Registration Form Verification

Description: Functionality involves verifying the student registration form.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The student is allowed for enrolling into college.

Certificate Verification 10.

Description: Functionality involves verifying certificates submitted by a student.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The student is allowed for enrolling into college.

11. Rank Declaration Based on Marks

Description: Functionality involves declaring rank for all the students.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: The student should have submitted proper certificates.

Post-Conditions: Nil.

12. Choice Filling and Locking

Description: Functionality involves filling up choices of the desired college.

Flow of Events

Alternative Flow: The student can opt not to fill choices if he is not interested.

Pre-Conditions: The student should have paid enrolment fees.

Post-Conditions: Nil.

13. Seat Allotment Based on Rank and Choice

Description: Functionality involves allotting seats to students in college based on choice

and rank.

Flow of Events

Alternative Flow: If the student didn’t fill the choice sheet, the seat is not allotted.

Pre-Conditions: The student should have paid enrolment fees.

Post-Conditions: Nil.

14. Admit Letter Generation

Description: Functionality involves generating admit letters for students.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The admit letter will be passed to the corresponding college.

15. Admit Letter Verification

Description: Functionality involves verifying the admit letter given by the admin team.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The student has to approach the college with admit letter generated.

16. Document Verification

Description: Functionality involves verifying documents submitted by a student.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The student can accept or decline the offer from the college.

17. Accept/Decline

Description: Functionality involves accepting/declining the student from the college side.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: The student should have passed all eligibility criteria.

Post-Conditions: Nil.

---

## 📊 UML Modeling Suite for Student Counselling Management System

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

- **Previous Chapter**: [Design of UML Diagrams for Diet Care](Chapter_28_Design_of_UML_Diagrams_for_Diet_Care.md)
- **Next Chapter**: [Design of UML Diagrams for E-Visa Processing and Follow-Up System](Chapter_30_Design_of_UML_Diagrams_for_E_Visa_Processing_and_Follow_Up_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
