from backend.io import ReactController
from backend.io import MQTTController
from backend.io import MessageHandler
from backend.structures import LoadBank
from backend.structures import TruckBank
import time

class GlobalController:
    ReactController = None
    MQTTController = None
    MessageHandler = None
    TruckBank = None
    LoadBank = None
    EmulatedTruckID = None

    def __init__(self):
        self.MessageHandler = MessageHandler.MessageHandler(self)
        self.LoadBank = LoadBank.LoadBank(self)
        self.TruckBank = TruckBank.TruckBank(self)
        self.MQTTController = MQTTController.MQTTController(self)
        self.ReactController = ReactController.ReactController(self)
    
    def StartDay(self):
        self.TruckBank.DeleteAll()
        self.LoadBank.DeleteAll()
    
    def SetEmulatedTruck(self):
        while(self.TruckBank.truck_list.empty):
            time.sleep(1)

        emulated_truck = self.TruckBank.truck_list.iloc[0]
        self.EmulatedTruckID = int(emulated_truck["ID"])
        return self.MessageHandler.CreateOutgoingMsg(['SET', 'TRUCK', list(emulated_truck)])


 
