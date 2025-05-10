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

![DBT Docs Screenshot](assets/dbt_docs_screenshot.png)

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
```

### Lambda Function + DB Loader

```bash
python run_pipeline.py   # Listens to Kafka → Transforms → Loads into DuckDB
```

### DBT Transformation (staging + marts)

```bash
cd dbt-analytics-stack
dbt seed --profiles-dir templates/
dbt run --profiles-dir templates/
```

### DBT Docs UI

```bash
dbt docs generate --profiles-dir templates/
dbt docs serve --profiles-dir templates/
```

---

## 📘 Full Walkthrough

📖 See [`RUN_GUIDE.md`](./RUN_GUIDE.md) for the complete step-by-step instructions to run this project from end to end.

---

## 👤 About Me

Hi, I'm **Ojas Shukla** — a Data Engineer passionate about building efficient, scalable data pipelines that solve real-world problems.

With 4+ years of experience in cloud-native data platforms, analytics engineering, and ETL systems, I specialize in:
- Real-time + batch processing
- GCP & AWS-based data stacks
- dbt, DuckDB, Python, SQL, Kafka

📫 [Connect with me on LinkedIn](https://www.linkedin.com/in/ojasshukla01)

🧰 [Explore other projects →](https://github.com/ojasshukla01)

---

Built with ❤️ to showcase the real-world data flow from stream ingestion to insight.
