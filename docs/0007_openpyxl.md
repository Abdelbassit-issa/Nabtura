# Dependency Justification — openpyxl

Purpose: justify openpyxl for financial modeling agent output (.xlsx reports).
Reason: PRD requires auto-generated Excel reports (§1.2, §3). openpyxl is minimal, battle-tested, already listed in PRD §2.4 minimal dependency list, and sufficient for basic spreadsheet generation. No abstraction layer needed (KISS, PRD §2.2).
Doc ref: docs/0004_team_state_schema.md (agent_output extends with xlsx paths).
