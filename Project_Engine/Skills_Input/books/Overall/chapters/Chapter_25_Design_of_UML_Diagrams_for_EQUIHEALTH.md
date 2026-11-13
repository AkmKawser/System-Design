# Chapter 25: Design of UML Diagrams for EQUIHEALTH

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 265–278 (Total: 14 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 24: Design of UML Diagrams for Online Pharmacy Management System](Chapter_24_Design_of_UML_Diagrams_for_Online_Pharmacy_Management_System.md) | [📚 Book Index](../Overall_Books.md) | [Chapter 26: Design of UML Diagrams for an OTT-Based System - MINI REEL &rarr;](Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_System_MINI_REEL.md)

---

## 📌 Chapter Overview

Chapter 25 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for EQUIHEALTH**. 
This case study presents an end-to-end software engineering analysis for **EQUIHEALTH**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **25.1 Problem Statement**
- **25.2 System Architecture**
- **25.3 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 25

Design of UML Diagrams

for EQUIHEALTH

### 25.1 Problem Statement

This case study mainly focusses on developing an application to address the health disparities among the various classes of patients and the appropriate medical interventions in order

to achieve health equity for every individual. The target users of the application are patients,

caretakers, healthcare providers, medical professionals and government officials. One of the

main functionalities of the system is a patient classification based on social determinants such as

economic backgrounds, health insurance amount received, medical allowances, demographics,

age, type of disability and hereditary health information. It has to be ensured that appropriate

treatment is administered for the people of all categories in an equitable manner. The patient

should be able to feed health details into the application that will be corroborated by the details

furnished by the healthcare providers and the patient’s public health records. Another important functionality is to notify the patients about the relevant medical events and health schemes

available based on the system’s categorization of the patient’s data. The system also must provide

personal health-tracking facilities for the patients by means of assessing the patients’ individual

medical records. The next function is to enable the healthcare providers such as hospitals and

clinics to plan and schedule health worker activity based on the patient’s need. Consequently,

the application should make available the analysis of these data to the government, thereby

assisting in the implementation of significant intervention schemes to offer medical facilities

without any conflicts and eliminate the health discrepancies. Thus, with a holistic approach,

the application should allow patients to register and upload social and medical data which get

classified based on criteria that are then used by the healthcare providers and governments to

extend healthcare to all individuals without any disparities.

DOI: 10.1201/9781003287124-25

Functionalities:

◾ Registration: The users of the application are registered with unique credentials and categorized as patients, health workers or a government authority.

◾ Login: The login section is for the users to login to the application using the unique credentials provided during the registration phase.

◾ Logout: The logout option is included in the user’s user interface enabling the user to log out

of the application at any time the user wants to.

◾ Data Entry: A section to enter all the medical details as well as the various social and economic details including unique identification details for the patient user and registered identification details for the health workers.

◾ Validation of Medical Data: The details entered by the patient will be corroborated by the

details furnished by the respective hospital medical records of the patients.

◾ Patient Dashboard: A catered dashboard for every patient user with articles relating to the

patient’s present medical conditions and the possible ailments that the patient may be prone

to, obtained by analysis of the patient’s medical records. It also incorporates a search bar to

search for specific articles relating to a medical term.

◾ Health Worker Dashboard: A dashboard for every health worker belonging to every registered medical institution that provides informative articles pertaining to the worker’s area

of specialization.

◾ Health Tracking: A section that provides a health-tracking facility by means of detailed

analytics of the patient’s individual health records furnished by the patient as well as the

healthcare establishments from where the patient receives active treatment. This section also

has provisions to synchronize the data from other health monitoring applications in the

user’s device and include them for health tracking.

◾ Alerts: Alerts are scheduled for all the users and dispatched to the patients whenever an

activity is due such as a health checkup or a medical camp and dispatched to the health

workers to catch up on a scheduled activity.

◾ Activity Scheduling: Activities of the health workers are scheduled according to the analysed

requirements of the patients based on various medical and social factors and the progress of

these planned activities can be tracked.

◾ Analytics: All the exhaustive data that goes into the application is analysed for patterns of medical disparities based on family and community issues and socio-economic

determinants and a holistic report of this data is presented in the dashboard accessible

to the authorized government authority to be used to bring about the appropriate health

interventions.

◾ Health Financing: Using the application’s analytics data, the government should be able to

implement substantial schemes to bring forth health equity for all the affected individuals by

initiating health financing schemes with various state-level agencies through an authorized

section in the application (Figures 25.1–25.12).

### 25.2 System Architecture

Figure 25.1 System architecture.

Figure 25.2 DFD – Level 0.

### 25.3 UML Diagrams

Actor Specification

1. Government – The government forms a crucial part of this project. The government receives

a complete detailed report of analytics of any kind of disparities or anomalies based on

region, location, history, economy and records. The government after receiving the data will

take the appropriate measures to overcome these disparities.

2. Health Worker – A health worker belongs to a particular health institution. The job of the

health worker is to verify the data provided by the patients to the records present in the hospital. This verified data is then sent to the cloud where analytics on the data is performed.

The analytics is based on region, location, history, economy and records. The health worker

also has access to the health performance of their patients. This health tracking helps the

health workers organize routine check-ups based on their health.

3. Patient – The patient is the most important aspect of this project. A patient provides his or

her medical data. This data is then verified by the health workers. The patient will be given

a detailed description of their health in a patient dashboard. The patient dashboard tracks

health of each patient. The health tracking enables the software to send alerts to the patients

on any kind of medical update.

4. State Agencies – After the government analyses the reports, the government takes the help

of the state agencies to solve these medical disparities. The state agencies have access to the

health financing data along with a detailed description of how the government wants them

to help. The state agencies have no access to the private data of the patient.

Figure 25.3 DFD – Level 1.

Usecase Specification

1. Activity Scheduling

Description: This usecase is used to schedule activity for the health workers on the basis

of the analyzed information in order to remove disparities’.

Flow of Events

Basic Flow: The activity scheduling usecase makes use of data from analytics usecase and

generates a health worker schedule accordingly.

Pre-Conditions: Data Entry and Analytics usecases should have been invoked.

Post-Conditions: The activity schedule is displayed on the health worker dashboard.

2. Alerts

Description: Alerts are scheduled for all the users and dispatched to the patients whenever an activity is due such as a health checkup or a medical camp and dispatched to the

health workers to catch up on a scheduled activity.

Flow of Events

Basic Flow: Based upon the activity schedule and the data analytics, appropriate alerts are

sent to the users.

Pre-Conditions: Activity Scheduling and Analytics usecases must be invoked.

Post-Conditions: The alerts are displayed on the patient or the health worker’s dashboard.

Figure 25.4 UML usecase diagram.

Figure 25.5 UML activity diagram – Part (1).

3. Analytics

Description: All the exhaustive data that goes into the application is analyzed for patterns of medical disparities based on family and community issues and socio-economic

determinants.

Flow of Events

Basic Flow: The data entered into the application is analyzed and categorized based on several factors and sent to the other usecases and results from those usecases are combined

to obtain a holistic report.

Alternate Flow: The data is categorized into Economy-, Location-, History- and Recordsbased classifications.

Pre-Conditions: Data Entry and Health Tracking usecases must be invoked.

Post-Conditions: The report of the analyzed data is sent for activity scheduling and health

financing alerts and the report details are displayed on the government dashboard.

4. Data Entry

Description: A section to enter all the medical details as well as the various social and

economic details including unique identification details for the patient user and for registered identification details for the health workers.

Flow of Events

Basic Flow: Various fields are provided for the user to feed the medical data into the

application.

Pre-Conditions: Login and Registration usecases must be invoked.

Post-Conditions: The data collected from the patients are sent for validation and following

the validation, the data is given to health tracking and analytics usecases.

Figure 25.6 UML activity diagram – Part (2).

5. Government Dashboard

Description: A holistic report of the analyzed data is presented in the dashboard accessible to the authorized government authority to be used to bring about the appropriate

health interventions.

Flow of Events

Basic Flow: The analyzed data is illustrated with graphical representations in the interface

for the government that can be used to implement the appropriate health intervention

schemes.

Pre-Conditions: Data Entry and Analytics usecases must be invoked.

Figure 25.7 UML sequence diagram.

6. Health Financing

Description: Using the application’s analytics data, the government should be able to

implement substantial schemes to bring forth health equity for all the affected individuals by

initiating health financing schemes with various state-level agencies through an authorized

section in the application.

Flow of Events

Basic Flow: Provides the options for implementing health financing schemes for the government in collaboration with state agencies.

Pre-Conditions: Data Entry and Analytics usecases must be invoked.

Post-Conditions: The various health financing requirements are displayed in the government

dashboard.

7. Health Tracking

Description: A section that provides a health-tracking facility by means of detailed analytics of the patient’s individual health records furnished by the patient as well as the healthcare establishments from where the patient receives active treatment.

Figure 25.8 UML collaboration diagram.

Figure 25.9 UML state machine diagram.

Figure 25.10 UML class diagram.

Figure 25.11 UML component diagram.

Figure 25.12 UML deployment diagram.

Flow of Events

Basic Flow: It performs a continuous tracking of the patient’s medical data and provides an

insight of this tracking to the patient and the concerned health workers.

Pre-Conditions: Data Entry usecase must be invoked.

Post-Conditions: The health-tracking data is displayed in the patient’s dashboard and is also

sent for analytics.

8. Health Worker Dashboard

Description: A dashboard for every health worker belonging to every registered medical

institution that provides informative articles pertaining to the worker’s area of specialization.

Flow of Events

Basic Flow: It collects the various data regarding the activity schedule and the concerned

patients’ data for validation and displays them for the health worker.

Pre-Conditions: Health Tracking and Activity Scheduling usecases must be invoked.

9. Login

Description: The login section is for the users to login to the application using the unique

credentials provided during the registration phase.

Flow of Events

Basic Flow: It authenticates and allows a registered user to access the facilities of the

application.

Alternative Flow: The user is directed to patient dashboard or health worker dashboard or

government dashboard.

Pre-Conditions: Registration usecase must be invoked.

Post-Conditions: The user is able to enter the application.

10. Logout

Description: The logout option is included in the user’s user interface enabling the user

to log out of the application at any time the user wants to.

Flow of Events

Basic Flow: The logged in user is enabled to safely log out of the application.

Alternative Flow: Nil.

Pre-Conditions: Login usecase must be invoked.

Post-Conditions: The user exits the application.

11. Patient Dashboard

Description: A catered dashboard for every patient user with articles relating to the

patient’s present medical conditions and the possible ailments that the patient may be prone

to, obtained by analysis of the patient’s medical records.

Flow of Events

Basic Flow: It collects the various data that are pertinent to the particular patient such as

health-tracking records and medical articles and displays them to the patient.

Alternative Flow: Nil.

Pre-Conditions: Registration and Login usecases must be invoked.

Post-Conditions: Nil.

12. Registration

Description: The users of the application are registered with unique credentials and categorized as patients, health workers or a government authority.

Flow of Events

Basic Flow: It allows new users to register for the application with new credentials.

Alternative Flow: Nil.

Pre-Conditions: Internet connectivity is required.

Post-Conditions: The user is directed to the login page.

13. Validation of Medical Data

Description: The details entered by the patient will be corroborated by the details furnished by the respective hospital medical records of the patients.

Flow of Events

Basic Flow: The data obtained from the patients is validated by the health workers using the

patient’s medical records.

Alternative Flow: Nil.

Pre-Conditions: Data entry usecase must be invoked.

Post-Conditions: The validated medical data is sent to the analytics and health-tracking

modules.

14. Economy-based

Description: This usecase is used to do a deep data analysis based on the economic data

provided by the user.

Flow of Events

Basic Flow: Here, the data are classified based on the user’s annual income, money previously spent on medical treatments and parent’s income.

Alternative Flow: Nil.

Pre-Conditions: Data entry usecase must be invoked.

Post-Conditions: The report of the analysis is sent to the analytics usecase.

15. History-based

Description: This usecase analyses data based on the medical history of the patient.

Flow of Events

Basic Flow: Here, the data is analyzed based on patient’s medical data along with the hereditary medical data of their family members.

Alternative Flow: Nil.

Pre-Conditions: Data entry usecase must be invoked.

Post-Conditions: The report of the analysis is sent to the analytics usecase.

16. Location-based

Description: This usescase analyses the data based on the geographical location of the

patients.

Flow of Events

Basic Flow: Here a detailed analysis is done based on the demographic details of the patients.

Alternative Flow: Nil.

Pre-Conditions: Data entry usecase must be invoked.

Post-Conditions: The report of the analysis is sent to the analytics usecase.

17. Records-based

Description: This usescase analyses the data based on the present medical data of the

patients.

Flow of Events

Basic Flow: Here a collective analysis is done based on the current medical data of the patients.

Alternative Flow: Nil.

Pre-Conditions: Data entry usecase must be invoked.

Post-Conditions: The report of the analysis is sent to the analytics usecase.

---

## 📊 UML Modeling Suite for EQUIHEALTH

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

- **Previous Chapter**: [Design of UML Diagrams for Online Pharmacy Management System](Chapter_24_Design_of_UML_Diagrams_for_Online_Pharmacy_Management_System.md)
- **Next Chapter**: [Design of UML Diagrams for an OTT-Based System - MINI REEL](Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_System_MINI_REEL.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/Overall_Books.md`](../Overall_Books.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
