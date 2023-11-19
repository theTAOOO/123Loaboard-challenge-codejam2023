import json

class MessageHandler:
    global_controller = None

    def __init__(self, global_controller):
        self.global_controller = global_controller

    def HandleMQTTIncomingMessage(self, message_payload_str):
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
        self.global_controller.LoadBank.AddLoad(message_payload)
        return
    
    def HandleStartMessage(self, message_payload):
        self.global_controller.StartDay()
        # raise Exception("[FATAL]: UNHANDLED START DAY REQ", message_payload)
        return
    
    def HandleEndDayMessage(self, message_payload):
        return
        raise Exception("[FATAL]: UNHANDLED END DAY REQ", message_payload)
        
    def HandleFEIncomingMessage(self, message):
        # structure: [Get/Set, Truck, ID, etc]
        if ("GET" == message[0]):
            self.HandleFEGetMsg(message[1:])
        elif ("SET" == message[0]):
            self.HandleFESetMsg(message[1:])
        else:
            raise Exception("[FATAL]: UNKNOWN CLIENT MSG RECEIVED: ", message)
    
    def HandleFEGetMsg(self, message):
        # structure: [Truck, ID, etc]
        if ("TRUCK" == message[0]):
            return
        # elif ("LOAD" == message[0]):
        #     return
        else:
            raise Exception("[FATAL]: UNKNOWN CLIENT GET REQ: ", message)
    
    def HandleFESetMsg(self, message):
        # if ("TRUCK" == message[0]):
        #     return
        if ("LOAD" == message[0]):
            return
        else:
            raise Exception("[FATAL]: UNKNOWN CLIENT GET REQ: ", message)
        return