"""
Periodic CSV Uploader to InfluxDB

This script monitors a directory for CSV log files and uploads new data entries
to an InfluxDB instance. It remembers the timestamp of the last uploaded entry
to avoid duplicate uploads and runs on an hourly schedule.

Dependencies:
- pandas
- influxdb-client
- schedule
"""

import os
import time
import pandas as pd
import schedule
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

# ============ CONFIGURATION ============
INFLUXDB_URL = "http://meridian.caltech.edu:8086"
INFLUXDB_TOKEN = "<InfluxDB_Token>"  # Replace with your InfluxDB token
INFLUXDB_ORG = "caltech"
INFLUXDB_BUCKET = "WaspLogs"

CSV_DIRECTORY = "../logs_from_wasp/"  # Directory containing CSV files
MEASUREMENT_NAME = "sensor_logs"  # InfluxDB measurement name
LAST_TIMESTAMP_FILE = "last_uploaded_timestamp.txt"  # File to store the last uploaded timestamp
# ========================================


def get_last_uploaded_timestamp():
    """
    Reads the timestamp of the last successfully uploaded data point from file.
    Returns:
        pd.Timestamp: The last uploaded timestamp, or the earliest possible timestamp if file doesn't exist.
    """
    if os.path.exists(LAST_TIMESTAMP_FILE):
        with open(LAST_TIMESTAMP_FILE, "r") as f:
            return pd.to_datetime(f.read().strip())
    return pd.Timestamp.min


def save_last_uploaded_timestamp(ts):
    """
    Saves the most recent uploaded timestamp to file.

    Args:
        ts (pd.Timestamp): The latest timestamp to save.
    """
    with open(LAST_TIMESTAMP_FILE, "w") as f:
        f.write(str(ts))


def upload_csv_to_influx():
    """
    Processes CSV log files in the directory, filters out already-uploaded entries,
    and uploads new rows to InfluxDB. Also updates the last uploaded timestamp.
    """
    print(f"[{datetime.now()}] Starting CSV upload process...")
    latest_ts = get_last_uploaded_timestamp()

    # Collect list of relevant CSV files
    csv_files = sorted(
        f for f in os.listdir(CSV_DIRECTORY)
        if f.startswith("log-") and f.endswith(".csv")
    )

    # Initialize InfluxDB client
    client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    new_latest_ts = latest_ts

    for file in csv_files:
        print(f"Processing {file}...")
        path = os.path.join(CSV_DIRECTORY, file)
        df = pd.read_csv(path)

        print(df)  # Debug: show data read from file

        # Ensure TIME column is parsed correctly
        df['TIME'] = pd.to_datetime(df['TIME'], format='ISO8601')
        df = df[df['TIME'] > latest_ts]

        if df.empty:
            continue  # Skip if there's no new data

        for _, row in df.iterrows():
            point = Point(MEASUREMENT_NAME).time(row['TIME'])
            for col in df.columns:
                if col != "TIME":
                    try:
                        point.field(col, float(row[col]))
                    except Exception:
                        pass  # Skip non-numeric fields

            # Write data point to InfluxDB
            write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)

        # Update new_latest_ts if newer timestamps were found
        max_time = df['TIME'].max()
        if max_time > new_latest_ts:
            new_latest_ts = max_time

    if new_latest_ts > latest_ts:
        save_last_uploaded_timestamp(new_latest_ts)
        print(f"Upload complete. Last timestamp: {new_latest_ts}")
    else:
        print("No new data to upload.")

    client.close()


# Schedule job to run hourly
schedule.every().hour.do(upload_csv_to_influx)

print("Uploader started. Waiting for the next hourly run.")
upload_csv_to_influx()  # Run once immediately on start

# Infinite loop to keep the scheduler alive
while True:
    schedule.run_pending()
    time.sleep(60)
