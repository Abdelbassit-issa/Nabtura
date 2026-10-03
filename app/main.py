# Ref: docs/0003_project_scaffold.md - Section 1
# Ref: docs/0005_graph_routing.md - Section 1
# Ref: docs/0006_docker_setup.md - Section 1
# Ref: docs/0013_arabic_pdf.md - Section 1
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from .graph import build_graph
from .report_generator import generate_report
from langgraph.checkpoint.postgres import PostgresSaver

app = FastAPI()

# PostgresSaver initialized at startup (hard-to-change, documented)
# This is the state persistence approach — if changed, must ask user.
import os
DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:5432/nabtura")
saver = PostgresSaver.from_conn_string(DB_URL)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)

@app.post("/feasibility-study")
async def feasibility_study(payload: dict, api_key: str = Depends(api_key_header)):
    graph = build_graph(saver)
    result = await graph.ainvoke({
        "idea": payload.get("idea"),
        "location": payload.get("location"),
        "budget": payload.get("budget"),
        "status": "running",
        "agent_output": {},
        "session_id": payload.get("session_id", "stub_session_1")
    })

    reports = generate_report(result)
    return {
        "status": result.get("status"),
        "agent_output": result.get("agent_output"),
        "segments": result.get("agent_output", {}).get("deep_insight", {}),
        "reports": reports
    }
