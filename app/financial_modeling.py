# Ref: docs/0007_openpyxl.md - Section 1
# Financial modeling agent (milestone 2) — KISS stub
from .state import TeamState

def financial_modeling(state: TeamState) -> TeamState:
    # Minimal: compute stub metrics (NPV placeholder)
    budget = state.get("budget", 0)
    return {**state, "agent_output": {**state.get("agent_output", {}),
                                       "npv_stub": budget * 0.1,
                                       "xlsx_path": "report.xlsx"}}
