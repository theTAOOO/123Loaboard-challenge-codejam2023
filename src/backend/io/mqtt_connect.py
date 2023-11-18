from datetime import datetime
import json
from paho.mqtt import client as mqtt_client
from backend.io import ParseRequests
from backend.structures import global_controller
import time

class MQTTConnect:
    client = None
    connect_data = None
    global_controller = None

    def __init__(self, global_controller):
        self.global_controller = global_controller

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
            self.client.loop_start()

        self.client = mqtt_client.Client(client_id=data["clientId"], clean_session=data["cleanSession"], userdata=None, protocol=mqtt_client.MQTTv31)
        self.client.username_pw_set(data["user"], data["password"])
        self.client.on_connect = on_connect
        self.client.on_subscribe = on_subscribe
        self.client.on_message = self.HandleRequest
        self.client.on_disconnect = on_disconnect

    def Connect(self):
        with open('src/backend/io/login.json', 'r') as json_file:
            data = json.load(json_file)

        self.client.connect(data["host"], data["port"])
        self.client.loop_start()
        self.client.subscribe(data["Topic"], qos=data["QoS"])

        while not self.client.is_connected():
            time.sleep(1)

    def HandleRequest(self, client, userdata, message):
        self.global_controller.MessageHandler.HandleIncomingMessage(message.payload.decode())
