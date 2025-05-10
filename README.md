# 🛠️ Data Engineering Case Studies

Welcome to my portfolio repository! This project showcases real-world data engineering workflows, simulating how modern teams integrate, transform, and analyze data using a cloud-native architecture.

These case studies demonstrate hands-on implementations with:
- **Kafka** for event streaming
- **AWS Lambda**-style Python functions for transformation
- **Snowflake** as the cloud data warehouse
- **DBT** for analytics modeling and documentation

---

## 🚀 Projects Overview

### 📡 1. Kafka → AWS Lambda (Python) → Snowflake Pipeline

This project demonstrates an end-to-end ingestion and transformation pipeline using streaming data:

- **Producer** simulates real-time events using [Faker](https://faker.readthedocs.io/)
- **Kafka** (via Docker) handles the streaming layer
- **Lambda-style Python function** applies transformations
- **Snowflake loader** inserts records into the warehouse
- **Docker Compose** provided for local simulation

📂 Folder: [`kafka-lambda-snowflake-pipeline/`](./kafka-lambda-snowflake-pipeline)

---

### 📊 2. DBT + Snowflake Analytics Stack

This project shows how raw data in Snowflake is transformed into analytics-ready models using [DBT](https://www.getdbt.com/):

- **Staging models** clean and standardize raw data
- **Mart models** provide aggregated business logic
- **Seed data** used to bootstrap the transformation
- Includes **profiles.yml** and `dbt_project.yml` for reproducibility

📂 Folder: [`dbt-analytics-stack/`](./dbt-analytics-stack)

---

## 🧱 Tech Stack

| Layer         | Tools Used                                      |
|---------------|--------------------------------------------------|
| Ingestion     | Kafka (self-hosted via Docker)                  |
| Processing    | Python, AWS Lambda (simulated)                  |
| Storage       | Snowflake (via Python connector + DBT)          |
| Modeling      | DBT, Jinja2, YAML                               |
| Orchestration | CLI runner for Kafka → Lambda → Snowflake flow |
| Simulation    | Faker, Docker, dotenv                           |

---

## 🧪 How to Run Locally

> Requires: Docker, Python 3.9+, pip, Git

### 📡 Kafka + Producer
```bash
cd kafka-lambda-snowflake-pipeline
docker-compose up  # starts Kafka & Zookeeper

python producer/produce_events.py  # sends fake clickstream data
