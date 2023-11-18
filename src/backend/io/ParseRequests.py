import json

class MessageHandler:
    def HandleIncomingMessage(message_payload_str):
        message_payload = json.loads(message_payload_str)
        if ("Truck" == message_payload["type"]):
            print("New Truck!")
            HandleTruckMessage(message_payload)
        elif ("Load" == message_payload["type"]):
            print("New Load!")
            HandleLoadMessage(message_payload)
        elif ("Start" == message_payload["type"]):
            print("Start day!")
            HandleStartMessage(message_payload)
        elif ("End" == message_payload["type"]):
            print("End day!")
            HandleEndDayMessage(message_payload)
        else:
            raise Exception("[FATAL]: RECEIVED GARBAGE: ", message_payload) 
        return
    
    def HandleTruckMessage(message_payload):
        return