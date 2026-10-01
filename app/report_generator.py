# Ref: docs/0007_openpyxl.md — Section 1
# Report generation agent using openpyxl (justified)
import openpyxl
from openpyxl.styles import Font

def generate_report(state_dict: dict) -> str:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Feasibility Report"
    ws["A1"] = "Nabtura Feasibility Study"
    ws["A2"] = "NPV: " + str(state_dict.get("agent_output", {}).get("npv_real", "N/A"))
    ws["A3"] = "IRR: " + str(state_dict.get("agent_output", {}).get("irr_approx", "N/A"))
    ws["A4"] = "GOPPAR: " + str(state_dict.get("agent_output", {}).get("goppar", "N/A"))
    ws["A5"] = "Segments: Corporate / Leisure / MICE / Long-Stay"
    path = "/tmp/feasibility_report.xlsx"
    wb.save(path)
    return path
