# Milestone 1 — Graph Architecture Decision

Decision: supervisor node uses explicit predefined routing (no LLM routing).
Reasoning: PRD §2.6 requires deterministic routing. Using `add_conditional_edges` with fixed function (`route_to_agent`) keeps routing deterministic, avoids LLM overhead, and satisfies KISS.
Doc ref: docs/0004_team_state_schema.md (TeamState isolation), PRD §2.5.
