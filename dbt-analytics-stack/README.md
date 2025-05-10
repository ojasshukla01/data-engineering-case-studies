# DBT Analytics Stack

This project demonstrates a lightweight analytics layer on Snowflake using dbt.

## Features

- Source → Staging → Marts pattern
- Uses `dbt seed` to load initial data
- Models are materialized as views (staging) and tables (marts)

## Commands

```bash
pip install dbt-snowflake python-dotenv
dbt seed
dbt run
dbt docs generate && dbt docs serve
```

## Setup

- Create a `.env` file based on `.env.example`
- Ensure your Snowflake role has permission to create schemas/tables

Enjoy!
