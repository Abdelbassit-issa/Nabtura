# TeamState Schema (Milestone 1)

Purpose: define the shared state schema for supervisor and agents.

Fields:
- `idea`: str (business concept)
- `location`: str (geographic market)
- `budget`: float (investment cap)
- `status`: str (running/completed/failed)
- `agent_output`: dict (stub agent results)
- `session_id`: str (PostgresSaver session key)

Isolation: no agent leaks state except through supervisor routing.
Ref: PRD §2.5, docs/0003_project_scaffold.md.
