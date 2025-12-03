import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883)

while True:
    client.publish("iot/sensor1", "Temperature: 25°C")
    print("Sent: Temperature: 25°C")
    time.sleep(2)
