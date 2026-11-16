# Course Curriculum: Fundamentals of Backend Engineering

> **Course Metadata**:
> - **Instructor**: Hussein Nasser
> - **Platform**: Udemy
> - **Subject**: Backend Engineering, Communication Design Patterns, Network Protocols, Execution Models & Proxies
> - **Ingestion Path**: [`topics/0.FUNDAMENTALS/API Architecture and Design/Data_Ingestion/Courses/Udemy-Fundamentals of Backend Engineering/`](./)
> - **Synthesis Deliverable**: [`API_Architecture_and_Design.md`](../../output/Note_version-1_API_Architecture_and_Design/API_Architecture_and_Design.md)

---

## 📋 Course Overview & Ingestion Objectives

This course establishes the low-level networking, transport protocols, connection management, threading execution models, and reverse proxy architectures required for resilient, high-throughput backend systems.

Per `engine/engine.md` § 4.2 (*Channel 2: Courses Ingestion*), this curriculum indexes all 8 modules and 64 lecture transcripts for deterministic retrieval and architectural synthesis.

---

## 🗂️ Detailed Module Breakdown

### Section 1: Introduction & Foundations (5 Lectures)
Foundational orientation, course objectives, and prerequisite alignment.

| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **1.1** | Welcome to the course | [01_Welcome.md](01_Introduction/01_Welcome.md) |
| **1.2** | Target audience & required engineering background | [02_Who is this course for.md](01_Introduction/02_Who%20is%20this%20course%20for.md) |
| **1.3** | Course outline & roadmap walkthrough | [03_Course Outline.md](01_Introduction/03_Course%20Outline.md) |
| **1.4** | Lecture notes and reference guides | [04_Course Notes.md](01_Introduction/04_Course%20Notes.md) |
| **1.5** | Resource downloads, slides, and source code | [05_Download all slides, source code and references.md](01_Introduction/05_Download%20all%20slides,%20source%20code%20and%20references.md) |

---

### Section 2: Backend Communication Design Patterns (11 Lectures)
Comprehensive analysis of interaction models between clients, frontends, and backend services.

| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **2.1** | Backend communication patterns introduction | [01_Backend Communication Design Patterns Intro.md](02_Backend%20Communication%20Design%20Patterns/01_Backend%20Communication%20Design%20Patterns%20Intro.md) |
| **2.2** | The Request-Response model: parsing streams, boundary delimiters | [02_Request Response.md](02_Backend%20Communication%20Design%20Patterns/02_Request%20Response.md) |
| **2.3** | The Push model: real-time updates and notification mechanics | [03_Push.md](02_Backend%20Communication%20Design%20Patterns/03_Push.md) |
| **2.4** | Synchronous vs. Asynchronous workloads: worker queues and job IDs | [04_Synchronous vs Asynchronous workloads.md](02_Backend%20Communication%20Design%20Patterns/04_Synchronous%20vs%20Asynchronous%20workloads.md) |
| **2.5** | Short Polling: repetitive queries and network cost | [05_Polling.md](02_Backend%20Communication%20Design%20Patterns/05_Polling.md) |
| **2.6** | Long Polling: open socket holds and browser connection limits | [06_Long Polling.md](02_Backend%20Communication%20Design%20Patterns/06_Long%20Polling.md) |
| **2.7** | Server-Sent Events (SSE): HTTP streaming push over `text/event-stream` | [07_Server Sent Events.md](02_Backend%20Communication%20Design%20Patterns/07_Server%20Sent%20Events.md) |
| **2.8** | Publish-Subscribe (PubSub): topic fan-out, RabbitMQ vs. Kafka | [08_Publish Subscribe (PubSub).md](02_Backend%20Communication%20Design%20Patterns/08_Publish%20Subscribe%20(PubSub).md) |
| **2.9** | Multiplexing vs. Demultiplexing: H2 proxying vs. connection pooling | [09_Multiplexing vs Demultiplexing.md](02_Backend%20Communication%20Design%20Patterns/09_Multiplexing%20vs%20Demultiplexing%20(h2%20proxying%20vs%20Connection%20Pooling).md) |
| **2.10** | Stateful vs. Stateless backends: sticky sessions vs. horizontal scale | [10_Stateful vs Stateless.md](02_Backend%20Communication%20Design%20Patterns/10_Stateful%20vs%20Stateless.md) |
| **2.11** | The Sidecar Pattern: proxying, mTLS, and observability offload | [11_Sidecar Pattern.md](02_Backend%20Communication%20Design%20Patterns/11_Sidecar%20Pattern.md) |

---

### Section 3: Protocols (14 Lectures)
Network and transport layer protocols that underpin API and backend communications.

| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **3.1** | Protocols overview and design tradeoffs | [01_Protocols Intro.md](03_Protocols/01_Protocols%20Intro.md) |
| **3.2** | Protocol properties: text vs. binary, stateful vs. stateless | [02_Protocol Properties.md](03_Protocols/02_Protocol%20Properties.md) |
| **3.3** | The OSI Model: Layer 1 through Layer 7 mechanics | [03_OSI Model.md](03_Protocols/03_OSI%20Model.md) |
| **3.4** | Internet Protocol (IP): IPv4 vs. IPv6 packet structures and MTU | [04_Internet Protocol.md](03_Protocols/04_Internet%20Protocol.md) |
| **3.5** | User Datagram Protocol (UDP): datagram boundaries and speed | [05_UDP.md](03_Protocols/05_UDP.md) |
| **3.6** | Transmission Control Protocol (TCP): 3-way handshake, ACKs, flow control | [06_TCP.md](03_Protocols/06_TCP.md) |
| **3.7** | Transport Layer Security (TLS): asymmetric encryption and certificates | [07_TLS.md](03_Protocols/07_TLS.md) |
| **3.8** | HTTP/1.1: persistent connections, pipelining, chunked transfer | [08_HTTP1.1.md](03_Protocols/08_HTTP1.1.md) |
| **3.9** | HTTPS, TLS, Public Keys, Certificates, and CA hierarchies | [09_HTTPS, TLS, Keys and Certificates.md](03_Protocols/09_HTTPS,%20TLS,%20Keys%20and%20Certificates.md) |
| **3.10** | WebSockets: HTTP 101 upgrade, framing, full-duplex streams | [10_WebSockets.md](03_Protocols/10_WebSockets.md) |
| **3.11** | HTTP/2: binary framing, streams, multiplexing, and HPACK | [11_HTTP2.md](03_Protocols/11_HTTP2.md) |
| **3.12** | HTTP/3: QUIC transport, solving TCP Head-of-Line blocking | [12_HTTP3.md](03_Protocols/12_HTTP3.md) |
| **3.13** | gRPC: Google RPC over HTTP/2 with Protocol Buffers | [13_gRPC.md](03_Protocols/13_gRPC.md) |
| **3.14** | WebRTC: peer-to-peer real-time audio, video, and data channels | [14_WebRTC.md](03_Protocols/14_WebRTC.md) |

---

### Section 4: Many Ways to HTTPS (7 Lectures)
Deep dive into cryptographic handshakes, TLS versions, and latency optimization.

| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **4.1** | HTTPS communication basics and handshake cost | [01_HTTPS Communication Basics Intro.md](04_Many%20ways%20to%20HTTPS/01_HTTPS%20Communication%20Basics%20Intro.md) |
| **4.2** | HTTPS over TCP with TLS 1.2 (2-RTT handshake) | [02_HTTPS over TCP with TLS 1.2.md](04_Many%20ways%20to%20HTTPS/02_HTTPS%20over%20TCP%20with%20TLS%201.2.md) |
| **4.3** | HTTPS over TCP with TLS 1.3 (1-RTT handshake) | [03_HTTPS over TCP with TLS 1.3.md](04_Many%20ways%20to%20HTTPS/03_HTTPS%20over%20TCP%20with%20TLS%201.3.md) |
| **4.4** | HTTPS over QUIC (HTTP/3 1-RTT connection setup) | [04_HTTPS over QUIC (HTTP3).md](04_Many%20ways%20to%20HTTPS/04_HTTPS%20over%20QUIC%20(HTTP3).md) |
| **4.5** | HTTPS over TCP Fast Open (TFO) with TLS 1.3 | [05_HTTPS over TFO with TLS 1.3.md](04_Many%20ways%20to%20HTTPS/05_HTTPS%20over%20TFO%20with%20TLS%201.3.md) |
| **4.6** | HTTPS over TCP with TLS 1.3 and 0-RTT: replay attack risks | [06_HTTPS over TCP with TLS 1.3 and 0RTT.md](04_Many%20ways%20to%20HTTPS/06_HTTPS%20over%20TCP%20with%20TLS%201.3%20and%200RTT.md) |
| **4.7** | HTTPS over QUIC with 0-RTT Early Data | [07_HTTPS over QUIC with 0RTT.md](04_Many%20ways%20to%20HTTPS/07_HTTPS%20over%20QUIC%20with%200RTT.md) |

---

### Section 5: Backend Execution Patterns (13 Lectures)
Kernel sockets, threading architectures, concurrency models, and low-level optimizations.

| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **5.1** | Backend execution patterns introduction | [01_Backend Execution Patterns Intro.md](05_Backend%20Execution%20Patterns/01_Backend%20Execution%20Patterns%20Intro.md) |
| **5.2** | The Process and The Thread: CPU scheduling and context switching | [02_The Process and The Thread.md](05_Backend%20Execution%20Patterns/02_The%20Process%20and%20The%20Thread%20and%20how%20they%20compete%20for%20CPU%20time.md) |
| **5.3** | How the backend accepts connections: SYN queue vs. Accept queue | [03_How The Backend Accepts Connections.md](05_Backend%20Execution%20Patterns/03_How%20The%20Backend%20Accepts%20Connections.md) |
| **5.4** | Reading and sending socket data: kernel buffers and system calls | [04_Reading and Sending Socket Data.md](05_Backend%20Execution%20Patterns/04_Reading%20and%20Sending%20Socket%20Data.md) |
| **5.5** | The Listener, Acceptor, and Reader responsibilities | [05_The Listener, The Acceptor and the Reader.md](05_Backend%20Execution%20Patterns/05_The%20Listener,%20The%20Acceptor%20and%20the%20Reader.md) |
| **5.6** | Single Listener, Acceptor, and Reader execution pattern | [06_Single Thread Pattern.md](05_Backend%20Execution%20Patterns/06_Single%20Listener,%20Acceptor%20and%20Reader%20Thread%20Execution%20Pattern.md) |
| **5.7** | Single Listener/Acceptor with Multiple Reader threads pattern | [07_Single Acceptor Multiple Readers.md](05_Backend%20Execution%20Patterns/07_Single%20Listener,%20Acceptor%20and%20Multiple%20Readers%20Thread%20Execution%20Pattern.md) |
| **5.8** | Single Listener/Acceptor/Reader with message load balancing | [08_Worker Pool Load Balancing.md](05_Backend%20Execution%20Patterns/08_Single%20Listener,%20Acceptor,%20Reader%20with%20Message%20Load%20Balancing%20Execution%20Pattern.md) |
| **5.9** | Multiple Acceptor threads on a single socket | [09_Multiple Acceptor Threads.md](05_Backend%20Execution%20Patterns/09_Multiple%20Accepter%20Threads%20on%20a%20Single%20Socket%20Execution%20Pattern.md) |
| **5.10** | Socket Sharding (`SO_REUSEPORT`): kernel-level port distribution | [10_Socket Sharding Pattern.md](05_Backend%20Execution%20Patterns/10_Multiple%20Listeners,%20Acceptors%20and%20Readers%20with%20Socket%20Sharding%20Execution%20Pattern.md) |
| **5.11** | Backend Idempotency: safe retries and deduplication tokens | [11_Backend Idempotency.md](05_Backend%20Execution%20Patterns/11_Backend%20Idempotency.md) |
| **5.12** | Nagle's Algorithm: buffering vs. Delayed ACK latency clashing | [12_Nagles Algorithm.md](05_Backend%20Execution%20Patterns/12_Nagle's%20Algorithm.md) |
| **5.13** | When to use threads: CPU-bound vs. I/O-bound workload allocation | [13_When do you use threads.md](05_Backend%20Execution%20Patterns/13_When%20do%20you%20use%20threads.md) |

---

### Section 6: Proxying & Load Balancing (3 Lectures)
Traffic routing, transport vs. application load balancing, and proxy protocols.

| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **6.1** | Forward Proxy vs. Reverse Proxy: client privacy vs. backend shielding | [01_Proxy vs Reverse Proxy.md](06_Proxying%20and%20Load%20Balancing/01_Proxy%20vs%20Reverse%20Proxy.md) |
| **6.2** | Layer 4 (TCP/UDP) vs. Layer 7 (HTTP/gRPC) Load Balancers | [02_Layer 4 vs Layer 7 Load Balancers.md](06_Proxying%20and%20Load%20Balancing/02_Layer%204%20vs%20Layer%207%20Load%20Balancers.md) |
| **6.3** | WebSocket Proxying: header preservation and stateful routing | [03_WebSocket Proxying.md](06_Proxying%20and%20Load%20Balancing/03_WebSocket%20Proxying.md) |

---

### Section 7: Extras (6 Lectures)
Real-world systems, architectural breakdowns, and performance pitfalls.

| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **7.1** | How ChatGPT uses Server-Sent Events (SSE) for streaming text | [01_How ChatGPT uses Server Sent Events.md](07_Extras/01_How%20ChatGPT%20uses%20Server%20Sent%20Events.md) |
| **7.2** | How I design software: architectural methodology and mental models | [02_How I design software.md](07_Extras/02_How%20I%20design%20software.md) |
| **7.3** | The 10-stage journey of a request to the backend | [03_The Journey of a Request to the Backend.md](07_Extras/03_The%20Journey%20of%20a%20Request%20to%20the%20Backend.md) |
| **7.4** | The Journey of a Request to the Backend (Video walkthrough) | [04_The Journey of a Request to the Backend (Video).md](07_Extras/04_The%20Journey%20of%20a%20Request%20to%20the%20Backend%20(Video).md) |
| **7.5** | JSON Web Token (JWT): stateless claims, pros, and security cons | [05_JSON Web Token (JWT), its Pros and Cons.md](07_Extras/05_JSON%20Web%20Token%20(JWT),%20its%20Pros%20and%20Cons.md) |
| **7.6** | Why `SELECT COUNT(*)` impacts backend database performance | [06_SELECT COUNT () can impact your Backend Application performance.md](07_Extras/06_SELECT%20COUNT%20()%20can%20impact%20your%20Backend%20Application%20performance,%20here%20is%20why.md) |

---

### Section 8: Bonus Content (5 Lectures)
Kernel internals, TCP corner cases, OWASP vulnerabilities, and connection shutdown.

| Lecture | Topic & Summary | Reference File |
| :--- | :--- | :--- |
| **8.1** | How the OS Kernel manages backend connections and queues | [01_How does the Kernel manage backend connections.md](08_Bonus%20Content/01_How%20does%20the%20Kernel%20manage%20backend%20connections.md) |
| **8.2** | Running out of TCP ports: ephemeral port exhaustion & `TIME_WAIT` | [02_Running out of TCP Ports.md](08_Bonus%20Content/02_Running%20out%20of%20TCP%20Ports.md) |
| **8.3** | Postgres failure caused by a Cisco router: MTU black hole & TCP window | [03_Postgres failure caused by a Cisco router (TCP issue).md](08_Bonus%20Content/03_Postgres%20failure%20caused%20by%20a%20Cisco%20router%20(TCP%20issue).md) |
| **8.4** | Building secure backend applications: OWASP top recommendations | [04_Building Secure Backend Applications (OWASP recommendations).md](08_Bonus%20Content/04_Building%20Secure%20Backend%20Applications%20(OWASP%20recommendations).md) |
| **8.5** | HTTP Graceful Connection Shutdown: TCP FIN handshakes & draining | [05_HTTP Graceful Connection Shutdown.md](08_Bonus%20Content/05_HTTP%20Graceful%20Connection%20Shutdown.md) |

---

## 🔗 Repository Integration & Traceability

1. **Full Text Transcript**: The unedited continuous course transcript is archived in [`Course Fundamentals of Backend Engineering_Full.md`](Course%20Fundamentals%20of%20Backend%20Engineering_Full.md).
2. **Master Architecture Synthesis**: Ingested architectural concepts, design patterns, socket models, and proxying strategies are permanently synthesized in [`API_Architecture_and_Design.md`](../../output/Note_version-1_API_Architecture_and_Design/API_Architecture_and_Design.md).
3. **Audit Compliance**: Verified with zero rendering errors under `engine/scripts/audit_rendering.py`.
