import sqlite3

# Create database connection
conn = sqlite3.connect("sensor_database.db")

# Create cursor
cursor = conn.cursor()

# Create sensor table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    device_id TEXT,
    temperature REAL,
    humidity REAL,
    pressure REAL,
    battery REAL,
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Save changes
conn.commit()

print("Database created successfully!")
print("Sensor table created successfully!")

# Close connection
conn.close()