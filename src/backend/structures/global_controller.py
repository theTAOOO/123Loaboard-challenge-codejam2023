from backend.io import mqtt_connect
from backend.io import ParseRequests
from backend.structures import truck_bank

class GlobalController:
    MQTTController = None
    MessageHandler = None
    TruckBank = None
    LoadBank = None

    def __init__(self):
        self.MQTTController = mqtt_connect.MQTTConnect(self)
        self.MessageHandler = ParseRequests.MessageHandler(self)
        self.TruckBank = truck_bank.TruckBank(self)
 
