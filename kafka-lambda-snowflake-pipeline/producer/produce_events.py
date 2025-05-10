from faker import Faker
import json
import time
from kafka import KafkaProducer

fake = Faker()
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    event = {
        "user_id": fake.uuid4(),
        "event_type": "click",
        "timestamp": fake.iso8601()
    }
    producer.send("events", event)
    print("Sent:", event)
    time.sleep(2)
