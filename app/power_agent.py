# Power Agent — Normal/Power Agent (Milestone 2)
# No new dependencies (stub, minimal)
# Ref: PRD §2.2
from .state import TeamState

def power_agent(state: TeamState) -> TeamState:
    return {**state, "agent_output": {**state.get("agent_output", {}), "power_consumption": 100}}
