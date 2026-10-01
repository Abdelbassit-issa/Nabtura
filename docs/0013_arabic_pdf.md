# Arabic PDF / Excel Generation — Milestone 4C
Purpose: justify Arabic report stack per PRD (§1.2 auto-export .xlsx/.pdf, Arabic text support).
Dependencies (each needs justification):
- `openpyxl` — already justified (docs/0007) for .xlsx
- `arabic_reshaper` + `python-bidi` — Arabic text reshaping/bidi
- `fpdf2` OR `WeasyPrint` — PDF generation (pick `WeasyPrint` for HTML→PDF with CSS, more flexible; if minimal only, `fpdf2` is lighter)
Choice: `fpdf2` (minimal, pure-python, sufficient for basic reports) + `arabic_reshaper`/`python-bidi`. Justify each in docs before adding to requirements.
