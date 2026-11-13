# Chapter 02: Design of UML Diagrams for Webmed - Healthcare Service System Services

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 23–38 (Total: 16 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 01: Introduction to UML Diagrams and Its Components](Chapter_01_Introduction_to_UML_Diagrams_and_Its_Components.md) | [📚 Book Index](../Overall_Books.md) | [Chapter 03: Design of UML Diagrams for Inventory Management System &rarr;](Chapter_03_Design_of_UML_Diagrams_for_Inventory_Management_System.md)

---

## 📌 Chapter Overview

Chapter 2 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Webmed - Healthcare Service System Services**. 
This case study presents an end-to-end software engineering analysis for **Webmed - Healthcare Service System Services**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **2.1 Problem Statement**
- **2.2  Major Functionalities and Its Description**
- **2.3  Data-Flow Diagrams**
- **2.4  Proposed Design – UML Diagrams**
- **2.4.1  Usecase Specification for the UML Usecase**

---

## 📝 Detailed Chapter Summary & Content

Chapter 2

Design of UML Diagrams

for Webmed – Healthcare

Service System Services

### 2.1 Problem Statement

Healthcare service has huge demand these days as it really helps in managing a hospital or a medical office. The scope of healthcare service systems is increasing by each day and it is true for the

entire world. Some of these solutions include improved awareness about healthcare services and

health policies. The objective of this system is to provide medical assistance to people instantly

with the help of technology. This system eradicates the cultural sensitivity that prevails in many

hospitals and improvises the quality of medical assistance. The captivating features of this system

are online doctors, medicines at doorstep and bulletin of awareness. The users can also navigate

and choose among various insurance schemes that are displayed.

The primary objectives of Webmed healthcare system are to enable all citizens to receive

healthcare services whenever needed, and to deliver health services that are cost-effective and

meet pre-established standards of quality. The main functions of this system deal with finance,

health A–Z, resources, drugs and supplements, news and experts, payment and feedback.

Register function allows the patients or the caregivers to register on the website. Login function allows the patients to access the website. Financing focuses on the purchase of insurance.

Health A–Z displays all the diseases along with their symptoms. Resources function consists

of the sub-functions including symptoms checker, health calculator, find a doctor based on the

geographical location of the patient, insurance guide and ambulance providence. Drugs and

supplements include online medicine delivery, where people could shop for medicines online.

News and experts function is to provide health awareness and threats that are prevailing. This

function also gives information regarding counselling programs and blood donation camps. The

payment function is to reimburse providers for services delivered. The feedback function collects

user reviews for the website.

DOI: 10.1201/9781003287124-2

### 2.2 Major Functionalities and Its Description

The major functionalities of this system along with their description are as follows:

Register – this functionality acts as a membership functionality that allows the users, patients

or caregivers to register into this website to access all the resources. Login – this functionality

authenticates the user to provide access permissions. Facilities – this functionality allows us to

access all the options available on the website. Logout – this functionality ends the access to the

website. Finance – this functionality allows to purchase insurance, or to pay for healthcare services consumed. Health A–Z – this functionality provides details of all the diseases. Resources –

this functionality has sub-functions, namely symptoms checker, health calculator, find a doctor,

insurance guide and ambulance providence. Drugs and supplements – this functionality provides online delivery of medicines. This functionality takes the doctor’s statement for the issue

of medicine and the patient’s willingness to buy it online. News and experts – this functionality

provides health awareness and threats that are prevailing. Payment – this functionality deals with

the payment for the services consumed. This functionality is split into two sub-functions namely,

payment for doctors, for the services issued and payment for online med-delivery. Feedback – this

functionality collects user reviews for this website.

System Architecture: System architecture is the conceptual model that defines the structure,

behaviour and more views of a system. An architecture description is a formal description and

representation of a system, organized in a way that supports reasoning about the structures

and behaviours of the system. This architecture diagram shown in Figure 2.1 includes all the

functionalities of the system in an ordered manner based on the sequence of occurrence of

these functionalities. It represents the complete data flow starting from the register functionality

through which the user could access the system to the logout functionality that ends the access

Log Out

Register

Login

PaymentNews and Experts

Feedback

Drugs and

supplements

Resources Health A- ZFinance

Figure 2.1 System architecture.

of the user to the system. Initially, the user must register onto the system. Once registered, the

user would be able to log on to the system and could access all the services offered – finance,

news and experts, resources that include finding a doctor, health A–Z that includes health calcu -

lator and fitness calculator, drug and supplements, payment and feedback. The payment is done

through the insurance for the services consumed. After consuming the services, the user could

log out of the system.

### 2.3 Data-Flow Diagrams

A data-flow diagram (DFD) is a way of representing a flow of a data of a process or a system.

The DFD also provides information about the outputs and inputs of each entity and the

process itself. A DFD has no control flow; there are no decision rules and no loops. A DFD

can dive into progressively more detail by using levels and layers. DFD levels are numbered

0, 1 and 2.

DFD Level 0 is also called a Context Diagram. It is a basic overview of the whole system or

process being analyzed or modelled. It is designed to be an at-a-glance view, showing the system

as a single high-level process, with its relationship to external entities. This level 0 DFD diagram

as shown in Figure 2.2 consists of the healthcare service provider system – Webmed and the

actors who affect those systems – the users that is the patients and the service providers who

are responsible for the maintenance of the system. This is the basic diagram that could be easily

understood by a wide audience. DFD Level 1 as shown in Figure 2.3 provides a more detailed

breakout of pieces of the Context Level Diagram. We will highlight the main functions carried

out by the system, as you break down the high-level process of the Context Diagram into its

sub-processes.

These systems too have the same external entities – patients who require the service and the

service providers who offer those services via the system. The Webmed system is broken down

into a number of sub-processes. These sub-processes represent the functionalities of the system –

register, login, finance, health A–Z, resources, drugs and supplements, news and experts,  payment,

feedback and logout. Payment is done to find a doctor and the drugs and supplements services

provided. The user could also give the feedback for the services available. Table 2.1 describes the

comparison between the existing system and the proposed system.

Figure 2.2 Level 0 DFD.

Figure 2.3 Level 1 DFD.

Table 2.1 Comparison of Proposed System and Existing System

Existing System

Additional Features of Proposed System with Reference to

Existing System

Register The same as that of the existing system

Login

Logout

Finance

Health A–Z It acts as a dictionary of diseases along with their symptoms.

Resources The same as that of existing system.

Drugs and supplements This functionality provides online delivery of medicines.

News and experts This functionality provides health awareness and threats that

are prevailing.

Payment The same as that of existing system.

Feedback This functionality collects user reviews for this website.

### 2.4 Proposed Design – UML Diagrams

### 2.4.1 Usecase Specification for the UML Usecase

Diagram Generated Using Star UML Tool

Actor Specification

1. Patient – This actor plays the role of a patient who can register on the website and can make

use of all the services provided by the website. This actor can also play a role of a caregiver.

2. Service Provider  – This actor acts as the master of this website who provides certain ser -

vices. This actor maintains a database of doctors that helps a patient to find a doctor and

looks after the finance, insurance and payment requirements. He also gives descriptions

regarding various diseases that can be referred by the users. He also provides a facility for

the users to purchase drugs and other medicines online and spreads awareness through news

regarding the prevailing threats (Figure 2.4).

Usecase Specification

1. Drugs and Supplements

Description: This functionality provides online delivery of medicines.

Flow of Events

Basic Flow: It allows the users to search for and purchase drugs and other medical supplies

like sringes, bandages and dressing, earloop face masks, etc.

Figure 2.4 UML usecase diagram.

Alternative Flow: Alternate flow for this usecase is: Health A-Z, resources, finance, news,

and experts.

Pre-Conditions: The user must have logged on to the website to make use of this functionality.

Post-Conditions: The drugs and medicines database get updated accordingly.

2. Facilities

Description: The service provider controls all the facilities on the website through this

usecase and the user can utilize these facilities.

Flow of Events

Basic Flow: The user can obtain the services like: Health A–Z, resources, drugs and supple -

ments, news and experts, and finance.

Alternative Flow: The user can provide his feedback for improvement of the website.

Pre-Conditions: The user must have logged on to the website in order to make use of this

functionality.

Post-Conditions: By getting into this usecase, the user can make use of the available

services.

3. Feedback

Description: This Feedback section helps the users to give their honest opinions about

the quality of services that have been provided. It also helps them to give their suggestions

for further improvements.

Flow of Events

Basic Flow: It verifies whether the feedback is given or not.

Alternative Flow: LOGOUT.

Pre-Conditions: The payment function should have been completed.

Post-Conditions: The feedback form is submitted.

4. Finance

Description: Negotiations regarding the financial status are done, eligibility for the

insurance is checked and the appropriate schemes are issued.

Flow of Events

Basic Flow: It checks if the user has availed any insurance for his health if not it checks for

insurance availability.

Alternative Flow: Instead of this usecase, the following usecases can be executed: Health

A-Z, resources, drugs and supplements, news, and experts.

Pre-Conditions: The patients should have a valid bank account.

Post-Conditions: The patient would have insured his life.

5. Health A–Z

Description: This functionality acts as a dictionary of the diseases along with their symptoms and the drugs that can be consumed.

Flow of Events

Basic Flow: It provides catalogue of all the diseases with their symptoms.

Alternative Flow: Instead of this usecase, the following usecases can be executed: finance,

resources, drugs and supplements, news, and experts.

Pre-Conditions: The user should have logged onto the website.

Post-Conditions: The user is now aware of the drugs that must be consumed for a specific

disease.

6. Login

Description: This functionality allows the patients and caregivers to login into the web -

site to get the access to all the resources.

Flow of Events

Basic Flow: It allows the user to access all the resources that are available in the website.

Alternative Flow: After this usecase is executed, then the control flows through any one of

the following usecases: Finance, health A-Z, resources, drugs and supplements, news,

and experts.

Pre-Conditions: The user should have registered into the website.

Post-Conditions: The user is given the complete access to all the resources available on the

website.

7. Logout

Description: This functionality ends the access to the website. So the user must log in

again to access all the resources.

Flow of Events

Basic Flow: It ends the access of the resources by the user.

Alternative Flow: It has no alternate flow.

Pre-Conditions: The user should have logged onto the website.

Post-Conditions: Once this usecase is executed, the user is denied from the resources pro -

vided by this website.

8. News and Experts

Description: A bulletin of news regarding the latest diseases that prevails in the envi -

ronment, expert opinions to avoid those communicable and non-communicable diseases,

awareness about the diseases will be displayed publicly.

Flow of Events

Basic Flow: The current affairs about the diseases are well received by the users.

Alternative Flow: Instead of this usecase, the following usecases can be executed: Health

A-Z, resources, drugs and supplements, and finance.

Pre-Conditions: The user should have logged in.

Post-Conditions: The user is enlightened about the prevalent diseases.

9. Payment

Description: This functionality deals with the payment for the services consumed.

Flow of Events

Basic Flow: This functionality involves the payment for the services provided by the

doctor.

Alternative Flow: After executing this usecase, the control moves to the usecase feedback.

Pre-Conditions: The user should have consumed the services provided by the doctor or

should have purchased medicines online.

Post-Conditions: After executing this usecase, the user has made the payment for the medi -

cines purchased or the service providers have made the payment to the doctors.

10. Register

Description: This acts as a membership functionality that allows the patients or caregiv -

ers to register into this website to access all the resources

Flow of Events

Basic Flow: It allows the user to register on the website.

Alternative Flow: After the register usecase is executed, the usecase that can be executed is:

LOGIN functionality.

Pre-Conditions: This is no precondition as register is the first usecase to be executed.

Post-Conditions: After the register usecase is executed, the user will be given a Webmed

membership.

11. Resources

Description: The resources such as health calculator, ambulance services, symptoms

checker, find a doctor and insurance guidance are unveiled in this segment.

Flow of Events

Basic Flow: Thus the resources are gathered by the users.

Alternative Flow: Instead of this usecase, the usecases that can be executed are: HEALTH

A–Z, NEWS AND EXPERTS, DRUGS AND SUPPLEMENTS, and FINANCE.

Pre-Conditions: The availability of the resources should be ensured.

Post-Conditions: The users have enjoyed the privileges of accessing the resources (Figure 2.5).

The two actors, user and the service providers can access the resources on the website. The facili -

ties class consists of the functions like news and experts, health A–Z and health calculator. The

finance class checks if the user has health insurance and if not alerts the service provider who buys

the insurance for the user. The realization relationship is used to link the user and the service pro -

vider with the finance class. The payment class involves the payment by the user for the services

consumed. The payment can either be an online payment or through cash on delivery of drugs

and other supplements. Thus the generalization relationship is used to represent the cash and

online payment of the payment class. The payment class is loosely related to the user class and it

is strongly related to the service provider class as the service provider takes care of all the payment

procedures. The resources like finding a doctor, which suggests a suitable doctor specialized for a

disease and purchase of drugs and supplements are the resources for which the payment is done.

So these resources are common to both the facilities class and the payment class. Hence these

resources are kept in an association class named as ‘utilization’ (Figure 2.6).

The activity diagram represents the flow of data through the system. It represents the entire

flow of data from the registration of the user, followed by logging on to the website with username

and password. Once the user has logged on to the system, the user could access all the resources

and can navigate through the resources again until the user wishes to log out the system. The user

needs to pay for the services which they acquired. The user could also give the feedback for the

system if the user opts it (Figure 2.7).

In this activity diagram, the register is a sub-activity. The register has an individual flow of

control that enables the user to enrol them into the system. The activity diagram above illustrates

the flow that takes place in the register function. The user is prompted to give all the details. The

service provider then generates the random id and receives the password from the user and confirms

the password. If the password and confirm password are the same then the user is registered to the

system else the user is prompted to give the text for the confirm password field alone (Figures 2.8

and 2.9).

The system first checks if the user is a registered user, if yes the user is prompted to the login

state, else the user is asked to register into the system and is prompted to the register state. Once

logged into the system, the user could access the facilities based on the choice of the user. Based

on the choice of the user, the user is prompted to the required state. In this diagram, the login is a

submachine state that consists of many disjoint states. If the user needs to find a doctor or needs

to purchase drugs then the user is checked for the availability of insurance. If not the system buys

an insurance for the user  and is allowed to use the services. The payment is done for the services

consumed using the payment state. Once the user has accessed the resources, the user could again

loop on all the resources again if required, else the user could log out of the system. Before logging

out of the system, the user could also give the feedback for the services provided by the system if the

user wishes to do so.

Figure 2.5 UML class diagram.

Figure 2.6 UML activity diagram (1).

The interaction between the user and the service provider is clearly depicted in this diagram.

The user is checked if the user is already registered to the system or not. If not registered to the

system, the register function takes place. If registered, the user can logged in the system with

username and password. For this if else case, the alternate fragment is used. After logging on to

the system, the user is correctly prompted to the functionality based on the choice of the user.

Hence to select the resource, the optional fragment is used. In order to access the find a doctor

and the drugs and supplements, the user is checked for the insurance. If not, the service provider

buys insurance for the user. This insurance is used for the payment of the resources utilized. The

request from the user is sent as a synchronous message as the user needs the response for the

request. The response is sent as a reply message. The complete flow of messages from the register

to the payment and delivery of the purchased drugs is clearly depicted in the sequence diagram

(Figure 2.10).

It focuses on the interaction between the actors in the system same as that of the sequence

diagram. The collaboration diagram does not consist of any fragments. Hence the messages are

used to represent the conditional and looping statement. The sequence diagram has 34 messages.

But the collaboration diagram has 35 messages. This extra one message (23) is used to prevent the

overlapping of messages. Since the entire payment function involves overlapping of messages, an

extra message is used to indicate the start of the payment function. A component is a replaceable

and executable piece of a system whose implementation details are hidden. A component provides

the set of interfaces that a component realizes or implements. Components also require interfaces

to carry out a function. Components also require interfaces to carry out a function. UML com -

ponent diagrams are used to represent different components of a system. In this diagram, every

component represents an individual module that encompasses all its attributes and operations. The

user component can access all the resources. The user component consists of the resources, health

A–Z, news and experts as it can access those directly. The database subsystem consists of all the

artefacts that are required for the system. The service provider is a service that takes care of the

processes like financing, placing order to buy those drugs that are out of stock. The drug supplier

component supplies the drugs to the service providers for which the payment is done (Figures 2.11

and 2.12).

Figure 2.7 UML activity diagram (2).

Figure 2.8 UML state machine diagram.

Figure 2.9 UML sequence diagram.

Figure 2.10 UML communication diagram.

The nodes and the Execution Environment Node are used to represent the OS, database and

the web browser. The attributes and the operations are represented using parts as that of the com -

ponent diagram. The database is maintained in the service provider as it needs to search for the

details of the patient in the event of register, login, finding a doctor and payment. The drug sup -

plier node is used to illustrate the attributes and operations involved in representing the ordering

and purchasing of the drugs. The protocol that is used between the user and the service provider

is Secure and Auditable Agent-based Communication Protocol (SAACP). SAACP is often used by

most of the hospitals to maintain the details of the patients in a secure way. Each node has parts

that denote the attributes and operations that it can involve.

Figure 2.11 UML component diagram.

Figure 2.12 UML deployment diagram.

---

## 📊 UML Modeling Suite for Webmed - Healthcare Service System Services

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

- **Previous Chapter**: [Introduction to UML Diagrams and Its Components](Chapter_01_Introduction_to_UML_Diagrams_and_Its_Components.md)
- **Next Chapter**: [Design of UML Diagrams for Inventory Management System](Chapter_03_Design_of_UML_Diagrams_for_Inventory_Management_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/Overall_Books.md`](../Overall_Books.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
