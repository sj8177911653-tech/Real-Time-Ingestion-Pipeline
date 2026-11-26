import json

print("REAL-TIME DATA INGESTION PIPELINE")
print("--------------------------------")

# Read sensor data from JSON file
with open("sensor_data.json", "r") as file:
    sensor_records = json.load(file)

# Display all sensor records
for sensor in sensor_records:
    print("\nReceived Sensor Data:")
    print(json.dumps(sensor, indent=4))

print("\nAll sensor data received successfully!")
