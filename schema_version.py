import json

# Read sensor data
with open("sensor_data.json", "r") as file:
    sensor_records = json.load(file)

# Define schema versions
schema_v1 = {
    "device_id",
    "temperature",
    "humidity"
}

schema_v2 = schema_v1 | {
    "pressure"
}

schema_v3 = schema_v2 | {
    "battery"
}

print("SCHEMA VERSION MANAGEMENT")
print("-------------------------")

for sensor in sensor_records:

    fields = set(sensor.keys())

    if fields.issubset(schema_v1):
        version = "Version 1"

    elif fields.issubset(schema_v2):
        version = "Version 2"

    elif fields.issubset(schema_v3):
        version = "Version 3"

    else:
        version = "Unknown Schema"

    print(
        "Device:", sensor["device_id"],
        "|", version
    )

print("\nSchema versioning completed!")