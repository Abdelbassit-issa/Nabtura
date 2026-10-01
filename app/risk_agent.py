# Risk Assessment Agent — Milestone 2
# Ref: docs/0008_risk_agent.md - Section 1
from .state import TeamState

def risk_assessment(state: TeamState) -> TeamState:
    return {**state, "agent_output": {**state.get("agent_output", {}), "risk_score": 0.2}}
