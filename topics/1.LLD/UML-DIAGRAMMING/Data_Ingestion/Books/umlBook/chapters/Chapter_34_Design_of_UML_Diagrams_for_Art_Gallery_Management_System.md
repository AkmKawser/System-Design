# Chapter 34: Design of UML Diagrams for Art Gallery Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 349–356 (Total: 8 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 33: Design of UML Diagrams for Green Rides](Chapter_33_Design_of_UML_Diagrams_for_Green_Rides.md) | [📚 Book Index](../UML_Book.md) | [Chapter 35: Design of UML Diagrams for GUIDE - Dropshipping Website &rarr;](Chapter_35_Design_of_UML_Diagrams_for_GUIDE_Dropshipping_Website.md)

---

## 📌 Chapter Overview

Chapter 34 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Art Gallery Management System**. 
This case study presents an end-to-end software engineering analysis for **Art Gallery Management System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **34.1 Problem Statement**
- **34.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 34

Design of UML

Diagrams for Art Gallery

Management System

### 34.1 Problem Statement

To provide an online platform to manage the buying, selling and storage of artistic creations provided by creators/other platforms or auctions and to organize events to exhibit these products. The

system is a gallery having art pieces with its description, price and other information and the order

activity, payment activity, order update activity and so on. The objective is to provide an online platform through which museums and art galleries can make use-off to exhibit their collections in times

of unavailable street galleries. Like in times of pandemic also people need not bother not going to a

museum or art gallery instead they can have online art shopping and art exhibits. The system should

be immune to any chances of misuse and unauthorized reproduction of works of arts and designs.

There will be two types of users accessing the system: Admin (Creators/authority of the art displayed)

and Customer (One who looks to buy the art). The main features provided for the admin are that

they will be able to update, add, delete, input price, description and information about an art (stock

availability), generate report of gallery and that for the customers are that they will be able to order

(Payment), delete order, view end-user projected art particulars (Figures 34.1–34.8).

### 34.2 UML Diagrams

Actor Specification

1. Admin – The person who has full access to the system and is responsible for all activities of

the system.

2. Customer – People who use the system for either buying or referring.

3. Delivery Person – The person who takes out orders of the customers to them.

4. System User – The people who own the art that is put in the system.

DOI: 10.1201/9781003287124-34

Usecase Specification

1. Buy Art

Description: Leads the customer to the process of buying the art they desire.

Flow of Events

Alternative Flow: Users can just make use of the system for viewing the items in the gallery

and not necessarily buy anything.

Pre-Conditions: The user should have properly logged in and should have checked for stock

availability.

Post-Conditions: Nil.

Figure 34.1 UML usecase diagram.

Figure 34.2 UML activity diagram.

Figure 34.3 UML sequence diagram.

Figure 34.4 UML collaboration diagram.

Figure 34.5 UML state chart diagram.

2. Cash on Delivery

Description: Final stage of the system.

Flow of Events

Alternative Flow: Can make use of any online payment mode.

Pre-Conditions: A person should have ordered for the delivery of an item.

Post-Conditions: Nil.

Figure 34.6 UML class diagram.

Figure 34.7 UML component diagram.

3. Change Info

Description: Allows the user to keep an updated profile.

Flow of Events

Alternative Flow: Can keep the information unchanged.

Pre-Conditions: Should have created an account prior.

Post-Conditions: Nil.

4. Display Login Error

Description: Checks for login details entered by the user while logging in and displays

if incorrect.

Flow of Events

Alternative Flow: User could have the details entered correctly.

Pre-Conditions: The user should have entered login details.

Post-Conditions: Nil.

5. Login & Logout

Description: Allows the user to login and logout of the system.

Flow of Events

Alternative Flow: Can create an account.

Pre-Conditions: This is the first step to use the system. The user should have an account to

login and out of the system.

Post-Conditions: Nil.

6. Maintain Profile Info

Description: Allows the user to keep a profile.

Flow of Events

Alternative Flow: Can keep the information unchanged.

Pre-Conditions: Should have created an account in prior.

Post-Conditions: Nil.

Figure 34.8 UML deployment diagram.

7. Make Payment

Description: Allows the user to make payment in order to buy an item.

Flow of Events

Alternative Flow: User can opt for cash on delivery or net payment.

Pre-Conditions: User should have selected an item from the system to buy.

Post-Conditions: Nil.

8. Manage Art Stock

Description: Keeps the system updated with new stocks.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Should be available to be put to display.

Post-Conditions: Nil.

9. Manage Arts

Description: Keeps the system updated with existing stocks (like the availability, quality,

delivery time, etc.).

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Should be already existing in the system.

Post-Conditions: Nil.

10. Manage Customers

Description: Maintains the records of the customers.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: The customer should have logged in and out at least once.

Post-Conditions: Nil.

11. Manage Deliver

Description: Should assure that the correct order is delivered to the correct customer.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: The customer should have ordered something.

Post-Conditions: Nil.

12. Manage Order

Description: Should be able to satisfy or complete an order.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: An art should have its values.

Post-Conditions: Nil.

13. Manage Order Update

Description: Updates the order tracks.

Flow of Events

Alternative Flow: Order should be appropriately cancelled.

Pre-Conditions: The order should be taken out for delivery.

Post-Conditions: Nil.

14. Manage Users and Full System

Description: Maintains complete system from end to end.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Should be given authority.

Post-Conditions: Nil.

15. Net Payment

Description: Allows customers to pay online.

Flow of Events

Alternative Flow: User can opt for cash on delivery.

Pre-Conditions: Customer should select an item to buy.

Post-Conditions: Nil.

16. Verification of Order

Description: Makes sure that the correct order is delivered to the correct customer.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Someone must have made an order.

Post-Conditions: Nil.

17. View Address

Description: Makes sure the order is delivered to the correct customer.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Someone must have made an order.

Post-Conditions: Nil.

18. View Customer Profile

Description: Allows the delivery person to view customer profiles for any reference.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: Someone must have made an order.

Post-Conditions: Nil.

19. View Product

Description: Allows the user to view any product available in the system.

Flow of Events

Alternative Flow: Nil.

Pre-Conditions: User should have logged in.

Post-Conditions: Nil.

---

## 📊 UML Modeling Suite for Art Gallery Management System

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

- **Previous Chapter**: [Design of UML Diagrams for Green Rides](Chapter_33_Design_of_UML_Diagrams_for_Green_Rides.md)
- **Next Chapter**: [Design of UML Diagrams for GUIDE - Dropshipping Website](Chapter_35_Design_of_UML_Diagrams_for_GUIDE_Dropshipping_Website.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
