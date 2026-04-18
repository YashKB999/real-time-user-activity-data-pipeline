import pyodbc
from kafka import KafkaConsumer
import json

# Azure SQL connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=deprojectserver426.database.windows.net;'
    'DATABASE=website_activity_db;'
    'UID=sqladmin;'
    'PWD=Sql@1234;'
    'TrustServerCertificate=yes;'
)

cursor = conn.cursor()

consumer = KafkaConsumer(
    'website_events',  # topic

    bootstrap_servers='localhost:9092',  # Kafka connection

    value_deserializer=lambda x: json.loads(x.decode('utf-8')),

    auto_offset_reset='earliest',  # read from start if no offset

    group_id='my-group-1'  # track consumption properly
)

print("Listening to Kafka topic...")

for message in consumer:
    data = message.value

    cursor.execute(
    "INSERT INTO website_logs (user_id, page, action, event_time_utc, product_id, device, location) VALUES (?, ?, ?, ?, ?, ?, ?)",
    data['user_id'],
    data['page'],
    data['action'],
    data['event_time'],
    data['product_id'],
    data['device'],
    data['location']
    )

    conn.commit()

    print("Inserted into SQL:", data)