import json

# Read sensor data
with open("sensor_data.json", "r") as file:
    sensor_records = json.load(file)

print("DATA VALIDATION AND TRANSFORMATION")
print("----------------------------------")

processed_records = []

for sensor in sensor_records:

    # Check required fields
    if "device_id" not in sensor:
        print("Invalid record: Device ID missing")
        continue

    # Create clean record
    clean_data = {
        "device_id": str(sensor["device_id"]),
        "temperature": float(sensor["temperature"]),
        "humidity": float(sensor["humidity"]),
        "pressure": float(sensor.get("pressure", 0)),
        "battery": float(sensor.get("battery", 100))
    }

    processed_records.append(clean_data)

# Display transformed data
for record in processed_records:
    print(record)

print("\nTotal processed records:", len(processed_records))