# Deep Search Agent — Search Deeply (Milestone 2)
# No new dependencies beyond existing minimal set (stub search)
# Ref: PRD §2.4 (minimal), docs/0002_queue_justification.md (RabbitMQ for distributed work if scaled)
from .state import TeamState

def deep_search(state: TeamState) -> TeamState:
    return {**state, "agent_output": {**state.get("agent_output", {}), "deep_insight": "stub deep result"}}
