# Chapter 37: Design of UML Diagrams for Book Bank Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 377–388 (Total: 12 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 36: Design of UML Diagrams for Online Quiz System](Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_System.md) | [📚 Book Index](../README.md) | [Chapter 38: Design of UML Diagrams for Website Development &rarr;](Chapter_38_Design_of_UML_Diagrams_for_Website_Development.md)

---

## 📌 Chapter Overview

Chapter 37 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Book Bank Management System**. 
This case study presents an end-to-end software engineering analysis for **Book Bank Management System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **37.2 Literature Review**
- **37.3 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 37

Design of UML

Diagrams for Book Bank

Management System

37 .1 Problem Statement

The book bank management is a software in which a member can register themselves and

then he can borrow books from the book bank or the members can buy the books from the

book bank.

A Book Bank lends books and magazines to member, who is registered in the system. It mainly

concentrates on providing the book for authorized members only. A member can reserve a book

or magazine that is not currently available in the book bank, so that when it is returned or purchased by the book bank, that person is notified. The book bank can easily create, replace and

delete information about the titles, members and reservations from the system. The main issue of

the system is that only registered members can lend the book from the book bank. In the case of

lending, we should maintain the database for the status and issue of the book and also we have to

calculate the fine amount with respect to the due date. We should maintain the book according

to the department, generals, and year of study. Another main issue of the system is that if the user

takes the book and misplace it on another shelf, then we have the chip of bar scanner to scan the

books and indicate to the admin that the book has been replaced. All the above issues will be satisfied by developing the software as a user-friendly system. The main functionality of the system is

that Sign in, Login, Log out, Book storing, Book retrieval, Book for buying, Stock Updating, Due

fine, E-books, Payment, Book maintenance, Sales report, User records and Sorting. If the software is not developed, the members will affect based on criteria like the book is not in stock, the

book is not arranged in order and maintenance will be more. The software is developed to satisfy

the needs according to the members. The software will be very useful in the area of institutions,

libraries and for general citizens. The software is developed to act as a useful interface for the users

to easily access books.

DOI: 10.1201/9781003287124-37

### 37.2 Literature Review

Existing System: The present system is only some book banks are partially automated, that is by

storing details in MS Excel Spreadsheets, whereas many other book banks are manual. A user

has to visit the book bank personally at least thrice to get a set of the books that are needed.

Also, only the user has to give the list of books needed along with the exact details of the ordered

books, such as author’s name, edition, name of the publication, etc. Only the list of users registered and the books available are stored in the database. Due to this the manual process and

work involved in the existing system are more. A user has to visit the book bank personally to

get registered, to request and also to receive books, and this is time-consuming. The book bank

works only for a specific time within which the user should visit and complete all the procedures.

The staff will have to manually search for the details of any particular user and the list of books

ordered by the user.

Proposed System: In our proposed system, the user can register online in the system, enter his/her

personal details, and can fill the registration form with a unique user Identifier. The user can complete

all the procedures such as ordering books and confirming the booklist online and go to the book bank

only for receiving the books. The system confirms the book list by means of automated email service.

The books that would be needed by the user are predicted by the system according to the department

and semester are chosen in the request books page. Hence the user is given a set of choices for selecting

a book. Due to this all the processes such as registering, requesting books, etc. can be done online and

automated. It saves a lot of time for the user and the book bank staff as well. There is no specific time

for the user to register into the system and download the registration form. The user need not give the

list of books needed, and can send only a confirmation for the same (Figures 37.1–37.8).

### 37.3 UML Diagrams

Actor Specification

1. Admin – Admin will manage the entire system periodically. The function of the admin

extends in ways of adding new books, monitoring book issue and book order details and

finally accepting payment of books.

2. Librarian – Librarian manages the books in the system making available the searched

books by the members. He is the one who checks and accepts the return of books.

3. User – The user or member is the one who gets full access to books either buying or borrowing a book. A member is a registered user of the system who can search their required books.

4. Visitor – Visitor is an unregistered user of the system. A visitor must sign up in to order to

view and search the books.

Usecase Specification

1. Book Borrow

Description: This usecase is used to lend books to the user who wished to borrow.

Flow of Events

Basic Flow: The normal flow is that the member borrows a book from this system.

Alternative Flow: The alternate flow is that if the required book is not available, then the

member may search for the book with a different author.

Figure 37.1 UML usecase diagram.

Pre-Conditions: The conditions to borrow a book is that the user should be a member and

the member should have cleared his previous dues.

Post-Conditions: The condition is that the member should return the book borrowed on

time on receiving the book.

2. Book Issue Details

Description: This usecase function deals with the details of the book that is to be issued.

Flow of Events

Basic Flow: The normal flow is that the book has been successfully issued and displayed.

Alternative Flow: The alternate flow is that book is not available and waiting to be returned

back or added by the admin.

Pre-Conditions: The condition for this usecase is that the book should be available.

Post-Conditions: The condition is that the book once returned should be updated in this

usecase.

3. Book Order

Description: This usecase function is used for placing an order to buy a book.

Flow of Events

Basic Flow: The normal flow is that the book has been ordered successfully.

Alternative Flow: The alternate flow is that the book has not been ordered due to any issues.

Pre-Conditions: The condition is that the user must be a member and should have selected

the required book.

Post-Conditions: The condition is the book should be returned within the specified time.

Figure 37.2 UML activity diagram.

Figure 37.3 UML sequence diagram.

4. Book Order Details

Description: This usecase function displays the details of the books that have been

ordered such as the person who ordered the book, its price etc.

Flow of Events

Basic Flow: The normal flow is that the book has been successfully ordered and detailed.

Alternative Flow: The alternate way is that the book requested is not available then the alternate book is ordered and listed.

Pre-Conditions: The condition is that the person should be a member and have selected his

required book.

Post-Conditions: The condition is that once the book has been returned the details should

be removed.

5. Book Return

Description: This usecase function is used for updating when the person returns the

book.

Flow of Events

Basic Flow: The normal form is that the member returns the book borrowed.

Alternative Flow: The alternate flow is that when the book has not been returned, calculating the appropriate fine amount.

Pre-Conditions: The condition is that the book should be from the library or the system.

Post-Conditions: The condition is that the book borrowed should be returned on time.

Figure 37.4 UML collaboration diagram.

Figure 37.5 UML state chart diagram.

6. Categories

Description: This usecase function displays the books under each category for fast

searching and easy retrieval.

Flow of Events

Basic Flow: The normal flow is that the book has been categorized accordingly.

Alternative Flow: The alternate flow is that the book does not belong to any of the categories.

Pre-Conditions: The condition is that the book should belong to a particular category.

Post-Conditions: The condition is that the book is selected from a category.

Figure 37.6 UML class diagram.

Figure 37.7 UML component diagram.

Figure 37.8 UML deployment diagram.

7. Due Fine Details

Description: This usecase function displays the details of the members who exceeded

their return date and displays the fine amount calculated accordingly.

Flow of Events

Basic Flow: The normal flow is that the due amount of eligible members is displayed.

Alternative Flow: The alternate flow is that the member has not cleared his dues.

Pre-Conditions: The condition is that the member must borrowed a book from the system.

Post-Conditions: The condition is that once the due has been cleared it can be removed

from the list.

8. Home Page

Description: This usecase function is the first screen of the system when the user

successfully logs in.

Flow of Events

Basic Flow: The normal flow is that the books are displayed once the member logs in.

Alternative Flow: The alternate flow is that the user can be as a visitor to enter.

Pre-Conditions: The credentials such as user name and password must be provided to view

the home page

Post-Conditions: The condition is that the member can search for his/her book after the

home page.

9. Login

Description: This usecase function is used as a prerequisite for a user to enter the system.

Each member is provided with a user name and password to log in.

Flow of Events

Basic Flow: The normal flow is to enter the user name and password to log in.

Alternative Flow: The alternate flow is that the user can be a visitor.

Pre-Conditions: The condition is that the user must be a member.

Post-Conditions: The member can select the book if he logs in successfully.

10. Logout

Description: This usecase function is used to leave the system by clicking the logout button available once the member logs in to the system.

Flow of Events

Basic Flow: The normal flow is that the member successfully logs out.

Alternative Flow: The alternate flow is when a network failure occurs.

Pre-Conditions: The condition is that the user should have logged in to the system first.

Post-Conditions: The condition is that the member can log in any other time.

11. Payment

Description: This usecase function is used to buy the selected book using various payment options available.

Flow of Events

Basic Flow: The normal flow is that the book has been successfully placed in an order.

Alternative Flow: The alternate flow is that the book has been not purchased.

Pre-Conditions: The condition is that the book must be from the system and should have a

valid payment option.

Post-Conditions: The condition is that the book is successfully bought by the member.

12. Search Books

Description: This usecase function is used to search books based on author name, id, etc.

Flow of Events

Basic Flow: The normal flow is that the searched results of books are displayed.

Alternative Flow: The alternate flow is that browsing books through various categories.

Pre-Conditions: The condition is that the searched criteria must be a valid one.

Post-Conditions: The condition is that the book can be forwarded for buying or

borrowing.

13. Signup

Description: This usecase function is used for the user to create a membership in the library.

Flow of Events

Basic Flow: It asks the user to input the username, password and email.

Alternative Flow: If the user doesn’t provide correct details the user can visit the system as

a user.

Pre-Conditions: The user must have a unique username, password and email.

Post-Conditions: The user can enter the system as a member.

14. User Details

Description: This functionality deals with the user details.it describes the total users who

are accessing the systems.

Flow of Events

Basic Flow: When the user details are given the user is taken to the home page where he can

access the books.

Alternative Flow: When the user is not registered the user can visit the system as a visitor.

Pre-Conditions: The user must be a member and he must give the perfect details.

Post-Conditions: Whenever the user logins he is taken to the home page where the user can

access the books.

15. With Fine

Description: This functionality says when the user doesn’t return the book ion the time

the user has to pay the fine.

Flow of Events

Basic Flow: The members who exceeded the return date must be displayed with their fine

amount.

Alternative Flow: The members of without fines are displayed.

Pre-Conditions: The user has to return the book with a fine when the user exceeds the due date.

Post-Conditions: The user must pay a fine in order to access the books.

16. Without Fine

Description: The functionality says that the user returns the book without any fine.

Flow of Events

Basic Flow: The system doesn’t show any information about the fine details with respect to

the users.

Alternative Flow: Fine amount is displayed if the user doesn’t return the book with respect

to time.

Pre-Conditions: The book must belong to the system and it should be returned within the

given time.

Post-Conditions: The members can use the book till the due date.

---

## 📊 UML Modeling Suite for Book Bank Management System

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

- **Previous Chapter**: [Design of UML Diagrams for Online Quiz System](Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_System.md)
- **Next Chapter**: [Design of UML Diagrams for Website Development](Chapter_38_Design_of_UML_Diagrams_for_Website_Development.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
