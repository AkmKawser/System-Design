# Chapter 09: Design of UML Diagrams for Online Marketplace

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 113–122 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 08: Design of UML Diagrams for DigiDocLocker](Chapter_08_Design_of_UML_Diagrams_for_DigiDocLocker.md) | [📚 Book Index](../Overall_Books.md) | [Chapter 10: Design of UML Diagrams for Product Recommendation System &rarr;](Chapter_10_Design_of_UML_Diagrams_for_Product_Recommendation_System.md)

---

## 📌 Chapter Overview

Chapter 9 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Online Marketplace**. 
This case study presents an end-to-end software engineering analysis for **Online Marketplace**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **9.1 Problem Statement**
- **9.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 9

Design of UML Diagrams

for Online Marketplace

### 9.1 Problem Statement

Various new small scale and medium scale sellers face difficulties to reach out to the customers and

sell their products along with other competing products in the market. This increases their overall

cost, thus reducing their profit or even causing loss. E-Retail is an online marketplace application

case study where small and medium scale sellers can list, showcase, advertise and sell their products directly to the customers without any physical store. E-Retail aims in providing a dynamic

platform for all small and medium scale sellers to reach out and sell their products directly to

all range of customers at a competing price without the need of any physical store. This enables

the sellers to eliminate the cost of rent or maintenance of a physical store and to minimize other

related costs. It also aims in promoting direct communication between the seller and customer,

hence providing a trusted relationship between them. New sellers can easily authenticate and

signup to the portal and sell their products in the portal. The application offers separate login for

sellers and customers, where the sellers and customers can sign in and start using the application.

Customers can view all the products available from various sellers and buy those products. It also

facilitates online payments for purchasing the products. Customers can rate or give a review for the

product and seller. Customers can also report a seller for any violations in delivery or if the product

does not meet the specified requirement. Customers can also view the contact information and the

rating of the seller before buying the product (Figures 9.1–9.9).

DOI: 10.1201/9781003287124-9

### 9.2 UML Diagrams

Actor Specification

1. Admin – Admin authenticates the new customers logging in to the system and verifies the

new seller that registers to the system. Admin also verifies the reports issued by the customers against the sellers.

2. Customers – Customers are the users who logins into the system, to view and buy products

sold by different sellers in the application.

3. Payment Service Provider – Payment service providers act as a mediator between merchants, customers, card brand networks and other financial institutions to process the electronic payment transactions in the application.

4. Sellers – Sellers are small or medium scale businesses, who can sell their products directly

to potential customers using the applications.

Usecase Specification

1. Customer Login

Description: Each customer has to login to the system using a username and password

for using the application.

Flow of Events

Basic Flow: Authenticates the user and grants access to the system.

Alternative Flow: Invalid username and password, try correct username and password.

Pre-Conditions: Valid username and password.

Post-Conditions: Nil.

Figure 9.1 UML usecase diagram.

2. Seller Registration

Description: Each Seller has to register themselves in the system to sell their products.

Flow of Events

Basic Flow: Sellers register with valid credentials.

Alternative Flow: Invalid credentials and retry.

Pre-Conditions: Valid credentials.

Post-Conditions: The registered seller is authenticated and they are verified.

3. Seller Verification

Description: After registration, each seller is verified before being able to sell.

Flow of Events

Basic Flow: The registered seller is verified and they can sell their products.

Alternative Flow: Verification of the seller is failed and they cannot sell their products.

Pre-Conditions: Each seller must be registered.

Post-Conditions: Nil.

Figure 9.2 UML activity diagram (part 1).

4. Sale Products

Description: Verified Sellers can showcase their products for sale.

Flow of Events

Basic Flow: Sellers list their products along with their description and price.

Alternative Flow: Sellers unable to sell the products.

Pre-Conditions: Sellers must be verified before listing the products for sale.

Post-Conditions: Nil.

5. Promote Products

Description: Sellers can promote their products listed for sale.

Flow of Events

Basic Flow: Sellers promoting their products

Alternative Flow: Sellers unable to promote their products

Pre-Conditions: The Seller must be verified and should list their product for sale before

promoting it.

Post-Conditions: Promoted products are displayed on the home page.

6. View Products

Description: Customers can view all the products listed for sale from various sellers.

Flow of Events

Basic Flow: Customers viewing the products available.

Alternative Flow: Products unavailable to view.

Pre-Conditions: Customer must be logged in.

Post-Conditions: Customers can select a product to buy that product.

Figure 9.3 UML activity diagram for sub-activity make payment.

Figure 9.4 UML sequence diagram.

Figure 9.5 UML collaboration diagram.

Figure 9.6 UML state machine diagram.

Figure 9.7 UML class diagram.

7. Search Products

Description: Customers can search for products using keywords.

Flow of Events

Basic Flow: Displays list of products available for the searched keyword.

Alternative Flow: No products available for the searched keyword.

Pre-Conditions: Customer must be logged in.

Post-Conditions: Searched products can be selected to view and buy.

8. Buy Products

Description: Customers can buy the product available.

Flow of Events

Basic Flow: Check out and buy the product.

Alternative Flow: Product unavailable for sale.

Pre-Conditions: Customer must be logged in.

Post-Conditions: Customers are asked for payment to buy the product.

9. Make Payment

Description: Customers are asked for a payment option after checkout

Flow of Events

Basic Flow: Customers are provided with the corresponding payment gateway for the

selected payment option in case of digital payment. Customers are asked for the delivery

address in case of Pay on Delivery.

Alternative Flow: Selected Payment option is unavailable.

Pre-Conditions: Customer must choose to buy the product.

Post-Conditions: Product purchase is updated and the order details are sent to the customer.

Figure 9.8 UML component diagram.

10. Credit/Debit Card

Description: Products can be purchased using Credit/Debit card for payment.

Flow of Events

Basic Flow: Credit/Debit card payment is successful.

Alternative Flow: Credit/Debit card payment is unsuccessful.

Pre-Conditions: Customers must choose to make payments through Credit/Debit card.

Post-Conditions: Payment details are updated.

11. Net Banking

Description: Products can be purchased by using net banking for payment.

Flow of Events

Basic Flow: Net Banking payment is successful

Alternative Flow: Net Banking payment is unsuccessful

Pre-Conditions: Customers must choose to make payment through net banking.

Post-Conditions: Payment details are updated.

Figure 9.9 UML deployment diagram.

12. Pay on Delivery

Description: Customers can make the payment at the time of delivery.

Flow of Events

Basic Flow: Selects delivery address and proceed.

Alternative Flow: Pay on Delivery is unavailable.

Pre-Conditions: Customers must have a delivery address and choose for Pay on Delivery

option.

Post-Conditions: Payment details are updated after payment is made at the time of delivery.

13. Rating and Review

Description: Customers can share their reviews and ratings for the purchased product.

Flow of Events

Basic Flow: Customers rate and review the product.

Alternative Flow: Customers skip rating and reviewing the product.

Pre-Conditions: Customer must have bought the product.

Post-Conditions: Rating and review of the product are updated.

14. Chat

Description: Customers can chat with the Seller to enquire on their products.

Flow of Events

Basic Flow: Customers sends messages to sellers and sellers reply to the messages sent.

Alternative Flow: Nil.

Pre-Conditions: Customer must be logged in and the Seller must be a verified seller.

Post-Conditions: Nil.

15. Report Seller

Description: Customer can report a seller if their sold product does not meet the specified requirement.

Flow of Events

Basic Flow: Customer reports the seller with description.

Alternative Flow: Nil.

Pre-Conditions: Customer must have bought the product from the reported seller.

Post-Conditions: The report is sent to the corresponding seller for explanation. Frequent

reports against specific sellers can remove the seller from the portal.

---

## 📊 UML Modeling Suite for Online Marketplace

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

- **Previous Chapter**: [Design of UML Diagrams for DigiDocLocker](Chapter_08_Design_of_UML_Diagrams_for_DigiDocLocker.md)
- **Next Chapter**: [Design of UML Diagrams for Product Recommendation System](Chapter_10_Design_of_UML_Diagrams_for_Product_Recommendation_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/Overall_Books.md`](../Overall_Books.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
