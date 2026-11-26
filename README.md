# Real-Time Ingestion Pipeline with Schema Drift Handling

## 1. Project Overview
This project implements a real-time IoT data ingestion pipeline that receives sensor data in JSON format, handles schema changes, processes incoming records, and stores the data for further analysis.

## 2. Problem Statement
IoT devices frequently update their firmware, which may change the structure of sensor data. These changes are known as schema drift. If a pipeline cannot handle these changes, data ingestion and processing may fail.

This project demonstrates a pipeline designed to handle changing JSON structures.

## 3. Objectives
- Ingest IoT sensor data.
- Handle schema drift in JSON messages.
- Support schema versioning.
- Normalize and transform sensor records.
- Perform data quality checks.
- Store processed data in a database.
- Monitor pipeline activity.

## 4. Technologies Used
- Python
- Apache Kafka
- SQLite
- JSON
- Pandas
- NumPy
- Docker Compose

## 5. Project Architecture
1. IoT sensor data is generated in JSON format.
2. A producer sends messages to the ingestion pipeline.
3. A consumer receives incoming messages.
4. The schema handler manages changes in data structure.
5. The data processor transforms sensor records.
6. Data quality checks validate the processed records.
7. The database stores the processed data.
8. Monitoring tracks pipeline activity and errors.

## 6. Schema Drift Handling
The project demonstrates sensor messages with different fields.

Examples:
- S101: device_id, temperature, humidity
- S102: device_id, temperature, humidity
- S103: device_id, temperature, humidity, pressure
- S104: device_id, temperature, humidity, pressure, battery

The pipeline is designed to handle optional fields and changing JSON structures.

## 7. Main Features
- Real-time ingestion pipeline components.
- Kafka producer and consumer modules.
- Schema handling and version management.
- Data processing and normalization.
- Data quality validation.
- SQLite database storage.
- Monitoring and logging.

## 8. Project Files
- `main.py` – Main application entry point.
- `streaming_pipeline.py` – Streaming pipeline logic.
- `kafka_producer.py` – Kafka producer module.
- `kafka_consumer.py` – Kafka consumer module.
- `schema_handler.py` – Schema drift handling.
- `schema_version.py` – Schema version management.
- `data_processor.py` – Data transformation.
- `data_quality.py` – Data quality checks.
- `monitoring.py` – Pipeline monitoring.
- `database_setup.py` – Database setup.
- `data_insert.py` – Sensor data insertion.
- `sensor_data.json` – Sample sensor data.
- `sensor_database.db` – SQLite database.
- `docker-compose.yml` – Docker Compose configuration.

## 9. Installation and Execution

### Step 1: Create virtual environment
```bash
python -m venv venv
```

### Step 2: Activate virtual environment
```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize database
```bash
python database_setup.py
```

### Step 5: Insert sensor data
```bash
python data_insert.py
```

### Step 6: Run the application
```bash
python main.py
```

## 10. Testing
The application was tested with multiple sensor records containing different JSON fields. The main application successfully received all four sample sensor records.

## 11. Conclusion
This project demonstrates the basic concepts of real-time IoT data ingestion and schema drift handling. It shows how changing sensor payload structures can be processed while maintaining a structured data pipeline.