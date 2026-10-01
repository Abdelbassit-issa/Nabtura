# Deep Search Agent — Search Deeply (Milestone 2)
# No new dependencies beyond existing minimal set (stub search)
# Ref: PRD §2.4 (minimal), docs/0002_queue_justification.md (RabbitMQ for distributed work if scaled)
from .state import TeamState

def deep_search(state: TeamState) -> TeamState:
    # Framework demand segments (economic_feasibility_hospitality_optimization_study.md §2)
    segments = {
        "corporate": {"stay": "1-3 nights", "price_sensitivity": "moderate-low", "ancillary": "moderate"},
        "leisure": {"stay": "2-5 nights", "price_sensitivity": "high", "ancillary": "high"},
        "mice": {"stay": "3-7 nights", "price_sensitivity": "low", "ancillary": "very high"},
        "long_stay": {"stay": "weeks-months", "price_sensitivity": "very high", "ancillary": "low"},
    }
    return {**state, "agent_output": {**state.get("agent_output", {}), "deep_insight": segments}}
