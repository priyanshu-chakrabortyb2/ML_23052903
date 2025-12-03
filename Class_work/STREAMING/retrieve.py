from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for i in range(5):
    msg = f"Sensor reading {i}"
    producer.send("sensor-topic", msg.encode())
    print("Sent:", msg)
    time.sleep(1)
