import pandas as pd
from backend.io import LogisticsOptimizer
from backend.structures import LoadBank

class TruckBank:
    global_controller = None
    truck_list = None

    def __init__(self, global_controller):
        self.global_controller = global_controller
        columns = ['ID', 'Timestamp', 'Latitude', 'Longitude', 'Vehicle Type', 'Trip Preference']
        self.truck_list = pd.DataFrame(columns=columns)
    
    def DeleteAll(self):
        self.truck_list = self.truck_list.drop(self.truck_list.index)
        print("Deleted all trucks!")

    # we won't really care abt sanitizing inputs until smt goes wrong
    def AddTruck(self, truck):
        new_truck = { 'ID': truck["truckId"], 
                    'Timestamp': truck["timestamp"],
                    'Latitude': truck["positionLatitude"],
                    'Longitude': truck["positionLongitude"],
                    'Vehicle Type': truck["equipType"],
                    'Trip Preference': truck["nextTripLengthPreference"] }
        
        if new_truck['ID'] in self.truck_list['ID'].values:
            self.truck_list.loc[self.truck_list["ID"] == new_truck['ID']] = list(new_truck.values())

            if self.global_controller.EmulatedTruckID is not None and self.global_controller.EmulatedTruckID == int(new_truck['ID']):
                self.global_controller.LogisticsOptimizer.UpdateLoads()
                self.global_controller.MessageHandler.CreateOutgoingMsg(['UPD', 'TRUCK', list(new_truck.values())])
            
            print("Updated existing truck!")
            return
        
        self.truck_list = pd.concat([self.truck_list, pd.DataFrame([new_truck])], ignore_index=True)
