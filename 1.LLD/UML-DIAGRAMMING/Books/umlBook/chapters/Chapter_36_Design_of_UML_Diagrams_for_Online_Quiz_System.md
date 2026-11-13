# Chapter 36: Design of UML Diagrams for Online Quiz System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 367–376 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 35: Design of UML Diagrams for GUIDE - Dropshipping Website](Chapter_35_Design_of_UML_Diagrams_for_GUIDE_Dropshipping_Website.md) | [📚 Book Index](../UML_Book.md) | [Chapter 37: Design of UML Diagrams for Book Bank Management System &rarr;](Chapter_37_Design_of_UML_Diagrams_for_Book_Bank_Management_System.md)

---

## 📌 Chapter Overview

Chapter 36 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Online Quiz System**. 
This case study presents an end-to-end software engineering analysis for **Online Quiz System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **36.1 Problem Statement**
- **36.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 36

Design of UML Diagrams

for Online Quiz System

### 36.1 Problem Statement

Online learning is a part of many institution’s course offerings around the world. The scope of

online quiz systems increased in this pandemic situation. The objective of the system is to maintain

and improve the education rate by conducting quizzes (exams). The system acts as a bridge between

student and teacher to gain knowledge and monitor it by the institution (admin). This system provides teachers to know about the students in remote education. The delightful features of the system

are online teachers, remote tests, auto evaluation and feedback from students. Admin is responsible

for the registration of both teachers and students. Teachers define the number of questions, time of

the quiz, schedule for the quiz and they can edit it. At the end of a quiz, students can see the correct

answers and their performance (Figures 36.1–36.10).

### 36.2 UML Diagrams

Actor Specification

1. Admin – Admin is responsible for registering both teacher and student into the system.

2. Student – Students are opting for the courses and answering the quiz.

3. Teacher – Teachers create, conduct and evaluate the test.

Usecase Specification

1. Registration

Description: It is the process of admitting students and teachers into the course by the admin.

Flow of Events

Basic Flow: Admitting students and teachers.

Alternative Flow: Try again with valid details of student and teacher

DOI: 10.1201/9781003287124-36

Figure 36.1 UML usecase diagram

Figure 36.2 UML activity diagram – Scenario 1.

Figure 36.3 UML activity diagram – Scenario 2.

Figure 36.4 UML sequence diagram – Scenario 1.

Figure 36.5 UML sequence diagram – Scenario 2.

Pre-Conditions: Nil.

Post-Conditions: Nil.

2. Login as Teacher

Description: Teacher login into his profile and prepare an analysis quiz.

Flow of Events

Basic Flow: Allowing into the system.

Alternative Flow: Try again with valid data.

Pre-Conditions: Teachers should be registered before login.

Post-Conditions: Nil.

Figure 36.6 UML collaboration diagram.

Figure 36.7 UML state chart diagram.

3. Create Quiz

Description: Preparing quiz questions and test schedule.

Flow of Events

Basic Flow: Allow to create a test.

Alternative Flow: Can delete the test.

Pre-Conditions: Teachers should be registered into the course.

Post-Conditions: Nil.

4. Enter Quiz Question

Description: Teachers can enter the quiz questions while creating the quiz.

Flow of Events

Basic Flow: Allow to create questions for the test.

Figure 36.8 UML class diagram.

Alternative Flow: Can delete the question.

Pre-Conditions: Nil.

Post-Conditions: Nil.

5. Enter Quiz Answer

Description: Enter the quiz answers for the corresponding question for auto-correction.

Flow of Events

Basic Flow: Allow to enter the answer for the corresponding question.

Alternative Flow: Can delete answer and try again.

Pre-Conditions: Nil.

Post-Conditions: Nil.

Figure 36.9 UML component diagram.

Figure 36.10 UML deployment diagram.

6. Set Quiz Answer

Description: Schedule the test start time, end time and time for each question.

Flow of Events

Basic Flow: Allow to set the test time.

Alternative Flow: Try again with a valid time and format.

Pre-Conditions: Before scheduling the time, a quiz should be created.

Post-Conditions: Nil.

7. Edit Quiz

Description: Modify the quiz question, answer and schedule time.

Flow of Events

Basic Flow: Allow to edit the created quiz.

Alternative Flow: Nil.

Pre-Conditions: At least one quiz should be created.

Post-Conditions: Nil.

8. View Quiz Result and Feedback

Description: This option provides the teacher to view the quiz result and feedback from

students.

Flow of Events

Basic Flow: Allow to view and analyse test results.

Alternative Flow: Try again and select the answered one.

Pre-Conditions: Quiz should be answered by students.

Post-Conditions: Nil.

9. Login as Student

Description: Students enter into their profile by entering their id and password.

Flow of Events

Basic Flow: Allow into the system.

Alternative Flow: Nil.

Pre-Conditions: Students should be registered by the admin before login.

Post-Conditions: Nil.

10. Select the Quiz

Description: Students select the course and quiz before answering.

Flow of Events

Basic Flow: Allow into the quiz.

Alternative Flow: Try again and select a valid quiz.

Pre-Conditions: Students must be enrolled in the course.

Post-Conditions: Nil.

11. Answer the Quiz

Description: After selecting the quiz, the student starts answering the quiz.

Flow of Events

Basic Flow: Allow to answer the question.

Alternative Flow: Quiz time over and contact your teacher.

Pre-Conditions: Students start answering the quiz only in the scheduled time.

Post-Conditions: Student finishes the quiz before its end time.

12. Submit

Description: After answering the quiz or schedule time, quiz answers are submitted for

evaluation.

Flow of Events

Basic Flow: Allow to submit and leave the quiz.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

13. Auto Submit

Description: Quiz answers are submitted automatically, after schedule time gets over.

Flow of Events

Basic Flow: Force to leave the quiz.

Alternative Flow: Nil.

Pre-Conditions: Auto submit, only if time is over.

Post-Conditions: Nil.

14. Manual Submit

Description: Students can submit answers before end time by manually.

Flow of Events

Basic Flow: Allow to leave the quiz.

Alternative Flow: Please answer all questions you have a time.

Pre-Conditions: Students should answer all questions before manual submission.

Post-Conditions: Nil.

15. Feedback

Description: After submitting the quiz, students can post the queries regarding the test.

Flow of Events

Basic Flow: Allow to send the queries to the teacher.

Alternative Flow: Ignore the feedback.

Pre-Conditions: Nil.

Post-Conditions: Nil.

16. View Quiz Result

Description: Students can view their performance and correct answers.

Flow of Events

Basic Flow: Allow to view the result and performance.

Alternative Flow: Try again or you did not attend the test.

Pre-Conditions: The quiz should be over.

Post-Conditions: Nil.

---

## 📊 UML Modeling Suite for Online Quiz System

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

- **Previous Chapter**: [Design of UML Diagrams for GUIDE - Dropshipping Website](Chapter_35_Design_of_UML_Diagrams_for_GUIDE_Dropshipping_Website.md)
- **Next Chapter**: [Design of UML Diagrams for Book Bank Management System](Chapter_37_Design_of_UML_Diagrams_for_Book_Bank_Management_System.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/UML_Book.md`](../UML_Book.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
