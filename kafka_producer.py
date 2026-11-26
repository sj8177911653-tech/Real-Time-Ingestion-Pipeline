from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

sensor_data = {
    "sensor_id": "S003",
    "temperature": 27.0,
    "humidity": 60,
    "schema_version": 1,
    "timestamp": time.time()
}

producer.send("sensor-data", value=sensor_data)
producer.flush()

print("Schema Version 1 Data Sent Successfully!")
print(sensor_data)

producer.close()