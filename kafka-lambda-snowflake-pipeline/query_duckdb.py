import duckdb
df = duckdb.connect('events.duckdb').execute("SELECT * FROM events LIMIT 5").fetchdf()
print(df)
