import json
from paho.mqtt import client as mqtt_client

def Connect():
    with open('src/io/login.json', 'r') as json_file:
        data = json.load(json_file)

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id=data["clientId"], clean_session=data["cleanSession"], userdata=None, protocol=mqtt_client.MQTTv31)
    client.username_pw_set(data["user"], data["password"])
    client.on_connect = on_connect
    client.connect(data["host"], data["port"])
    return client

mqtt_client = Connect()
mqtt_client.loop_start()