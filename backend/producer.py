from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',   # Connection to Kafka in Docker
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_event(event):
    producer.send('website_events', event)  # Sending Data to Kafka Topic
    producer.flush()