# Chapter 30: Design of UML Diagrams for E-Visa Processing and Follow-Up System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 313–324 (Total: 12 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 29: Design of UML Diagrams for Student Counselling Management System](Chapter_29_Design_of_UML_Diagrams_for_Student_Counselling_Management_System.md) | [📚 Book Index](../Overall_Books.md) | [Chapter 31: Design of UML Diagrams for Placement Automation System &rarr;](Chapter_31_Design_of_UML_Diagrams_for_Placement_Automation_System.md)

---

## 📌 Chapter Overview

Chapter 30 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for E-Visa Processing and Follow-Up System**. 
This case study presents an end-to-end software engineering analysis for **E-Visa Processing and Follow-Up System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **30.1 Problem Statement**
- **30.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 30

Design of UML Diagrams

for E-Visa Processing and

Follow-Up System

### 30.1 Problem Statement

A visa is a document issued by a country giving a certain individual permission to enter a country

for a given period of time for certain purposes. It is received after several verifications through

offline mode. It requires the applicant to go to the Passport Verification Centre for the verification

of documents. Sometimes even the cost of getting the visa will be high as there may be middlemen

involved in it. It takes anywhere from two weeks to two months to receive the visa if applied in

offline mode. With the use of an online visa processing system, the middlemen entry in getting

the visa gets reduced and the process of application of visa becomes easier. The overall aim of the

system is that the applicant can apply for the visa from anywhere and at any time. The applicant

can apply for the visa and submit it online. It provides more flexibility to the applicant compared

to the existing system. There are certain types of visas that the applicant can apply for such as

employment visa, study visa, resident visa, H1 visa, business visa, etc. People who apply for the visa

for work, education, etc will be benefitted a lot from this system. The applicant should register by

providing a valid email and a password. The applicant has to log in to apply for the visa. The credentials are checked for correctness and the applicant to allow to log in. Once the applicant logs in,

he/she will be shown the application form which asks the applicant to provide the necessary details

and asks him/her to attach the necessary documents. It also provides a list of visas to choose from.

He/she can also view the details of fair to visa for each country. The applicant can view, modify

and delete the details applied. The system will have a provision for the administrator to view the

details of what types of visas are required by the applicant. The administrator will also be able to

update and delete the details of the applicants. The administrator will have a facility to interact

with the Visa Consultant Officer. The Visa Consultant Officer can be able to view and check the

document proofs (valid passport, Demand Draft Visa Fee I-20 form, letter of admission, aid letter,

etc.) submitted by the applicant and can be able to view the purpose of application of visa. He/She

has the authority to accept/reject the visa application applied by the applicant (Figures 30.1–30.9).

DOI: 10.1201/9781003287124-30

Figure 30.1 UML usecase diagram.

Figure 30.2 UML activity diagram – Scenario 1.

Figure 30.3 UML activity diagram – Scenario 2.

Figure 30.4 UML sequence diagram.

Figure 30.5 UML collaboration diagram.

Figure 30.6 UML state chart diagram.

Figure 30.7 UML class diagram.

Figure 30.8 UML component diagram.

### 30.2 UML Diagrams

Actor Specification

1. Administrator – The administrator can view applicants’ details, accept applications, view

and update the status of the visa.

2. Applicant – The applicant can apply for a visa, view details, modify details, cancel the application, check the status and give feedback (optional).

3. Visa Consultant Officer – The Visa Consultant Officer views the purpose of the application, verifies the document proofs and accepts or rejects the visa.

Figure 30.9 UML deployment diagram.

Usecase Specification

1. Accept Application

Description: Enables the administrator to accept applications submitted by the applicants.

Flow of Events

Basic Flow: After submitting the form online and making payment, the application is

accepted.

Alternative Flow: Nil.

Pre-Conditions: The details should be filled correctly in the application form and the payment for processing the visa should be made.

Post-Conditions: Nil.

2. Accept Visa

Description: Enables the Visa Consultant Officer to accept (approve) visa of applicants.

Flow of Events

Basic Flow: After verifying the documents to be correct, the Visa Consultant Officer accepts

the visa.

Alternative Flow: Nil.

Pre-Conditions: Valid document proofs should be attached correctly.

Post-Conditions: Nil.

3. Apply for Visa

Description: Helps the applicants to apply for a visa by filing an application form online.

Flow of Events

Basic Flow: Set of details that are to be filled correctly before submitting the form online.

Alternative Flow: Nil.

Pre-Conditions: The applicant should have registered with the system.

Post-Conditions: The details that are filled by the applicant should be correct.

4. Approve Visa

Description: Enables the Visa Consultant Officer to either accept or reject the visa.

Flow of Events

Basic Flow: The visa consultant officer, after verifying the document proofs that are submitted accepts or rejects the visa.

Alternative Flow: Nil.

Pre-Conditions: The document proofs should be checked for correctness.

Post-Conditions: If the documents are verified to be correct, the visa is accepted. Otherwise,

it is rejected.

5. Authentication

Description: Used to verify the credentials when an actor logs in.

Flow of Events

Basic Flow: The actor is asked to enter a valid username and a password.

Alternative Flow: The actor is redirected to the login page.

Pre-Conditions: The user should have entered valid credentials.

Post-Conditions: The credentials should be correct.

6. Cancel Application

Description: Enables the user to cancel his/her application.

Flow of Events

Basic Flow: The applicant is given an option to cancel his/her application if he/she no longer

has to apply for the visa.

Alternative Flow: Nil.

Pre-Conditions: The application form should be submitted earlier.

Post-Conditions: Nil.

7. Check Status

Description: Enables the applicant to check the status of his/her application.

Flow of Events

Basic Flow: The applicant can check the status of his/her application (in progress, approved,

rejected).

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The application should be submitted.

8. Give Feedback

Description: Enables the user to give feedback about the visa that is being processed.

Flow of Events

Basic Flow: After checking the status, the applicant can give optional feedback.

Alternative Flow: Nil.

Pre-Conditions: The status should be checked.

Post-Conditions: Nil.

9. Log Out

Description: enables all the actors to log out of the system.

Flow of Events

Basic Flow: After performing all the operations that the actor wants, he/she can log out of

the system.

Alternative Flow: Nil.

Pre-Conditions: The user should have signed in.

Post-Conditions: Nil.

10. Make Payment

Description: Enables the applicant to make payment.

Flow of Events

Basic Flow: The applicant will pay for the processing of the visa.

Alternative Flow: The applicant will be redirected to the home page.

Pre-Conditions: The application form should be submitted.

Post-Conditions: The amount paid is checked.

11. Modify Details

Description: Enables the applicant to modify the details that were given in the application form.

Flow of Events

Basic Flow: If the applicant feels that he/she has given the wrong details, he/she can modify

the details.

Alternative Flow: Nil.

Pre-Conditions: The application should be submitted.

Post-Conditions: The modifications are to be done in the database.

12. Register

Description: Enables a user to register with the system.

Flow of Events

Basic Flow: The actor registers with the system by entering a valid username and a password.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The user should enter a valid credentials (email and password).

13. Reject Visa

Description: Enables the Visa Consultant Officer to reject the visa.

Flow of Events

Basic Flow: The visa consultant officer rejects the visa if the document proofs submitted are

not verified to be correct.

Alternative Flow: The applicant is shown the next date when he/she can reapply.

Pre-Conditions: The document proofs submitted should be invalid.

Post-Conditions: Nil.

14. Update Status

Description: Updating the status of the visa as per the process being carried out.

Flow of Events

Basic Flow: The administrator updates the status of the applicant’s visa application after each

stage is completed.

Alternative Flow: Nil.

Pre-Conditions: The application form should be submitted.

Post-Conditions: Nil.

15. Verify Document Proofs

Description: The document proofs submitted by the applicant are verified for correctness

by the Visa Consultant Officer.

Flow of Events

Basic Flow: The visa consultant officer verifies whether the document proofs submitted are

valid and correct.

Alternative Flow: Nil.

Pre-Conditions: The purpose of the application should be checked by the Visa Consultant

Officer.

Post-Conditions: The document proofs submitted should not be invalid.

16. View Details

Description: Enables the applicant to view the details which he/she gave in the form.

Flow of Events

Basic Flow: The applicant can view the details that he/she provided in the application form.

Alternative Flow: Nil.

Pre-Conditions: The form should be submitted.

Post-Conditions: Nil.

17. View Applicants' Details

Description: Enables the Administrator to view the details provided by the applicants.

Flow of Events

Basic Flow: The administrator views the applicants’ details.

Alternative Flow: Nil.

Pre-Conditions: The application should be accepted.

Post-Conditions: It is checked whether the applicants have provided all the details.

18. View Purpose of Application

Description: The Visa Consultant Officer can view the purpose of visa application (tourist visa, study visa, etc.).

Flow of Events

Basic Flow: The visa consultant officer views the purpose of the application to check what

documents to verify.

Alternative Flow: Nil.

Pre-Conditions: The application should be accepted by the administrator.

Post-Conditions: The documents needed for getting the particular type of visa should be

checked.

19. View Status

Description: Enables the administrator can view the status of the visa of the applicants.

Flow of Events

Basic Flow: The administrator views the status of all the applications.

Alternative Flow: Nil.

Pre-Conditions: The application should be accepted by the administrator.

Post-Conditions: The status should be updated if the processing of the visa moves to the

next state.

---

## 📊 UML Modeling Suite for E-Visa Processing and Follow-Up System

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

- **Previous Chapter**: [Design of UML Diagrams for Student Counselling Management System](Chapter_29_Design_of_UML_Diagrams_for_Student_Counselling_Management_System.md)
- **Next Chapter**: [Design of UML Diagrams for Placement Automation System](Chapter_31_Design_of_UML_Diagrams_for_Placement_Automation_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/Overall_Books.md`](../Overall_Books.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
