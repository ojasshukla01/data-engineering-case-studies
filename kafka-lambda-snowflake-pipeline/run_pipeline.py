import json
from kafka import KafkaConsumer
from lambda_function.transform import lambda_handler
from snowflake_loader.load import load_to_snowdb

consumer = KafkaConsumer(
    'events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='data-engineer-group'
)

print("Starting pipeline... Listening to Kafka topic 'events'")

for message in consumer:
    raw_event = message.value
    print("Received:", raw_event)

    try:
        transformed_event = lambda_handler(raw_event)
        print("Transformed:", transformed_event)

        load_to_snowdb(transformed_event) 
    except Exception as e:
        print("Error processing message:", e)
