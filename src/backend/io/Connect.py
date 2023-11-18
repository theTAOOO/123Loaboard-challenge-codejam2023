from datetime import datetime
import json
from paho.mqtt import client as mqtt_client

class MyConnection:
    client = NULL

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
    
    def __init__(self):
        self.client = self.Connect()

    def StartDay():
        with open('src/io/new_day.json', 'r') as json_file:
            data = json.load(json_file)
        data["timestamp"] = datetime.now().isoformat()

        print(data)

StartDay()
# mqtt_client = Connect()
# mqtt_client.loop_start()