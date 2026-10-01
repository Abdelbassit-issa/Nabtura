# Ref: docs/0004_team_state_schema.md - Section 2.1
from typing import TypedDict, Any

class TeamState(TypedDict):
    idea: str
    location: str
    budget: float
    status: str
    agent_output: dict[str, Any]
    session_id: str
