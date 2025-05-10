# 🛠️ Data Engineering Case Studies

Welcome to my portfolio repository! This project simulates real-world data engineering workflows using open-source and cloud-native tools — from streaming ingestion to analytics-ready models.

It features:
- **Kafka** for real-time data ingestion
- **AWS Lambda-style Python functions** for transformations
- **Snowflake** (or DuckDB locally) for cloud data warehousing
- **DBT** for analytics modeling, testing, and documentation

---

## 🚀 Projects Overview

### 📡 1. Kafka → AWS Lambda (Python) → Snowflake Pipeline

This pipeline showcases end-to-end streaming ingestion:
- **Producer** simulates events using [Faker](https://faker.readthedocs.io/)
- **Kafka** (via Docker Compose) handles the streaming layer
- **Lambda-style Python function** transforms events
- **Snowflake/DBT/DuckDB** stores and queries transformed data
- CLI runner script orchestrates the full pipeline

📂 Folder: [`kafka-lambda-snowflake-pipeline/`](./kafka-lambda-snowflake-pipeline)

---

### 📊 2. DBT + DuckDB Analytics Stack

This DBT project models raw event data into analytics-friendly marts:
- `stg_events`: staging model
- `fct_actions`: fact model
- Powered by **DBT** with **DuckDB**, no cloud account required

📂 Folder: [`dbt-analytics-stack/`](./dbt-analytics-stack)

---

### 🖼️ Visual Preview – DBT Docs

Below is a screenshot of the lineage and documentation generated using `dbt docs`:

![DBT Docs Screenshot](![image](https://github.com/user-attachments/assets/54aa7cec-6c3c-43a2-ae41-62488f808291))

---

## 🧱 Tech Stack

| Layer         | Tools Used                                      |
|---------------|--------------------------------------------------|
| Ingestion     | Kafka (Docker)                                  |
| Transformation| Python (Lambda-style)                           |
| Orchestration | CLI-based pipeline runner                       |
| Storage       | Snowflake (simulated via DuckDB)                |
| Modeling      | DBT, Jinja2, YAML                               |
| Testing       | dbt seed/run/test/docs                          |

---

## 🧪 How to Run Locally

> Requires: Docker, Python 3.9+, pip, dbt-duckdb

### Kafka + Event Producer

```bash
cd kafka-lambda-snowflake-pipeline
docker-compose up        # Start Kafka and Zookeeper
python producer/produce_events.py
