# Queue Choice Justification

## Selection: RabbitMQ (pika/aiokafka not needed at milestone 1)

For milestone 1 we use RabbitMQ via the `pika` client for message queuing between potential future agent workers. Kafka (via `aiokafka`) is over-engineered for a single stub agent workflow; RabbitMQ provides simpler exchange/routing, lower memory footprint, and faster startup inside a single `docker-compose.yml` command. If throughput demands exceed single-node RabbitMQ limits, we will justify a Kafka migration in a new docs/ file.

Ref: PRD §2.4 (minimal dependencies), §2.6 (deterministic routing).
