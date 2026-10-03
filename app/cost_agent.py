# Cost Agent — Normal/Cost Agent (Milestone 2)
# No new dependencies (stub, minimal)
# Ref: PRD §2.2 (KISS)
import math
from .state import TeamState

def _safe_float(val, default=0.0):
    try:
        f = float(val) if val is not None else default
        if math.isnan(f) or math.isinf(f) or f < 0:
            return default
        return f
    except (ValueError, TypeError):
        return default

def cost_agent(state: TeamState) -> TeamState:
    budget = _safe_float(state.get("budget", 0))
    return {**state, "agent_output": {**state.get("agent_output", {}), "cost_estimate": budget * 0.05}}
