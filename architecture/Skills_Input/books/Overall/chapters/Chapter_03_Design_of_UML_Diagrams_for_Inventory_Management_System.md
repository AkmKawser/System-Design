# Chapter 03: Design of UML Diagrams for Inventory Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 39–58 (Total: 20 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 02: Design of UML Diagrams for Webmed - Healthcare Service System Services](Chapter_02_Design_of_UML_Diagrams_for_Webmed_Healthcare_Service_System_Services.md) | [📚 Book Index](../README.md) | [Chapter 04: Design of UML Diagrams for Business Process Outsourcing (BPO) Management System &rarr;](Chapter_04_Design_of_UML_Diagrams_for_Business_Process_Outsourcing_BPO_Management_System.md)

---

## 📌 Chapter Overview

Chapter 3 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Inventory Management System**. 
This case study presents an end-to-end software engineering analysis for **Inventory Management System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **3.1 Problem Statement**
- **3.2  Software Requirements Specification**
- **3.3 Functional Requirements**
- **3.4 D  esign and Design Constraints**
- **3.5 UML Diagrams**
- **3.6 Code Generated**
- **3.6.1 Inventree.java**
- **3.6.2 AddGoods.java**
- **3.6.3  Screenshots of the Project**

---

## 📝 Detailed Chapter Summary & Content

Chapter 3

Design of UML Diagrams for

Inventory Management System

### 3.1 Problem Statement

This chapter aims to create an inventory management system for the efficient management of

goods. The performance will be guided by clear and concise strategic practices for each functional

unit by an ongoing quest for perfection. The current systems use a manual method to keep track of

the records at stores, but the current system is difficult to maintain due to the difficulty in searching and retrieving products, cost of material, human errors, less data integrity, and feasible loss of

records and retrieving files. Therefore, by developing such a system, we propose to increase sales by

creating the complete inventory records of stock, receipt, details of purchasers and sellers at the store

and also to facilitate the salespersons and inventory managers. The ever-growing population creates

a high demand. Thus, the responsibility of delivering goods on time lies in the hands of an effective

inventory management system. The inventory management system will be installed in both the

warehouse and at the billing counter thereby enabling the salespersons and the inventory managers

to get instantaneous information and use it on demand. The customer billing process will happen at

the main counter and the inventory management will happen in the background in the warehouse.

### 3.2 Software Requirements Specification

The current inventory system is difficult to maintain due to the difficulty in searching and retrieving products, cost of material, human errors, less data integrity, and feasible loss of records and

retrieving files. So there is a need to create robust inventory management software that ensures

a reduction in customer’s complaints as well as the reduction in inventory cost. The demand for

goods accrues from the growing population. To meet these demands, the inventory managers and

salespersons require an application with on-demand information retrieval and update. The system

will feature a secure login for salespersons and inventory managers. At the warehouse, the inventory application will manage the available goods and resources. At the billing counter, the application will have the ability to create bills along with proper discount and tax evaluations.

DOI: 10.1201/9781003287124-3

### 3.3 Functional Requirements

Authentication – Login: This will allow inventory managers and salespersons to log in to the system.

Change Password: This will allow inventory managers and salespersons to change the password.

Add Goods: This will allow adding goods and their corresponding details to the current inventory.

Remove Goods: This will allow removing goods from the current inventory.

Place Order: This will allow placing a wholesale order to the supplier.

Invoice Generation: This will allow generating an invoice for the order request to the supplier.

Search Item: This will allow searching the item details in the current inventory.

Receipt Generation: This will generate a bill for the customer selected items from the inventory.

Discount and Tax Generation: This will calculate the discount and tax based on the quantity

selected by the customer.

Replace Item: This will replace the item in the current inventory.

Cancel Receipt: This will cancel the currently generated receipt.

Price Updating: This will update the price details of the corresponding item.

Customer Request: This will log an item request from the customer.

View Summary Report: This will generate the summary report for all the transactions that

have taken place.

Expired Goods: This will notify about the removal of goods from the current inventory.

### 3.4 D  esign and Design Constraints

The constraints are that a lot of information should not be displayed on the screen while placing

the order or using the interface. By reducing it to a minimalistic interface, we are able to deliver an

elevated user experience (Figures 3.1–3.11).

Figure 3.1 Login functionality (home dashboard).

Figure 3.2 Dashboard popup.

Figure 3.3 Change password.

Figure 3.4 Add goods.

Figure 3.5 Remove goods.

Figure 3.6 View summary.

Figure 3.7 Place order.

Figure 3.8 Tax details.

Figure 3.9 Search item.

### 3.5 UML Diagrams

The purpose of a Usecase diagram is to list out all the functional requirements of the system. In

the following diagram, the functional requirements of Inventree are diagrammatically represented

(Figure 3.12)

Actor Specification

1. Administrator – The functionality of this actor is to authenticate users who have registered

to the system. More importantly, if a change has occurred in an inventory such as price updation, removing expired goods, these changes are made subsequently by the administrator.

2. Inventory manager – This actor takes care of the inventory, its associated goods and the

transactions that occur within the inventory.

Figure 3.10 Expired goods.

Figure 3.11 Billing counter.

3. Store manager – The store manager would effectively manage the stored goods that are

obtained from the supplier and dispatch, when requested.

4. Supplier – The work of this actor is to supply the goods that are requested by the store,

subsequently responding to requests made at regular instants of time.

Usecase Specification

1. Login

Description: This usecase allows the actors to login to the system with the credentials.

Flow of Events

Basic Flow: The actor enters the username and password and clicks on login button.

Alternative Flow: The actor may have forgotten the password and clicks on Forgot password

button.

Pre-Conditions: The actors should have already registered and should have their credentials

ready.

Post-Conditions: The entered credentials will be checked and if the entries are correct, the

actor is let in.

Administrator

Inventory Manager

Store Manager

Suppli er

System

Login Change Password

AddGoods

Remove Goods

<<include>>

Expired Goods

View Summary report

Place Order

Customer Request

Search Item

Edit Goods

<<include>>

Receipt Generation

Invoice Generation

<<include>>

<<extend>>

Discount and tax generation

<<extend>>

Cancel Receipt

Replace Item

Figure 3.12 UML usecase diagram.

2. Change Password

Description: This allows the users to change the already set password to a new one.

Flow of Events

Basic Flow: The user enters the old password, new password and retypes the new password

for confirmation.

Alternative Flow: The user may not want to change the password and can go back.

Pre-Conditions: The users should have a user account and an existing password.

Post-Conditions: The old password is verified with the database and if it is correct, the new

password is checked with the retyped password and that password is set.

3. Add Goods

Description: This usecase allows the actors to add goods to the inventory.

Flow of Events

Basic Flow: The actor enters all the details about a particular good including the name, price

and quantity added.

Alternative Flow: No goods would have arrived from the supplier and the actor goes back.

Pre-Conditions: The goods should have arrived and the actor should have known all the

details about the goods.

Post-Conditions: The entered details of a particular good will be stored in the inventory.

4. Remove Goods

Description: This usecase allows the actors to remove one or more goods from the

inventory.

Flow of Events

Basic Flow: The actor enters the item’s ID or the item’s name and quantity to be removed.

Alternative Flow: The actor may not want to remove the good or may not know the number

of goods to be removed and goes back.

Pre-Conditions: The actor should know which item he/she is going to remove and the quantity to be removed.

Post-Conditions: The item’s id or the name is searched for in the inventory and the specified

number of that item is removed.

5. Expired Goods

Description: This usecase allows the actors to view all the expired goods and allow them

to remove those goods from the inventory.

Flow of Events

Basic Flow: The expired goods are displayed and the actor clicks on the remove button to

remove that item.

Alternative Flow: The expired goods are displayed but the actor decides to have them on the

inventory and goes back.

Pre-Conditions: There should be atleast one expired good for this usecase to function.

Post-Conditions: The expired good is removed from the inventory.

6. Place Order

Description: This usecase allows the actors to place an order from the inventory.

Flow of Events

Basic Flow: The actor chooses the item he/she wants to buy, specifies the quantity, gives the

address and contact details and clicks on place order.

Alternative Flow: The actor may decide not to buy anything at that instant and goes back.

Pre-Conditions: The actor is allowed to choose only between the items that are available in

the inventory.

Post-Conditions: The requested item and the quantity is recorded and the item is delivered

to the specified address.

7. Invoice Generation

Description: This usecase generates the invoice for the items that are bought from the

supplier.

Flow of Events

Basic Flow: The item’s name, price and quantity are taken and the total amount is

calculated.

Alternative Flow: The required details may not be present and thus invoice is not

generated.

Pre-Conditions: The requested item by the inventory manager should be available with the

supplier.

Post-Conditions: The invoice is generated and the item is received.

8. Search Item

Description: The usecase allows the actors to search for an item that is present in the

inventory.

Flow of Events

Basic Flow: The actor enters the item’s id or the item’s name and clicks on the search

button.

Alternative Flow: The actor may not know which item he/she wants to search and goes

back.

Pre-Conditions: The item that is to be searched must be present in the inventory.

Post-Conditions: The entered item is searched and displayed.

9. Edit Goods

Description: This usecase allows the actors to edit the details regarding the goods that

have been entered already.

Flow of Events

Basic Flow: The required item is searched, old details are deleted and the new details are

entered.

Alternative Flow: The item that is searched for may not be present in the inventory.

Pre-Conditions: The searched item should be present in the inventory.

Post-Conditions: The details that are changed are updated and stored.

10. Customer Request

Description: This usecase allows the customers (actors) to place a request for the item

they need.

Flow of Events

Basic Flow: The actor enters the item and the quantity he/she needs.

Alternative Flow: The actor may not know what he/she needs clearly and can go back.

Pre-Conditions: The requested item should not exist in the inventory.

Post-Conditions: The requested item is stored and it is placed as an order to the supplier.

11. Receipt Generation

Description: This usecase generates the receipt for the items that the customers buy.

Flow of Events

Basic Flow: The item, quantity the customer buys is entered and the bill amount is calculated.

Alternative Flow: The customer may not buy any item.

Pre-Conditions: The items should be present in the inventory.

Post-Conditions: The bill amount is generated and the customer is notified.

12. Discount and Tax Generation

Description: This usecase calculates the discount and tax for the total bill amount.

Flow of Events

Basic Flow: The net total amount is taken and the corresponding discount and the tax is

calculated and added to the net total to get the grand total.

Alternative Flow: There may not be any discounts.

Pre-Conditions: The net total should be calculated for the items bought.

Post-Conditions: The grand total is calculated and the customer is notified.

13. Cancel Receipt

Description: This allows the actors to cancel a generated receipt.

Flow of Events

Basic Flow: The actor enters the bill number and clicks on the Cancel button.

Alternative Flow: The receipt may not be cancelled and it is correct.

Pre-Conditions: The searched receipt that needs to be cancelled should be generated

previously.

Post-Conditions: The selected receipt is cancelled and the respective items are added back

to the inventory.

14. Replace Item

Description: This usecase allows the actors to replace an item from the inventory.

Flow of Events

Basic Flow: The actor enters the item to be replaced.

Alternative Flow: The actor does not want to replace and goes back.

Pre-Conditions: The item to be replaced must be bought beforehand.

Post-Conditions: The specified item is replaced with another item from the inventory.

15. View Summary Report

Description: This usecase allows the actors to view the summary report of all transactions.

Flow of Events

Basic Flow: The actor views the summary report that is generated.

Alternative Flow: The actor goes back without viewing.

Pre-Conditions: There must be some transactions that should have taken place.

Post-Conditions: The summary report is generated and is viewed by the actors.

UML Class Diagram: It focuses on the relationship among various attributes along with the

operations associated with each of them, with respect to classes (Figure 3.13).

UML Activity Diagram: The purpose of the activity diagram is to have a visual depiction of

the flow of activities in the system (Figure 3.14).

UML State Machine Diagram: The purpose of the state machine diagram is to design and

understand time-critical systems. It helps in understanding the behaviour of the system and it

expresses the behaviour in terms of a series of steps, triggering events and the actions that may

occur (Figure 3.15).

UML Sequence Diagram: The purpose of this diagram is to order the events identified earlier

using usecase, class and activity diagram. It is also used to trace the execution of the problem

domain (Figure 3.16).

UML Communication Diagram: The diagram focuses on how strongly objects communicate

with each other with the help of messages (Figure 3.17).

UML Component Diagram: It focuses on how every component collaborates with every

other component using available interfaces to provide the major functionalities of the system

(Figure 3.18).

Figure 3.13 UML class diagram.

Figure 3.14 UML activity diagram.

Figure 3.15 UML state machine diagram.

Figure 3.16 UML sequence diagram.

Figure 3.17 UML communication diagram.

Figure 3.18 UML component diagram.

UML Deployment Diagram: It strongly focuses on the mapping of software elements to

physical architectures and represents the communication between all the physical elements

(Figure 3.19).

### 3.6 Code Generated

### 3.6.1 Inventree.java

package Inventree; import java.sql.*; import java.io.*;

import java.util.Scanner;

public class Inventree {

public String username; protected String password; public String

userType; public int flag;

public void receiveCredentials() {

Scanner scuser=new Scanner(System.in); System.out.

println("Enter username");

username = scuser.next(); System.out.println("Enter

password"); password =

scuser.next();

}

Figure 3.19 UML deployment diagram.

public boolean checkCredentials() {

//System.out.println("Comes here"); receiveCredentials();

if(username.equals("admin")&&password.equals("admin"))

return true;

else

} }

return false;

### 3.6.2 AddGoods.java

import java.sql.*; import java.io.*;

import java.util.Scanner; import Inventree.Inventree; import java.

util.*;

public class AddGoods extends Inventree { public String itemId;

public String itemName; public int itemQty; public double

itemPrice;

public String itemManufacturer; public String

itemOriginAddress; public String comments;

public Date expiryDate;

public void receiveInput() { if(checkCredentials()){

Scanner sc = new Scanner(System.in);

System.out.print(String.format("%40s","Add Goods\n"));

System.out.println("\n\n");

System.out.println("Enter the item Id"); itemId =

sc.next();

System.out.println("Enter the item Name"); itemName =

sc.next();

System.out.println("Enter the item Qty"); itemQty =

sc.nextInt();

System.out.println("Enter the item Price"); itemPrice

= sc.nextDouble();

System.out.println("Enter the item Manufacturer");

itemManufacturer =

sc.next(); System.out.println("Enter the item Origin

Address");

itemOriginAddress = sc.next();

System.out.println("Enter the item comments");

comments = sc.next();

}

}

public void addToDatabase() {

}

public static void main(String[] argv){ int choice;

Scanner sc=new Scanner(System.in); AddGoods obj=new

AddGoods();

do{     System.out.println("\n\n"); System.out.print(String.

format("%40s","Inventree\n")); System.out.print(String.

format("%50s","Inventory Management

System.out.println("Choose an option"); System.out.print(String.forma

t("%15s%40s","1","Login\n")); System.out.print(String.

format("%15s%40s","2" ,"About\n"));

System.out.print(String.format("%15s%40s","3", "EXIT\n")); choice =

sc.nextInt();

switch(choice){

case 1:  obj.receiveInput(); break;

case 2: System.out.println("Developed by TEAM 5"); break;

case 3: break;

default: System.out.println("Enter a correct option"); break;

}

}

while(choice!=3);

} }

### 3.6.3 Screenshots of the Project

See Figures 3.20–3.22

Figure 3.20 Case 1.

Figure 3.21 Case 2.

Figure 3.22 Case 3.

---

## 📊 UML Modeling Suite for Inventory Management System

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

- **Previous Chapter**: [Design of UML Diagrams for Webmed - Healthcare Service System Services](Chapter_02_Design_of_UML_Diagrams_for_Webmed_Healthcare_Service_System_Services.md)
- **Next Chapter**: [Design of UML Diagrams for Business Process Outsourcing (BPO) Management System](Chapter_04_Design_of_UML_Diagrams_for_Business_Process_Outsourcing_BPO_Management_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
