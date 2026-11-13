# Upcoming Updates & Roadmap (`Upcoming Updates.md`)

A centralized tracking board for upcoming LLD and HLD topics, UML modeling manuals, design pattern deep-dives, specification skills, ingestion pipelines, and system milestones for **System-Design**.

---

## 📌 Milestones & Task Status

### 1. Core Architecture & Infrastructure
- [x] Initial Repository Architecture initialization
- [x] Skill Typology manual (`.agent/skills/type of skills.md`)
- [x] Universal Skill Generator (`.agent/skills/SkillGenerator/`)
- [x] Single-Pass Rendering Auditor (`scripts/audit_rendering.py`)
- [x] Governance & Mandatory 3-Tier Mapping Directives (`chat/finalized chat.md`)
- [x] Core Modeling Engineering Templates (`Skills_Input/Templates/`):
  - [x] Class & Object Diagram Template
  - [x] Sequence & Interaction Diagram Template
  - [x] State Machine & Activity Diagram Template
  - [x] Use Case & Component Diagram Template

### 2. Theoretical & Specification Skills (`SkillsOnFixedResources`)
- [x] Setup `UML25Spec` OMG UML 2.5 Specification Skill
  - [x] Machine-readable TOC (`toc.json` & `table_of_contents.md`)
  - [x] Precision query CLI (`query_uml25spec.py`)
  - [x] Comprehensive 22-clause specification outline (`UML25Spec_Complete_Outline.md`)
  - [x] Published inaugural query manual: `001_uml_2_5_taxonomy_structural_vs_behavioral.md`
- [ ] Setup `Fowler_UML` reference skill (Martin Fowler's *UML Distilled* 3rd Edition)
- [ ] Setup `Booch_OOAD` reference skill (Grady Booch's *Object-Oriented Analysis and Design with Applications*)

### 3. Dynamic Problem Intake & Solutions (`SkillsOnDynamicResources`)
- [x] Setup `UMLSkill` dynamic ingestion and solution skill
  - [x] Multi-source drop zone (`Source of Problem/put the file here/`)
  - [x] Real-time 2-tier Category & Subcategory taxonomy (`problem categories.md`)
  - [x] Automated status & categories CLI (`ingest_manager.py`)
  - [x] Master question bank (`question bank.md`)
  - [x] Multi-representation solution specification (Diagram + Java + Derivation)

### 4. System-Design Topics (LLD & HLD)
- [x] Restructure into `Project_Engine/`, `1.LLD/`, `2.HLD/`
- [x] LLD: Design Patterns Chapters 1-5 (Strategy, Observer, Decorator, Factory, Singleton)
- [ ] LLD: Case studies using `Project_Engine` skills and templates
- [ ] HLD: First topics (e.g. URL Shortener, Rate Limiter) following the 3-tier mapping rule
- [ ] Wire `Project_Engine/scripts/audit_rendering.py` into every topic workflow

### 5. Advanced Architecture Syntheses & Design Patterns
- [ ] Microservice Event-Driven Saga Pattern Manual (Choreography vs Orchestration)
- [ ] GoF Structural Patterns Class & Sequence Breakdown
- [ ] Distributed Concurrency & Lock Modeling (State Machine & Sequence Diagrams)

