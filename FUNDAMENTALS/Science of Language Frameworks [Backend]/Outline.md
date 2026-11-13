# Science of Language Frameworks [Backend] - Outline

Deep mechanical analysis of server-side programming runtimes, language ecosystems, and backend web frameworks.

---

## 📌 Core Modules

### 1. Runtime Mechanics & Execution Models
- **Thread Models**: Thread-per-request vs Event Loop (Reactor / Proactor pattern).
- **Concurrency & Parallelism**: OS threads, green threads / virtual threads (Java Project Loom, Go goroutines), async/await (Node.js, Rust, Python asyncio).
- **Memory Management & Garbage Collection**: JVM generational GC (G1, ZGC), Go non-generational concurrent mark-sweep, Rust compile-time RAII / ownership & borrowing.

### 2. Language Ecosystems & Frameworks
- **Java / JVM**: Spring Boot (Spring MVC vs Spring WebFlux), Quarkus, Micronaut, Dependency Injection (IoC), Reflection vs Ahead-of-Time (AOT) compilation.
- **Go**: Gin, Echo, Fiber, standard library `net/http`, channels, worker pools, zero-allocation design.
- **Node.js / TypeScript**: Express, NestJS, Fastify, event loop phases (`libuv`), cluster module, worker threads.
- **Python**: FastAPI, Django, Flask, ASGI vs WSGI, async database drivers, GIL limitations and multi-processing.
- **Rust / C++**: Actix-web, Axum, Tokio runtime, zero-cost abstractions, memory safety without GC.

### 3. Networking, Protocols & I/O
- **Sockets & Transport**: TCP vs UDP, HTTP/1.1 (pipelining, keep-alive) vs HTTP/2 (multiplexing, binary framing) vs HTTP/3 (QUIC).
- **API Paradigms**: RESTful principles, gRPC (Protocol Buffers, streaming RPCs), GraphQL (schemas, resolvers, N+1 query problem), WebSockets, Server-Sent Events (SSE).
- **Serialization & Deserialization**: JSON, Protocol Buffers, FlatBuffers, Avro, performance benchmarks and byte layouts.

### 4. Persistence & Data Access Layers
- **Object-Relational Mapping (ORM) vs Raw SQL**: Hibernate/JPA, Prisma, GORM, SQLAlchemy, lazy loading traps, connection pooling (HikariCP).
- **Database Drivers & Connection Management**: Socket pooling, prepared statements, transaction boundaries (`@Transactional`), ACID vs BASE semantics.
- **Caching Integration**: In-process cache (Guava, Caffeine) vs Distributed cache (Redis, Memcached), cache serialization overhead.

### 5. Resilience & Production Readiness
- **Stability Patterns**: Circuit breakers (Resilience4j), rate limiting, exponential backoff with jitter, bulkhead isolation.
- **Observability**: Structured logging (Logback, Winston), distributed tracing (OpenTelemetry, Jaeger), application metrics (Prometheus, Micrometer).
- **Graceful Shutdown & Health Checks**: Liveness and readiness probes, signal handling (SIGTERM, SIGINT).

