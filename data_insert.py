import json
import sqlite3

# Read sensor data
with open("sensor_data.json", "r") as file:
    sensor_records = json.load(file)

# Connect to database
conn = sqlite3.connect("sensor_database.db")
cursor = conn.cursor()

print("INSERTING SENSOR DATA")
print("----------------------")

# Insert each sensor record
for sensor in sensor_records:

    if "device_id" not in sensor:
        print("Invalid record skipped")
        continue

    temperature = float(sensor["temperature"])
    humidity = float(sensor["humidity"])
    pressure = float(sensor.get("pressure", 0))
    battery = float(sensor.get("battery", 100))

    cursor.execute("""
        INSERT INTO sensor_data
        (device_id, temperature, humidity, pressure, battery)
        VALUES (?, ?, ?, ?, ?)
    """, (
        str(sensor["device_id"]),
        temperature,
        humidity,
        pressure,
        battery
    ))

    print("Data inserted for:", sensor["device_id"])

# Save data
conn.commit()

print("\nTotal records inserted:", len(sensor_records))
print("Database updated successfully!")

conn.close()
