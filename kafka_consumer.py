from kafka import KafkaConsumer
import json
import sqlite3
import logging
from datetime import datetime

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

conn = sqlite3.connect("sensor_database.db")
cursor = conn.cursor()

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="sensor-drift-handler-v3",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Schema Drift Consumer Started...")
print("Waiting for sensor messages...")

try:
    for message in consumer:
        data = message.value

        device_id = data.get("sensor_id", data.get("device_id"))
        temperature = data.get("temperature")
        humidity = data.get("humidity")
        pressure = data.get("pressure")
        battery = data.get("battery")
        schema_version = data.get("schema_version", 1)
        firmware_version = data.get("firmware_version")

        if device_id is None or temperature is None or humidity is None:
            logging.warning("Invalid sensor message: %s", data)
            print("Invalid data skipped:", data)
            continue

        temperature = float(temperature)
        humidity = float(humidity)
        pressure = float(pressure) if pressure is not None else None
        battery = float(battery) if battery is not None else None
        schema_version = int(schema_version)

        temperature_status = (
            "High" if temperature > 30 else "Normal"
        )

        processing_time = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO sensor_data
            (device_id, temperature, humidity, pressure, battery,
             schema_version, firmware_version,
             temperature_status, processing_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            device_id, temperature, humidity, pressure, battery,
            schema_version, firmware_version,
            temperature_status, processing_time
        ))

        conn.commit()

        logging.info("Enriched sensor data saved: %s", data)
        print("Enriched Data Saved!")
        print(data)
        print("Temperature Status:", temperature_status)
        print("Processing Time:", processing_time)

except KeyboardInterrupt:
    print("Consumer stopped.")

except Exception as e:
    logging.error("Pipeline error: %s", e)
    print("Error:", e)

finally:
    consumer.close()
    conn.close()
    