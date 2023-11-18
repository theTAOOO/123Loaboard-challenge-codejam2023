from datetime import datetime
import json
from paho.mqtt import client as mqtt_client
import time

class MQTTConnect:
    client = None
    connect_data = None

    def __init__(self):
        self.client = self.Connect()

    def Connect(self):
        with open('src/backend/io/login.json', 'r') as json_file:
            data = json.load(json_file)

        self.connect_data = data

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        
        def on_subscribe(client, userdata, mid, granted_qos):
            print("Subscription successful!")
            print("Granted QoS: ", granted_qos)
            
        def on_disconnect(client, userdata, rc):
            print("Connection terminated!")
            print("Reconnecting...")
            client.loop_start()

        client = mqtt_client.Client(client_id=data["clientId"], clean_session=data["cleanSession"], userdata=None, protocol=mqtt_client.MQTTv31)
        client.username_pw_set(data["user"], data["password"])
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
        client.on_message = self.HandleRequest
        client.on_disconnect = on_disconnect

        client.connect(data["host"], data["port"])
        client.loop_start()
        client.subscribe(data["Topic"], qos=data["QoS"])

        while not client.is_connected():
            time.sleep(1)

        return client

    def HandleRequest(self, client, userdata, message):
        print("Message Received!")
        print("Userdata: ", userdata)
        print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))