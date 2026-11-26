import logging
import sqlite3

# Monitoring setup
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def monitor_pipeline():
    try:
        conn = sqlite3.connect("sensor_database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM sensor_data")
        total_records = cursor.fetchone()[0]

        logging.info(
            f"Pipeline running successfully. Total records: {total_records}"
        )

        print("Monitoring Started")
        print("Total Records:", total_records)

        conn.close()

    except Exception as e:
        logging.error(f"Pipeline Error: {e}")
        print("Alert! Pipeline Error:", e)

monitor_pipeline()