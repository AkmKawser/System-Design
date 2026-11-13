# Chapter 23: Design of UML Diagrams for AAROGYA SETU - Health Care APP

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 237–246 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 22: Design of UML Diagrams for Job Seeker Portal System](Chapter_22_Design_of_UML_Diagrams_for_Job_Seeker_Portal_System.md) | [📚 Book Index](../Overall_Books.md) | [Chapter 24: Design of UML Diagrams for Online Pharmacy Management System &rarr;](Chapter_24_Design_of_UML_Diagrams_for_Online_Pharmacy_Management_System.md)

---

## 📌 Chapter Overview

Chapter 23 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for AAROGYA SETU - Health Care APP**. 
This case study presents an end-to-end software engineering analysis for **AAROGYA SETU - Health Care APP**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **23.1 Problem Statement**
- **23.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 23

Design of UML Diagrams

for AAROGYA SETU –

Health Care APP

### 23.1 Problem Statement

Coronavirus pandemic is spreading in large numbers. Experts suggest that social distancing has

been used for a long time as one of the methods to reduce the spike in diseases and infectious illnesses. In India alone, the cases have sharply spiked up in the past two weeks, which has led to

imposing even tougher measures. By identifying ‘hotspots’, necessary mapping can help deal with

the problem of community transmission, i.e., when cases start

Spreading within the population in such a way that people don’t know how they were exposed

to the contagion. This is known as ‘Stage 3’ of an outbreak. The Aarogya Setu app, which is a

coronavirus tracker of sorts works on the basis of contact tracing and can help a user identify possible coronavirus ‘hotspot’ around his or her area. It can help people stay safe and adopt necessary

precautions in some areas where there are cases and accordingly, help stop or prevent community

transmission to an extent. On the basis of geotagging, it can also alert a specific user about their

proximity to a nearby infection case or hotspot. The app also helps users self-identify their risk and

monitor their health assessment, considering the times when it can get difficult (and most of all, is

not particularly safe to step out and visit health clinics).

Aarogya Setu app also helps people identify the symptoms, alert them about the best safety

precautions and other relevant information concerning the spread of COVID-19. While this is a

noble initiative, the app also lists down basic quarantine measures for those who are considered to

be in the ‘high-risk’ category. It can also help people, who have had a travel history self-quarantine

and prevent any risk of transmission (Figures 23.1–23.8).

DOI: 10.1201/9781003287124-23

### 23.2 UML Diagrams

Actor Specification

1. User – User has to register by giving personal details and the verification process.

2. Admin – Admin provides authorization to the user by the verification process.

Figure 23.1 UML usecase diagram.

Figure 23.2 UML activity diagram.

Figure 23.3 UML sequence diagram.

Figure 23.4 UML collaboration diagram.

Figure 23.5 UML state machine diagram.

Figure 23.6 UML class diagram.

Figure 23.7 UML component diagram.

Usecase Specification

1. Register

Description: User should register to get access to the application.

Flow of Events

Basic Flow: Allows user to undergo the verification process.

Pre-Conditions: User should be the citizen of India.

Post-Conditions: Providing proper details and verification process.

2. Verify OTP Number

Description: User should enter the OTP number provided by the system for the verification process.

Flow of Events

Basic Flow: Allows user into the system after getting authorized by the admin.

Alternate Flow: Displays error message if the user has entered an incorrect OTP number.

Pre-Conditions: Nil.

Post-Conditions: Nil.

3. Access Device Location

Description: The user must turn on his/her device location and accept the terms and

conditions of the application.

Flow of Events

Figure 23.8 UML deployment diagram.

Basic Flow: Allows user into the system after getting authorized by the admin.

Alternate Flow: Displays error message if the location is not turned on.

Pre-Conditions: Users location should be in India.

Post-Conditions: Nil.

4. Personal Details

Description: Users should provide all the necessary personal details asked by the system.

Flow of Events

Basic Flow: Allows user into the system after getting authorized by the admin.

Alternate Flow: Displays an error message if the provided details are wrong.

Pre-Conditions: Nil.

Post-Conditions: Nil.

5. Error Message

Description: If the entered user’s OTP number is wrong.

Flow of Events

Basic Flow: Gets out of the system.

Alternate Flow: Nil.

Pre-Conditions: User should enter the correct OTP number.

Post-Conditions: Nil.

6. Authorize

Description: Admin authorizes the user into the system after the verification process.

Flow of Events

Basic Flow: Allows into the system.

Alternate Flow: Displays an error message if the verification process gets failed.

Pre-Conditions: Verification process should be done correctly by the user.

Post-Conditions: Nil.

7. Error Message Retry Again

Description: If the admin did not authorize the user, users should retry again.

Flow of Events

Basic Flow: Gets out of the system.

Alternative Flow: Nil.

Pre-Conditions: Authorization should be done properly.

Post-Conditions: Nil.

8. User Status

Description: To check the users’ health conditions.

Flow of Events

Basic Flow: Allows user to take a self-analysis test.

Alternate Flow: Nil.

Pre-Conditions: The admin should authorize the user.

Post-Conditions: User should answer the health care questions correctly.

9. Media

Description: The System provides the users with advices, healthcare tips and trending

videos.

Flow of Events

Basic Flow: Allows user too many categories of videos provided by the system.

Alternate flow: Nil.

Pre-Conditions: The admin should authorize the user.

Post-Conditions: Nil.

10. Covid-19 Updates

Description: The system provides the users with a daily number of positive cases.

Flow of Events

Basic Flow: Allows users to know the number of cases around their area.

Alternate Flow: Nil.

Pre-Conditions: The admin should authorize the user.

Post-Conditions: Nil.

11. Health-Related Questions

Description: The user should answer the health care questions in order to check their

health condition.

Flow of Events

Basic Flow: Splits the users into feeling well and not feeling well categories accordingly.

Alternative Flow: Nil.

Pre-Conditions: The admin should authorize the user.

Post-Conditions: If the user is not feeling well, he/she should consult a doctor.

12. Feeling Well

Description: The system provides the users with the output of the self-analysis test as

feeling well.

Flow of Events

Basic Flow: Nil.

Alternative Flow: Nil.

Pre-Conditions: The users must take the self-analysis test.

Post-Conditions: Nil.

13. Not Feeling Well

Description: The system provides the users with the output of the self-analysis test as not

feeling well.

Flow of Events

Basic Flow: Suggests users to consult a doctor.

Alternative Flow: Nil.

Pre-Conditions: The users must take the self-analysis test.

Post-Conditions: Nil.

14. Consult Doctor

Description: If the users are not feeling well, the system suggests the users to consult a

doctor.

Flow of Events

Basic Flow: Suggests users to call healthcare members.

Alternative Flow: Nil.

Pre-Conditions: The users must take the self-analysis test.

Post-Conditions: Nil.

15. Call Helpline

Description: In case if the users are not feeling well, the system suggests the users to call

helpline.

Flow of Events

Basic Flow: Nil.

Alternative Flow: Nil.

Pre-Conditions: The users must take the self-analysis test.

Post-Conditions: Nil.

16. Advice from Doctors

Description: The system provides the users with many advising videos of doctors.

Flow of Events

Basic Flow: The system provides many health-related videos to the users.

Alternative Flow: Nil.

Pre-Conditions: The admin must authorize the user.

Post-Conditions: Nil.

17. Immunity-Boosting Tips

Description: The system provides many immunity-boosting tips to the users.

Flow of Events

Basic Flow: Nil.

Alternative Flow: Nil.

Pre-Conditions: The Admin must authorize the user.

Post-Conditions: Nil.

18. Positive Cases around User’s Surroundings

Description: The system provides the number of positive corona cases around users’ area.

Flow of Events

Basic Flow: Nil.

Alternative Flow: Nil.

Pre-Conditions: The admin should authorize the users.

Post-Conditions: Nil.

---

## 📊 UML Modeling Suite for AAROGYA SETU - Health Care APP

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

- **Previous Chapter**: [Design of UML Diagrams for Job Seeker Portal System](Chapter_22_Design_of_UML_Diagrams_for_Job_Seeker_Portal_System.md)
- **Next Chapter**: [Design of UML Diagrams for Online Pharmacy Management System](Chapter_24_Design_of_UML_Diagrams_for_Online_Pharmacy_Management_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/Overall_Books.md`](../Overall_Books.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
