# Ref: docs/0003_project_scaffold.md - Section 1
# Ref: docs/0005_graph_routing.md - Section 1
# Ref: docs/0006_docker_setup.md - Section 1
from fastapi import FastAPI
from .graph import build_graph
from langgraph.checkpoint.postgres import PostgresSaver
import psycopg

app = FastAPI()
# Minimal endpoint; uses explicit supervisor routing (deterministic)

# PostgresSaver initialized at startup (hard-to-change, documented)
# This is the state persistence approach — if changed, must ask user.
DB_URL = "postgresql://user:pass@postgres:5432/nabtura"
saver = PostgresSaver.from_conn_string(DB_URL)

@app.post("/feasibility-study")
async def feasibility_study(payload: dict):
    # Stub agent output only (milestone 1); no real modeling
    graph = build_graph(saver)
    result = await graph.ainvoke({"idea": payload.get("idea"),
                                  "location": payload.get("location"),
                                  "budget": payload.get("budget"),
                                  "status": "running",
                                  "agent_output": {},
                                  "session_id": "stub_session_1"})
    return {"status": result.get("status"), "agent_output": result.get("agent_output")}
