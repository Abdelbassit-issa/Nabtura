# Security / Fuzz Testing — Milestone 4A
Purpose: justify fuzz/penetration testing per PRD §2.9.
Tools: `pytest` + basic input validation (no new framework needed; minimal).
Approach: fuzz budget/location inputs; verify isolation (agent failure doesn't crash graph); document results in docs/.
No new dependency beyond pytest (already minimal test stack — justification: required by PRD §2.9 security constraint).
