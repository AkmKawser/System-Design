# 2. Architecture Patterns: Comprehensive Taxonomy, Mechanics, and Trade-Off Catalog

> **Canonical References**: 
> - Richards, Mark, and Neal Ford. *Fundamentals of Software Architecture: A Modern Engineering Approach*. O'Reilly Media, 2020.
> - Richards, Mark, Neal Ford, and Raju Gandhi. *Software Architecture: Patterns, Antipatterns, and Pitfalls*. O'Reilly Media.
> - Fowler, Martin. *Patterns of Enterprise Application Architecture*. Addison-Wesley.
> - Buschmann, Frank, et al. *Pattern-Oriented Software Architecture (POSA)*, Volumes 1–4. Wiley.

---

## 1. Executive Summary & Granularity Taxonomy

Architectural Patterns are distinct from both macro **Architectural Styles** and micro **Design Patterns**:

| Hierarchy Tier | Granularity & Scope | Responsibility | Representative Examples |
| :--- | :--- | :--- | :--- |
| **1. Architectural Style (Macro)** | Entire System / Deployment Unit | Defines physical deployment boundaries, runtime distribution, and enterprise topology. | Layered (N-Tier), Microservices, Event-Driven (EDA), Space-Based, Microkernel. |
| **2. Architectural Pattern (Meso)** | Subsystem / Application Layer | Concrete, reusable structural templates solving specific subsystem communication, state, and coordination challenges. | **MVC**, **CQRS**, **Saga**, **Transactional Outbox**, **BFF**, **Circuit Breaker**. |
| **3. Design Pattern (Micro)** | In-Memory Class / Object | Localized object-oriented design solutions solving class creation, composition, and behavioral interaction (GoF). | Strategy, Observer, Factory Method, Decorator, Composite, Singleton. |

---

## 2. Presentation & Interaction Patterns (UI & Client Tier)
*Decouples user interfaces, user input handling, and domain data.*

### 2.1 Model-View-Controller (MVC)
- **Problem**: Tight coupling between presentation markup and business domain logic.
- **Mechanism**: Deconstructs presentation into three components:
  - **Model**: Encapsulates business entities, data validation, and state.
  - **View**: Renders visual representation to the client.
  - **Controller**: Translates incoming user inputs/actions into model mutations and view selections.
- **Trade-Offs**: High testability and separation of concerns; risk of "Fat Controllers" if orchestration leaks out of domain services.

### 2.2 Model-View-ViewModel (MVVM)
- **Problem**: Imperative boilerplate code required to synchronize UI widgets with underlying data states.
- **Mechanism**: Introduces **two-way data binding**. The ViewModel exposes observable state properties without referencing specific UI widgets; the View binds directly to properties.
- **Trade-Offs**: Eliminates manual UI sync code; high memory overhead and difficult stack-trace debugging in complex bindings.

### 2.3 Model-View-Presenter (MVP)
- **Problem**: Inability to unit-test UI presentation logic without running a graphical emulator.
- **Mechanism**: The Presenter acts as a strict mediator between Model and View. The View is completely passive, exposing setter interfaces (`setUserName()`, `showError()`).
- **Trade-Offs**: Extremely high testability; requires significant interface boilerplate.

### 2.4 Model-View-Intent (MVI)
- **Problem**: Non-deterministic state race conditions in highly reactive, concurrent mobile/web applications.
- **Mechanism**: **Unidirectional Data Flow (UDF)**:
  `User Action → Intent → State Machine → Immutable Single State → View Render`.
- **Trade-Offs**: Deterministic, 100% reproducible time-travel debugging; steep learning curve and boilerplate overhead.

### 2.5 Front Controller
- **Problem**: Duplicated cross-cutting concerns (authentication, request routing, session validation, metric logging) across multiple view endpoints.
- **Mechanism**: A centralized entry point dispatcher receives all incoming requests, executes pre-processing filters, and delegates to specialized sub-controllers.
- **Trade-Offs**: Centralized security and routing governance; potential single bottleneck / god-object antipattern if logic bloats.

---

## 3. Distributed Data & Consistency Patterns
*Manages transactions, state projection, and data synchronization across services without distributed locking (2PC).*

### 3.1 Command Query Responsibility Segregation (CQRS)
- **Problem**: Read and write workloads have conflicting schema, performance, and scaling demands.
- **Mechanism**: Separates operations into:
  - **Command Model**: Handles writes, state mutations, and strict business validation rules.
  - **Query Model**: Optimized, denormalized read projections powered by asynchronous event synchronization.
- **Trade-Offs**: Extreme read throughput and independent scaling; eventual consistency lag between command execution and query visibility.

### 3.2 Event Sourcing
- **Problem**: Traditional CRUD updates destructively overwrite state history, leaving zero audit trail of *why* state changed.
- **Mechanism**: Stores state changes as an **immutable, append-only chronological log of domain events**. Current entity state is derived by replaying events from genesis (or snapshots).
- **Trade-Offs**: Complete auditability, time-travel debugging, and historical replay; requires complex event schema evolution and snapshotting for query performance.

### 3.3 Saga Pattern
- **Problem**: Multi-service distributed transactions cannot use Two-Phase Commit (2PC) due to latency and locking bottlenecks.
- **Mechanism**: Breaks distributed transaction into a sequence of local database transactions:
  - **Orchestrated Saga**: Central orchestrator commands participants and triggers compensations on failure.
  - **Choreographed Saga**: Participants react to domain events and emit follow-up events.
  - **Compensating Transactions**: Semantic inverse actions executed in reverse order on failure (`Step 3 fails → Compensate 2 → Compensate 1`).
- **Trade-Offs**: High availability and no distributed locks; complex rollback mechanics and transient dirty read states.

### 3.4 Transactional Outbox Pattern
- **Problem**: The Dual-Write Problem—database commit succeeds, but message broker publish fails (or vice versa), leading to data corruption.
- **Mechanism**: Persists domain entity mutations and outbound event records in the **same atomic local database transaction**. A background Change Data Capture (CDC) worker (e.g., Debezium) tails the outbox table and streams events to the message broker.
- **Trade-Offs**: Guaranteed At-Least-Once event publishing with zero dual-write inconsistency; requires outbox table cleanup and downstream idempotent consumer deduplication.

### 3.5 Cache-Aside (Lazy Loading)
- **Problem**: Relational databases bottleneck under high-volume read traffic.
- **Mechanism**: Application checks cache first. On miss, it reads database, populates cache, and returns. Writes bypass cache or invalidate the specific key.
- **Trade-Offs**: Simple, resilient (system stays up if cache fails); eventual consistency lag and thundering herd risk on cold cache.

### 3.6 Read-Through / Write-Through / Write-Behind
- **Read-Through**: Application treats cache as main store; cache library transparently fetches from DB on miss.
- **Write-Through**: Application writes to cache, which synchronously writes to database before returning.
- **Write-Behind (Write-Back)**: Application writes to cache, which acknowledges immediately and asynchronously flushes batches to database.
- **Trade-Offs**: Simplified client code and fast write performance; risk of data loss on node failure in Write-Behind.

### 3.7 Service & Database Sharding
- **Problem**: Single database hits hardware I/O and CPU limits under extreme transaction volume.
- **Mechanism**: Partitions compute and storage horizontally by a shard key (e.g., `user_id`, `tenant_id`), keeping transactions strictly local to a shard.
- **Trade-Offs**: Horizontal elasticity and high throughput; cross-shard joins and aggregations become complex and expensive.

---

## 4. Edge, Gateway & Ingress Composition Patterns
*Optimizes network traffic, protocol translation, and client-to-backend communication boundaries.*

### 4.1 API Gateway Pattern
- **Problem**: Exposing dozens of internal microservices directly to client apps creates security risks and chatty networks.
- **Mechanism**: Central reverse proxy handling TLS termination, JWT validation, rate limiting, and traffic routing.
- **Trade-Offs**: Centralized perimeter security and unified contract; potential single point of failure and bottleneck.

### 4.2 Backend-for-Frontend (BFF)
- **Problem**: Mobile, Desktop, and Third-Party clients require wildly different payload structures and bandwidth constraints.
- **Mechanism**: Builds dedicated gateway services per client type (Mobile BFF, Web BFF, IoT BFF).
- **Trade-Offs**: Highly optimized client performance and UI team autonomy; potential code duplication across BFF services.

### 4.3 Aggregator / Composition Pattern
- **Problem**: A single user screen requires composite data owned across 5 independent backend services.
- **Mechanism**: An orchestrator receives client request, calls all 5 upstream services concurrently, merges responses into a single JSON response, and returns.
- **Trade-Offs**: Drastically reduces mobile network round-trips; latency bound to the slowest upstream service.

### 4.4 Scatter-Gather (Fan-Out / Fan-In)
- **Problem**: Querying multiple dynamic providers (e.g., flight booking, insurance aggregators) within strict SLAs.
- **Mechanism**: Broadcasts request concurrently to *N* providers with a hard timeout. Gathers all responses that arrive before timeout, ranks/aggregates them, and drops late responses.
- **Trade-Offs**: High responsiveness and fault isolation; resource-intensive concurrency and partial result handling.

### 4.5 Sidecar / Ambassador Pattern
- **Problem**: Cross-cutting platform concerns (mTLS encryption, distributed tracing, metrics, retries) polluting business codebases.
- **Mechanism**: Deploys a secondary helper container sharing the same network namespace and pod lifecycle (e.g., Envoy in Istio).
- **Trade-Offs**: Complete polyglot language independence; operational footprint and small container networking overhead.

### 4.6 Anti-Corruption Layer (ACL)
- **Problem**: Migrating or integrating with messy legacy systems corrupts new clean microservice domain models.
- **Mechanism**: A mediating translation layer translates legacy schemas and protocols into clean, modern domain models bidirectionally.
- **Trade-Offs**: Protects domain model purity; requires maintaining mapping code.

---

## 5. Workflow & Coordination Patterns
*Governs multi-step operational logic and message routing across components.*

### 5.1 Orchestration Pattern
- **Problem**: Complex distributed workflows with strict business SLAs become chaotic and unobservable when handled purely via events.
- **Mechanism**: A central orchestrator explicitly directs participants, enforces state machine transitions, and coordinates compensation logic (e.g., Temporal, AWS Step Functions).
- **Trade-Offs**: High workflow visibility and deterministic error handling; central dependency and potential bottleneck.

### 5.2 Choreography Pattern
- **Problem**: Central orchestrators introduce tight coupling and operational bottlenecks in high-throughput systems.
- **Mechanism**: Completely decentralized. Services react to upstream domain events and emit downstream events without central supervision.
- **Trade-Offs**: Loose coupling and extreme horizontal scale; poor end-to-end workflow visibility and difficult compensation logic.

### 5.3 Pipes and Filters
- **Problem**: Complex sequential data transformations requiring flexible re-ordering, independent scaling, and modular reuse.
- **Mechanism**: Divides task into discrete processing components (**Filters**) connected by unidirectional channels (**Pipes**).
- **Trade-Offs**: High modularity and composability; serialization overhead between filters.

### 5.4 Blackboard Pattern
- **Problem**: Non-deterministic, open-ended problem domains with no single mathematical algorithm (e.g., speech parsing, AI scheduling).
- **Mechanism**: A shared data repository (**Blackboard**) is continuously inspected by autonomous **Knowledge Sources** that opportunistically contribute partial solutions until a result emerges.
- **Trade-Offs**: Handles non-deterministic complex optimization; non-deterministic execution times and synchronization overhead.

---

## 6. Resiliency & Traffic Shaping Patterns
*Prevents cascading outages, system crashes, and resource starvation during partial system failure.*

### 6.1 Circuit Breaker Pattern
- **Problem**: Repeatedly calling an unresponsive downstream service leads to thread exhaustion and cascading system outages.
- **Mechanism**: State machine intercepts remote calls:
  - **Closed**: Normal execution; counts failures.
  - **Open**: Error threshold exceeded; fails fast immediately with fallback response without hitting network.
  - **Half-Open**: Sleep window expires; allows trial requests through to probe downstream recovery.
- **Trade-Offs**: Immediate thread recovery and fault containment; fallback design complexity.

### 6.2 Bulkhead Pattern
- **Problem**: A single failing or slow endpoint consumes all available threads/connections, starving critical business flows.
- **Mechanism**: Partitions resources into isolated pools (thread pools, connection pools, CPU limits) so an issue in one compartment cannot sink the ship.
- **Trade-Offs**: Strict failure containment; slightly reduced maximum resource pooling efficiency.

### 6.3 Ambulance / Priority Queue Pattern
- **Problem**: High-volume routine transactions delay mission-critical, time-sensitive requests.
- **Mechanism**: Routes traffic into a high-priority "ambulance" queue and a normal queue, serviced by prioritized consumer threads.
- **Trade-Offs**: Guaranteed responsiveness for VIP workloads; potential starvation of normal queues under heavy load.

### 6.4 Dead Letter Queue (DLQ)
- **Problem**: Unparseable or poison-pill messages crash consumer workers repeatedly, blocking entire queues.
- **Mechanism**: After maximum retry threshold is exceeded, the broker reroutes the poison message to a DLQ for offline analysis and alerting.
- **Trade-Offs**: Prevents queue head-of-line blocking; requires manual or automated DLQ replay mechanisms.

### 6.5 Supervisor Consumer Pattern
- **Problem**: Static consumer worker pools either waste compute during quiet periods or fall catastrophically behind during bursts.
- **Mechanism**: A supervisor process inspects message queue backlog depth and dynamically scales worker consumers up or down elastically.
- **Trade-Offs**: Optimal resource utilization and predictable SLA; coordination churn on short-lived traffic spikes.

### 6.6 Thread Delegate Pattern
- **Problem**: Concurrent multi-threaded consumers cause race conditions and out-of-order execution on ordered financial/entity events.
- **Mechanism**: A dispatcher receives messages, hashes the entity key (e.g., `account_id`), and routes all messages for that key to the same dedicated single-threaded queue.
- **Trade-Offs**: Strict in-order processing with massive parallel throughput; potential hot-thread bottleneck if one entity has huge traffic.

---

## 7. Domain Decoupling & Modernization Patterns
*Structural patterns that protect core business models and manage system evolution.*

### 7.1 Ports and Adapters (Hexagonal Architecture)
- **Problem**: Domain business logic becomes tangled with database SQL, web frameworks, and messaging libraries.
- **Mechanism**: Core domain models and use cases live inside a boundary defined by **Ports** (interfaces). External drivers and infrastructure connect through pluggable **Adapters** (REST, gRPC, PostgreSQL, Kafka).
- **Trade-Offs**: 100% testable domain logic independent of frameworks; requires interface mapping boilerplate.

### 7.2 Clean / Onion Architecture
- **Problem**: Inverted dependency violations where enterprise rules depend on persistence and UI frameworks.
- **Mechanism**: Concentric rings where dependencies strictly point **inward**:
  `Frameworks & Drivers → Interface Adapters → Application Business Rules → Enterprise Entities`.
- **Trade-Offs**: Complete technology agnostic architecture; high package layering overhead.

### 7.3 Strangler Fig Pattern
- **Problem**: "Big Bang" rewrites of critical legacy monoliths almost always fail or run over budget.
- **Mechanism**: Places an edge router in front of the legacy monolith. New features or extracted modules are built as microservices; the router gradually diverts traffic until the old monolith is decommissioned.
- **Trade-Offs**: Low-risk continuous migration with zero downtime; requires maintaining legacy and new systems concurrently.

### 7.4 Microkernel (Plugin) Pattern
- **Problem**: Monolithic systems needing dynamic functional extensions without recompiling the core codebase.
- **Mechanism**: A minimal **Core System** defines baseline lifecycle and extension hooks; independent **Plugin Modules** supply custom features.
- **Trade-Offs**: High extensibility and feature isolation; core system contract versioning complexity.

### 7.5 Broker Pattern (POSA)
- **Problem**: Distributed systems needing service location, marshalling, and invocation without hardcoded IP bindings.
- **Mechanism**: An intermediary Broker maintains service registries, forwards client requests, unmarshalls parameters, and returns results.
- **Trade-Offs**: Location transparency; extra network hop and broker reliability requirement.

---

## 8. Summary Decision Guide: Which Pattern When?

| Architectural Goal | Primary Recommended Pattern |
| :--- | :--- |
| **Separating UI from Domain Logic** | **MVC** (Server web apps) or **MVVM** (Reactive client apps) |
| **Optimizing Read vs. Write Workloads** | **CQRS** |
| **Audit Trails & Complete History** | **Event Sourcing** |
| **Distributed Multi-Service Transactions** | **Saga Pattern** (Orchestrated or Choreographed) |
| **Reliable Event Publishing without Dual-Writes** | **Transactional Outbox Pattern** (with CDC) |
| **Diverse Multi-Platform Clients (Mobile/Web)** | **Backend-for-Frontend (BFF)** |
| **Preventing Cascading Distributed Failures** | **Circuit Breaker** + **Bulkhead** |
| **Safely Modernizing a Legacy Monolith** | **Strangler Fig Pattern** + **Anti-Corruption Layer (ACL)** |
| **Prioritizing Critical Workloads under Load** | **Ambulance (Priority Queue) Pattern** |
| **Preserving Domain Purity from Frameworks** | **Ports and Adapters (Hexagonal Architecture)** |
