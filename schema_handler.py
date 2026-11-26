import json

# Read sensor data
with open("sensor_data.json", "r") as file:
    sensor_records = json.load(file)

# Define original schema
known_fields = {
    "device_id",
    "temperature",
    "humidity"
}

print("SCHEMA DRIFT DETECTION")
print("----------------------")

# Check each sensor
for sensor in sensor_records:

    new_fields = set(sensor.keys()) - known_fields

    if new_fields:
        print("Device:", sensor["device_id"])
        print("New fields detected:", new_fields)

        known_fields.update(new_fields)

print("\nUpdated Schema:")
print(known_fields)