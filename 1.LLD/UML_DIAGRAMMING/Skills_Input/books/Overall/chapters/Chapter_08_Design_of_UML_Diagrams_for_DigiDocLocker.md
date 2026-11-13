# Chapter 08: Design of UML Diagrams for DigiDocLocker

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 105–112 (Total: 8 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 07: Design of UML Diagrams for E-Province](Chapter_07_Design_of_UML_Diagrams_for_E_Province.md) | [📚 Book Index](../Overall_Books.md) | [Chapter 09: Design of UML Diagrams for Online Marketplace &rarr;](Chapter_09_Design_of_UML_Diagrams_for_Online_Marketplace.md)

---

## 📌 Chapter Overview

Chapter 8 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for DigiDocLocker**. 
This case study presents an end-to-end software engineering analysis for **DigiDocLocker**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **8.1 Problem Statement**
- **8.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 8

Design of UML Diagrams

for DigiDocLocker

### 8.1 Problem Statement

Maintaining the authentic documents physically in a single location is considered to be a challenging task. Thus, digitizing documents enables centralized storage of all the physical documents

enabling easy retrieval from anywhere at anytime. It also prevents the troubles caused by missing

any of those physical certificates. This can be achieved through the DigiDocLocker which is a

platform for issuance and verification of documents and certificates in a digital format, thereby

eliminating the use of physical documents. DigiDocLocker aims at benefitting all the citizens

of the country by providing to access authentic documents/certificates such as driving licence,

vehicle registration and academic mark sheet in digital format from the original issuers of these

certificates. DigiDocLocker has the following functionalities:

i. A Registration module allows the users to register and a Login module that allows the authorized users.

ii. An Upload Document module allows the users to upload documents such as driving licence,

vehicle registration, academic mark sheet and other relevant documents in various file

formats.

iii. A Profile module displays the complete profile of the user as available in the database.

iv. An Issuer module displays the certificate issuers’ names and the number of documents issued

to the user by the issuer. For example, the Income Tax Department, Government of India

has provided PAN Verification Records to Indian citizens via DigiLocker.

v. A Requester module displays the requesters’ names and the number of documents requested

from the user by the requesters. For example, Citizen applying through Union Public

Service Commission (UPSC)’s Online Recruitment Application (ORA) can upload documents through DigiDocLocker as well (Figures 8.1–8.8).

DOI: 10.1201/9781003287124-8

### 8.2 UML Diagrams

Usecase Specification

1. Registration Process

Description: This process enables the new users to register with the DigiDocLocker System.

Flow of Events

Basic Flow: Register with the DigiDocLocker System successfully.

Alternative Flow: Display an error message if the registration details provided by the user

are not valid or Nil.

Pre-Conditions: The user must possess a valid national identity card (Aadhaar).

Post-Conditions: The user is registered with the DigiDocLocker System successfully and

this is reflected in the registered users’ database.

2. Login Process

Description: This process enables the authorized users to login into the DigiDocLocker

System.

Flow of Events

Basic Flow: Login into the DigiDocLocker System.

Alternative Flow: Display an error message if the credentials are not valid or Nil.

Pre-Conditions: The user should be registered with the system prior to the login process.

Post-Conditions: The user is successfully logged in to the DigiDocLocker System.

Figure 8.1 UML usecase diagram.

3. Document Requesting Process

Description: This process enables the Requesters (e.g. UPSC) to request for various

authentic documents/certificates of the citizens that are to be verified online.

Flow of Events

Basic Flow: Display the requested certificate.

Alternative Flow: Request for another certificate or Nil.

Pre-Conditions: The certificate requested by the Requester must have been uploaded by the

user prior.

Post-Conditions: The requested certificate is displayed to the Requester for verification.

Figure 8.2 UML class diagram.

Figure 8.3 UML sequence diagram.

Figure 8.4 UML collaboration diagram.

Figure 8.5 UML state machine diagram.

4. Document Uploading Process

Description: This process enables the users to upload authentic documents/certificates

such as driving licence, vehicle registration, academic mark sheet and other relevant documents in various file formats online.

Flow of Events

Basic Flow: Upload the documents successfully and update the user database.

Alternative Flow: Upload another authentic document/certificate or Nil.

Pre-Conditions: The users should possess valid documents and certificates in an acceptable

file format.

Post-Conditions: The document gets uploaded into the user database.

Figure 8.6 UML class diagram.

Figure 8.7 UML component diagram.

5. Profile Viewing Process

Description: This process enables the users to view their complete profile as available in

the database.

Flow of Events

Basic Flow: Display the complete profile of the user.

Alternative Flow: Display an error message if no documents are available for the user in his

profile or Nil.

Pre-Conditions: The documents should be uploaded by the user prior.

Post-Conditions: The complete profile of the user is displayed.

6. Document Issuing Process

Description: This process enables the citizens to apply for various authentic documents/

certificates online which will be provided by the Issuers (e.g. Income Tax Department).

Flow of Events

Basic Flow: Apply for a certificate to the corresponding authority.

Alternative Flow: Apply for another certificate or Nil.

Pre-Conditions: The user must possess the pre-requisite documents (e.g. Aadhaar card) in

order to apply for a specific certificate.

Post-Conditions: The certificate application process is successfully completed.

Figure 8.8 UML deployment diagram.

---

## 📊 UML Modeling Suite for DigiDocLocker

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

- **Previous Chapter**: [Design of UML Diagrams for E-Province](Chapter_07_Design_of_UML_Diagrams_for_E_Province.md)
- **Next Chapter**: [Design of UML Diagrams for Online Marketplace](Chapter_09_Design_of_UML_Diagrams_for_Online_Marketplace.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/Overall_Books.md`](../Overall_Books.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
