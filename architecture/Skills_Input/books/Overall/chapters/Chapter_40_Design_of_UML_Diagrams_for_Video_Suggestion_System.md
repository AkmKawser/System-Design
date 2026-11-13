# Chapter 40: Design of UML Diagrams for Video Suggestion System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 405–417 (Total: 13 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 39: Design of UML Diagrams for STARTUP MEET](Chapter_39_Design_of_UML_Diagrams_for_STARTUP_MEET.md) | [📚 Book Index](../README.md)

---

## 📌 Chapter Overview

Chapter 40 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Video Suggestion System**. 
This case study presents an end-to-end software engineering analysis for **Video Suggestion System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **40.1 Problem Statement**
- **40.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 40

Design of UML Diagrams for

Video Suggestion System

### 40.1 Problem Statement

The Video Suggestion System is used in social networking platforms such as YouTube and

Facebook. The ultimate aim of this system is to suggest the videos to the users based on the factors

such as trending, similar views of the people and their search results. The Video Suggestion System

will be found helpful in place of searching a video based on the preference and taste of the user

and it also found that it can play a role in the entertainment sector. The system begins with the

collection of the history or activities of the users, processing the collected data, creating dataset for

suggesting videos and finally when people refresh for the suggestion, it loads videos based on the

dataset (Figures 40.1–40.14).

### 40.2 UML Diagrams

Actor Specification

1. Administrator – Administrator is the superuser who has the access to edit and view all the

records in the database.

2. Normal User – Normal user who will be surfing the videos on the internet, get suggested

videos and whose history and recorded will be recorded for further suggestions.

Usecase Specification

1. Store Personal Information

Description: This function stores the personal information of the normal user in the

database.

Flow of Events

Basic Flow: This function stores the personal information of the normal user in the database.

Alternative Flow: NIL.

DOI: 10.1201/9781003287124-40

Pre-Conditions: Gets write access for the user’s personal information in the database.

Post-Conditions: Check whether the record is stored in the database.

2. Retrieve Locality Information

Description: This function retrieve the locality information from the personal of the

current user.

Flow of Events

Basic Flow: Retrieves the location information of the given user.

Alternative Flow: NIL.

Figure 40.1 UML usecase diagram.

Figure 40.2 UML activity diagram – Main scenario.

Pre-Conditions: Gets the read access to the user location in the database.

Post-Conditions: Return the location of the current user.

3. Display Login Error

Description: Functionality involves throwing an error if the username or password

doesn’t match.

Flow of Events

Basic Flow: It calculates the trending videos for the given locality based on the views of the

users in that location.

Figure 40.3 UML activity diagram – Other videos watched by similar user scenario.

Figure 40.4 UML activity diagram – Paid promotion videos scenario.

Figure 40.5 UML activity diagram – Similar genre videos scenario.

Alternative Flow: NIL.

Pre-Conditions: Get the input as the location of the current user.

Post-Conditions: Returns the video ids of trending videos.

4. Retrieve Current User History

Description: This function retrieves the history details of the current user.

Flow of Events

Basic Flow: It retrieves the recent history of the given user.

Alternative Flow: NIL.

Figure 40.6 UML activity diagram – Similar tag videos scenario.

Figure 40.7 UML activity diagram – Trending videos scenario.

Figure 40.8 UML Activity diagram – Video attributes scenario.

Pre-Conditions: Check the connection of the database and gets access to read user history

in the database.

Post-Conditions: Returns the video ids of the recent history.

5. Common Genre from History

Description: This function returns common genres from the users’ history.

Flow of Events

Basic Flow: It extracts the common genre from the user history.

Alternative Flow: NIL.

Pre-Conditions: The student should have an account in a bank.

Post-Conditions: NIL.

6. High Viewed of Given Genre

Description: This function returns highly viewed videos for the given genre.

Flow of Events

Basic Flow: It fetches the highly viewed videos for the given genre.

Alternative Flow: NIL.

Figure 40.9 UML sequence diagram.

Figure 40.10 UML collaboration diagram.

Figure 40.11 UML state chart diagram.

Figure 40.12 UML class diagram.

Pre-Conditions: Gets the read access for the videos and their attributes in the database and

also receive the genre as input.

Post-Conditions: Returns the high viewed video id for the given genre.

7. Paid Promotion Videos for the Targeted User

Description: This function returns the video ids of specially promoted by the administrator.

Flow of Events

Basic Flow: It checks whether the targeted attributes match with the current user (such as

locality and gender) and if matches, pass the video to the suggestion.

Alternative Flow: NIL.

Pre-Conditions: Check whether the administrator posted promotion videos.

Post-Conditions: Return the video id of the promoted videos.

8. Common Tags from the History

Description: This function returns common tags using the recent history of the user.

Flow of Events

Basic Flow: It extracts the common tags from the user history.

Alternative Flow: NIL.

Pre-Conditions: Gets the inputs from user history.

Post-Conditions: Returns list of common tags.

9. High Viewed Videos of the Given Tags

Description: This function returns highly viewed videos for the given tag.

Flow of Events

Basic Flow: It fetches the current highly viewed videos for the given tags.

Alternative Flow: NIL.

Figure 40.13 UML component diagram.

Pre-Conditions: Gets the read access for the videos and their attributes in the database and

also receive the tags as input.

Post-Conditions: Returns video ids for the given tags.

10. Retrieve Other Users History

Description: This function retrieves the other similar users’ history from the database.

Flow of Events

Basic Flow: It fetches the videos from the database based on the user history.

Alternative Flow: NIL.

Pre-Conditions: Checks the database connection and gets access to read other common user

history.

Post-Conditions: Return the videos of the other similar user.

11. Other Videos Watched by Users Who Has Similar Videos

Description: This function returns the similarly viewed videos ids using the history of

other users.

Flow of Events

Basic Flow: It matches the current user history with other user history and retrieves the

similar videos watched by the other users.

Figure 40.14 UML deployment diagram.

Alternative Flow: NIL.

Pre-Conditions: Gets the current user history and other common users history as input.

Post-Conditions: Returns the videos id of a similarly viewed video.

12. Video Suggestion

Description: This function suggests the video with the related attributes such as thumbnail, upload time, channel, views using the video id as input.

Flow of Events

Basic Flow: It prioritize the video Ids received as input and sends the video and its related

attributes, when the user request for the suggestion of videos.

Alternative Flow: NIL.

Pre-Conditions: Gets read access to the videos and related attributes in the database and also

receives the list of video Id for the suggestion.

Post-Conditions: Returns the video and its related attributes.

Index

action state 7

activation bar 10

activity diagram 2, 6, 32–33, 51, 64–67, 78, 89, 97,

107, 115–116, 124, 131, 140, 149, 159, 169,

178, 186, 192–193, 200, 211, 220, 228, 238,

249–251, 270–271, 281, 288, 296–297, 304,

315, 327, 335, 343, 350, 358, 368–369, 380,

391, 399, 406–408

actor 4

actors involved 6

aggregation 17, 18

Alpha testing 1

alt fragment 13

alternate flow 6

Artifact 20, 21

association 5, 17, 20, 22

association class 19

Asynchronous message 11

attribute 17

Beta testing 2

business functions 4

business process 4

choice point 16

class 3, 17

class diagram 2, 17, 31, 51, 63, 77, 88, 101, 110, 119, 127,

135, 143, 153, 162, 172, 180, 188, 197, 203,

213, 223, 231, 241, 258–259, 274, 284, 291,

300, 308, 318, 330, 337, 346, 353, 362, 372,

384, 394, 402, 410

class relationships 17

collaboration diagram/communication diagram 2, 13,

36, 53, 67, 82, 92, 99, 109, 118, 125, 133,

142, 151, 161, 171, 179, 187, 196, 202, 212,

222, 230, 240, 253, 273, 283, 290, 299, 306,

317, 329, 336, 345, 352, 360, 371, 382, 393,

401, 409

component 4, 20

component diagram 2, 20, 37, 53, 70, 83, 92, 110, 120,

128, 135, 143, 153, 162, 172, 181, 189, 197,

203, 214, 224, 231, 241, 259–260, 275, 284,

291, 301, 308, 318, 330, 338, 346, 353, 363,

373, 385, 394, 402, 411

composition 17, 18

conditional message 12

construction 1

Context Diagram 24

Create Message 12

data flow diagram 24, 85, 267

decision 8

deep history 16

dependency 6, 17, 18, 22

deployment diagram 2, 21, 37, 54, 71, 83, 93, 101, 111,

121, 128, 136, 144, 154, 163, 173, 181, 189,

198, 204, 215, 225, 232, 242, 261, 275, 285,

292, 301, 309, 319, 331, 338, 347, 354, 364,

373, 385, 395, 403, 412

derived attributes 17

Destroy message 12

destruction 12

Device node 21

diagrammatic tool 2

directed association 5, 17, 18, 22

Do – Action 15

elaboration 1

end state 15

Entry – Action 15

events 3

Execution Environment Node 21

Exit – Action 15

Extend 5

Final State 7, 15

Flow final 9, 15

focus of control 10

Fork 8

Forward stimulus 14

fragments 12

functional requirements 3

generalization 6, 17, 18

Guard 12

healthcare service 23

horizontal swimlane 7

inception 1

Include 5

Initial State 7, 15

interface 19, 20

Join 8

Junction Point 15

lifeline 10

Link 14

loop fragment 13

looping message 12

Main Flow 6

merge 9

message 10

message types 11

methods 17

Nesting of fragments 13

node 21

object 3, 8, 10, 14

operations 17

opt fragment 12

parallel activities 3

port 20, 21

Post Conditions 6

Preconditions 6

process 7

provider interface 19, 20

realization 17, 19

reply message 11

required interface 19, 20

Return Message 11

Reverse stimulus 14

scope 4

self link 14

Self-Transition 9, 15

sequence diagram 2, 10, 35, 52, 68, 80–81, 91, 98, 108,

117, 126, 132, 141, 150, 160, 170, 179, 187,

194–195, 201, 211, 221, 229, 239, 252–253,

272, 282, 289, 298–299, 305, 316, 328, 336,

344, 351, 359, 369–370, 381, 392, 400, 409

sequential activities 3

shallow history 16

Signal Accept State 10

Signal Send State 9

Software Development Process 1

start state 15

state 3, 15

state chart diagram/state machine diagram 2, 14, 34, 52,

68–70, 79, 90, 100, 109, 118, 127, 134, 142, 152,

161, 171, 180, 188, 196, 202, 212, 222, 230,

240, 255–257, 274, 283, 290, 300, 307, 317, 329,

337, 345, 352, 361, 371, 383, 393, 401, 410

stereotype 12

subactivity 10

submachine state 16

swimlanes 7

synchronization 8

synchronous message 11

system architecture 24, 267

System Boundary 4

transition 1, 3, 9, 15

UML (Unified Modeling Language) 1

Unified Process 1

Usecase 4

Usecase Diagram 2, 27, 47, 62, 76, 87, 96, 106, 114, 124,

130, 140, 148, 158, 168, 178, 186, 192, 200,

210, 220, 228, 238, 248, 269, 280, 288, 296,

304, 314, 326, 334, 342, 350, 358, 368, 379,

390, 398, 406

Usecase ID 6

Usecase Name 6

Usecase Template 6

vertical swimlane 7

wait semantics 11

---

## 📊 UML Modeling Suite for Video Suggestion System

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

- **Previous Chapter**: [Design of UML Diagrams for STARTUP MEET](Chapter_39_Design_of_UML_Diagrams_for_STARTUP_MEET.md)
- **Next Chapter**: None (Last Chapter)
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
