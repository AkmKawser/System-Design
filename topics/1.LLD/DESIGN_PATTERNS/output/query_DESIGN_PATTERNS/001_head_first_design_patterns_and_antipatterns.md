# Head First Design Patterns: Complete Patterns & Anti-Patterns Catalog

> **Source Attribution**: Extracted and synthesized directly from ***Head First Design Patterns (2nd Edition)*** by Eric Freeman & Elisabeth Robson (O'Reilly Media), cross-referencing Chapters 1 through 14, Chapter 13 (*"Better Living with Patterns: Annihilating Evil with Anti-Patterns"*, pp. 592–593), and the GoF catalog in Chapter 14.

---

## 1. What is an Anti-Pattern according to *Head First Design Patterns*?

In Chapter 13 (*Annihilating evil with Anti-Patterns*, p. 592), the authors define an **Anti-Pattern**:

> *"An Anti-Pattern tells you how to go from a problem to a **BAD** solution.*
> *An anti-pattern always looks like a good solution, but then turns out to be a bad solution when it is applied.*
> *By documenting anti-patterns we help others to recognize bad solutions before they implement them. Avoiding bad solutions can be just as valuable as finding good ones!"*

### Core Anatomy of an Anti-Pattern (HFDP Specification):
1. **Name**: A distinctive, memorable label (e.g. *Golden Hammer*).
2. **Problem & Context**: The scenario where the problem occurs.
3. **Forces**: Why developers are tempted into this bad solution (unfamiliarity, time pressure, perceived risk).
4. **Supposed Solution**: The seductive, flawed choice made up front.
5. **Why It Fails**: Long-term consequences (rigidity, fragile base classes, tight coupling).
6. **Refactored Solution**: The clean, pattern-grounded resolution.

---

## 2. Complete Patterns Catalog: Book Invariants vs. Seductive Anti-Patterns

The table below catalogs every pattern featured in *Head First Design Patterns (2nd Edition)*, mapping each to:
- **HFDP Chapter & Role**: Primary chapter coverage.
- **Pattern Classification**: Creational, Structural, Behavioral, or Compound.
- **The Book's Initial Flawed / Naive Design**: The exact anti-pattern or design trap presented at the beginning of each chapter in the book.
- **The Pattern's Clean Resolution**: How the design pattern refactors the problem.
- **Post-Adoption Anti-Patterns & Misuse**: How developers misuse or over-apply the pattern (the *"Patterns Overuse / Golden Hammer"* trap discussed in Chapter 13).

| Chapter & Pattern | Type | The Seductive Initial Trap / Anti-Pattern (Book Problem) | The Pattern Solution (Head First Design) | Post-Adoption Anti-Patterns & Misuse Traps |
| :--- | :--- | :--- | :--- | :--- |
| **Ch 1: Strategy Pattern** | Behavioral | **Inheritance Explosion & Fragile Base Class**:<br>Adding `fly()` to the `Duck` superclass caused rubber ducks and wooden decoy ducks to fly in the `SimUDuck` app. Attempting to use interfaces (`Flyable`, `Quackable`) resulted in code duplication across dozens of concrete duck classes. | **Encapsulate What Varies via Composition**:<br>Separate fly and quack behaviors into behavior interfaces (`FlyBehavior`, `QuackBehavior`). Duck delegates behavior dynamically at runtime (`HAS-A` instead of `IS-A`). | **Strategy Creep / Classitis**:<br>Creating 20 separate one-line strategy classes instead of using simple lambdas or method references; forcing context classes to expose private internals to strategies. |
| **Ch 2: Observer Pattern** | Behavioral | **Hardcoded Concrete Dispatch / Spaghetti Coupling**:<br>The initial `WeatherData` implementation hardcoded method calls to specific concrete display objects (`currentConditionsDisplay.update()`, `statisticsDisplay.update()`), violating OCP whenever new displays were added or removed. | **One-to-Many Loose Coupling (Pub/Sub)**:<br>`Subject` interface maintains dynamic collection of `Observer` interfaces. Observers register/unregister dynamically and are notified uniformly via `update()`. | **Lapsed Listener (Memory Leaks) & Cascades**:<br>Subscribers failing to unregister causing memory retention; notification storms where Observer A triggers Subject B, triggering A recursively. |
| **Ch 3: Decorator Pattern** | Structural | **Class Explosion via Subclassing**:<br>`Starbuzz Coffee` attempted to subclass `Beverage` for every combination of condiments (`HouseBlendWithSteamedMilkAndMocha`), leading to dozens of classes, or stuffed boolean flags into the base class, breaking whenever condiment prices changed or customers ordered double mocha. | **Dynamic Runtime Wrapping**:<br>Decorators implement the same abstract type as the component they wrap. They pass through calls while adding new behavior before/after, adhering to the Open-Closed Principle. | **Decorator Hell / Russian Doll**:<br>Stacking 10+ decorator layers obscuring stack traces; order-dependency bugs where wrappers behave differently if chained out of sequence. |
| **Ch 4: Factory Method Pattern** | Creational | **Monster Conditional Instantiation**:<br>`PizzaStore` contained a giant `if/else` or `switch` block instantiating concrete pizzas (`new NYCheesePizza()`, `new ChicagoClamPizza()`), tying order logic directly to concrete implementations. | **Subclasses Decide Instantiation**:<br>Defines an abstract `createPizza(String type)` factory method, letting regional subclasses (`NYPizzaStore`, `ChicagoPizzaStore`) determine concrete product instantiation. | **Poltergeist Factories**:<br>Spawning parallel class hierarchies where trivial one-line classes each demand their own dedicated factory class. |
| **Ch 4: Abstract Factory Pattern** | Creational | **Inconsistent Family Composition**:<br>Stores had no mechanism to enforce that NY pizza received fresh marinara and thin crust, while Chicago received plum tomatoes and thick crust, leading to mismatched ingredient assemblies. | **Families of Related Objects**:<br>`PizzaIngredientFactory` provides an interface to create a whole family of compatible products (`createDough()`, `createSauce()`) without coupling to concrete classes. | **Factory Factory Over-Engineering**:<br>Nesting factories inside factories for systems with only 1 or 2 static product types; rigid abstract factory interfaces requiring global edits when adding products. |
| **Ch 5: Singleton Pattern** | Creational | **Global Variable Chaos & Race Conditions**:<br>Multiple chocolate boilers (`ChocolateBoiler`) instantiated simultaneously in a multithreaded runtime, spilling hundreds of gallons of unboiled milk due to unsynchronized static state. | **Controlled Unique Instance Access**:<br>Private constructor, private static instance, and public static `getInstance()`. Thread safety achieved via Double-Checked Locking or Bill Pugh static holder. | **The Global Variable Anti-Pattern**:<br>Using Singletons as disguised global state; God Object absorbing unrelated logic; concurrency bottlenecks due to synchronized methods. |
| **Ch 6: Command Pattern** | Behavioral | **Tight Client-Vendor Coupling**:<br>The Home Automation Remote Control needed to control dozens of vendor appliances with incompatible method names (`on()`, `off()`, `setSpeed()`, `dim()`). Hardcoding vendor calls inside remote button slots created rigid, non-extensible code. | **Encapsulate Invocation as Objects**:<br>Decouple the invoker (Remote) from receiver (Light, Fan) using a uniform `Command` interface with `execute()` and `undo()`, enabling macro commands, logging, and queues. | **Class Explosion & Stale State**:<br>Creating standalone command classes for trivial single-line statements; undo queues holding stale memory references to deleted domain entities. |
| **Ch 7: Adapter Pattern** | Structural | **Interface Incompatibility Breakdown**:<br>The client application expects `Duck` instances (`quack()`, `fly()`), but only has access to a `Turkey` (`gobble()`, `flyShort()`). Changing vendor code was impossible or violated client contracts. | **Interface Translation Wrapper**:<br>`TurkeyAdapter` implements `Duck` and wraps a `Turkey` instance, translating calls transparently without modifying either party. | **Two-Way Adapter Spaghetti**:<br>Complex bidirectional state mutations across disparate APIs; wrapping trivial calls in redundant indirection layers. |
| **Ch 7: Facade Pattern** | Structural | **Subsystem Coupling Nightmare**:<br>To watch a movie, a user had to manually invoke 10 different subsystem devices in sequence (`popper.on()`, `lights.dim()`, `screen.down()`, `projector.wideScreen()`, `amp.setSurroundSound()`). | **Simplified Unified Interface**:<br>`HomeTheaterFacade` exposes a high-level `watchMovie()` method, encapsulating subsystem complexity while preserving direct access to subsystems if needed (Principle of Least Knowledge). | **God Facade / Walled Garden**:<br>Facade expanding into a monolithic god class; facade completely blocking access to underlying subsystem low-level primitives. |
| **Ch 8: Template Method Pattern** | Behavioral | **Duplicated Algorithm Scaffolding**:<br>`Coffee` and `Tea` classes shared an identical 4-step preparation algorithm (`boilWater()`, `brew()`, `pourInCup()`, `addCondiments()`), but implemented the workflow independently, duplicating control flow and invariants. | **Algorithm Skeleton in Superclass**:<br>Define the invariant algorithm steps in a `final` base method (`prepareRecipe()`), deferring specific variant steps (`brew()`, `addCondiments()`) to abstract methods in subclasses (The Hollywood Principle). | **Fragile Base Class & Inheritance Rigidity**:<br>Subclasses unintentionally breaking the algorithm lifecycle; forced inheritance preventing runtime algorithm swapping (unlike Strategy). |
| **Ch 9: Iterator Pattern** | Behavioral | **Leaky Collection Implementations**:<br>`Lou's Diner` stored menu items in an `ArrayList`, while `Mel's Pancake House` stored them in an `Array`. Merging menus forced clients to write two incompatible looping constructs (`length` vs `size()`), leaking internal representations. | **Uniform Sequential Traversal**:<br>Encapsulate iteration inside a common `Iterator` interface (`hasNext()`, `next()`), enabling polymorphic iteration across any data structure without exposing internal structures. | **Concurrent Modification & Eager Buffering**:<br>Mutating underlying data while iterating; eagerly reading millions of rows into memory before returning an iterator instead of streaming. |
| **Ch 9: Composite Pattern** | Structural | **Duplicate Code for Groups vs Items**:<br>Adding submenus (dessert menu within dinner menu) broke flat iteration. Code had to distinguish between single `MenuItem` and nested menu collections, complicating traversal and printing logic. | **Uniform Part-Whole Tree Hierarchies**:<br>`MenuComponent` provides a unified interface for both leaf items (`MenuItem`) and composite nodes (`Menu`), letting clients treat individual objects and compositions uniformly. | **Type Safety Loss**:<br>Exposing `add()` and `remove()` on leaf nodes that throw runtime `UnsupportedOperationException`; naive recursive traversals causing stack overflow. |
| **Ch 10: State Pattern** | Behavioral | **Conditional Spaghetti Explosion**:<br>The Gumball Machine used integer state constants (`SOLD_OUT`, `NO_QUARTER`, `HAS_QUARTER`, `SOLD`) with 50-line `if/else` ladders across every action method (`insertQuarter()`, `turnCrank()`). Adding a new `WINNER` state required editing every single method, introducing bugs. | **Encapsulate State as Objects**:<br>Extract state-specific behaviors into distinct `State` classes (`NoQuarterState`, `HasQuarterState`). The Gumball Machine delegates actions to its current state object, which manages transitions cleanly. | **Combinatorial State Explosion**:<br>Creating classes for micro-variations of state instead of hierarchical/composite state machines; state objects leaking tight coupling to downstream states. |
| **Ch 11: Proxy Pattern** | Structural | **Unconstrained Direct Access & Latency**:<br>Clients accessing remote gumball machines (`GumballMachineRemote`), expensive CD cover images (`ImageProxy`), or unauthorized user profiles (`ProtectionProxy`) directly, causing crashes, UI freezes, or security violations. | **Surrogate Object Access Controller**:<br>A `Proxy` object implements the same interface as the real subject, intercepting calls to manage remote RPC, defer expensive lazy loading, or enforce security permissions. | **Ghost Operations & N+1 Latency**:<br>Virtual proxies triggering heavy hidden network queries transparently inside simple getter calls; broken identity on internal self-invocations. |
| **Ch 12: Compound Patterns (MVC)** | Compound | **Monolithic View-Data Coupling**:<br>Mixing business rules, data models, and GUI rendering logic into single monolithic UI classes, making automated testing impossible and preventing multiple views of the same model. | **Patterns of Patterns (Observer + Strategy + Composite)**:<br>**Model** (Observer subject holding state), **View** (Composite GUI elements observing Model), and **Controller** (Strategy intercepting user input and updating Model). | **Fat Controller / Anemic Model**:<br>Controller absorbing all business domain logic while the Model degrades into a passive data holder; tightly coupled View-Controller cycles. |

---

## 3. Leftover Patterns (Chapter 14 Appendix) & Their Anti-Patterns

Chapter 14 catalogs the remaining Gang of Four design patterns not covered in full standalone chapters:

| Leftover Pattern | Type | Intent & Use Case | Common Anti-Patterns & Misuse Traps |
| :--- | :--- | :--- | :--- |
| **Bridge** | Structural | Decouples an abstraction from its implementation so the two can vary independently across two orthogonal dimensions (e.g. GUI widgets and OS windowing systems). | **Over-Abstraction**: Splitting hierarchies that have no realistic future variation, adding redundant indirection and mental load. |
| **Builder** | Creational | Encapsulates the step-by-step construction of complex objects, allowing different representations using the same construction process. | **Telescoping Builder**: Chaining 30 setters for simple records/DTOs; leaking mutable object references during build phase without defensive copying. |
| **Chain of Responsibility** | Behavioral | Decouples the sender of a request from its receivers by giving more than one object a chance to handle the request along a sequential chain. | **Black Hole Request**: Request passes through all handlers unhandled and drops silently with no fallback; infinite handler loops from cyclic links. |
| **Flyweight** | Structural | Shares fine-grained object instances to support massive quantities of objects efficiently without exhausting JVM memory. | **Leaky Extrinsic State**: Failing to isolate intrinsic (shared) state from extrinsic (context-specific) state; heavy synchronization bottlenecks on shared factory. |
| **Interpreter** | Behavioral | Given a language, defines its grammar along with an interpreter to evaluate sentences. | **Grammar Bloat**: Using tree-based interpretation for complex grammars instead of parser generators or AST compilers, destroying performance. |
| **Mediator** | Behavioral | Encapsulates how a set of objects interact to prevent them from referring to each other explicitly, centralizing communication. | **God Mediator**: Central mediator turns into a monolithic brain that knows too much about every participant, becoming impossible to maintain. |
| **Memento** | Behavioral | Captures and externalizes an object's internal state without violating encapsulation, allowing restoration later (undo/snapshot). | **Memory Hog**: Storing full object graph snapshots repeatedly instead of delta changes; leaking internal mutable state via public memento getters. |
| **Prototype** | Creational | Creates new objects by cloning a prototypical instance rather than going through standard instantiation. | **Shallow Copy Bug**: Cloning objects with mutable references causing shared state corruption; circular references crashing deep clone logic. |
| **Visitor** | Behavioral | Defines a new operation to be performed on elements of an object structure without changing the element classes. | **Double Dispatch Rigidity**: Adding a new element type forces modification of every single visitor class across the codebase. |

---

## 4. The Meta-Anti-Pattern: Golden Hammer (Chapter 13, p. 593)

Chapter 13 explicitly profiles the most dangerous anti-pattern of all when studying design patterns:

### **Anti-Pattern: Golden Hammer**
- **Problem**: You need to choose design strategies for software architecture and you believe that **exactly one pattern or technology must dominate the architecture**.
- **Context**: The team has recently learned a new design pattern or technology and feels eager to use it everywhere.
- **Forces**:
  - Developers want to showcase their knowledge of newly learned patterns.
  - Familiarity makes the pattern feel safe and exciting.
  - Pattern-Driven Development (PDD) replaces problem-driven engineering.
- **Supposed Solution**: Apply the pattern obsessively to every problem, even where simple plain code or 2-line functions would suffice.
- **Why It Fails**: Leads to massive over-engineering, unneeded indirection, bloated class hierarchies, and reduced system performance.
- **Refactored Solution**:
  1. **Simplicity First (KISS & YAGNI)**: Always start with the simplest design that could possibly work.
  2. **Rule of Three**: Only introduce a design pattern when a problem has surfaced at least three distinct times.
  3. **Refactor Toward Patterns**: Do not design patterns into a system upfront before the need is proven; refactor toward patterns as requirements evolve.
