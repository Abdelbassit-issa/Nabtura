# Nabtura

Enterprise-grade multi-agent SaaS platform for economic feasibility studies, investment simulation, and operational optimization in hospitality, restaurant, and bakery sectors.

## Project Description
Nabtura decomposes compound investment queries into deterministic multi-agent workflows using LangGraph v0.2+: strategy verification, market localization, dynamic financial modeling (NPV/IRR/Payback), scenario-based risk optimization, and auto-generated report exports (.xlsx, .pdf). Built for 1,000,000+ registered active entities with durable PostgreSQL checkpointing (PostgresSaver), deterministic supervisor routing, and strict TeamState isolation.

## Milestones Completed
- Milestone 1: FastAPI skeleton, Docker (Postgres + Redis + RabbitMQ), PostgresSaver-backed LangGraph, smoke endpoint POST /feasibility-study
- Milestone 2: Financial modeling agent + openpyxl justification (docs/0007)
- Milestone 3: Full 5-agent topology (financial_modeling, risk_assessment, cost_agent, power_agent, deep_search), docs 0001-0010, Docker verified end-to-end

## Architecture
- Orchestration: LangGraph with deterministic supervisor→agent routing (no LLM routing)
- State: TeamState (TypedDict) — isolated per agent, only supervisor routes
- Persistence: PostgresSaver + Redis + RabbitMQ
- Container: docker-compose up --build (FastAPI + Postgres 15 + Redis 7 + RabbitMQ)
- Dependencies (minimal, justified): langgraph, fastapi, psycopg2-binary, redis, pika, openpyxl, uvicorn, python-dotenv

## Quick Start
docker-compose up --build -d
POST /feasibility-study {"idea":"...","location":"...","budget":100000}

## Documentation
See docs/ — sequential from 0001_PRD.md (binding) through 0010_deep_search.md, with index.md updated per commit.

Co-Authored-By: Claude Code <noreply@anthropic.com>
🤖 Generated with [Claude Code](https://claude.com/claude-code)
