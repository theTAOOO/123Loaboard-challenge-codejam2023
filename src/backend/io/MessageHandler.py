import json
from backend.structures import GlobalController
from backend.structures import TruckBank

class MessageHandler:
    global_controller = None

    def __init__(self, global_controller):
        self.global_controller = global_controller

    def HandleIncomingMessage(self, message_payload_str):
        message_payload = json.loads(message_payload_str)
        if ("Truck" == message_payload["type"]):
            print("New Truck!")
            self.HandleTruckMessage(message_payload)
        elif ("Load" == message_payload["type"]):
            print("New Load!")
            self.HandleLoadMessage(message_payload)
        elif ("Start" == message_payload["type"]):
            print("Start day!")
            self.HandleStartMessage(message_payload)
        elif ("End" == message_payload["type"]):
            print("End day!")
            self.HandleEndDayMessage(message_payload)
        else:
            raise Exception("[FATAL]: RECEIVED GARBAGE: ", message_payload) 
        return
    
    def HandleTruckMessage(self, message_payload):
        self.global_controller.TruckBank.AddTruck(message_payload)
        return
    def HandleLoadMessage(self, message_payload):
        return
    def HandleStartMessage(self, message_payload):
        return
    def HandleEndDayMessage(self, message_payload):
        return