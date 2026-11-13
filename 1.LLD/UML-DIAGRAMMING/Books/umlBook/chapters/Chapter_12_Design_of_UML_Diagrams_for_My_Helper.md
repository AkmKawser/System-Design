# Chapter 12: Design of UML Diagrams for My Helper

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 139–146 (Total: 8 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 11: Design of UML Diagrams for Advocate Diary](Chapter_11_Design_of_UML_Diagrams_for_Advocate_Diary.md) | [📚 Book Index](../UML_Book.md) | [Chapter 13: Design of UML Diagrams for COVID-19 Management System &rarr;](Chapter_13_Design_of_UML_Diagrams_for_COVID_19_Management_System.md)

---

## 📌 Chapter Overview

Chapter 12 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for My Helper**. 
This case study presents an end-to-end software engineering analysis for **My Helper**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **12.1 Problem Statement**
- **12.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 12

Design of UML Diagrams

for My Helper

### 12.1 Problem Statement

This case study is helpful to people who forget their mobile phones at home as a part of their

busy daily routines. Keeping tick of essentials in this fast-paced life sometimes turns out to be

quite demanding. People sometimes forget their phones at home. What if we need to make an

important call and we don’t remember the contact number? Sometimes our phones just get disappeared and the scariest part is when the phone is put on silent mode. We sometimes want to lock

our phones when they aren’t around us. Need to know the exact location of your phone? Therein

comes the use of ‘My Helper’. The solutions to all the problems stated above can be solved easily

and very quickly if u have the application ‘My Helper’ pre-installed on your phone and u have

completed configuring the app. All you need to do is just send an SMS to your mobile number

from any phone that you have access to…and there goes your problem solved. The scope of this

system is increasing every day across the entire world where everything is happening at the speed

of a Formula 1 Car on a race track. The objective of this system is to provide help to people facing

these types of problems instantly with the help of advanced technology. The alluring features of

this system are Remote Access without the Internet, Track your phone through an SMS, HassleFree as no OTP and ID PASSWORD is required and an SMS can help you change the sound

profile of your phone (silent to normal) without Internet. The system is user friendly and the application will be available to even basic smartphones (Figures 12.1–12.8).

DOI: 10.1201/9781003287124-12

Figure 12.1 UML usecase diagram.

Figure 12.2 UML activity diagram.

### 12.2 UML Diagrams

Usecase Specification

1. Login

Description: This usecase allows the user to get started with the system.

Flow of Events

Basic Flow: Entering valid details to get started with the system.

Alternative Flow: If invalid details are entered, the user is redirected to fill out correctly.

Pre-Conditions: Nil.

Post-Conditions: User gets registered, data of the user gets stored into the database.

Figure 12.3 UML sequence diagram.

2. Set Password

Description: Allows user to set a strong password to use it later.

Flow of Events

Basic Flow: Setting a strong password (e.g. Using numbers, Special characters, Lowercase

and uppercase letters).

Figure 12.4 UML collaboration diagram.

Figure 12.5 UML state machine diagram.

Figure 12.6 UML class diagram.

Figure 12.7 UML component diagram.

Alternative Flow: If the password is weak, the user is redirected to enter a strong password.

Pre-Conditions: The user must have entered the email address, phone number and username

before setting the password.

Post-Conditions: Password is set successfully and it gets stored in the database.

3. Send SMS

Description: This usecase allows the user to send SMS to his/her’s mobile number from

any other mobile phone.

Flow of Events

Basic Flow: Sending SMS successfully.

Alternative Flow: If SMS sending is failed due to any issue, the user should resend the SMS.

Pre-Conditions: The user must have completed configuring the ‘MY HELPER’ system on

his mobile phone.

Post-Conditions: SMS is successfully sent.

4. Read SMS

Description: This usecase is about the ‘My Helper’ application reading SMS sent to the

phone.

Flow of Events

Basic Flow: The system reads the SMS, checks for a password that has been set by the user.

Alternative Flow: If the password sent in the SMS doesn’t match the password set by the

user, My Helper sends back an SMS stating invalid details.

Pre-Conditions: The SMS should have been received and the user should have given ‘My

Helper’ access to read messages.

Post-Conditions: SMS is read successfully and ‘My Helper’ now starts checking details of

the requirement.

5. Checks Requirement

Description: Checks for a valid requirement.

Flow of Events

Basic Flow: If it is a valid requirement, ‘My Helper’ now starts processing the requirement.

Alternative Flow: If the requirement is not valid, My Helper sends back an SMS stating

invalid details.

Pre-Conditions: SMS should have been received and successfully read.

Post-Conditions: The requirement fulfilment process gets started.

Figure 12.8 UML deployment diagram.

6. Error

Description: If SMS sending fails, it results in an error.

Flow of Events

Basic Flow: Error in sending.

Alternative Flow: Send another SMS or Nil.

Pre-Conditions: Nil.

Post-Conditions: Send SMS again (or) Don’t send an SMS.

7. Fulfil Requirement

Description: Performs operations and satisfies user requirements.

Flow of Events

Basic Flow: After scanning the requirement, start processing the requirement.

Alternative Flow: Requirement processing is failed, request another requirement.

Pre-Conditions: Requirement should be read and valid.

Post-Conditions: After fetching the requirement, send the requested details back to the user.

8. Requirement Error

Description: If the requirement cannot be satisfied by ‘My helper’, it results in an error.

Flow of Events

Basic Flow: Requirement has been read, and it resulted in an error.

Alternative Flow: Request another requirement or satisfy the requirement if it is valid.

Pre-Conditions: Nil.

Post-Conditions: Send another requirement or Nil.

9. Send Requested Details

Description: Fetch user requirements and send them to the user in the form of SMS.

Flow of Events

Basic Flow: Requirement details have been fetched completely and send it to the user.

Alternative Flow: Requested detail fetching has been failed or Nil.

Pre-Conditions: Requirement details should have been fetched.

Post-Conditions: Nil.

10. Verif y Password

Description: Verifying if the password sent in SMS matches the user-set-password

Flow of Events

Basic Flow: Verify password.

Alternative Flow: Wrong password.

Pre-Conditions: Should have received SMS.

Post-Conditions: Password is successfully verified.

---

## 📊 UML Modeling Suite for My Helper

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

- **Previous Chapter**: [Design of UML Diagrams for Advocate Diary](Chapter_11_Design_of_UML_Diagrams_for_Advocate_Diary.md)
- **Next Chapter**: [Design of UML Diagrams for COVID-19 Management System](Chapter_13_Design_of_UML_Diagrams_for_COVID_19_Management_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
