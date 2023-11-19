from backend.io import ReactController
from backend.io import MQTTController
from backend.io import MessageHandler
from backend.structures import LoadBank
from backend.structures import TruckBank

class GlobalController:
    ReactController = None
    MQTTController = None
    MessageHandler = None
    TruckBank = None
    LoadBank = None

    def __init__(self):
        self.ReactController = ReactController.ReactController(self)
        self.MQTTController = MQTTController.MQTTController(self)
        self.MessageHandler = MessageHandler.MessageHandler(self)
        self.LoadBank = LoadBank.LoadBank(self)
        self.TruckBank = TruckBank.TruckBank(self)
    
    def StartDay(self):
        self.TruckBank.DeleteAll()
        self.LoadBank.DeleteAll()

 
