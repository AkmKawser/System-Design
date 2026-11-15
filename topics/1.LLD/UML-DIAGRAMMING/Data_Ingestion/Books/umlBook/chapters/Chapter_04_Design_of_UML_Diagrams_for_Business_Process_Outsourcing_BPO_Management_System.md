# Chapter 04: Design of UML Diagrams for Business Process Outsourcing (BPO) Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 59–74 (Total: 16 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 03: Design of UML Diagrams for Inventory Management System](Chapter_03_Design_of_UML_Diagrams_for_Inventory_Management_System.md) | [📚 Book Index](../UML_Book.md) | [Chapter 05: Design of UML Diagrams for E-Ticketing for Buses &rarr;](Chapter_05_Design_of_UML_Diagrams_for_E_Ticketing_for_Buses.md)

---

## 📌 Chapter Overview

Chapter 4 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Business Process Outsourcing (BPO) Management System**. 
This case study presents an end-to-end software engineering analysis for **Business Process Outsourcing (BPO) Management System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **4.1 Problem Statement**
- **4.2 Functional Requirements**
- **4.3  Design and Design Constraints**

---

## 📝 Detailed Chapter Summary & Content

Chapter 4

Design of UML Diagrams for

Business Process Outsourcing

(BPO) Management System

### 4.1 Problem Statement

The proposed software will be user-friendly, so that all interactions between a BPO (Business process outsourcing) organization and clients can be done through the software. The required source

documents can be easily uploaded and sent to the BPO organization and vice versa. One of the

problems is the communication between the client and the BPO organization being limited to

face-to-face interaction for assurance, which is costly and time-consuming. There are costs due to

printing and the security of documents, which can be prevented as document are stored in digital form with high security. The system should mainly focus on providing login for the separate

users (client and BPO organization), and a facility to search the other party to initiate any project

agreements. Source documents can be easily uploaded, and the service provided by the BPO organization can also be uploaded for quality testing. The core motive of the software is to provide

communication between the users, with the least cost. The BPO management system proves to

be essential because of the over growth of the BPO segment in the present economy. This system

will be crucial when organizations wish to outsource their work. It will affect the BPO organizations and the clients who wish to seek their service. If this software gets implemented, conveying

information will be easier as it is through the internet.

### 4.2 Functional Requirements

Login – provides a personalized profile for each user, to ensure security. Profile changes – each user

can personalize their account, and change their password. Post project request – clients post their

request with requirements for BPO organizations to choose from. Search project requests – BPO

organizations can search and respond to the requests. Upload source documents – the documents

required by the BPO organization can be transferred through the system, and the receiver can

DOI: 10.1201/9781003287124-4

download them. Check progress – clients should be constantly updated with the progress of the

work. Quality check and testing – the clients can check their product and quote any modifications. Upload product/service – BPO organization should upload their product/service for the

further procedure (payment, shipment, etc.). Payment – clients should pay the BPO organization

at the end of their agreement. Shipment – the product/service should be delivered to the clients.

Rating – the clients can rate the service provided by the BPO organization (Figures 4.1–4.19).

### 4.3 Design and Design Constraints

Usecase Specification

1. Accept Request

Description: It allows BPO organization to accept the request.

Flow of Events

Basic Flow: BPO organization accepts the request and thereby initiates the deal.

Figure 4.1 Login page.

Figure 4.2 Client profile – Upload request.

Alternative Flow: BPO organization can search for other clients.

Pre-Conditions: The client should post a request.

Post-Conditions: It should be added into the current deals.

2. Card

Description: It is sub-usecase of payment, where this method can be chosen in case the

client wishes to pay by card.

Flow of Events

Basic Flow: The final amount of money will be displayed, and once paid; the BPO organization can verify the status of the agreement to ‘paid’.

Alternative Flow: The BPO can sue the client using the evidence of their agreement from

the database.

Pre-Conditions: Previous procedures, such as upload the final product and quality check

must be completed.

Post-Conditions: The status of the agreement should be updated in the database as ‘paid’ or

‘completed’.

Figure 4.3 Client profile – Current deals.

Figure 4.4 Client profile – Search BPO Organization.

3. Cash

Description: It is sub-usecase of payment, where this method can be chosen in case the

client wishes to pay by cash.

Flow of Events

Basic Flow: The final amount of money will be displayed, and once paid, the status of the

agreement will be updated.

Alternative Flow: The BPO can sue the client using the evidence of their agreement from

the database.

Pre-Conditions: Previous procedures, such as upload the final product and quality check

must be completed.

Post-Conditions: The status of the agreement should be updated in the database as ‘paid’ or

‘completed’.

Client

BPOo rganization

System

Registration

<<include>>

Profile Login

<<extend>>

<<extend>>

<<extend>>

<<extend>> <<extend>>

Search users

Upload Request

Edit profile <<extend>>

<<include>> CurrentD eals

<<include>> Filter by rating

<<extend>>

Accept request Filter by category

<<extend>>

Change password Contactu ser

<<extend>>

<<include>>

Upload finalp roduct

Upload finalp roduct

Trackp rogress

<<include>>

Qualityc heck

Cash<<include>>

Payment

Payment

Card

<<include>>

Shipment

<<include>>

Rating

Figure 4.5 UML usecase diagram.

4. Change Password

Description: This allows you to change your password.

Flow of Events

Basic Flow: The user can change their password for security purposes.

Alternative Flow: They can stick with their old password itself.

Pre-Conditions: They should enter into their profile page.

Post-Conditions: Changes should be updated in the database successfully.

5. Contact User

Description: This provides a communication between users.

Flow of Events

Basic Flow: The users are allowed to communicate with each other.

Alternative Flow: Try alternate methods of contacting.

Pre-Conditions: Contact details should be available for users.

Post-Conditions: None.

6. Current Deals

Description: The users are allowed to view all of their deals.

Flow of Events

Basic Flow: The users can view their pending and completed deals.

Alternative Flow: They can contact the other user involved in the deal.

Pre-Conditions: The user should have at least one deal to view.

Post-Conditions: They can track the progress of the pending deals.

7. Edit Profile

Description: The users are allowed to edit their profiles.

Flow of Events

Basic Flow: The user can edit their profile and save the changes.

Figure 4.6 UML class diagram.

Alternative Flow: They can just view the profile.

Pre-Conditions: They should enter into the profile page.

Post-Conditions: Changes should be updated to the database successfully.

8. Filter by Category

Description: This is a sub-usecase of searching users, where the users can be filtered by

category (finance, etc.).

Flow of Events

Basic Flow: The category type should be specified by the user and that category will be compared with the database to retrieve the required users.

Alternative Flow: The user can filter by rating or can view all users without any filters.

Pre-Conditions: The user should have an authenticated profile by registering in the system

to search other profiles.

Post-Conditions: The user can contact any other user.

Figure 4.7 UML activity diagram (part 1).

Figure 4.8 UML activity diagram (part 2).

Figure 4.9 UML activity diagram (part 3).

9. Filter by Rating

Description: This is a sub-usecase of searching users, where the users can be filtered by

rating value, which ranges between 0 and 5 stars.

Flow of Events

Figure 4.10 UML activity diagram (part 4).

Basic Flow: The range of rating should be specified by the user and that rating range will be

compared with the database to retrieve the required users.

Alternative Flow: User can filter by category or can view all users without any filters.

Pre-Conditions: User should have an authenticated profile by registering in the system to

search other profiles.

Post-Conditions: The user can contact any other user.

Figure 4.11 UML activity diagram (part 5).

Figure 4.12 UML collaboration diagram.

Figure 4.13 UML sequence diagram.

Figure 4.14 UML state machine diagram (part 1).

10. Login

Description: The users are allowed to login.

Flow of Events

Basic Flow: The user can login to the system with a valid username and password.

Alternative Flow: They can register as a fresh user.

Pre-Conditions: They should be an authenticated user to login.

Post-Conditions: Basic details of the user will be retrieved to be displayed on all the othe

sections using username.

r

11. Payment

Description: At the end of the deal, the client should pay the BPO organization for their

service, which will be provided by this functionality.

Flow of Events

Figure 4.15 UML state machine diagram (part 2).

Figure 4.16 UML state machine diagram (part 3).

Basic Flow: The client will choose the method of payment, provide the necessary details to

complete the transaction.

Alternative Flow: The BPO can sue the client using the evidence of their agreement from

the database.

Figure 4.17 UML state machine diagram (part 4).

Figure 4.18 UML component diagram.

Pre-Conditions: Previous procedures, such as upload the final product and quality check

must be completed.

Post-Conditions: The status of the agreement should be updated in the database as ‘paid’.

12. Profile

Description: The user can view their basic provided details in the profile view

Flow of Events

Basic Flow: The username from login will be used to compare in the database to retrieve the

basic details and display them in the profile.

Alternative Flow: They can choose to do other functionalities like change password, search

users, etc.

Pre-Conditions: User should have an authenticated profile by registering in the system.

Post-Conditions: No changes will be made as it is only displayed functionality.

13. Quality Check

Description: The client should be able to check the quality of the product before proceeding to payment.

Flow of Events

Basic Flow: The uploaded final product from the BPO organization can be retrieved and

reviewed for quality and testing.

Alternative Flow: Quality and testing can be skipped to the payment procedure at the end.

Pre-Conditions: BPO organization should upload documents of the final product.

Post-Conditions: Comments from the client should be sent to the BPO organization.

14. Rating

Description: One user can rate the other user’s service based on their previous dealings.

Flow of Events

Basic Flow: At the end of the deal, the two users involved in the agreement should rate the

other on a rating of 5 based on their service.

Alternative Flow: The user can choose to rate later or ignore.

Pre-Conditions: The status of agreement should be closed – payment and shipment stages

should be completed

Post-Conditions: The rating given should be averaged with previous ratings and stored in

database for data retrieval when displaying.

Figure 4.19 UML deployment diagram.

15. Registration

Description: The user should be registered to have a profile in the system

Flow of Events

Basic Flow: Basic details are collected from the user and an account will be created with a

profile as per the details they have provided.

Alternative Flow: Contact developers for more information.

Pre-Conditions: Should be a valid user, who will be affected by the system.

Post-Conditions: The provided basic details about the user should be stored in the database.

16. Search Users

Description: Among the two user types, client and BPO organization, and they can

search the other.

Flow of Events

Basic Flow: All the users of the other user type should be searched and displayed from the

database.

Pre-Conditions: User should have an authenticated profile by registering in the system to

search other profiles.

Post-Conditions: The user can contact the other user.

17. Shipment

Description: The product after payment can be shipped from the BPO organization to

the client as per the client’s wish.

Flow of Events

Basic Flow: The status of payment should be verified, then the product is collected from the

BPO organization and delivered to the client.

Alternative Flow: The client and BPO organization can have their methods of shipment and

skip this procedure.

Pre-Conditions: Payment procedure should be done (verified either by cash or card).

Post-Conditions: The status of the agreement should be updated in the database as ‘completed’.

18. Track Progress

Description: The client can track the progress of their product or service that has been

service.

Flow of Events

Basic Flow: BPO organization should constantly update the status of their progress so that

the client can view them.

Alternative Flow: Previous updates of progress should be displayed in case the BPO organization fails to give a recent update.

Pre-Conditions: BPO organization and the client should agree with the request.

Post-Conditions: The current status of BPO organization with respect to the service should

be updated in database.

19. Upload Request

Description: This allows the client to post a request

Flow of Events

Basic Flow: The clients will have to enter the category, due date and description of their

request along with an uploaded document.

Alternative Flow: Contact BPO organization and deal directly.

Pre-Conditions: Client should be a registered user.

Post-Conditions: Request information and ID should be stored in the database.

20. Upload Final Product

Description: It will allow the BPO organization to upload their end product/service for

further procedures (quality check, payment, shipment).

Flow of Events

Basic Flow: BPO organization can upload necessary documents.

Alternative Flow: Contact client and extend due date to upload final product

Pre-Conditions: BPO organization and the client should be in agreement with the request.

Post-Conditions: The document will be stored in database.

---

## 📊 UML Modeling Suite for Business Process Outsourcing (BPO) Management System

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

- **Previous Chapter**: [Design of UML Diagrams for Inventory Management System](Chapter_03_Design_of_UML_Diagrams_for_Inventory_Management_System.md)
- **Next Chapter**: [Design of UML Diagrams for E-Ticketing for Buses](Chapter_05_Design_of_UML_Diagrams_for_E_Ticketing_for_Buses.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
