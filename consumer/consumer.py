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
    'website_events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening to Kafka topic...")

for message in consumer:
    data = message.value

    cursor.execute(
        "INSERT INTO website_logs (page, action) VALUES (?, ?)",
        data['page'],
        data['action']
    )

    conn.commit()

    print("Inserted into SQL:", data)