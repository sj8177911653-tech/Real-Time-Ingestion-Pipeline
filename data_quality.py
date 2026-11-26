import sqlite3
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

conn = sqlite3.connect("sensor_database.db")
cursor = conn.cursor()

print("Data Quality and Alerting Started")

total = cursor.execute(
    "SELECT COUNT(*) FROM sensor_data"
).fetchone()[0]

missing_device = cursor.execute(
    "SELECT COUNT(*) FROM sensor_data WHERE device_id IS NULL"
).fetchone()[0]

missing_temperature = cursor.execute(
    "SELECT COUNT(*) FROM sensor_data WHERE temperature IS NULL"
).fetchone()[0]

missing_humidity = cursor.execute(
    "SELECT COUNT(*) FROM sensor_data WHERE humidity IS NULL"
).fetchone()[0]

invalid_temperature = cursor.execute(
    "SELECT COUNT(*) FROM sensor_data WHERE temperature < -50 OR temperature > 100"
).fetchone()[0]

invalid_humidity = cursor.execute(
    "SELECT COUNT(*) FROM sensor_data WHERE humidity < 0 OR humidity > 100"
).fetchone()[0]

print("Total Records:", total)
print("Missing Device ID:", missing_device)
print("Missing Temperature:", missing_temperature)
print("Missing Humidity:", missing_humidity)
print("Invalid Temperature:", invalid_temperature)
print("Invalid Humidity:", invalid_humidity)

if (
    missing_device == 0
    and missing_temperature == 0
    and missing_humidity == 0
    and invalid_temperature == 0
    and invalid_humidity == 0
):
    print("Data Quality Check Passed!")
    logging.info("Data Quality Check Passed")

else:
    print("ALERT: Data Quality Failure!")
    logging.error(
        "ALERT: Data Quality Failure! "
        "Missing Device=%s, Missing Temperature=%s, "
        "Missing Humidity=%s, Invalid Temperature=%s, Invalid Humidity=%s",
        missing_device, missing_temperature,
        missing_humidity, invalid_temperature, invalid_humidity
    )

conn.close()
if (
    missing_device == 0
    and missing_temperature == 0
    and missing_humidity == 0
    and invalid_temperature == 0
    and invalid_humidity == 0
):
    print("Data Quality Check Passed!")
    logging.info("Improved Data Quality Check Passed")
else:
    print("Data Quality Check Failed!")
    logging.warning("Improved Data Quality Check Failed")

conn.close()
