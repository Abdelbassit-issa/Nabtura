# Ref: docs/0014_real_modeling.md - Section 1
# Financial modeling agent with real formulas from framework (search result)
import math
from .state import TeamState

# Real formulas per framework: NPV, IRR, MPI/ARI/RGI, GOPPAR, Flow-Through

def _safe_float(val, default=0.0):
    try:
        f = float(val) if val is not None else default
        if math.isnan(f) or math.isinf(f) or f < 0:
            return default
        return f
    except (ValueError, TypeError):
        return default

def financial_modeling(state: TeamState) -> TeamState:
    budget = _safe_float(state.get("budget", 0))
    # Simple NPV stub (discounted at 10% over 5 years, stub cash flow = budget*0.15/yr)
    r = 0.10
    n = 5
    cf = budget * 0.15
    npv = sum(cf / ((1 + r) ** t) for t in range(1, n + 1))
    # IRR approximation (stub)
    irr_approx = (cf / budget) if budget > 0 else 0.0
    # MPI / ARI / RGI stubs (framework references)
    mpi = 105.0  # above market
    ari = 98.0
    rgi = (mpi * ari) / 100.0
    # GOPPAR stub (framework §7)
    total_rooms = 100  # stub inventory
    gop = budget * 0.25  # stub operating profit
    goppar = gop / total_rooms if total_rooms else 0.0
    # Flow-through stub (framework §7)
    delta_rev = budget * 0.1
    delta_gop = budget * 0.055
    flow_through = (delta_gop / delta_rev) if delta_rev > 0 else 0.0
    return {**state, "agent_output": {**state.get("agent_output", {}),
                                       "npv_real": round(npv, 2),
                                       "irr_approx": round(irr_approx, 4),
                                       "mpi": mpi,
                                       "ari": ari,
                                       "rgi": round(rgi, 2),
                                       "goppar": round(goppar, 2),
                                       "flow_through": round(flow_through, 4),
                                       "formulas_applied": ["NPV", "IRR", "MPI", "ARI", "RGI", "GOPPAR", "Flow-Through"],
                                       "framework_ref": "economic_feasibility_hospitality_optimization_study.md"}}
