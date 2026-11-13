# Chapter 14: Design of UML Diagrams for Car Care

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 157–166 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 13: Design of UML Diagrams for COVID-19 Management System](Chapter_13_Design_of_UML_Diagrams_for_COVID_19_Management_System.md) | [📚 Book Index](../UML_Book.md) | [Chapter 15: Design of UML Diagrams for E-Ration Shop &rarr;](Chapter_15_Design_of_UML_Diagrams_for_E_Ration_Shop.md)

---

## 📌 Chapter Overview

Chapter 14 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Car Care**. 
This case study presents an end-to-end software engineering analysis for **Car Care**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **14.1 Problem Statement**
- **14.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 14

Design of UML Diagrams

for Car Care

### 14.1 Problem Statement

Most of the car owners do not know whether their car is at risk and needs to be serviced. This

considerably increases the risk of malfunctioning of major parts of a car such as the braking system

and engine which lead to accidents.

Car Care is a multi-brand car service and maintenance application that maintains the date at

which the specific part of a car is installed and notifies the expiry date of the parts of the car for

both the driver and authorized service centre, so that the car can be serviced.

This application enables car owners and service centres to separately login and enter their cars

information. After issuing the car, the service centre employee enters the estimated expiry dates of

parts of the car in this app.

This application notifies the car owners and service centres when the expiry date for parts of

the car is reached. Then the service centre employee contacts the owner of a car about service, once

the owner accepts service request, the service centre employee picks up the car from home, this

saves the time for owner of car.

And then service centre employee examines the entire car and prepares the list of the damaged parts of the car and send it to the owner of the car through this app, once the owner selects

the damaged parts to be serviced, the employee services the owner selected parts and updates

the information about changed parts in the app so that the car can be service again on the

expiry date of changed parts. Thus, this application helps in exchanging information between

car owners and service centres. This application also enables the online payment for the services

(Figures 14.1–14.8).

DOI: 10.1201/9781003287124-14

### 14.2 UML Diagrams

Usecase Specification

1. Registration

Description: Registration of car owner and service centre is required to use the system.

Flow of Events

Basic Flow: Profile for a car owner and service centre is created.

Alternative Flow: If the car owner and service centre are already registered, they can go with

login and get access to the system.

Pre-Conditions: Nil.

Post-Conditions: Allows the car owner and service centre to login into system.

2. Login

Description: Login is required to get access to the system.

Flow of Events

Basic Flow: If the password is correct, then the car owner and service centre can get access

to the system.

Alternative Flow: If the password is incorrect, try with the correct password and forgot

password facility is available.

Pre-Conditions: Registration is required.

Figure 14.1 UML usecase diagram.

Post-Conditions: This allows the car owner and service centre to access the Vehicle

Information System.

3. Vehicle Information System

Description: Vehicle Information System maintains the information of the vehicle and

when the expiry date of parts of car is reached, it notifies both the owner and service centre,

so that car can be serviced.

Flow of Events

Basic Flow: Maintains the information of the vehicle and sends a notification when the

expiry date of parts of the car is reached.

Alternative Flow: Nil.

Pre-Conditions: Login is required.

Post-Conditions: The car owner and service centre can view the information of car.

4. Views Information

Description: This allows the car owner and service centre to know the conditions of parts

of the car and other information.

Figure 14.2 UML activity diagram.

Figure 14.3 UML sequence diagram.

Flow of Events

Basic Flow: User gets to know the status of parts of the car.

Alternative Flow: Nil.

Pre-Conditions: Registration and login are required.

Post-Conditions: Nil.

5. Enters and Modifies Car Parts Information

Description: Service centre employee modifies the car parts information after every

service.

Flow of Events

Basic Flow: Service centre employee updates the information in Vehicle Information System

after every service which is helpful further services.

Figure 14.4 UML collaboration diagram.

Figure 14.5 UML state machine diagram.

Alternative Flow: Nil.

Pre-Conditions: Registration and login of the service centre are required.

Post-Conditions: The information updated by the service centre employee is used for expiry

notification of upcoming services.

6. Vehicle Parts Expiry Notification

Description: Expiry notification will be sent to the owner and service centre so that the

car can be serviced.

Figure 14.6 UML class diagram.

Figure 14.7 UML component diagram.

Flow of Events

Basic Flow: Once the expiry notification is received, service centre employee contacts car

owner and asks for service.

Alternative Flow: Nil.

Pre-Conditions: Information of cars should be present in Vehicle Information System.

Post-Conditions: Service centre employee contacts car owner and asks for service.

7. Service Acceptance

Description: The Car owner may or may not accept the service request from service

centre.

Flow of Events

Basic Flow: If the car owner accepts the service, further steps for service is carried out.

Alternative Flow: Car owner denies the service request.

Pre-Conditions: Service requests from the service centre is required.

Post-Conditions: Nil.

Figure 14.8 UML deployment diagram.

8. Service Cost Estimation for all Damaged Parts

Description: Once the service request is accepted by the car owner, service cost estimation for all damaged parts will be carried out.

Flow of Events

Basic Flow: Once the service request is accepted, service centre employee examines the car

and creates the list of damaged parts and updates in the app.

Alternative Flow: Nil.

Pre-Conditions: Service Acceptance.

Post-Conditions: Parts selection and service confirmation.

9. Parts Selection and Service Confirmation

Description: Once the service employee updates the list of damaged parts of the car in

the app, the car owner can select the required parts to be serviced.

Flow of Events

Basic Flow: Car owner selects the required parts to be serviced and confirm the service.

Alternative Flow: Service cancellation is also possible.

Pre-Conditions: The selection list must be updated in the app by the employee.

Post-Conditions: Changed parts list must be updated in the Vehicle Information System.

10. Updating Changed Parts Expiry Information

Description: After changing the damaged parts the service centre employee, updates the

information.

Flow of Events

Basic Flow: The employee edits the changed parts information in the Vehicle Information

System of this application.

Alternative Flow: Nil.

Pre-Conditions: Service is required.

Post-Conditions: The payment process is carried out.

11. Online Payment

Description: Online payment for the service is done by the Car owner.

Flow of Events

Basic Flow: Payment Service provider provides an easy way to use interface for making

payments.

Alternative Flow: Nil.

Pre-Conditions: All car service process should be completed.

Post-Conditions: Car owner can report to admin.

12. Net Banking

Description: Car owner can use net banking facility provided by the payment service

provider.

Flow of Events

Basic Flow: Car owner can use net banking for making payments.

Alternative Flow: Car owner can choose any other payment method.

Pre-Conditions: All the car service processes should be completed.

Post-Conditions: Car owner can report to admin.

13. UPI

Description: Car owner can use UPI (Unified Payment Interface) facility provided by

the payment service provider.

Flow of Events

Basic Flow: Car owner can use UPI for making payments.

Alternative Flow: Car owner can choose any other method for making payments.

Pre-Conditions: All the car service processes should be completed.

Post-Conditions: Car owner can report to admin.

14. Report

Description: Car owner reports to the admin about the service centre.

Flow of Events

Basic Flow: Car owner reports to admin so that necessary actions could be taken.

Alternative Flow: Car owner can give positive feedback as well.

Pre-Conditions: All service and payment process should be done.

Post-Conditions: Nil.

---

## 📊 UML Modeling Suite for Car Care

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

- **Previous Chapter**: [Design of UML Diagrams for COVID-19 Management System](Chapter_13_Design_of_UML_Diagrams_for_COVID_19_Management_System.md)
- **Next Chapter**: [Design of UML Diagrams for E-Ration Shop](Chapter_15_Design_of_UML_Diagrams_for_E_Ration_Shop.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
