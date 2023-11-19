import pandas as pd

class TruckBank:
    GlobalController = None
    truck_list = None

    def __init__(self, global_controller):
        self.global_controller = global_controller
        columns = ['ID', 'Timestamp', 'Latitude', 'Longitude', 'Vehicle Type', 'Trip Preference']
        self.truck_list = pd.DataFrame(columns=columns)
    
    def DeleteAll(self):
        self.truck_list = None
    
    # we won't really care abt sanitizing inputs until smt goes wrong
    def AddTruck(self, truck):
        new_row = { 'ID': truck["truckId"], 
                    'Timestamp': truck["timestamp"],
                    'Latitude': truck["positionLatitude"],
                    'Longitude': truck["positionLongitude"],
                    'Vehicle Type': truck["equipType"],
                    'Trip Preference': truck["nextTripLengthPreference"] }
        
        if new_row['ID'] in self.truck_list['ID'].values:
            self.truck_list.loc[self.truck_list["ID"] == new_row['ID']] = list(new_row.values())
            print("Updated existing truck!")
        else:
            self.truck_list = pd.concat([self.truck_list, pd.DataFrame([new_row])], ignore_index=True)
