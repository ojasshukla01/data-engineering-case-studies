import duckdb

# Connect to or create a local DuckDB file
conn = duckdb.connect(database='events.duckdb')

# Ensure table exists
conn.execute("""
CREATE TABLE IF NOT EXISTS events (
    id VARCHAR,
    action VARCHAR,
    event_time TIMESTAMP
)
""")

def load_to_snowdb(record):
    try:
        conn.execute(
            "INSERT INTO events (id, action, event_time) VALUES (?, ?, ?)",
            (record['id'], record['action'], record['event_time'])
        )
        print("✅ Inserted into DuckDB:", record)
    except Exception as e:
        print("❌ Failed to insert into DuckDB:", e)
