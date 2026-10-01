# Product Requirements Document (PRD)

## 1. Executive Summary & Vision

### 1.1 Product Purpose
**Nabtura** is an enterprise-grade SaaS platform engineered for dynamic economic feasibility studies, investment simulation, and operational optimization within the hospitality, restaurant, and bakery sectors.

By leveraging a multi-agent orchestration architecture on top of **LangGraph v0.2+**, Nabtura decomposes compound investment queries into deterministic agent workflows: initial strategy verification, local market extraction, dynamic financial modeling (NPV, IRR, Payback), scenario-based risk optimization, and auto-generated report exports (.xlsx, .pdf).

### 1.2 Architectural Core & Scalability Target
* **Target Throughput**: Built to handle **1,000,000+ registered active entities / high-concurrency request bursts**.
* **Orchestration**: LangGraph (v0.2+) with strict state graph isolation (`TeamState`).
* **Persistence & State**: Redis + PostgreSQL (`PostgresSaver`) for durable state persistence, time-travel history inspection, and session recovery.
* **Concurrency Pattern**: Asynchronous I/O via FastAPI + RabbitMQ / Apache Kafka task queues for scalable distributed agent workloads.

---

## 2. Core Architectural Principles & Strict Constraints

All engineers and AI agents working on this codebase must adhere strictly to the following rules:

1. **Sequential Traceable Documentation (`docs/` Protocol):** Every architectural decision or new agent/node implementation creates a new file: `docs/XXXX_description.md`. `docs/index.md` is the master index and MUST be updated in the same commit every time a new doc file is added.

2. **KISS & Anti-Over-Engineering:** Every node in the LangGraph graph stays as simple as possible. No abstraction layers or extra design patterns unless explicitly justified in writing in the corresponding `docs/` entry.

3. **Code-to-Doc Traceability:** Every major agent/node/function carries a header comment linking back to its doc reference, e.g. `# Ref: docs/000X_....md - Section Y.Z`.

4. **Minimal Dependencies Policy:** Only audited, battle-tested core libraries (LangGraph, FastAPI, PostgresSaver/psycopg, redis-py, pika/aiokafka, openpyxl, arabic_reshaper/python-bidi, fpdf2 or WeasyPrint). Any new dependency requires a written justification in `docs/` before being merged.

5. **Strict State Isolation (`TeamState` Isolation):** Every agent subgraph operates on an isolated copy of state. No state leaks between agents except through routing paths explicitly defined by the supervisor.

6. **Deterministic Routing:** Supervisor/Orchestrator routing paths between agents are explicit and predefined. Avoid arbitrary branching or delegating routing decisions to the LLM wherever it can be avoided.

7. **Durable, Resumable Execution:** Every session/query persists its progress to PostgreSQL (`PostgresSaver`) so that any interrupted run can resume without re-executing from scratch.

8. **Containerized Build, Run & Test:** Full development, run, and test environment via Docker (FastAPI + Redis + Postgres + message queue), runnable end-to-end with a single command.

9. **Security & Load Testing:** Fuzz/penetration testing on user inputs (especially budget and location data) before release, plus load testing simulating the target concurrency level (1M+ entities).

10. **Local Failure, Not System Failure:** A single agent's failure (e.g. a market-data fetch failure) must be isolated and must not bring down the rest of the workflow — one failed step does not stop the whole pipeline.

---

## 3. Core Functional Requirements & Agent Topology

The system operates under a **Supervisor/Orchestrator Pattern**, enforcing strict task isolation, deterministic routing, and automated validation.

*(To be detailed: agent roles — market research & localization, financial modeling, risk assessment & optimization, document generation — per the existing architecture notes.)*
