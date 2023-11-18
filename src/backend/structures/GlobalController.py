from backend.io import MQTTController
from backend.io import MessageHandler
from backend.structures import TruckBank

class GlobalController:
    MQTTController = None
    MessageHandler = None
    TruckBank = None
    LoadBank = None

    def __init__(self):
        self.MQTTController = MQTTController.MQTTController(self)
        self.MessageHandler = MessageHandler.MessageHandler(self)
        self.TruckBank = TruckBank.TruckBank(self)
 
