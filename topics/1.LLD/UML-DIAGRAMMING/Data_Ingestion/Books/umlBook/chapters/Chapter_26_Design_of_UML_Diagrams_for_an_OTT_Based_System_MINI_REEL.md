# Chapter 26: Design of UML Diagrams for an OTT-Based System - MINI REEL

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 279–286 (Total: 8 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 25: Design of UML Diagrams for EQUIHEALTH](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md) | [📚 Book Index](../UML_Book.md) | [Chapter 27: Design of UML Diagrams for e-Med Medical Assistance Tool &rarr;](Chapter_27_Design_of_UML_Diagrams_for_e_Med_Medical_Assistance_Tool.md)

---

## 📌 Chapter Overview

Chapter 26 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for an OTT-Based System - MINI REEL**. 
This case study presents an end-to-end software engineering analysis for **an OTT-Based System - MINI REEL**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **26.1 Problem Statement**
- **26.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 26

Design of UML Diagrams

for an OTT-Based

System – MINI REEL

### 26.1 Problem Statement

An over-the-top (OTT) media service is a streaming media service offered directly to viewers

via the internet. The OTT media can be streamed anywhere with just the use of an internet

connection. The scope of this project lies in the maximised use of the internet by the current

generation. The system aims at providing a fun-filled and informative services that they would

be able to access easily from their place. This system includes streaming of shows and movies

that could be viewed by the users and an administrator governing the updates in the OTT

based on the schedule of the show or movie release. Users can have a trial package of the services offered for 1 month and further subscriptions are based on the amount paid categorised

as normal users and premium users. Creating an account involves payment to the services provided. Hence the trial users could use the trial package for a month and create an account for

them maintaining a secret password that makes their account safe from other people accessing

it. The premium users have the privilege of providing suggestions of the shows in the discussion room. All the users should be provided with the facility of a chat room where the users

can chat and express their views and comments. The administrator will have control over the

shows broadcasted and maintain a proper timeline of the shows, movies and live shows. News

feeds highlighting the recent updates in the world will also be available in MINIREELS in a

brief format. Users can also add their favourite videos to LIKES list and watch them whenever

needed (Figures 26.1–26.8).

DOI: 10.1201/9781003287124-26

### 26.2 UML Diagrams

Actor Specification

1. Administrator – Takes care of all updates of shows and movies along with database

maintenance.

2. Normal User – Watch shows and movies streamed upon creation of an account by paying a

specified amount.

3. Trial User – Watch shows and movies streamed without account creation and use the trial

service for a month.

4. Premium User – Watch shows and movies streamed upon creation of an account by paying

amount higher than the normal user.

5. User – Premium user, trial user and normal user are generalized as users who can watch

movies, show and use chat room.

Usecase Specification

1. Maintain Database and Follow Timeline Scheduled

Description: Maintain a proper database and schedule the update of shows, movies, etc.

Flow of Events

Basic Flow: Maintain the database.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Update shows and movies based on the database.

2. Discussion Room

Description: A chat room where only premium users can provide suggestions or complaints to the administrator directly.

Flow of Events

Basic Flow: Discussion Room.

Figure 26.1 UML usecase diagram.

3. Update Shows, Movies, Live Stream and Recent News

Description: Update the shows, movies or news based on a schedule maintained so that

users can watch it.

Flow of Events

Basic Flow: Update of shows and movies.

Figure 26.2 UML activity diagram.

Alternative Flow: Nil.

Pre-Conditions: Creation of Premium Account.

Post-Conditions: Nil.

Figure 26.3 UML sequence diagram.

Alternative Flow: Nil.

Pre-Conditions: Maintain a proper database and schedule the updates.

Post-Conditions: Users watch the updated shows, movies, news, etc.

4. Maintain LIKES List for Every User and Upload Videos Based on It

Description: Maintain a LIKES list for every user and upload videos based on it so that

it would interest the users.

Flow of Events

Basic Flow: Maintain LIKES list.

Alternative Flow: Normal Update of shows, movies, etc.

Pre-Conditions: Users save videos in the LIKES list.

Post-Conditions: Update of videos.

Figure 26.4 UML collaboration diagram.

Figure 26.5 UML state chart diagram.

5. Creation of Account

Description: Normal and premium users create a account by paying a specified amount

and enjoy the services.

Flow of Events

Basic Flow: Creation of account.

Alternative Flow: For 1 month, no account need to be created. Users can use the trial version.

Pre-Conditions: Nil.

Post-Conditions: Users can watch videos and use chat room.

Figure 26.6 UML class diagram.

Figure 26.7 UML component diagram.

6. Premium Account Creation

Description: Creates an account for premium users by paying an amount higher than

the normal user.

Flow of Events

Basic Flow: Creation of Premium account.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Watch videos and can use discussion rooms where they can discuss about

suggestions and complaints.

7. Normal Account Creation

Description: Creates an account for normal users by paying a specified amount.

Flow of Events

Basic Flow: Normal account creation.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Watch videos and use chat room to chat with other users.

8. Chat Room

Description: A room where users can chat among themselves.

Flow of Events

Basic Flow: Chat room.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Creation of account. Trial users can enjoy it only for a month.

Figure 26.8 UML deployment diagram.

9. Save Videos in LIKES

Description: Save videos, shows or movies in LIKES list and can watch it later.

Flow of Events

Basic Flow: Save the videos in the LIKES list.

Alternative Flow: Nil.

Pre-Conditions: Creation of account. Trial users can use it just for a month.

Post-Conditions: Get videos related to those LIKED videos.

10. Watch Shows, Movies, Live Shows and News Updates

Description: Watch shows, movies and news updated by the administrator.

Flow of Events

Basic Flow: Watch videos.

Alternative Flow: Nil.

Pre-Conditions: Creation of account. Trial users can use it just for a month.

Post-Conditions: Save videos in LIKES list and can watch them later.

---

## 📊 UML Modeling Suite for an OTT-Based System - MINI REEL

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

- **Previous Chapter**: [Design of UML Diagrams for EQUIHEALTH](Chapter_25_Design_of_UML_Diagrams_for_EQUIHEALTH.md)
- **Next Chapter**: [Design of UML Diagrams for e-Med Medical Assistance Tool](Chapter_27_Design_of_UML_Diagrams_for_e_Med_Medical_Assistance_Tool.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
