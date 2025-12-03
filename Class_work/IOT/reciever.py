import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Sensor Data:", msg.payload.decode())

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883)
client.subscribe("iot/sensor1")
client.on_message = on_message

client.loop_forever()
