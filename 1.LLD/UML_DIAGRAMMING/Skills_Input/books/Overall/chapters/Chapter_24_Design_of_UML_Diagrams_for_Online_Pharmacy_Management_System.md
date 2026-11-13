# Chapter 24: Design of UML Diagrams for Online Pharmacy Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 247–264 (Total: 18 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 23: Design of UML Diagrams for AAROGYA SETU - Health Care APP](Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP.md) | [📚 Book Index](../README.md) | [Chapter 25: Design of UML Diagrams for EQUIHEALTH &rarr;](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md)

---

## 📌 Chapter Overview

Chapter 24 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Online Pharmacy Management System**. 
This case study presents an end-to-end software engineering analysis for **Online Pharmacy Management System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **24.1 Problem Statement**
- **24.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 24

Design of UML Diagrams

for Online Pharmacy

Management System

### 24.1 Problem Statement

The customer goes to the shop and purchases the medicine required. So a lot of time is wasted

and the person gets tired. If he wants to exchange the product, once again he goes to the shop and

replaces them. The complete process depends on the physical interactions. The Online Pharmacy

is easy to use and order. The customer selects the required medicines and orders them with a single

click. Before it, the customer needs to create a login account and fill all the details like name,

address, any id no, etc. The client can able to view the status of the medicines. The business goal

for the application is to provide the medicines to all the people and admin will provide the supplier

details (Figures 24.1–24.20).

### 24.2 UML Diagrams

Actor Specification

1. Customer – He/she can create an account to order/view medicines online.

2. Admin – He/she can view, update medicines availability based on the needs. He/she can

view customer details and can update delivery man attendance.

3. Delivery Man – He can view the address to be delivered, he can update/view his profile his

attendance.

Usecase Specification

1. Login

Description: It allows the customer to login into the page.

Flow of Events

DOI: 10.1201/9781003287124-24

Basic Flow: Login into the page.

Alternate Flow: Requests to create a login for the new customers.

Pre-Conditions: The customer should already have an account to login.

Post-Conditions: It directs to the home page.

2. Register

Description: It allows the customer to create an account.

Flow of Events

Basic Flow: Creates an account.

Alternate Flow: Already registered customers can login directly.

Pre-Conditions: All the required details should be mentioned to create an account.

Post-Conditions: After registration, it directs to the login page.

3. Account/Profile Information

Description: Customer can edit their information.

Flow of Events

Figure 24.1 UML usecase diagram.

Figure 24.2 UML activity diagram – User.

Basic Flow: Can edit/update the information.

Alternative Flow: Can view the information.

Pre-Conditions: Valid information has to be mentioned by the customers.

Post-Conditions: It directs to the home page.

4. View Orders

Description: Customers can view the orders they have selected.

Flow of Events

Basic Flow: Customer can add/delete products.

Alternative Flow: It directs to the homepage.

Pre-Conditions: It displays the number of orders that have been added.

Post-Conditions: It directs to the wish list page or to the cart page.

5. Add to Wish List

Description: Customers can wish to list a product of their choice.

Flow of Events

Basic Flow: Wish lists a product of customer choice.

Alternative Flow: It redirects to the homepage.

Pre-Conditions: It displays the wish-listed products of customer’s choice.

Post-Conditions: It directs to the home page.

6. Add to Cart

Description: It displays the products added to the cart by customers.

Flow of Events

Figure 24.3 UML activity diagram – Admin.

Basic Flow: It displays the product in the cart.

Alternative Flow: It redirects to the view orders page.

Pre-Conditions: Items must be added to the cart to order them.

Post-Conditions: It directs to the view orders page or to the order confirm or order cancel

option.

Figure 24.4 UML activity diagram – Delivery Man.

7. Order Confirm

Description: It displays the confirmed orders by the customers.

Flow of Events

Basic Flow: Orders confirmed are displayed.

Alternative Flow: It redirects to the cart page.

Pre-Conditions: There must be at least one order to confirm it.

Post-Conditions: It directs to the update delivery info page.

8. Order Cancel

Description: It provides an option to delete the orders confirmed by the customers.

Flow of Events

Basic Flow: It cancels the orders.

Alternative Flow: It redirects to the cart page.

Pre-Conditions: There must be at least one order to cancel it.

Post-Conditions: It directs to the cart page.

Figure 24.5 UML sequence diagram – Customer.

Figure 24.6 UML sequence diagram – Admin.

Figure 24.7 UML sequence diagram – Delivery Man.

9. Update Delivery Info

Description: The customer can update the delivery address where the products are to be

delivered.

Flow of Events

Basic Flow: Delivery information has to be updated.

Alternative Flow: It redirects to the order confirmation page.

Pre-Conditions: Address to be mentioned in order to deliver the products.

Post-Conditions: It directs to the track order/payment page.

Figure 24.9 UML collaboration diagram – Admin.

Figure 24.10 UML collaboration diagram – Delivery Man.

Figure 24.8 UML collaboration diagram – Customer.

Figure 24.11 UML state machine diagram – Customer.

Figure 24.12 UML state machine diagram – Admin.

10. Track Orders

Description: This page allows the customer to track their orders.

Flow of Events

Basic Flow: It requires the order to display the tracking option.

Alternative Flow: It directs to the payment/update delivery info page.

Pre-Conditions: It requires order to track them.

Post-Conditions: It directs to the update delivery info page.

Figure 24.13 UML State machine diagram – Delivery Man.

Figure 24.14 UML class diagram – Customer.

Figure 24.15 UML class diagram – Admin.

11. Payment

Description: This page allows the customer to pay for the ordered products.

Flow of Events

Basic Flow: It requires the payment details.

Alternative Flow: It directs to update delivery info page.

Pre-Conditions: It requires payment details to proceed.

Post-Conditions: It directs to the Net banking or COD page.

Figure 24.16 UML class diagram – Delivery Man.

Figure 24.17 UML component diagram – Customer.

12. Net Banking

Description: It allows to update the bank details for the payment.

Flow of Events

Basic Flow: It requires bank details.

Alternative Flow: It directs to the payment page.

Pre-Conditions: It requires bank details.

Post-Conditions: Once payment is successful, it directs to the homepage.

13. COD

Description: It provides an option for the customers to pay at the time of delivery.

Flow of Events

Basic Flow: It provides an option for pay on delivery.

Alternative Flow: It directs to the payment page.

Pre-Conditions: It requires confirmation on orders in order to pay on delivery.

Post-Conditions: It directs to the payment page.

Figure 24.18 UML component diagram – Admin.

Figure 24.19 UML component diagram – Delivery Man.

14. View Users

Description: Admin can view the users who logged in into the page.

Flow of Events

Basic Flow: It allows to view the users who are currently logged in into the system.

Alternative Flow: It directs to the home page.

Pre-Conditions: He/she must be an admin to view the users.

Post-Conditions: It directs to the home page.

15. Update Medicine

Description: Admin can view the number of medicines available and update them on

the website.

Flow of Events

Basic Flow: Allows to update the medicine.

Alternative Flow: It directs to the home page.

Pre-Conditions: Update the medicines.

Post-Conditions: It directs to the home page.

16. Add/Delete Medicine

Description: It allows the admin to add/delete medicines based on the quantity available.

Flow of Events

Basic Flow: Adding/deleting the medicines.

Alternative Flow: It redirects to the update medicine page.

Pre-Conditions: It adds/deletes the medicines.

Post-Conditions: It redirects to the update medicine page.

17. Maintain Orders

Description: It allows the admin to maintain orders.

Flow of Events

Basic Flow: Admin maintains the orders ordered by the customer.

Alternative Flow: It redirects to the home page.

Pre-Conditions: There must be some orders to maintain them.

Post-Conditions: It redirects to the home page.

Figure 24.20 UML deployment diagram.

18. View Delivery Address

Description: It allows the admin to view the address of the customers.

Flow of Events

Basic Flow: View the address of the customers.

Alternative Flow: It redirects to the home page.

Pre-Conditions: Admin can view the address.

Post-Conditions: It redirects to the home page.

19. View Delivery Man Info

Description: It allows the admin to view the information about the delivery man.

Flow of Events

Basic Flow: View the info about the delivery man.

Alternative Flow: It redirects to the home page.

Pre-Conditions: It must contain the info about the delivery man in order to view them.

Post-Conditions: It redirects to the home page.

20. Update Salary

Description: It allows the admin to update the salary for the delivery man.

Flow of Events

Basic Flow: Updating salary for the delivery man.

Alternative Flow: It redirects to the view delivery man info page.

Pre-Conditions: There must be delivery man info to update salary to them.

Post-Conditions: It redirects to the view delivery man info page.

21. Maintain Attendance

Description: It allows the admin to maintain attendance for the delivery man.

Flow of Events

Basic Flow: Allows to maintain attendance based on their working days.

Alternative Flow: It redirects to the view delivery man info page.

Pre-Conditions: There must be delivery man info to maintain attendance for them.

Post-Conditions: It redirects to the view delivery man info page.

22. Check Orders

Description: It allows the delivery man to check orders in order to deliver them.

Flow of Events

Basic Flow: It must allow to check orders in order to deliver.

Alternative Flow: It redirects to the home page.

Pre-Conditions: There must be orders in order to check them to deliver.

Post-Conditions: It redirects to the home page.

23. Contact Delivery Address

Description: It allows the delivery man to contact the address of the customers to deliver

them.

Flow of Events

Basic Flow: Allows to view address in order to deliver them.

Alternative Flow: It redirects to the home page.

Pre-Conditions: Address must be mentioned correctly to deliver them.

Post-Conditions: It redirects to the home page.

24. Delivered

Description: Delivery mentions the status that he delivered the order to the customer.

Flow of Events

Basic Flow: Order must be delivered in order to mention the status delivered.

Alternative Flow: It redirects to the contact delivery address page.

Pre-Conditions: Order must be delivered in order to mention the status delivered.

Post-Conditions: It redirects to the contact delivery address page.

25. Not Delivered

Description: It allows the delivery man to update the status of not delivered.

Flow of Events

Basic Flow: It allows the delivery man to update not delivered status.

Alternative Flow: It redirects to the contact delivery address page.

Pre-Conditions: It allows the delivery man to update not delivered status.

Post-Conditions: It redirects to the contact delivery address page.

26. Reason for Not Delivered

Description: It allows the delivery man to mention why the order has not been delivered.

Flow of Events

Basic Flow: Allow to mention the reason for not delivered.

Alternative Flow: It redirects to the not delivered page.

Pre-Conditions: Allow to mention the reason for not delivered.

Post-Conditions: It redirects to the not delivered page.

27. Update/View Profile

Description: It allows the delivery man to edit/view his profile.

Flow of Events

Basic Flow: It allows to edit profile.

Alternative Flow: It redirects to the home page.

Pre-Conditions: It allows to edit profile.

Post-Conditions: It redirects to the home page.

28. View Attendance

Description: It allows the delivery man to view attendance.

Flow of Events

Basic Flow: Allows to view attendance.

Alternative Flow: It redirects to the update/view profile page.

Pre-Conditions: Allows to view attendance.

Post-Conditions: It redirects to the update/view profile page

---

## 📊 UML Modeling Suite for Online Pharmacy Management System

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

- **Previous Chapter**: [Design of UML Diagrams for AAROGYA SETU - Health Care APP](Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP.md)
- **Next Chapter**: [Design of UML Diagrams for EQUIHEALTH](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
