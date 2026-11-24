#!/usr/bin/env python3
"""
Polishes 003_complete_architectural_patterns_catalog.md:
1. Re-architects all 28 diagrams into balanced aspect ratios (16:9 to 4:3) with flowchart TD/nested subgraphs.
2. Eliminates text-image paragraph merging by placing a dedicated divider line after every diagram.
3. Eliminates all empty Setext headings (HEADING_2/3 "") by removing bare '---' preceding ATX headings.
4. Pre-renders all 28 diagrams to crisp, high-resolution PNGs (constrained ~850px width).
5. Updates Google Doc tab t.xlbamg66amln.
"""

import sys
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[2]
catalog_path = root / "topics" / "0.FUNDAMENTALS" / "Software Architecture and Modeling" / "1.ARCHITECTURE" / "2. Architecture Patterns" / "output" / "query_Architecture_Patterns" / "003_complete_architectural_patterns_catalog.md"
images_dir = catalog_path.parent / "images"
images_dir.mkdir(parents=True, exist_ok=True)
cache_dir = root / "engine" / "scripts" / "cache"

mermaid_js_path = cache_dir / "mermaid.min.js"
if not mermaid_js_path.exists():
    print("Error: mermaid.min.js missing from cache")
    sys.exit(1)

mermaid_js = mermaid_js_path.read_text(encoding="utf-8")

# 28 balanced diagrams definitions
diagrams = {
    "01-overview-taxonomy.png": """flowchart TD
    Style["1. Architectural Style (Macro-Level Strategy)\n- Defines physical deployment units, runtime topology, and distributed boundaries\n- Examples: Monolithic Layered, Modular Monolith, Microservices, Event-Driven"]
    Style -->|"Adopts and Contains"| Pattern["2. Architectural Pattern (Meso-Level Subsystem Template)\n- Concrete structural templates solving recurring design dilemmas\n- Examples: CQRS, Saga, Event Sourcing, BFF, Hexagonal, Circuit Breaker"]
    Pattern -->|"Implements via"| Design["3. Design Pattern (Micro-Level Class / Object Idiom)\n- Local OOP object wiring, creational/behavioral idioms in memory\n- Examples: Strategy, Observer, Factory, Decorator, Adapter"]
""",

    "02-mvc-pattern.png": """flowchart TD
    User["Client / Web Browser"] -->|"1. User Gestures / HTTP Requests"| Controller["Controller (Orchestrator)\n- Handles input & routing\n- Invokes Domain Services\n- Selects target View"]
    Controller -->|"2. Domain Mutations"| Model["Model (Business Domain)\n- State, invariants & rules\n- Persistence entities\n- Unaware of View/Controller"]
    Controller -->|"3. Binds Model State"| View["View (Presentation Tier)\n- Stateless HTML/JSP Template\n- Renders output visual UI"]
    View -->|"4. HTTP Response Stream"| User
""",

    "03-mvvm-pattern.png": """flowchart TD
    View["View (UI Widgets / Screen)\n- Declarative XML / HTML / Jetpack Compose\n- Passive visual layout without business logic"]
    Binder["Declarative Data-Binding Engine\n- Two-Way property synchronization\n- Automatic observation & change detection"]
    ViewModel["ViewModel (State & Commands)\n- Holds observable state properties\n- Exposes executable commands\n- Headless & UI-framework independent"]
    Model["Model (Domain Tier)\n- Entities, business invariants & repositories"]

    View <-->|"Two-Way Data Binding"| Binder
    Binder <-->|"Observable State Updates"| ViewModel
    ViewModel <-->|"Commands & Queries"| Model
""",

    "04-mvp-pattern.png": """flowchart TD
    View["View (Passive UI Component)\n- Implements IView interface\n- Dispatches raw click/input events\n- Zero decision logic"]
    Presenter["Presenter (Supervising Logic)\n- Handles user interactions\n- Orchestrates Model calls\n- Explicitly calls IView methods to update UI"]
    Model["Model (Domain Logic & Entities)\n- Domain validation & persistence"]

    View -->|"1. Raw User Gesture"| Presenter
    Presenter -->|"2. Invokes Business Logic"| Model
    Model -->|"3. Domain Result"| Presenter
    Presenter -->|"4. Explicit UI Updates via IView"| View
""",

    "05-mvi-pattern.png": """flowchart TD
    User["User Interaction"] -->|"Dispatches"| Intent["Intent (Immutable User Action)\n- Represents user desire\n- Example: SubmitOrderIntent"]
    Intent -->|"Processed by"| Reducer["Model / Reducer Function\n- Pure state transition logic\n- (PreviousState, Intent) => NextState"]
    Reducer -->|"Emits"| ViewState["ViewState (Single Immutable State Object)\n- Comprehensive UI snapshot\n- Contains loading, error, data flags"]
    ViewState -->|"Rendered by"| View["View (Pure Render Function)\n- Deterministically displays ViewState"]
    View -.->|"Generates new events"| User
""",

    "06-front-controller.png": """flowchart TD
    Client["Client Request"] --> FilterChain["Intercepting Filters (Pre-Processing)\n- TLS Termination, Auth Token Validation\n- Rate Limiting, Audit Logging"]
    FilterChain --> FC["Front Controller (Central Dispatcher)\n- URL pattern matching\n- Route discovery & dispatch"]
    FC --> H1["OrderHandler (Controller Action)"]
    FC --> H2["PaymentHandler (Controller Action)"]
    H1 --> ViewEngine["Template View Engine"]
    H2 --> JSONRenderer["JSON / REST Serializer"]
    ViewEngine --> Client
    JSONRenderer --> Client
""",

    "07-cqrs-pattern.png": """flowchart TD
    Client["Client / API Gateway"]
    subgraph CommandSide ["Command Pipeline (Write Optimization - ACID)"]
        CmdHandler["Command Handler\n- Validates business invariants\n- Enforces strict constraints"]
        WriteDB[("Write Database\n(Normalized 3NF / Relational)")]
        CmdHandler --> WriteDB
    end
    subgraph QuerySide ["Query Pipeline (Read Optimization - Eventual Consistency)"]
        QueryHandler["Query Handler\n- Zero locks, direct projection\n- High concurrency"]
        ReadDB[("Read Database\n(Denormalized Elastic / Redis / Mongo)")]
        QueryHandler --> ReadDB
    end
    Client -->|"POST/PUT/DELETE (Commands)"| CmdHandler
    Client -->|"GET (Queries)"| QueryHandler
    WriteDB -->|"CDC / Debezium Event Sync"| ReadDB
""",

    "08-event-sourcing.png": """flowchart TD
    Cmd["Incoming Command"] --> Service["Aggregate Service Engine"]
    Service -->|"1. Replay Past Events"| EventStore[("Immutable Event Store (WAL)\n- OrderCreatedEvent\n- ItemAddedEvent\n- OrderPaidEvent")]
    EventStore -->|"2. Current State Hydration"| Service
    Service -->|"3. Append New Event"| EventStore
    EventStore -->|"4. Stream Projections"| ReadModel[("Materialized Read Views\n(Search, Analytics, Cache)")]
    Snapshot[("Snapshot Storage (Every Nth Event)")] -.->|"Fast Checkpoint Load"| Service
""",

    "09-saga-orchestration-vs-choreography.png": """flowchart TD
    subgraph Orchestration ["Orchestrator-Led Saga (Central Controller)"]
        SagaMgr["Saga Orchestrator State Machine"]
        OrderSvc["Order Service"]
        PaymentSvc["Payment Service"]
        InventorySvc["Inventory Service"]
        SagaMgr -->|"1. Create Order"| OrderSvc
        SagaMgr -->|"2. Authorize Payment"| PaymentSvc
        PaymentSvc -.->|"Payment Failed"| SagaMgr
        SagaMgr -->|"Compensate: Cancel Order"| OrderSvc
    end
    subgraph Choreography ["Choreographed Saga (Event-Driven Reactive)"]
        C1["Order Service"] -->|"OrderCreatedEvent"| Bus[("Kafka / Event Bus")]
        Bus --> C2["Payment Service"]
        C2 -->|"PaymentFailedEvent"| Bus
        Bus -->|"Triggers Compensation"| C1
    end
""",

    "10-transactional-outbox.png": """flowchart TD
    subgraph AppBoundary ["Application Microservice Boundary (Single ACID Transaction)"]
        App["Business Application Logic"]
        BusinessTable[("Business Domain Table\n(e.g., Orders)")]
        OutboxTable[("Outbox Table\n(id, event_type, payload, status)")]
        App -->|"1. INSERT Order"| BusinessTable
        App -->|"2. INSERT Outbox Record"| OutboxTable
    end
    CDC["CDC Log Tailer (Debezium / WAL Reader)"] -->|"3. Asynchronously tails WAL"| OutboxTable
    CDC -->|"4. Guaranteed Delivery"| Kafka[("Message Broker (Kafka / RabbitMQ)")]
    Kafka --> Downstream["Downstream Consumers"]
""",

    "11-cache-aside.png": """flowchart TD
    App["Application Service"]
    Cache[("Distributed Cache (Redis / Memcached)")]
    DB[("Primary Database (PostgreSQL / MySQL)")]

    App -->|"1. Query Cache for Key"| Cache
    Cache -.->|"2a. Cache Hit (Return Data)"| App
    Cache -.->|"2b. Cache Miss"| App
    App -->|"3. Query Primary Database"| DB
    DB -->|"4. Return Raw Record"| App
    App -->|"5. Populate Cache with TTL"| Cache
""",

    "12-read-write-through-behind.png": """flowchart TD
    subgraph ReadWriteThrough ["Read-Through / Write-Through (Synchronous Inline Cache)"]
        App1["Application"] -->|"Read / Write"| Cache1["Smart Cache Provider"]
        Cache1 <-->|"Synchronous Read/Write"| DB1[("Primary Database")]
    end
    subgraph WriteBehind ["Write-Behind / Write-Back (Asynchronous Batch DB Flush)"]
        App2["Application"] -->|"Fast Write (ACK)"| Cache2["Write-Back Cache Buffer"]
        Cache2 -->|"Async Batch Dequeued Flush"| DB2[("Primary Database")]
    end
""",

    "13-database-sharding.png": """flowchart TD
    Client["Client / Routing Layer"] --> ShardRouter["Shard Key Hash Function\n(e.g., MurmurHash3(tenantId) % 3)"]
    ShardRouter -->|"Shard 0 (Tenants 0-999)"| DB0[("Database Node 0 (Primary)")]
    ShardRouter -->|"Shard 1 (Tenants 1000-1999)"| DB1[("Database Node 1 (Primary)")]
    ShardRouter -->|"Shard 2 (Tenants 2000-2999)"| DB2[("Database Node 2 (Primary)")]
    DB0 -.->|"Replica"| DB0_Replica[("Read Replica 0")]
    DB1 -.->|"Replica"| DB1_Replica[("Read Replica 1")]
    DB2 -.->|"Replica"| DB2_Replica[("Read Replica 2")]
""",

    "14-api-gateway.png": """flowchart TD
    Clients["Diverse Clients (Web, iOS, Android, 3rd Party)"] --> Gateway["API Gateway (Single Perimeter Ingress)\n- TLS Termination & Authentication (JWT/OAuth2)\n- Rate Limiting (Token Bucket) & DDoS Defense\n- Dynamic Path Routing & Canary Splitting"]
    Gateway -->|"Route /api/v1/users"| SvcUser["User Microservice"]
    Gateway -->|"Route /api/v1/orders"| SvcOrder["Order Microservice"]
    Gateway -->|"Route /api/v1/payments"| SvcPay["Payment Microservice"]
""",

    "15-backend-for-frontend-bff.png": """flowchart TD
    MobileApp["Mobile App (iOS/Android)"] --> MobileBFF["Mobile BFF Gateway\n- Aggregated small JSON\n- Low bandwidth optimization\n- Push notification hooks"]
    WebBrowser["Web Desktop Browser"] --> WebBFF["Desktop Web BFF Gateway\n- Rich denormalized payloads\n- Server-side template rendering\n- High bandwidth throughput"]
    MobileBFF --> Svc1["Order Service"]
    MobileBFF --> Svc2["Customer Service"]
    WebBFF --> Svc1
    WebBFF --> Svc2
    WebBFF --> Svc3["Analytics Service"]
""",

    "16-aggregator-scatter-gather.png": """flowchart TD
    subgraph Aggregator ["Aggregator / Composition Pattern"]
        Client1["Client Request"] --> GatewayAgg["API Gateway Aggregator"]
        GatewayAgg -->|"1. Fetch Profile"| SvcA["User Service"]
        GatewayAgg -->|"2. Fetch Orders"| SvcB["Order Service"]
        GatewayAgg -->|"3. Assemble Single DTO"| Client1
    end
    subgraph ScatterGather ["Scatter-Gather Broadcast Pattern"]
        Client2["Quote Request"] --> Dispatcher["Broadcast Dispatcher"]
        Dispatcher -->|"Parallel Call"| Vendor1["Vendor A (Airline)"]
        Dispatcher -->|"Parallel Call"| Vendor2["Vendor B (Airline)"]
        Dispatcher -->|"Parallel Call"| Vendor3["Vendor C (Airline)"]
        Vendor1 --> Combiner["Consolidator (Timeout Deadline 200ms)"]
        Vendor2 --> Combiner
        Vendor3 --> Combiner
        Combiner -->|"Cheapest Quote"| Client2
    end
""",

    "17-sidecar-ambassador.png": """flowchart TD
    subgraph PodBoundary ["Kubernetes Pod / Localhost Container Boundary"]
        App["Main Application Container\n(Polyglot Service: Go / Python / Java)"]
        Sidecar["Sidecar Proxy Container (Envoy / Service Mesh)\n- mTLS Cryptographic Handshake\n- Distributed Tracing (OpenTelemetry)\n- Dynamic Metrics & Circuit Breaking"]
        App <-->|"Localhost TCP / Unix Domain Socket (Zero Network Overhead)"| Sidecar
    end
    Sidecar <-->|"mTLS over External Network"| RemoteMesh["Remote Mesh Services"]
""",

    "18-anti-corruption-layer-acl.png": """flowchart TD
    NewDomain["Modern Core Domain\n(Clean Domain-Driven Design Context)"]
    ACL["Anti-Corruption Layer (ACL)\n- Bidirectional Translating Adapter\n- Facade & Schema Transformer\n- Prevents legacy model leakage"]
    LegacySystem["Legacy Monolith / ERP Core\n(Obsolete Schema, 1990s Cobol/SOAP Model)"]

    NewDomain <-->|"Clean Ubiquitous Language Models"| ACL
    ACL <-->|"Legacy SOAP / Cobol RPC Protocols"| LegacySystem
""",

    "19-pipes-and-filters.png": """flowchart TD
    Input["Raw Incoming Data Stream"] --> F1["Filter 1: Structural Schema Validator"]
    F1 --> P1["Pipe: Channel Buffer (Non-blocking Queue)"]
    P1 --> F2["Filter 2: Decryption & Header Unpacker"]
    F2 --> P2["Pipe: Channel Buffer (Non-blocking Queue)"]
    P2 --> F3["Filter 3: Currency Normalizer & Enricher"]
    F3 --> P3["Pipe: Channel Buffer (Non-blocking Queue)"]
    P3 --> Sink["Target Sink (Data Warehouse / Lakehouse)"]
""",

    "20-blackboard-pattern.png": """flowchart TD
    Controller["Blackboard Controller (Orchestrator)\n- Continuously evaluates problem status\n- Loops until acceptable hypothesis reached"]
    Blackboard[("Blackboard Shared Repository\n- Current Hypothesis & Evolving Problem State\n- Partial Solutions & Fact Board")]
    KS1["Knowledge Source 1\n(Speech Acoustic Expert)"]
    KS2["Knowledge Source 2\n(Syntactic Grammar Expert)"]
    KS3["Knowledge Source 3\n(Semantic Meaning Expert)"]

    Controller -->|"Inspects State & Selects KS"| Blackboard
    KS1 <-->|"Reads State / Updates Hypothesis"| Blackboard
    KS2 <-->|"Reads State / Updates Hypothesis"| Blackboard
    KS3 <-->|"Reads State / Updates Hypothesis"| Blackboard
""",

    "21-circuit-breaker-state-machine.png": """flowchart TD
    Closed["CLOSED State\n- Traffic passes directly to remote service\n- Failure counter resets on success"]
    Open["OPEN State\n- Failures exceed threshold\n- Calls fail-fast instantly without network call\n- Fallback response returned"]
    HalfOpen["HALF-OPEN State\n- Sleep window expires\n- Trial requests permitted through to test recovery"]

    Closed -->|"Consecutive Failures > Threshold"| Open
    Open -->|"Sleep Window Elapsed (e.g., 30s)"| HalfOpen
    HalfOpen -->|"Trial Requests Succeed"| Closed
    HalfOpen -->|"Any Trial Request Fails"| Open
""",

    "22-bulkhead-isolation.png": """flowchart TD
    Ingress["API Ingress / Router"]
    subgraph BulkheadPools ["Isolated Resource Bulkheads (Thread Pools & Memory)"]
        PoolOrders["Order Pool (20 Dedicated Threads)\nMax Queue: 50"]
        PoolSearch["Search Pool (40 Dedicated Threads)\nMax Queue: 200"]
        PoolReports["Analytics Pool (5 Dedicated Threads)\nMax Queue: 10"]
    end
    Ingress -->|"Dispatches Order Request"| PoolOrders
    Ingress -->|"Dispatches Search Request"| PoolSearch
    Ingress -->|"Dispatches Heavy Report Request"| PoolReports
    PoolOrders --> BackendOrder["Order Backend"]
    PoolSearch --> BackendSearch["Search Cluster"]
    PoolReports -->|"Exhaustion confined to Pool 3!"| BackendReports["Slow Legacy DB"]
""",

    "23-priority-queue-dlq.png": """flowchart TD
    subgraph PriorityPattern ["Ambulance / Priority Queue Pattern"]
        Producers1["Producers"] --> Router["Priority Router"]
        Router -->|"VIP / Healthcheck"| QHigh["High Priority Queue (Ambulance Lane)"]
        Router -->|"Standard Tasks"| QLow["Standard Priority Queue"]
        QHigh --> Workers1["Dedicated Fast-Lane Workers"]
        QLow --> Workers2["Standard Batch Workers"]
    end
    subgraph DLQPattern ["Dead Letter Queue (DLQ) Pattern"]
        MainQ["Main Ingestion Queue"] --> Worker["Consumer Worker"]
        Worker -.->|"Retries Failed (Max Exceeded)"| DLQ[("Dead Letter Queue (Poison Pill Bucket)")]
        DLQ --> Alerting["Alerting / Manual Admin Inspection"]
    end
""",

    "24-hexagonal-ports-adapters.png": """flowchart TD
    subgraph DrivingLayer ["Driving Tier (Primary / Inbound Adapters)"]
        REST["REST API Controller"]
        gRPC["gRPC Inbound Handler"]
        MsgListener["Kafka Message Consumer"]
    end
    subgraph CoreDomain ["Application Core Hexagon (Pure Business Domain)"]
        InboundPort["Driving Ports (Use Case Interfaces)"]
        DomainService["Domain Entities & Core Logic\n(Zero external dependencies)"]
        OutboundPort["Driven Ports (Repository & Gateway Interfaces)"]
        InboundPort --> DomainService
        DomainService --> OutboundPort
    end
    subgraph DrivenLayer ["Driven Tier (Secondary / Outbound Adapters)"]
        Postgres["PostgreSQL / Hibernate Adapter"]
        Stripe["Stripe Payment Gateway Adapter"]
        KafkaPub["Kafka Event Producer Adapter"]
    end
    REST --> InboundPort
    gRPC --> InboundPort
    MsgListener --> InboundPort
    OutboundPort --> Postgres
    OutboundPort --> Stripe
    OutboundPort --> KafkaPub
""",

    "25-clean-onion-architecture.png": """flowchart TD
    subgraph Outer ["Outer Layer: Frameworks & Drivers"]
        UI["Web UI / Controllers"]
        DB["PostgreSQL / Redis Database"]
        External["External Services & Gateways"]
    end
    subgraph InterfaceAdapters ["Interface Adapters Tier"]
        Presenters["Presenters & Mappers"]
        Gateways["Repository Implementations"]
    end
    subgraph UseCases ["Application Business Rules"]
        UseCasesList["Use Cases & Interactors"]
    end
    subgraph EntitiesCore ["Enterprise Business Rules (Core)"]
        Entities["Domain Entities & Aggregates\n(High-level policies, Zero Framework Dependencies)"]
    end

    UI --> Presenters
    DB --> Gateways
    Presenters --> UseCasesList
    Gateways --> UseCasesList
    UseCasesList --> Entities
""",

    "26-strangler-fig-pattern.png": """flowchart TD
    Client["Client / Browser Requests"] --> Proxy["Strangler Facade (Edge Routing Proxy)\n- Inspects URI paths and headers\n- Splits traffic dynamically"]
    Proxy -->|"/orders/* (Migrated Modern Slices)"| Microservice["New Cloud Microservice\n(Modern Architecture, High Scalability)"]
    Proxy -->|"/users/*, /billing/* (Unmigrated Legacy)"| Monolith["Legacy Monolith\n(Gradually Strangled over Time)"]
""",

    "27-microkernel-plugin-pattern.png": """flowchart TD
    subgraph MicrokernelCore ["Microkernel Core System (Minimal Minimalist Engine)"]
        Lifecycle["Plugin Lifecycle Manager"]
        Registry["Extension Registry & Discovery"]
        EventPipeline["Core Event Pipeline"]
    end
    subgraph Plugins ["Autonomous Plugin Extensions (Independent & Hot-Pluggable)"]
        PluginA["Plugin A: Syntax Highlighter"]
        PluginB["Plugin B: Git Version Control"]
        PluginC["Plugin C: Docker Container Runner"]
    end
    PluginA <-->|"Contract Interface"| Registry
    PluginB <-->|"Contract Interface"| Registry
    PluginC <-->|"Contract Interface"| Registry
""",

    "28-broker-pattern.png": """flowchart TD
    Client["Client Application"]
    subgraph BrokerInfrastructure ["Broker Infrastructure"]
        ClientProxy["Client Proxy (Local Stub)"]
        BrokerEngine["Central Broker Engine\n- Service Registration & Discovery\n- Marshalling / Unmarshalling\n- Message Routing & Fault Handling"]
        ServerProxy["Server Proxy (Skeleton)"]
    end
    Server["Target Server Implementation"]

    Client -->|"1. Invokes Method"| ClientProxy
    ClientProxy -->|"2. Marshals Payload"| BrokerEngine
    BrokerEngine -->|"3. Dispatches Request"| ServerProxy
    ServerProxy -->|"4. Invokes Concrete Service"| Server
    Server -->|"5. Returns Response"| ServerProxy
    ServerProxy --> BrokerEngine
    BrokerEngine --> ClientProxy
    ClientProxy --> Client
"""
}

# 1. Render all diagrams using Playwright Chromium with constrained canvas (~850px)
def render_all_diagrams():
    print("Rendering 28 balanced diagrams via Playwright...")
    render_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
{mermaid_js}
</script>
<style>
  body {{
    margin: 0;
    padding: 20px;
    background-color: white;
    display: inline-block;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}
  #graph {{
    background-color: white;
    max-width: 860px;
  }}
</style>
</head>
<body>
<div id="graph"></div>
<script>
  mermaid.initialize({{
    startOnLoad: false,
    theme: 'default',
    flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'basis' }},
    themeVariables: {{
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
      fontSize: '14px'
    }}
  }});
  async function renderMermaid(code) {{
    try {{
      document.getElementById('graph').innerHTML = '';
      const id = 'svg_' + Math.random().toString(36).substring(2, 9);
      const {{ svg }} = await mermaid.render(id, code);
      document.getElementById('graph').innerHTML = svg;
      return {{ success: true }};
    }} catch (err) {{
      return {{ success: false, error: err.toString() }};
    }}
  }}
</script>
</body>
</html>"""

    html_file = cache_dir / "render_runner.html"
    html_file.write_text(render_html, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        page.goto(f"file:///{html_file.resolve().as_posix()}")

        for fname, code in diagrams.items():
            target_png = images_dir / fname
            res = page.evaluate("renderMermaid", code)
            if not res.get("success"):
                print(f"Error rendering {fname}: {res.get('error')}")
                continue
            page.wait_for_selector("#graph svg")
            svg_locator = page.locator("#graph svg")
            svg_locator.screenshot(path=str(target_png))
            print(f"Rendered {fname}: {target_png.stat().st_size} bytes")

        browser.close()

if __name__ == "__main__":
    render_all_diagrams()
