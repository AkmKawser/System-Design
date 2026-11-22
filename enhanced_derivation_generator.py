# -*- coding: utf-8 -*-
import os
import re

def derive_components_and_steps(fig_title, category, clean_sys, arch_role, capabilities, ps_text):
    cat_lower = category.lower()
    
    # Extract top capability names
    cap_names = [c[0] for c in capabilities[:6]] if capabilities else ["User Authentication", "Service Catalog", "Core Transaction", "Status Tracking", "Reports & Audit"]
    cap_str = ", ".join(f"`{name}`" for name in cap_names)
    
    # Specific handling for Chapter 1
    if "introduction to uml" in clean_sys.lower() or "pyramid" in fig_title.lower() or "phase" in fig_title.lower():
        phase_name = fig_title.split(":")[-1].strip()
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Methodology & Phase Focus Selection**:
  - **Engineering Need**: Complex software systems require progressive risk reduction before heavy capital investment; `{phase_name}` is derived from the Unified Process (UP) lifecycle to address critical feasibility, architecture, or deployment risks.
  - **Artifacts & Deliverables**: Formulates core engineering blueprints (Vision documents, Use Case models, Architecture Baselines, or Release Bundles) required to pass the lifecycle milestone gate.
- **Role & Stakeholder Involvement**:
  - **Business Analysts & Project Sponsors**: Own feasibility assessment, budget bounds, and business justification.
  - **Software Architects & Engineers**: Establish architectural baselines, executable prototypes, and subsystem modularity.
- **Structural Organization & Taxonomy**:
  - Organizes modeling artifacts into **Structural Perspectives** (static code, database schemas, component wiring, hardware deployment) and **Behavioral Perspectives** (dynamic operational workflows, time-ordered sequence calls, entity state changes).

#### 🛠️ Step-by-Step Construction Guide

1. **Define Lifecycle Stage & Milestone Goals**:
   - Establish the primary engineering objective of `{phase_name}` within the Unified Process development framework.
2. **Identify Required Input Artifacts & Stakeholder Goals**:
   - Map business requirements, risk assessments, and architectural hypotheses into actionable engineering artifacts.
3. **Model Process Workflows & Iteration Cycles**:
   - Draw sequential workflow stages depicting the transition from requirements capture to implementation and verification.
4. **Establish Review Gates & Exit Criteria**:
   - Define concrete milestone checkpoints (e.g., Lifecycle Architecture Milestone, Initial Operational Capability) needed to authorize transition to the next phase.
5. **Verify Methodological Consistency**:
   - Ensure alignment between business feasibility criteria and technical software engineering artifacts."""

    # Identify domain actors based on system name
    primary_actor = "End User / Customer"
    secondary_actor = "External Payment / Verification Gateway"
    admin_actor = "System Administrator"
    
    sys_lower = clean_sys.lower()
    if "health" in sys_lower or "webmed" in sys_lower or "med" in sys_lower or "diet" in sys_lower:
        primary_actor = "Patient / Caregiver"
        secondary_actor = "Doctor / Diagnostic Lab / Ambulance Service"
        admin_actor = "Hospital Admin / Pharmacist"
    elif "inventory" in sys_lower or "textile" in sys_lower or "ration" in sys_lower:
        primary_actor = "Store Clerk / Salesperson"
        secondary_actor = "Supplier / Wholesale Vendor"
        admin_actor = "Inventory Manager / Warehouse Supervisor"
    elif "bus" in sys_lower or "ticketing" in sys_lower or "traffic" in sys_lower or "ride" in sys_lower:
        primary_actor = "Commuter / Passenger"
        secondary_actor = "Payment Gateway / Fleet Tracking GPS"
        admin_actor = "Transport Operator / Dispatch Officer"
    elif "bpo" in sys_lower or "placement" in sys_lower or "job" in sys_lower or "counselling" in sys_lower:
        primary_actor = "Client / Job Seeker / Student"
        secondary_actor = "Employer / Counselor / External Recruiter"
        admin_actor = "HR Manager / Placement Coordinator"
    elif "crime" in sys_lower or "visa" in sys_lower or "province" in sys_lower or "locker" in sys_lower:
        primary_actor = "Citizen / Applicant"
        secondary_actor = "Verification Authority / Law Enforcement Agency"
        admin_actor = "Investigating Officer / Embassy Admin"
    elif "marketplace" in sys_lower or "dropshipping" in sys_lower or "art" in sys_lower:
        primary_actor = "Buyer / Art Collector"
        secondary_actor = "Independent Seller / Artist / Courier Service"
        admin_actor = "Marketplace Platform Moderator"
    elif "weather" in sys_lower or "farm" in sys_lower:
        primary_actor = "Farmer / General Public"
        secondary_actor = "Meteorological Sensor Network / Market Price Feed"
        admin_actor = "Agricultural Officer / Weather Analyst"
    elif "quiz" in sys_lower or "magazine" in sys_lower or "book" in sys_lower:
        primary_actor = "Student / Library Member"
        secondary_actor = "Faculty / Content Contributor"
        admin_actor = "Librarian / Chief Editor / Exam Controller"
    elif "car" in sys_lower:
        primary_actor = "Vehicle Owner / Driver"
        secondary_actor = "Mechanic / Diagnostic Service Center"
        admin_actor = "Garage Workshop Manager"
    elif "startup" in sys_lower:
        primary_actor = "Startup Founder / Entrepreneur"
        secondary_actor = "Angel Investor / Venture Capitalist"
        admin_actor = "Incubator Mentor / Loan Officer"
    elif "video" in sys_lower or "reel" in sys_lower or "ott" in sys_lower:
        primary_actor = "Content Viewer / Subscriber"
        secondary_actor = "Content Creator / Ad Network"
        admin_actor = "Platform Content Manager / Streaming Ops"

    if "use case" in cat_lower or "usecase" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Actors Selection (Why they are chosen)**:
  - **Primary Actor (`{primary_actor}`)**: Derived from the problem statement as the core user who directly experiences operational pain points and initiates service requests (e.g., self-service tasks, browsing, and transacting).
  - **Secondary Supporting Actor (`{secondary_actor}`)**: Extracted as the external authority or service partner required to fulfill requests (e.g., financial settlements, identity verifications, or physical fulfillment).
  - **Administrative Actor (`{admin_actor}`)**: Required by governance rules to oversee security, manage backend configurations, and monitor operational compliance.
- **Use Cases Selection (Why these functions exist)**:
  - High-priority functional requirements ({cap_str}) were converted into core use cases inside the system boundary to directly satisfy user business goals.
  - Each use case corresponds directly to a distinct business capability needed to eliminate manual delays, paperwork, or operational bottlenecks.
- **Relationships & Dependency Rationale**:
  - **Associations**: Direct solid lines link `{primary_actor}` to primary operational use cases, establishing who has authorization to trigger each transaction.
  - **`<<include>>` Dependencies**: Factored out mandatory sub-routines (such as `Login / Authenticate`, `Verify Eligibility`, and `Process Payment`) that must execute unconditionally during transactions to guarantee security and data consistency.
  - **`<<extend>>` Dependencies**: Attached optional or conditional paths (such as `Apply Promotional Discount`, `Trigger Emergency Escalation`, or `Cancel Request`) that execute only when specific business guard conditions are satisfied.

#### 🛠️ Step-by-Step Construction Guide

1. **Define System Boundary & Scope**:
   - Draw an outer rectangular boundary box representing **{clean_sys}**.
   - Ensure external actors remain outside the boundary while all functional capabilities reside inside.
2. **Identify Primary & Secondary External Actors**:
   - Place `{primary_actor}` on the left side of the boundary to initiate business interactions.
   - Position `{secondary_actor}` and `{admin_actor}` on the right side as secondary or administrative actors.
3. **Identify & Model Business Use Cases**:
   - Draw horizontal ellipses inside the boundary representing key operational goals ({cap_str}).
   - Name each use case with an active verb-noun phrase.
4. **Establish Relationships & Stereotypes (`<<include>>`, `<<extend>>`)**:
   - Connect actors to relevant use cases using solid, unarrowed association lines.
   - Use dashed arrows labeled `<<include>>` directed toward mandatory shared sub-routines (e.g., authentication, data validation).
   - Use dashed arrows labeled `<<extend>>` directed from optional or conditional extension workflows toward base use cases.
5. **Verify Completeness & Cross-Check Requirements**:
   - Trace every functional requirement from the problem specification to confirm complete coverage without disconnected use cases."""

    elif "class" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Domain Classes & Classifiers Selection**:
  - **Entity Classes**: Extracted key nouns from the domain requirements to form core data models holding system state (e.g., `{primary_actor.split('/')[0].strip()}`, `Transaction`, `Record`, `Item/Service`).
  - **Boundary & Controller Classes**: Introduced interface controllers (e.g., `ServiceController`, `SessionManager`) to decouple user presentation inputs from backend database persistence.
- **Attributes & Methods Selection**:
  - **Attributes**: Assigned explicit data types and access modifiers (private `-` for information hiding) to track business properties (e.g., unique IDs, statuses, monetary values, timestamps).
  - **Operations**: Converted domain capabilities ({cap_str}) into public (`+`) member methods equipped with validated parameters and deterministic return signatures.
- **Relationships & Multiplicities Rationale**:
  - **Composition (Solid Diamond)**: Applied to strong whole-part relationships where child entities cannot exist independently of their parent aggregate (e.g., an invoice strictly owns its line items).
  - **Aggregation (Hollow Diamond)**: Applied to shared associations where components exist independently in the business domain.
  - **Multiplicities**: Annotated with strict operational constraints (e.g., `1` user owns `0..*` transactions; each transaction maps to exactly `1` payment record) to maintain data integrity.

#### 🛠️ Step-by-Step Construction Guide

1. **Identify Domain Entities & Boundary Objects**:
   - Analyze requirements for **{clean_sys}** to extract core business entities, controllers, and data structures.
   - Represent each entity as a three-compartment rectangular classifier (Class Name, Attributes, Operations).
2. **Define Attributes with Visibility & Data Types**:
   - Populate the middle compartment with private (`-`), protected (`#`), or public (`+`) attributes.
   - Assign standardized data types (e.g., `- id: String`, `- status: Boolean`, `- createdAt: DateTime`).
3. **Specify Member Operations & Business Methods**:
   - Populate the bottom compartment with functions and interface methods that define class behavior.
   - Include parameter types and return signatures (e.g., `+ executeTransaction(amount: Float): Boolean`).
4. **Establish Structural Relationships & Multiplicities**:
   - Connect related classes using solid association lines annotated with numerical multiplicities (e.g., `1`, `0..*`, `1..*`).
   - Apply Composition (solid diamond) for lifecycle-dependent objects, and Aggregation (hollow diamond) for shared references.
   - Model inheritance hierarchies using Generalization (solid line with closed hollow triangular arrowhead).
5. **Validate Architecture & Reduce Coupling**:
   - Review class cohesion to verify single-responsibility principles across data access and business logic layers.
   - Ensure interfaces isolate clients from direct database dependencies."""

    elif "activity" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Workflow Actions Selection**:
  - Derived step-by-step action states directly from the chronological steps required to complete {cap_names[0] if cap_names else 'the core transaction'}.
  - Modeled each human action (e.g., entering data, confirming selection) and automated system action (e.g., validating rules, computing totals, updating records) as discrete rounded rectangles.
- **Swimlanes & Responsibility Partitioning**:
  - Partitioned the workflow across swimlanes representing `{primary_actor}`, the Application Controller, and `{secondary_actor}`/Database.
  - Visualizes exactly where operational responsibility transfers across architectural boundaries.
- **Decisions, Guards & Concurrent Forks**:
  - **Decision Diamonds**: Inserted wherever business logic requires verification (e.g., `[Valid Credentials]`, `[Stock Available]`, `[Payment Approved]`), ensuring explicit error handling paths.
  - **Synchronization Bars (Fork/Join)**: Utilized where parallel background tasks (e.g., sending an alert while updating audit logs) occur simultaneously without blocking user execution.

#### 🛠️ Step-by-Step Construction Guide

1. **Establish Initial Node & Execution Swimlanes**:
   - Start the workflow with a solid black circle (Initial Node) representing the trigger event in **{clean_sys}**.
   - Organize participating roles and subsystems into vertical or horizontal swimlanes to establish organizational accountability.
2. **Plot Sequential Action & State Steps**:
   - Draw rounded rectangles for each discrete functional task in chronological order.
   - Connect sequential actions with directed control flow arrows indicating the progression of execution.
3. **Incorporate Decision & Branching Diamonds**:
   - Place diamond decision nodes where the business logic branches based on conditions.
   - Label outgoing paths with explicit boolean guard conditions in brackets (e.g., `[Valid Input]` vs `[Invalid Input]`).
4. **Model Concurrency with Fork & Join Bars**:
   - Use solid horizontal or vertical synchronization bars (Forks) to divide a single flow into simultaneous parallel operations.
   - Pair each Fork with a corresponding Join bar to synchronize parallel tasks before advancing to subsequent stages.
5. **Terminate Flow at Final State Nodes**:
   - Guide successful workflow branches to an encircled solid black dot (Activity Final Node).
   - Use flow final nodes (circle with an X) to terminate individual canceled sub-branches without stopping the entire workflow."""

    elif "sequence" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Participating Lifelines Selection**:
  - Selected key participants along the communication path: `{primary_actor}` (initiator), Boundary Controller (API/UI), Business Service Layer, and the Persistent Database / `{secondary_actor}`.
  - Ensures full horizontal separation between user interaction, application logic, and backend data storage.
- **Message Invocations & Temporal Sequence**:
  - Derived sequential message flows from the transaction lifecycle: initialization -> validation -> business calculation -> persistence -> return response.
  - Uses solid arrows with filled heads for synchronous calls where the caller waits for a response before proceeding.
- **Return Payloads & Conditional Fragments**:
  - **Dashed Return Arrows**: Modeled data payloads and status confirmations returned to the caller to maintain state awareness.
  - **`alt` Combined Fragments**: Partitioned if-else execution paths (e.g., success vs. validation error) with explicit boolean guard conditions.

#### 🛠️ Step-by-Step Construction Guide

1. **Arrange Participating Lifelines Horizontally**:
   - Position `{primary_actor}`, boundary controllers, service managers, and persistence models horizontally across the top.
   - Drop vertical dashed lines (lifelines) downward from each participant to represent the passage of time from top to bottom.
2. **Overlay Activation Focus Bars**:
   - Place thin vertical rectangular boxes on lifelines to indicate active execution periods where an object is processing instructions.
3. **Model Synchronous & Asynchronous Invocations**:
   - Draw solid horizontal arrows with filled triangular arrowheads for synchronous method calls (e.g., `validateRequest()`).
   - Draw open arrowheads for asynchronous events or non-blocking notification dispatches.
4. **Represent Return Messages & Reply Payloads**:
   - Draw dashed horizontal lines with open arrowheads pointing back to the calling lifeline to model return data or acknowledgment signals.
   - Label return lines with explicit payload descriptions (e.g., `statusConfirmation: Boolean`).
5. **Structure Logic with Combined Interaction Fragments**:
   - Enclose conditional logic within an `alt` fragment box partitioned into alternative execution compartments with bracketed guard expressions.
   - Utilize `opt` frames for optional branches and `loop` frames for iterative business operations."""

    elif "communication" in cat_lower or "collaboration" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Collaborating Object Nodes Selection**:
  - Selected runtime instances of the core architectural entities required to complete the business scenario in **{clean_sys}**.
  - Emphasizes the structural network of communicating instances rather than chronological time progression.
- **Structural Links & Message Numbering**:
  - **Association Links**: Created direct communication links between objects that possess references to each other.
  - **Hierarchical Numbering (`1`, `1.1`, `2`)**: Formulated numbered message vectors along links to preserve the exact call-stack sequence and nested function invocations.

#### 🛠️ Step-by-Step Construction Guide

1. **Place Collaborating Object Nodes**:
   - Position key runtime instances of classes as rectangular nodes labeled `instanceName : ClassName` across the canvas for **{clean_sys}**.
   - Arrange objects to emphasize physical structural connections and organizational proximity.
2. **Draw Structural Association Links**:
   - Connect communicating objects with solid undirected lines representing communication paths and active object references.
3. **Overlay Directional Message Vectors**:
   - Place directional arrows alongside the association links pointing from caller to receiver.
4. **Apply Hierarchical Decimal Sequence Numbering**:
   - Number each message sequentially using decimal nesting (e.g., `1: initiateRequest()`, `1.1: verifyParameters()`, `1.2: queryDatabase()`, `2: returnStatus()`).
   - Use hierarchical numbers to clearly convey the nested call stack and execution chronology without a vertical time axis.
5. **Validate Link Topology & Message Continuity**:
   - Verify that all collaborating objects participate in valid message exchange paths and that message signatures match class definitions."""

    elif "state" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Entity & Lifecycle States Selection**:
  - Selected the central transactional entity in **{clean_sys}** whose lifecycle undergoes critical state changes.
  - Derived distinct operational states (e.g., `Created`, `PendingApproval`, `Active / InProgress`, `Completed`, `Cancelled`) from domain business rules.
- **State Transitions, Triggers & Guard Rules**:
  - Identified the exact events (e.g., `submit()`, `verify()`, `processPayment()`, `cancel()`) that trigger transitions between states.
  - Formulated transition syntax: `Event [GuardCondition] / ActionEffect` to prevent invalid state jumps and enforce business integrity.

#### 🛠️ Step-by-Step Construction Guide

1. **Identify the Initial Pseudostate**:
   - Begin with a solid black circle (Initial State) marking the creation or activation trigger of the target entity in **{clean_sys}**.
2. **Define Distinct Operational States**:
   - Draw rounded rectangles representing every discrete state the entity can assume during its lifecycle (e.g., `Created`, `Pending`, `Processing`, `Completed`, `Failed`).
   - Add internal behavior compartments for `entry /`, `do /`, and `exit /` action routines where applicable.
3. **Map State Transitions & Triggers**:
   - Connect states using directed transition arrows indicating valid status changes.
   - Label transitions using the formal UML format: `TriggerEvent [GuardCondition] / ActionEffect` (e.g., `confirmTransaction [balanceValid] / generateReceipt()`).
4. **Model Superstates & Substates (Hierarchical States)**:
   - Group related substates within an enclosing composite state rectangle when multiple states share common exit or exception transitions.
5. **Terminate at Final State Nodes**:
   - Direct all terminal lifecycle outcomes (successful fulfillment or terminal rejection) to an encircled black dot (Final State)."""

    elif "component" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Modular Components Selection**:
  - Decomposed **{clean_sys}** into autonomous, reusable software units based on separation of concerns: User Interface Controller, Business Service Core, Persistence Engine, and External Integration Gateways.
  - Ensures each component encapsulates a specific domain capability ({cap_str}) without tight coupling.
- **Provided & Required Interfaces Selection**:
  - **Provided Interfaces (Ball)**: Defined public APIs and services exposed by components to serve consumer requests.
  - **Required Interfaces (Socket)**: Defined downstream dependencies, such as database connectors and third-party API contracts required for operation.

#### 🛠️ Step-by-Step Construction Guide

1. **Identify Autonomous Modular Units**:
   - Analyze **{clean_sys}** to identify independent deployable subsystems, microservices, databases, and third-party integrations.
   - Represent each unit as a rectangular component symbol adorned with the `<<component>>` stereotype or component icon tabs.
2. **Define Provided Interfaces (Ball / Lollipop Notation)**:
   - Attach solid circle "ball" connectors to components that provide public API endpoints, RPC interfaces, or query services to external callers.
3. **Define Required Interfaces (Socket Notation)**:
   - Attach semicircular "socket" connectors to components that depend on external services or client data contracts.
4. **Assemble Ball-and-Socket Connectors**:
   - Align matching ball and socket connectors to model direct architectural wiring, loose coupling, and dependency injection.
5. **Group into Architectural Subsystems**:
   - Enclose related components inside package boundaries (e.g., Presentation Layer, Business Core, Data Storage) to enforce clean layer isolation."""

    elif "deployment" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Hardware Nodes & Infrastructure Selection**:
  - Derived execution nodes from physical hosting requirements: Client Devices (Smartphones/Desktops), Web & Application Servers, and Database Clusters.
  - Isolates public-facing presentation endpoints from secure, internal database storage to comply with enterprise security standards.
- **Artifact Allocation & Communication Protocols**:
  - **Artifact Deployment**: Mapped executable binaries (`.jar`, `.war`, `.apk`, client web bundles) onto their corresponding execution environments.
  - **Protocol Selection**: Assigned standard secure networking protocols (`<<HTTPS/TLS>>`, `<<TCP/IP>>`, `<<JDBC>>`) based on data sensitivity and network boundaries.

#### 🛠️ Step-by-Step Construction Guide

1. **Identify Physical & Virtual Hardware Nodes**:
   - Draw 3D isometric box cubes representing physical host servers, cloud instances, client smartphones, and database clusters for **{clean_sys}**.
   - Label nodes with stereotypic descriptions (e.g., `<<device>>`, `<<database server>>`, `<<cloud container>>`).
2. **Specify Runtime Execution Environments**:
   - Nest runtime environments inside node cubes (e.g., `<<execution environment>> Web Browser`, `Docker Engine`, `JVM Runtime`).
3. **Assign Executable Artifacts to Nodes**:
   - Place software artifacts (rectangles with `<<artifact>>` stereotype, `.jar`, `.war`, `.apk`, `.sql`) inside their corresponding hosting execution environments.
4. **Draw Network Communication Paths & Protocols**:
   - Connect nodes using solid communication lines labeled with transport protocols and security stereotypes (e.g., `<<HTTPS/TLS>>`, `<<TCP/IP>>`, `<<JDBC>>`, `<<gRPC>>`).
5. **Verify High Availability & Security Boundaries**:
   - Ensure clear physical separation between public demilitarized zones (DMZ), application compute layers, and protected private database networks."""

    elif "data flow" in cat_lower or "dfd" in cat_lower:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **External Entities & Process Selection**:
  - **External Terminators**: Mapped `{primary_actor}` and `{secondary_actor}` as peripheral entities that input raw business data or receive processed reports.
  - **Processes**: Formulated transformation bubbles representing algorithmic data processing steps (e.g., validation, calculation, update) derived from domain capabilities ({cap_str}).
- **Data Stores & Information Flows**:
  - **Data Stores (`D1`, `D2`)**: Defined persistence boundaries for storing accounts, transaction logs, and operational catalog data.
  - **Directional Flows**: Labeled directed arrows with substantive nouns (not verbs) representing data packets in transit.

#### 🛠️ Step-by-Step Construction Guide

1. **Identify External Entities (Terminators)**:
   - Draw rectangular boxes on the periphery representing external users, devices, or third-party organizations that supply data or receive outputs.
2. **Define Transformation Processes**:
   - Draw numbered circular or rounded process bubbles (`0` for Level 0 Context Diagram, `1.0`, `2.0`, `3.0` for Level 1 DFD) that perform data transformations.
3. **Identify & Model Persistent Data Stores**:
   - Draw parallel horizontal open-ended bars labeled `D1: StoreName`, `D2: ...` representing internal persistent database tables or file storage systems.
4. **Trace Directional Data Flows**:
   - Connect entities, processes, and stores using directed arrows labeled with descriptive noun phrases (e.g., `User Credentials`, `Order Details`, `Verification Token`).
5. **Verify Data Conservation & Flow Balancing**:
   - Check for conservation of data: ensure no "black-hole" processes (inputs with zero outputs) and no "miracle" processes (outputs with zero inputs).
   - Verify that data inputs and outputs balance perfectly across hierarchical DFD levels."""

    else:
        return f"""#### 🔍 Component Derivation from Problem Requirements

- **Architectural Units & Module Selection**:
  - Decomposed **{clean_sys}** into structural modules and interface layers directly supporting the business requirements ({cap_str}).
  - Identified data origins, processing checkpoints, and terminal delivery interfaces.
- **Interface Pathways & Control Logic**:
  - Established operational connection pathways linking human operator touchpoints to backend compute services and persistent data repositories.
  - Defined explicit data contracts and protocol boundaries ensuring reliable inter-module communication.

#### 🛠️ Step-by-Step Construction Guide

1. **Establish Diagram Purpose & System Boundary**:
   - Define the architectural scope and structural boundaries for **{clean_sys}**, identifying all interacting internal and external modules.
2. **Identify Primary System Entities & Structural Units**:
   - Lay out primary subsystems, data structures, controllers, and workflow pipelines required to fulfill the illustrated architectural role.
3. **Map Control & Information Transfer Flows**:
   - Draw directional connection lines between entities, specifying whether the interaction is synchronous, event-driven, or batch-processed.
4. **Apply Architectural Rules & Guard Constraints**:
   - Label transitions, data contracts, and operational states with explicit conditions, protocol types, and operational invariants.
5. **Validate Architectural Cohesion & Traceability**:
   - Cross-reference the diagram against system functional specifications to confirm complete coverage, clear modular decoupling, and robust failure handling."""
