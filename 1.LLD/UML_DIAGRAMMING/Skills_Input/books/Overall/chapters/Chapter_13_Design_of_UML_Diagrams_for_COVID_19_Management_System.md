# Chapter 13: Design of UML Diagrams for COVID-19 Management System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 147–156 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 12: Design of UML Diagrams for My Helper](Chapter_12_Design_of_UML_Diagrams_for_My_Helper.md) | [📚 Book Index](../README.md) | [Chapter 14: Design of UML Diagrams for Car Care &rarr;](Chapter_14_Design_of_UML_Diagrams_for_Car_Care.md)

---

## 📌 Chapter Overview

Chapter 13 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for COVID-19 Management System**. 
This case study presents an end-to-end software engineering analysis for **COVID-19 Management System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **13.1 Problem Statement**
- **13.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 13

Design of UML

Diagrams for COVID-19

Management System

### 13.1 Problem Statement

The all in one COVID-19 management system simplifies the entire process of decreasing the

virus load in the community by digitalization. It includes tracking and treating COVID-19

patients and monitoring the spread of the virus. It aims to assist healthcare organizations and

governments to assess patient risk profiles and provide awareness to common people by connecting them with virtual care capabilities. With the current epidemiological situation of COVID-19,

there is a high demand to reduce contact between persons and digitize the whole process. This

will effectively reduce the infection rate, help the common people and empower medical professionals across the world to help more patients through telemedicine and virtual care.

Functionalities:

1. Medical Professionals (Doctors/Nurses): Can monitor the oxygen level, blood pressure level,

temperature, symptoms, medicine intake and diet of the registered patient. All the information of the patients from screening to discharge can be viewed. Medicines can also be

prescribed to a specific patient.

2. COVID-19 Patients: View the data shared by the doctor, home quarantined patients can

update data and checklist of medical shops in their locality.

3. Common People: Check the number of people infected (symptomatic and asymptomatic)

and death in their locality ranging from current street, 500 m, 1 km, 5 km, 10 km and view

a blog where recovered persons share their experience.

4. COVID-19 Essentials Seller: Can stock up essentials like masks and gloves according to

infection in an area. Medical shops nearby the area will be listed.

DOI: 10.1201/9781003287124-13

5. Corporation Worker Head: Workers will be assigned to disinfect Covid-affected areas regularly based on infection data and updates status.

6. Admin: Updates current number of infected persons in a locality (Figure 13.1–13.9).

Figure 13.1 UML usecase diagram.

### 13.2 UML Diagrams

Usecase Specification

1. Monitor Oxygen Levels, BP, Symptoms, etc.

Description: To monitor the oxygen level, blood pressure level, temperature, symptoms,

medicine intake and diet of the registered patient.

Flow of Events

Figure 13.2 UML activity diagram (part 1).

Figure 13.3 UML activity diagram (part 2).

Figure 13.4 UML sequence diagram.

Figure 13.5 UML collaboration diagram.

Figure 13.6 UML state machine diagram.

Basic Flow: Correctly choose a patient to view the respective details.

Alternative Flow: Nil.

Pre-Conditions: Patient has to record the set of details precisely.

Post-Conditions: Medical professionals can prescribe medicines if required.

2. View Patient Info from Screening to Discharge

Description: Enables the medical professional to view all patients’ records from screening to discharge.

Flow of Events

Basic Flow: Date and time must be entered to view patients’ records within that period.

Alternative Flow: Nil.

Pre-Conditions: All patients must be registered and personal details and health conditions

must be entered with credibility.

Post-Conditions: Nil.

Figure 13.7 UML class diagram.

Figure 13.8 UML component diagram.

3. Prescribe Medicines

Description: Enables doctors to prescribe medicines to specific patients.

Flow of Events

Basic Flow: Enter the appropriate medicine with dosage for the patient.

Alternative Flow: Nil.

Pre-Conditions: Doctors must have viewed the patient’s health conditions.

Post-Conditions: Nil.

4. Update Data by Home Quarantined Patients

Description: Enable home quarantined patients to update their health conditions.

Flow of Events

Basic Flow: Enter temperature, oxygen level and other symptoms.

Alternative Flow: Nil.

Pre-Conditions: Patients must be registered with credible credentials.

Post-Conditions: Nil.

5. View Data Shared by Doctor

Description: Enables patient to view prescription and other remarks of the doctor.

Flow of Events

Basic Flow: View the data shared by the doctor when notified.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

Figure 13.9 UML deployment diagram.

6. Buy Medicine

Description: Enables patients to view the list of medical shops in their locality.

Flow of Events

Basic Flow: The patient will be shown a list of medical shops based on the place he/she is

located.

Alternative Flow: Nil.

Pre-Conditions: All available medical shops must be listed or updated by the COVID essential shop.

Post-Conditions: Nil.

7. Read Blog of Recovered Patients

Description: Enables users to read blogs of recovered patients.

Flow of Events

Basic Flow: View all the blogs uploaded by several recovered patients.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

8. View the Number of Deaths in the Locality

Description: Enables users to view the number of deaths in the locality.

Flow of Events

Basic Flow: The total number of deaths in a locality is displayed.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

9. View the Number of Infected People in the Locality

Description: Enables users to view the exact number of infected people in their locality.

Flow of Events

Basic Flow: The exact number of infected people in a particular locality is displayed.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

10. List all Medical Shops in the Locality

Description: Enables the COVID essentials shops to list all the medical shops in the locality.

Flow of Events

Basic Flow: All available medical shops in the locality is entered and listed.

Alternative Flow: Nil.

Pre-Conditions: COVID essential shops should be registered.

Post-Conditions: Can be viewed by patients who want to buy medicines.

11. Update Status of Cleanliness

Description: Enables corporation worker head to update the status of cleanliness after a

particular area has been disinfected.

Flow of Events

Basic Flow: Updating the status of cleanliness like cleaned/not cleaned/in progress.

Alternative Flow: Nil.

Pre-Conditions: Checking of the number of infected people in the locality.

Post-Conditions: Assign workers to disinfect the particular area.

12. Assign Workers to Disinfect in an Area

Description: Workers are assigned according to the infection rate in the locality.

Flow of Events

Basic Flow: After assigning workers, status is changed by the corporation worker head to

‘assigned workers’.

Alternative Flow: Nil.

Pre-Conditions: The head has to view the number of infected people in the locality from

time to time.

Post-Conditions: Update status of cleanliness.

13. Register

Description: All users except the general public must register to ensure their access control and make use of their distinct functions in the COVID-19 management system.

Flow of Events

Basic Flow: All the details must be filled correctly before submitting.

Alternative Flow: Invalid credentials leads to improper registration.

Pre-Conditions: Nil.

Post-Conditions: Authentication is performed to ensure the proper functioning of access

control list.

14. Authenticate User

Description: To check the access control of the user in this system.

Flow of Events

Basic Flow: The profile of the user is checked and given distinct functions respectively.

Alternative Flow: In case of failed authentication, the user won’t be able to use the

system.

Pre-Conditions: Registration.

Post-Conditions: Nil.

15. Update the Current Number of Infected People

Description: Enables the admin to update the exact number of infected people belonging to a place frequently.

Flow of Events

Basic Flow: Enter the number of people infected and their place.

Alternative Flow: Nil.

Pre-Conditions: Admin must be registered to have administrative rights over updating the

number of people infected.

Post-Conditions: Nil.

16. Stock Up Masks and Gloves

Description: Enables the Covid essentials shops to show their updated stock of the essentials like masks, gloves, hand sanitizers and other disinfectants.

Flow of Events

Basic Flow: Update/increase stock of essential products.

Alternative Flow: Nil.

Pre-Conditions: View mask demand.

Post-Conditions: Nil.

17. View Mask Demand

Description: Enables the COVID essential shops to view the demand for masks as the

number of infected people in locality increases.

Flow of Events

Basic Flow: Analyze mask demand by viewing number of infected people in a locality.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Stock up all essentials.

---

## 📊 UML Modeling Suite for COVID-19 Management System

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

- **Previous Chapter**: [Design of UML Diagrams for My Helper](Chapter_12_Design_of_UML_Diagrams_for_My_Helper.md)
- **Next Chapter**: [Design of UML Diagrams for Car Care](Chapter_14_Design_of_UML_Diagrams_for_Car_Care.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
