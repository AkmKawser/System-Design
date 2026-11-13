# Chapter 11: Design of UML Diagrams for Advocate Diary

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 129–138 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 10: Design of UML Diagrams for Product Recommendation System](Chapter_10_Design_of_UML_Diagrams_for_Product_Recommendation_System.md) | [📚 Book Index](../Overall_Books.md) | [Chapter 12: Design of UML Diagrams for My Helper &rarr;](Chapter_12_Design_of_UML_Diagrams_for_My_Helper.md)

---

## 📌 Chapter Overview

Chapter 11 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Advocate Diary**. 
This case study presents an end-to-end software engineering analysis for **Advocate Diary**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **11.1 Problem Statement**
- **11.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 11

Design of UML Diagrams

for Advocate Diary

### 11.1 Problem Statement

The need for law and enforcement in a country with a high population like India is salient. Lawyers

play a major role in maintaining most of their data as hard copies. This project is mainly designed for

lawyers to make their work more easy and efficient. It is a responsive web application that would provide lawyers with various services that would help them to maintain their documents. The services

include a logbook that has details about the cases along with a calendar. The lawyers can also upload

and save documents related to their case. It contains formats of model forms and links to online filing. It also provides quick references of common cases and detailed information about laws through

e-books. Information about the judicial exams for lawyers is also made available. Furthermore, the

web application contains news updates for lawyers, blogs and feedback. This case study will serve as

a small hand tool for lawyers to maintain the soft copies of their data (Figures 11.1–11.8).

### 11.2 UML Diagrams

Usecase Specification

1. Register

Description: Register allows a new lawyer to create an account.

Flow of Events

Basic Flow: User enters proper credentials.

Alternative Flow: If improper credentials are entered.

Pre-Conditions: Nil.

Post-Conditions: The data entered are saved in the database. The user is allowed to login.

2. Login

Description: It allows a valid user to login to the page.

Flow of Events

Basic Flow: Enters user id and password.

DOI: 10.1201/9781003287124-11

Alternative Flow: Invalid ID or password leads to improper login.

Pre-Conditions: The user should have registered.

Post-Conditions: Nil.

3. View Case Details and Logs

Description: Displays details about both existing and completed cases along with the

calendar.

Flow of Events

Basic Flow: Allows user to view and edit details.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: If edited, the remainders will be reflected in the calendar.

4. Add Case

Description: Allows user to add new case.

Flow of Events

Basic Flow: User can add details about new cases.

Alternative Flow: User may not add details.

Pre-Conditions: Nil.

Post-Conditions: Nil.

5. Update Details

Description: This allows the user to enter specific details about the case.

Flow of Events

Basic Flow: User enters the proper details.

Alternative Flow: User may enter wrong details.

Pre-Conditions: User must have details about the cases.

Post-Conditions: The details are reflected in the View table.

Figure 11.1 UML usecase diagram.

6. Criminal

Description: It specifies whether the case is a criminal case.

Flow of Events

Basic Flow: The user selects if it is a criminal case.

Alternative Flow: The user doesn’t select it if it’s not a criminal case.

Pre-Conditions: Nil.

Post-Conditions: The information is reflected in the view table.

7. Civil

Description: It specifies whether the case is a civil case.

Flow of Events

Basic Flow: The user selects if it is a civil case.

Alternative Flow: The user doesn’t select it if it’s not a civil case.

Figure 11.2 UML activity diagrams.

Figure 11.3 UML sequence diagram.

Pre-Conditions: Nil.

Post-Conditions: The information is reflected in the view table.

8. Update Logs

Description: This updates the view table with the data provided.

Flow of Events

Basic Flow: The data given is added to the view table.

Alternative Flow: Nil.

Pre-Conditions: The details should be entered by the user.

Post-Conditions: Nil.

9. Set Remainders

Description: It allows users to add date and time details for the case.

Flow of Events

Figure 11.4 UML collaboration diagram.

Basic Flow: The user enters the date and time the case will be held.

Alternative Flow: The user may not enter the date and time.

Pre-Conditions: The user should have entered details of the case.

Post-Conditions: The remainder is reflected in the view and calendar table.

10. Update Calendar

Description: This function updates the calendar with the remainder.

Flow of Events

Basic Flow: The calendar is updated with the remainders.

Figure 11.5 UML state machine diagram.

Alternative Flow: Nil.

Pre-Conditions: The user should have set remainders.

Post-Conditions: Nil.

11. Upload Document

Description: A user can upload the documents related to the case.

Flow of Events

Basic Flow: The user uploads the document.

Alternative Flow: The user may not upload the document.

Pre-Conditions: The details of the case must be entered.

Post-Conditions: The documents are saved in the drives.

Figure 11.6 UML class diagram.

Figure 11.7 UML component diagram.

12. Filing Online

Description: It is used to file a case or do any other legal related filing online.

Flow of Events

Basic Flow: It displays the various types of online legal services.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

13. Display Links

Description: It displays links to various online filings.

Flow of Events

Basic Flow: The links based on the type of service needed is displayed.

Alternative Flow: Nil.

Pre-Conditions: The user should choose a type.

Post-Conditions: Redirects to the respective page selected.

14. Redirected to Respective Page

Description: This redirects to the link selected.

Flow of Events

Basic Flow: The page of the link selected for online filing is displayed.

Alternative Flow: Nil.

Pre-Conditions: A link should be clicked.

Post-Conditions: Nil.

15. Download Model Forms

Description: This allows users to download model forms.

Flow of Events

Basic Flow: This displays different categories of cases.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

Figure 11.8 UML deployment diagram.

16. Display Forms

Description: It displays various forms on the category selected.

Flow of Events

Basic Flow: The user can select any form to be downloaded.

Alternative Flow: Nil.

Pre-Conditions: The category must be selected.

Post-Conditions: Nil.

17. Download

Description: This allows the user to download a model form.

Flow of Events

Basic Flow: It displays the option to view and download the form.

Alternative Flow: Nil.

Pre-Conditions: The form to be downloaded must be selected.

Post-Conditions: The downloaded document will be saved in the system.

18. Reference

Description: It displays quick references and books for the user to choose.

Flow of Events

Basic Flow: The user selects for quick reference or books.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

19. Quick Reference

Description: It displays various information about the most common cases.

Flow of Events

Basic Flow: The important information for the most common cases are listed.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

20. Books

Description: Helps the user to get information via law e-books.

Flow of Events

Basic Flow: It displays the title of the book.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: The book selected will be displayed.

21. Feedback

Description: This allows users to add feedbacks.

Flow of Events

Basic Flow: The user is allowed to add feedbacks.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

22. Add Feedback

Description: This allows the user to type in and send feedbacks.

Flow of Events

Basic Flow: The user sends the feedback.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: If any problem, it’ll be rectified by the developer.

23. View Blogs and Updates

Description: It allows users to view blogs and news updates.

Flow of Events

Basic Flow: Both registered and unregistered users can see blogs and news updates regarding

legal activities.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

---

## 📊 UML Modeling Suite for Advocate Diary

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

- **Previous Chapter**: [Design of UML Diagrams for Product Recommendation System](Chapter_10_Design_of_UML_Diagrams_for_Product_Recommendation_System.md)
- **Next Chapter**: [Design of UML Diagrams for My Helper](Chapter_12_Design_of_UML_Diagrams_for_My_Helper.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/Overall_Books.md`](../Overall_Books.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
