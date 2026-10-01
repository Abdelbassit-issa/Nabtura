# Milestone 1 — Docker Setup

Decision: `docker-compose.yml` uses FastAPI + Postgres + Redis + RabbitMQ in a single command.
No additional services (Kafka) — too heavy for stub agent (docs/0002_queue_justification.md).
PostgresSaver uses `postgresql://` URL; `redis://` URL for session cache not strictly needed for milestone 1 but included for future resumability.
