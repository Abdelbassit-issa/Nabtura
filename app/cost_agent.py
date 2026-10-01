# Cost Agent — Normal/Cost Agent (Milestone 2)
# No new dependencies (stub, minimal)
# Ref: PRD §2.2 (KISS)
from .state import TeamState

def cost_agent(state: TeamState) -> TeamState:
    return {**state, "agent_output": {**state.get("agent_output", {}), "cost_estimate": state.get("budget", 0) * 0.05}}
