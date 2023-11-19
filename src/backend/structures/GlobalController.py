from backend.io import LogisticsOptimizer
from backend.io import MessageHandler
from backend.io import MQTTController
from backend.io import ReactController
from backend.structures import LoadBank
from backend.structures import TruckBank
import time

class GlobalController:
    LogisticsOptimizer = None
    MessageHandler = None
    MQTTController = None
    ReactController = None
    LoadBank = None
    TruckBank = None
    EmulatedTruckID = None

    def __init__(self):
        self.LogisticsOptimizer = LogisticsOptimizer.LogisticsOptimizer(self)
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
        self.MessageHandler.CreateOutgoingMsg(['SET', 'TRUCK', list(emulated_truck)])

        # TODO: replace with async/await resp
        # Wait for them to receive it
        time.sleep(1)
        self.LogisticsOptimizer.UpdateLoads()
