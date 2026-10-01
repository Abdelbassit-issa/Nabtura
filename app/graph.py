# Ref: docs/0005_graph_routing.md - Section 2
# Ref: docs/0004_team_state_schema.md - Section 1
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.postgres import PostgresSaver
from .state import TeamState
from .financial_modeling import financial_modeling
from .risk_agent import risk_assessment
from .cost_agent import cost_agent
from .power_agent import power_agent
from .deep_search import deep_search

def build_graph(saver: PostgresSaver):
    workflow = StateGraph(TeamState)
    workflow.add_node("supervisor", lambda s: {**s, "status": "routed"})
    workflow.add_node("financial_modeling", financial_modeling)
    workflow.add_node("risk_assessment", risk_assessment)
    workflow.add_node("cost_agent", cost_agent)
    workflow.add_node("power_agent", power_agent)
    workflow.add_node("deep_search", deep_search)
    workflow.set_entry_point("supervisor")
    # Deterministic routing (explicit, no LLM)
    workflow.add_edge("supervisor", "financial_modeling")
    workflow.add_edge("financial_modeling", "risk_assessment")
    workflow.add_edge("risk_assessment", "cost_agent")
    workflow.add_edge("cost_agent", "power_agent")
    workflow.add_edge("power_agent", "deep_search")
    workflow.add_edge("deep_search", END)
    return workflow.compile(checkpointer=saver)
