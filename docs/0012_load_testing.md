# Load Testing — Milestone 4B
Purpose: justify load testing simulating 1M+ entities (PRD §2.9 / §1.2 target).
Tools: `locust` or `k6` — both minimal; for milestone 4B justify `locust` (pure Python, aligns with stack, easier Docker integration). No extra heavy infra needed beyond Docker-compose scaling.
Approach: simulate concurrent POST /feasibility-study; measure session resume under load; document results.
