# Ref: docs/0007_openpyxl.md — Section 1
# Ref: docs/0013_arabic_pdf.md — Section 1
# Report generation: Excel (openpyxl) + optional PDF
# If fpdf2 / arabic_reshaper / python-bidi are not installed, graceful fallback to Excel-only or basic output

import openpyxl
from openpyxl.styles import Font

try:
    from fpdf import FPDF
    _HAS_FPDF = True
except ImportError:
    _HAS_FPDF = False

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    _HAS_ARABIC = True
except ImportError:
    _HAS_ARABIC = False


def _arabic(text: str) -> str:
    """Reshape Arabic text for PDF rendering if libraries are available."""
    if _HAS_ARABIC:
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    return text


def generate_excel_report(state_dict: dict) -> str:
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


def generate_pdf_report(state_dict: dict, lang: str = "en") -> str:
    if not _HAS_FPDF:
        return ""

    class SimplePDF(FPDF):
        def header(self):
            self.set_font("Helvetica", "B", 16)
            self.cell(0, 10, "Nabtura Feasibility Study", ln=True, align="C")
            self.ln(5)

        def footer(self):
            self.set_y(-15)
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    pdf = SimplePDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    # Title
    pdf.set_font("Helvetica", "B", 14)
    title = "تقرير جدوى اقتصادية" if lang == "ar" else "Feasibility Study Report"
    pdf.cell(0, 10, _arabic(title) if lang == "ar" else title, ln=True, align="C")
    pdf.ln(5)

    # Data
    data = state_dict.get("agent_output", {})
    rows = [
        ("NPV", str(data.get("npv_real", "N/A"))),
        ("IRR", str(data.get("irr_approx", "N/A"))),
        ("GOPPAR", str(data.get("goppar", "N/A"))),
        ("Segments", "Corporate / Leisure / MICE / Long-Stay"),
    ]

    for label, value in rows:
        pdf.set_font("Helvetica", "B", 11)
        l = _arabic(label) if lang == "ar" else label
        pdf.cell(60, 8, l)
        pdf.set_font("Helvetica", size=11)
        v = _arabic(value) if lang == "ar" else value
        pdf.cell(0, 8, v, ln=True)

    path = f"/tmp/feasibility_report_{lang}.pdf"
    pdf.output(path)
    return path


def generate_report(state_dict: dict) -> dict:
    """
    Generate report files based on available libraries.
    Always produces Excel; optionally produces English and Arabic PDFs.
    """
    reports = {
        "excel": generate_excel_report(state_dict)
    }

    if _HAS_FPDF:
        reports["pdf"] = generate_pdf_report(state_dict, lang="en")
        if _HAS_ARABIC:
            reports["pdf_ar"] = generate_pdf_report(state_dict, lang="ar")

    return reports
