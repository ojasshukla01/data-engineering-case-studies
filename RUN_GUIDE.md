# ▶️ RUN GUIDE: Kafka → Python → DuckDB → DBT Pipeline

This guide walks you through running the full real-time data pipeline simulation.

---

## 🧰 Prerequisites

- Docker Desktop (with WSL2/Linux containers enabled)
- Python 3.10+
- `pip` and `virtualenv` (optional)
- Git (to clone the repo)

---

## 📦 Project Structure

```
data-engineering-case-studies/
├── kafka-lambda-snowflake-pipeline/
│   ├── docker-compose.yml
│   ├── producer/produce_events.py
│   ├── run_pipeline.py
│   ├── snowflake_loader/load.py
│   └── events.duckdb
├── dbt-analytics-stack/
│   ├── models/
│   ├── data/events.csv
│   ├── dbt_project.yml
│   ├── templates/profiles.yml
│   └── ...
├── .venv/
├── RUN_GUIDE.md
└── README.md
```

---

## 🛠️ Step 1: Set Up the Environment

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> Don't have a `requirements.txt`? Run `pip freeze > requirements.txt` once everything works.

---

## 🐳 Step 2: Start Kafka and Zookeeper

In PowerShell or Terminal:

```bash
cd kafka-lambda-snowflake-pipeline
docker-compose up
```

✅ **Expected output:** Kafka and Zookeeper logs. Look for:
```
KafkaServer id=1 started
```

📌 Leave this terminal open while running the rest.

---

## 📡 Step 3: Start Producing Events (Simulated)

In a new terminal window:

```bash
cd kafka-lambda-snowflake-pipeline
.\.venv\Scripts\Activate.ps1
python producer/produce_events.py
```

✅ **Expected output:**
```
Sent: {'user_id': ..., 'event_type': 'click', 'timestamp': ...}
```

📌 This runs **forever**. Stop it anytime using `Ctrl + C`.

---

## 🔄 Step 4: Start the Pipeline Listener

In another terminal:

```bash
cd kafka-lambda-snowflake-pipeline
.\.venv\Scripts\Activate.ps1
python run_pipeline.py
```

✅ **Expected output:**
```
Received: ...
Transformed: ...
✅ Inserted into DuckDB: ...
```

📌 This also runs indefinitely — `Ctrl + C` to stop.

---

## 🧪 Step 5: Query the Local Database (Optional)

Check if events are being stored:

```bash
python query_duckdb.py
```

✅ **Expected output:**
```text
                                  id   action         event_time
0  a1b2c3d4-...                   click  2025-05-10T...
```

---

## 📊 Step 6: Run DBT Analytics Models

In a new terminal:

```bash
cd dbt-analytics-stack
.\.venv\Scripts\Activate.ps1

# Run analytics
dbt debug --profiles-dir templates/
dbt seed --profiles-dir templates/
dbt run --profiles-dir templates/
```

✅ **Expected output:**
```
Finished running 2 models
```

---

## 📖 Step 7: Generate and View DBT Documentation

```bash
dbt docs generate --profiles-dir templates/
dbt docs serve --profiles-dir templates/
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

✅ Explore:
- Model lineage
- SQL preview
- Column-level descriptions

---

## 🧼 Step 8: Shut Down Everything

When done:

1. Stop all running Python scripts with `Ctrl + C`
2. Stop Docker:
   ```bash
   docker-compose down
   ```

---

## ✅ Summary

| Step                    | Description                           | Runs Until       |
|-------------------------|----------------------------------------|------------------|
| Docker Compose          | Starts Kafka & Zookeeper               | Manual Ctrl+C    |
| `produce_events.py`     | Sends fake events                      | Manual Ctrl+C    |
| `run_pipeline.py`       | Transforms & loads to DuckDB           | Manual Ctrl+C    |
| `query_duckdb.py`       | Validates data landed                  | One-time query   |
| DBT + Docs              | Models & visualizes event data         | `Ctrl+C` to exit |

---

## 🧠 Pro Tips

- All data is stored locally in `events.duckdb`
- You can reset the DB by deleting that file
- `query_duckdb.py` is your best friend for debugging
- The system simulates **real-time pipelines** in a fully local setup

---

Built by [Ojas Shukla](https://www.linkedin.com/in/ojasshukla01)
