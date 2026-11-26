import json
import sqlite3
import time
from queue import Queue

# Create message queue
sensor_queue = Queue()

print("REAL-TIME STREAMING PIPELINE")
print("----------------------------")

# Producer: Read sensor messages
with open("sensor_data.json", "r") as file:
    sensor_records = json.load(file)

for sensor in sensor_records:
    sensor_queue.put(sensor)

print("All sensor messages received!")

# Consumer: Process messages
conn = sqlite3.connect("sensor_database.db")
cursor = conn.cursor()

while not sensor_queue.empty():

    sensor = sensor_queue.get()

    device_id = str(sensor["device_id"])
    temperature = float(sensor["temperature"])
    humidity = float(sensor["humidity"])
    pressure = float(sensor.get("pressure", 0))
    battery = float(sensor.get("battery", 100))

    cursor.execute("""
        INSERT INTO sensor_data
        (device_id, temperature, humidity, pressure, battery)
        VALUES (?, ?, ?, ?, ?)
    """, (
        device_id,
        temperature,
        humidity,
        pressure,
        battery
    ))

    print("Processed:", device_id)

    conn.commit()
    time.sleep(1)

conn.close()

print("\nReal-time streaming completed!")