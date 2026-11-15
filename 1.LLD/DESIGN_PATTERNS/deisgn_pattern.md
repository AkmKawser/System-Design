# Software Design Patterns & Anti-Patterns Guide

Design patterns are formalized, reusable solutions to recurring problems in software engineering. When used incorrectly, overused, or misapplied, they can evolve into architectural **anti-patterns** that harm maintainability, performance, and testability.

This document classifies design patterns into their primary categories:
1. **Creational Patterns** (Object creation mechanisms)
2. **Structural Patterns** (Class & object composition)
3. **Behavioral Patterns** (Algorithms & assignment of responsibilities between objects)
4. **Concurrency / Architectural Patterns** (Multithreading & system-level organization)

---

## 1. Creational Patterns

Creational patterns abstract the instantiation process, decoupling a system from how its objects are created, composed, and represented.

| Pattern | Intent / Core Mechanism | Common Anti-Patterns / Misuse |
| :--- | :--- | :--- |
| **Singleton** | Ensures a class has only one instance and provides a global point of access to it. | **Global State & Hidden Dependencies**: Becomes an untestable global variable disguised as an object.<br>**God Object / Kitchen Sink**: The singleton slowly absorbs unrelated domain responsibilities.<br>**Concurrency Bottleneck**: Locks on shared singleton instances cause contention and race conditions. |
| **Factory Method** | Defines an interface for creating an object, but lets subclasses decide which class to instantiate. | **Poltergeist Factory**: Factories with no complex logic that simply do `return new Foo()`.<br>**Parallel Class Hierarchies**: Adding a new product requires creating a matching factory subclass every single time. |
| **Abstract Factory** | Provides an interface for creating families of related or dependent objects without specifying concrete classes. | **Factory Factory / Over-Engineering**: Nesting factories inside factories creating rigid, boilerplate-heavy class trees.<br>**Leaky Abstractions**: Generic product interfaces failing to expose family-specific functionality. |
| **Builder** | Separates construction of a complex object from its representation, enabling step-by-step creation. | **Telescoping Builder**: Endless chained setter methods where default values or simple configuration records/DTOs would suffice.<br>**Incomplete / Inconsistent State**: Instances accessed before calling `build()`, or builder lacking terminal validation. |
| **Prototype** | Specifies the kinds of objects to create using a prototypical instance, creating new objects by cloning. | **Shallow Copy Bug**: Cloning objects containing mutable references, corrupting state across copies.<br>**Circular Reference Lock**: Deep copy implementations encountering circular references leading to stack overflow. |
| **Object Pool** | Reuses objects from a pre-allocated pool instead of instantiating and destroying them on demand. | **Memory Leaks / Zombie Objects**: Borrowed objects not returned to the pool, or returned with dirty state.<br>**Premature Optimization**: Pooling cheap, short-lived objects that modern garbage collectors handle more efficiently. |

---

## 2. Structural Patterns

Structural patterns deal with object and class composition, using inheritance and interfaces to compose larger structures out of flexible components.

| Pattern | Intent / Core Mechanism | Common Anti-Patterns / Misuse |
| :--- | :--- | :--- |
| **Adapter** (Wrapper) | Converts the interface of a class into another interface clients expect, enabling incompatible interfaces to collaborate. | **Two-Way Adapter Spaghetti**: Overly complex bidirectional translations leading to unpredictable state mutations.<br>**Adapter Overload**: Wrapping trivial APIs with thin layers that obscure native errors and add indirection. |
| **Bridge** | Decouples an abstraction from its implementation so that the two can vary independently. | **Over-Abstraction**: Splitting hierarchies that have no realistic future variation, increasing cognitive load.<br>**Explosion of Small Interfaces**: Fragmenting simple designs into excessive layers of abstraction without clear bounds. |
| **Composite** | Composes objects into tree structures to represent part-whole hierarchies, treating individual objects and compositions uniformly. | **Type Safety Violation**: Exposing child management methods (`add()`, `remove()`) on leaf nodes, leading to runtime unsupported-operation exceptions.<br>**Deep Recursive Traversal**: Naive traversals causing stack overflow or severe performance degradation on large hierarchies. |
| **Decorator** | Attaches additional responsibilities to an object dynamically as an alternative to subclassing. | **Decorator Hell / Russian Doll**: Stacking 10+ layers of decorators, making debugging and stack trace analysis nearly impossible.<br>**Order Dependency**: Behavior silently breaks if decorators are wrapped in the incorrect sequence. |
| **Facade** | Provides a unified, simplified interface to a complex subsystem or library. | **God Facade**: Facade expands into a monolithic module that knows too much about internal subsystems.<br>**Walled Garden**: Facade completely prevents clients from accessing necessary lower-level functionality when special cases arise. |
| **Flyweight** | Shares fine-grained object instances to support large quantities of objects efficiently with minimal memory. | **Leaky Extrinsic State**: Failing to strictly decouple intrinsic (shared) state from extrinsic (context-specific) state, causing data corruption across threads.<br>**Thread Synchronization Bottlenecks**: Heavy locking overhead on the shared flyweight factory cancelling out memory savings. |
| **Proxy** | Provides a surrogate or placeholder for another object to control access, delay initialization, or provide remote communication. | **Ghost Operations / Hidden Latency**: Virtual proxies triggering expensive I/O operations transparently during simple getter calls.<br>**Broken Identity (Self-Invocation Issue)**: Calling methods internally within a proxied object bypasses proxy interceptors (common in Spring `@Transactional` pitfalls). |

---

## 3. Behavioral Patterns

Behavioral patterns focus on algorithms, responsibility assignments, and communication mechanisms between interacting objects.

| Pattern | Intent / Core Mechanism | Common Anti-Patterns / Misuse |
| :--- | :--- | :--- |
| **Chain of Responsibility** | Passes requests along a chain of handlers until one of them processes the request. | **Black Hole Request**: Request travels through the entire chain unhandled and is silently dropped with no fallback.<br>**Hidden Cycles**: Misconfigured chain references creating an infinite loop at runtime. |
| **Command** | Encapsulates a request as an object, allowing parameterization, queuing, logging, and undoable operations. | **Class Explosion**: Generating a standalone command class for every trivial single-line action.<br>**Stale Command State**: Cached command objects holding references to outdated or mutated domain models during undo/redo operations. |
| **Interpreter** | Given a language, defines a representation for its grammar along with an interpreter that uses the representation to evaluate sentences. | **Grammar Bloat**: Using tree-based interpretation for complex languages instead of parser generators or AST compilers, destroying performance.<br>**Unbounded Recursion**: Deep syntax trees leading to call stack exhaustion. |
| **Iterator** | Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. | **Concurrent Modification Hell**: Modifying an underlying collection during traversal without proper synchronized snapshots or concurrent iterators.<br>**Dual Traversal Inefficiency**: Iterators holding lock states over distributed or remote data stores. |
| **Mediator** | Defines an object that encapsulates how a set of objects interact, preventing them from referring to each other explicitly. | **God Mediator**: Central mediator turns into a complex monolithic brain that knows every detail about every participant.<br>**Tight Coupling to Mediator**: Colleague objects become useless outside the context of that specific mediator. |
| **Memento** | Captures and externalizes an object’s internal state without violating encapsulation, allowing restoration later. | **Memory Hog**: Storing full object snapshots frequently instead of delta states, leading to out-of-memory errors.<br>**Encapsulation Breach**: Exposing private state fields via public memento getters. |
| **Observer** (Pub/Sub) | Defines a one-to-many dependency so that when one object changes state, all its dependents are notified and updated automatically. | **Lapsed Listener (Memory Leak)**: Subscribers fail to unsubscribe, causing the subject to retain strong references and preventing garbage collection.<br>**Cascade / Ripple Effects**: Notification storms and cyclic updates where Observer A updates Subject B, which triggers Observer A again. |
| **State** | Allows an object to alter its behavior when its internal state changes, appearing to change its class. | **Combinatorial Explosion of States**: Defining separate classes for minor state nuances instead of composite state machines.<br>**Leaky Transitions**: State classes knowing concrete downstream states, creating tight circular coupling between states. |
| **Strategy** | Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime. | **Strategy Creep**: Creating micro-strategies for 2-line functions that could simply be passed as lambdas / first-class functions.<br>**Context Pollution**: Strategy requiring broad context access, forcing the context to expose internal private variables. |
| **Template Method** | Defines the skeleton of an algorithm in an operation, deferring some steps to subclasses without changing algorithm structure. | **Fragile Base Class**: Subclasses inadvertently break the template algorithm flow by failing to call `super` or violating base invariants.<br>**Inheritance Rigidity**: Forced inheritance prevents classes from using alternative algorithms at runtime. |
| **Visitor** | Represents an operation to be performed on elements of an object structure, letting you define new operations without changing element classes. | **Double Dispatch Complexity**: Adding a new element type requires modifying every single visitor implementation in the codebase.<br>**Encapsulation Breakdown**: Elements forced to expose their internal implementation details publicly so visitors can operate on them. |

---

## 4. Concurrency & Architectural Patterns

| Pattern | Intent / Core Mechanism | Common Anti-Patterns / Misuse |
| :--- | :--- | :--- |
| **Active Object** | Decouples method execution from method invocation for objects that reside in their own thread of control. | **Queue Starvation & OOM**: Unbounded request queues running out of memory under burst traffic.<br>**Priority Inversion**: High-priority tasks stuck behind slow tasks in FIFO execution queues. |
| **Circuit Breaker** | Prevents an application from repeatedly trying to execute an operation that's likely to fail. | **Premature Opening / Flapping**: Setting trip thresholds too low, causing transient blips to shut down traffic.<br>**Infinite Half-Open Loop**: Poor probe requests that always succeed while real payloads consistently fail. |
| **Read-Write Lock** | Allows concurrent read access while restricting write access to exclusive locks. | **Writer Starvation**: Continuous influx of readers preventing write operations from acquiring the lock.<br>**Lock Convoy**: High lock contention degrading throughput below single-thread performance. |
| **Producer-Consumer** | Decouples producers of work from consumers through a synchronized shared queue. | **Unbounded Buffer Overflow**: Producers outpacing consumers, leading to system crash.<br>**Poison Pill Failure**: Malformed tasks persistently failing and blocking downstream consumers. |

---

## Summary: The "Golden Rules" to Avoid Pattern Abuse

1. **Rule of Three**: Do not introduce a pattern before a problem has surfaced at least three distinct times in your system.
2. **Prefer Composition Over Inheritance**: Patterns like Strategy and Decorator are safer long-term than rigid inheritance structures like Template Method.
3. **Beware Pattern-Driven Development (PDD)**: Patterns are tools to solve specific problems, not badges of design superiority. Favor simplicity (KISS / YAGNI) first.
