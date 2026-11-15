# Chapter 35: Design of UML Diagrams for GUIDE - Dropshipping Website

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 357–366 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 34: Design of UML Diagrams for Art Gallery Management System](Chapter_34_Design_of_UML_Diagrams_for_Art_Gallery_Management_System.md) | [📚 Book Index](../UML_Book.md) | [Chapter 36: Design of UML Diagrams for Online Quiz System &rarr;](Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_System.md)

---

## 📌 Chapter Overview

Chapter 35 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for GUIDE - Dropshipping Website**. 
This case study presents an end-to-end software engineering analysis for **GUIDE - Dropshipping Website**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **35.1 Problem Statement**
- **35.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 35

Design of UML Diagrams for

GUIDE – Dropshipping

Website

### 35.1 Problem Statement

The students in our college have a lot of unnecessary goods lying around, whereas many other

people might be benefitted from those things. So I would like to put forward a website that can be

used to sell or trade the goods with someone who needs them. It proves to be extremely useful in

cases like buying and trading second- hand books or study materials among students and faculties.

Initially, the website can exclusively only be accessed by the students within the PSG Tech College

campus. Later on, if expected demands are met, it shall be expanded to other colleges. The sellers

are given special accounts in which they are rated based on their previous records with which the

buyers can choose their seller.

Functionalities:

1. The buyer can opt for the payment options with which they control the risk.

2. User- friendly website layout.

3. The buyer gets to inspect the product in front of the seller which ensures customer satisfaction (Figures 35.1–35.8).

### 35.2 UML Diagrams

Actor Specification

1. Administrator – Admin controls the organization of the products and reports the statistics

about the movement of products and goods.

2. Customer – Customers get to view the products and can purchase the products if they want

to. They will be asked to rate the product after a successful purchase.

DOI: 10.1201/9781003287124-35

3. Seller – Seller can add or delete the products he posted. This does not deny him from buyer

products from other sellers with the same account.

Figure 35.1 UML usecase diagram.

Figure 35.2 UML activity diagram.

Figure 35.3 UML sequence diagram.

Usecase Specification

1. Login

Description: Buyer has his/her own username and password. Using this, he/she has to

log in to the system.

Flow of Events

Basic Flow: Allows into the system.

Alternative Flow: Throw an error message.

Pre- Conditions: The username and password should be correct.

Post- Conditions: Nil.

2. Register

Description: The buyer and seller can register for a new account.

Flow of Events

Basic Flow: Adds a new account for the user.

Alternative Flow: Can dismiss the registration for any practical reason.

Pre- Conditions: The username and password should be according to the regulations and

conditions set by the developers.

Post- Conditions: Nil.

3. Message

Description: The buyer and seller can contact each other with the chat functionality.

Flow of Events

Basic Flow: Allows message exchange between users.

Figure 35.4 UML collaboration diagram.

Figure 35.5 UML state chart diagram.

Alternative Flow: Dismiss the message request if not accepted by the seller.

Pre- Conditions: The buyer and seller should mutually accept the deal.

Post- Conditions: Nil.

4. View Product

Description: The buyer can view products that the person wishes to purchase.

Flow of Events

Basic Flow: The users communicate through the chat application and seal the deal.

Alternative Flow: The product will not be sold.

Pre- Conditions: The buyer has to approach the seller quickly.

Post- Conditions: Nil.

5. Verify Login Details

Description: The login details provided by the user is verified in the database.

Flow of Events

Basic Flow: Gets the username and password from the user and cross- check it with the

details in the database.

Alternative Flow: Try another account.

Pre- Conditions: The details given by the buyer should be correct and should be accepted by

admin.

Post- Conditions: Nil.

6. Login Error

Description: If the details provided by the user does not match the details in the database, then this throws an error.

Figure 35.6 UML class diagram.

Flow of Events

Basic Flow: Verifies details and throws and errors if the provided conditions are not met.

Alternative Flow: Nil.

Pre- Conditions: Wrong information must be provided to invoke the error.

Post- Conditions: Nil.

7. Help

Description: The users can surf through FAQs and also post questions to which answers

will be provided by our team.

Flow of Events

Basic Flow: The users can click on a link to visit the page to answer all their questions.

Alternative Flow: Nil.

Pre- Conditions: Nil.

Post- Conditions: Nil.

8. Delete Products

Description: The seller can delete the products they listed if they don’t want to sell the

product.

Flow of Events

Basic Flow: Sellers have the access to delete their uploaded products.

Figure 35.7 UML component diagram.

Alternative Flow: Nil.

Pre- Conditions: The seller should have some products queued for selling.

Post- Conditions: Nil.

9. Add Product

Description: The seller can add a product for selling.

Flow of Events

Basic Flow: Can add products for selling.

Alternative Flow: Nil.

Pre- Conditions: The seller should have an account. This avoids technical issues.

Post- Conditions: Nil.

10. Purchasing Products

Description: The buyer can pay a fair price for the products.

Flow of Events

Basic Flow: Paying the seller for their products.

Alternative Flow: Nil.

Pre- Conditions: The offer must be above the price set by the seller.

Post- Conditions: Nil.

11. Rate Products

Description: The buyer can rate their experience of the purchase with respect to the

product quality and seller response.

Flow of Events

Basic Flow: Rating the seller interaction.

Alternative Flow: They can skip from rating the product.

Pre- Conditions: A successful purchase should be made.

Post- Conditions: Nil.

Figure 35.8 UML deployment diagram.

12. Money Transaction

Description: The customer pays the seller through external means mediated by the chat

application.

Flow of Events

Basic Flow: Chat functionality can modulate the payment method both the users can agree

upon.

Alternative Flow: Nil.

Pre- Conditions: The seller should be satisfied with the price.

Post- Conditions: Nil.

13. Organize Product Categories

Description: The administrator organizes the product categories that may sometimes be

included in the wrong categories by the seller.

Flow of Events

Basic Flow: It allows the administrator to shift products from one category to another.

Alternative Flow: Nil.

Pre- Conditions: The product should be input in the wrong categories.

Post- Conditions: Nil.

14. Report Statistics

Description: The administrator prepares statistics based on pre- defined criteria.

Flow of Events

Basic Flow: The administrator prepares statistics.

Alternative Flow: Nil.

Pre- Conditions: Purchases of products should have been carried out.

Post- Conditions: Nil.

---

## 📊 UML Modeling Suite for GUIDE - Dropshipping Website

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

- **Previous Chapter**: [Design of UML Diagrams for Art Gallery Management System](Chapter_34_Design_of_UML_Diagrams_for_Art_Gallery_Management_System.md)
- **Next Chapter**: [Design of UML Diagrams for Online Quiz System](Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
