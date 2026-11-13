# Chapter 22: Design of UML Diagrams for Job Seeker Portal System

> **Book**: *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy (CRC Press, 2022)  
> **Pages**: 227–236 (Total: 10 pages)  
> **Classification**: Industrial Case Study & Diagram Suite  
> **Navigation**: [&larr; Chapter 21: Design of UML Diagrams for Smart Traffic Management System](Chapter_21_Design_of_UML_Diagrams_for_Smart_Traffic_Management_System.md) | [📚 Book Index](../README.md) | [Chapter 23: Design of UML Diagrams for AAROGYA SETU - Health Care APP &rarr;](Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP.md)

---

## 📌 Chapter Overview

Chapter 22 of *UML Diagramming: A Case Study Approach* focuses on **Design of UML Diagrams for Job Seeker Portal System**. 
This case study presents an end-to-end software engineering analysis for **Job Seeker Portal System**, establishing formal requirements, data-flow models, and complete UML diagram specifications.

---

## 📑 Core Topics & Sections

- **22.1 Problem Statement**
- **22.2 UML Diagrams**

---

## 📝 Detailed Chapter Summary & Content

Chapter 22

Design of UML Diagrams for

Job Seeker Portal System

### 22.1 Problem Statement

Job seekers work hard to gain the right skills and knowledge to give them an edge over others in the

role they seek. However, at times, despite their best efforts, one may find it difficult to move a step

closer to this sought-after job. Hence a platform for listing out the availability of jobs irrespective of

the field is required. Furthermore, a job site serves a dual purpose. On one hand, it lists out the availability of jobs to candidates, and on the other, it serves as a database of registered candidate’s profiles

for companies to shortlist. The objective is to develop a software solution to predict the availability

of jobs based on location, sectors, package, platform, interest and eligibility. As it is important to

keep the candidates engaged during their job search, it is important to provide facets on the abovementioned criteria so that they can narrow down to the jobs of their choice (Figures 22.1–22.8).

### 22.2 UML Diagrams

Actor Specification

1. Admin – Verifies the company/seeker and maintains the system.

2. Recruiter – Posts job vacancies and its requirements.

3. Seeker – Can apply for a job posting.

Usecase Specification

1. Approve New Companies

Description: Checks the credibility of the company and admits the company into the

system.

Flow of Events

Basic Flow: Verifies the Company’s information.

Pre-Conditions: Checking the proofs submitted.

Post-Conditions: Background checks.

DOI: 10.1201/9781003287124-22

Figure 22.1 UML usecase diagram.

Figure 22.2 UML activity diagram.

Figure 22.3 UML sequence diagram.

Figure 22.4 UML collaboration diagram.

Figure 22.5 UML state machine diagram.

Figure 22.6 UML class diagram.

Figure 22.7 UML component diagram.

2. Deletion of Fraudulent Companies

Description: The admin can delete the company from the system if it is proven to be a

false/fraudulent company.

Flow of Events

Basic Flow: Deletion of a company from the system.

Pre-Conditions: Rechecking the submitted proof.

Post-Conditions: From feedback from job seekers.

3. Maintenance/Updating

Description: Refers to change an existing information in the system to fix errors or

enhance functionality and deleting outdated information and updating of new data into

the system.

Flow of Events

Basic Flow: Modifying and updating of the database based on the various criteria.

Pre-Conditions: Status of each company/seeker.

Post-Conditions: Based on the feedback received from recruiters/seekers.

4. Feedback

Description: Getting input from recruiter/seeker to verify the credibility of the users and

to modify/update the system for better enhancements/quality.

Flow of Events

Figure 22.8 UML deployment Diagram.

Basic Flow: Input from both recruiter and seeker.

Pre-Conditions: The feedback collected must be from the registered users of the system.

Post-Conditions: Nil.

5. Registration

Description: Every recruiter/seeker must first register to avail the opportunity to use the

system.

Flow of Events

Basic Flow: Every user must submit the needed requirements for registration.

Pre-Conditions: The proofs/ID must be credible.

Post-Conditions: Nil.

6. Profile

Description: This contains the information which will be displayed to all other users of

the system.

Flow of Events

Basic Flow: The information available in the profile should be credible.

Pre-Conditions: Only required information to be displayed.

Post-Conditions: Additional information can be added.

7. Recruiter Login

Description: The recruiter/company login through a separate login page.

Flow of Events

Basic Flow: Login into the system using the recruiter password.

Alternative Flow: Logins through alternate means provided by admin (Forgot_password).

Pre-Conditions: Username and password must be correct.

Post-Conditions: Can change username/password.

8. Manage Profile

Description: Displays the information about the company.

Flow of Events

Basic Flow: Display Company information.

Pre-Conditions: Can input the credible information about the company.

Post-Conditions: Update the required information.

9. Post Job Vacancy

Description: Can post a job vacancy and the required information about the field, category and salary and so on about the job.

Flow of Events

Basic Flow: Post a job vacancy with the required details.

Pre-Conditions: Should post all the details that the seeker must know.

Post-Conditions: Can post what is needed from the seeker for the required post.

10. Job Requirements

Description: Displays the information of the job posted.

Flow of Events

Basic Flow: Job requirement information.

Pre-Conditions: Information about what is to be expected from the seeker.

Post-Conditions: Additional requirements along with the existing information from the

company.

11. Delete Job Vacancy

Description: If a job vacancy is filled or if it’s no longer needed, the company could delete

the job posting from the system.

Flow of Events

Basic Flow: Deletion of job posting if the post is filled.

Alternative Flow: Deletion of job post if it’s no longer needed.

Pre-Conditions: The recruiter should only delete the job posting for an appropriate reason.

Post-Conditions: Can notify the admin after the change is made.

12. Communicate with Job Seeker

Description: If a job seeker applies for a job vacancy, the recruiter should communicate

with the seeker to provide the information such as interview date, company test and so on.

Flow of Events

Basic Flow: Communication between recruiter and seeker through the system.

Alternative Flow: Nil.

Pre-Conditions: The seeker must satisfy the required job specification for the posting.

Post-Conditions: Nil.

13. Manage Account

Description: This detail actions such as change/update username and password and deletion of the account of the recruiter.

Flow of Events

Basic Flow: Updation/deletion of account.

Alternative Flow: Nil.

Pre-Conditions: Must be a registered user.

Post-Conditions: Nil.

14. Seeker Login

Description: The job seeker logins through a separate login page.

Flow of Events

Basic Flow: Seeker login through password.

Alternative Flow: Logins through alternate means provided by admin (Forgot_password).

Pre-Conditions: Username and password must be correct.

Post-Conditions: Can change username/password.

15. Manage Profile/Seeker Details

Description: Displays the information of the seeker provided during registration.

Flow of Events

Basic Flow: Information about seeker.

Alternative Flow: Nil.

Pre-Conditions: Nil.

Post-Conditions: Nil.

16. Upload/Update CV

Description: The CV/resume, submitted in the profile section is a requirement for applying for jobs.

Flow of Events

Basic Flow: Upload/update resume.

Alternative Flow: Nil.

Pre-Conditions: Only credible information must be presented in the resume.

Post-Conditions: Can update the resume whenever it’s required.

17. View Job Vacancy

Description: A job seeker can browse through various job postings, based on category

and field and further constraints.

Flow of Events

Basic Flow: Browsing job vacancies.

Alternative Flow: Nil.

Pre-Conditions: Must be a registered user.

Post-Conditions: Nil.

18. Apply for Job Vacancy

Description: A job seeker, if interested in a certain job posting, can apply for that posting.

Flow of Events

Basic Flow: Applying for job vacancy.

Alternative Flow: Nil.

Pre-Conditions: Should meet the required requirements of the posting.

Post-Conditions: Upload CV.

19. Modify Account

Description: This detail actions such as change/update username and password and deletion of the account of the job seeker.

Flow of Events

Basic Flow: Account modification/updation.

Alternative Flow: Nil.

Pre-Conditions: Must be a registered user.

Post-Conditions: Nil.

---

## 📊 UML Modeling Suite for Job Seeker Portal System

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

- **Previous Chapter**: [Design of UML Diagrams for Smart Traffic Management System](Chapter_21_Design_of_UML_Diagrams_for_Smart_Traffic_Management_System.md)
- **Next Chapter**: [Design of UML Diagrams for AAROGYA SETU - Health Care APP](Chapter_23_Design_of_UML_Diagrams_for_AAROGYA_SETU_Health_Care_APP.md)
- **Central Book Guide**: [`Skills_Input/books/Overall/README.md`](../README.md)
- **Problem Bank Intake**: [`Skills_Output/UMLSkill_output/Problem Files/question bank.md`](../../../Skills_Output/UMLSkill_output/Problem%20Files/question%20bank.md)
