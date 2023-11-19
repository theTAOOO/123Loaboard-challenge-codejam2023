import pandas as pd

class LoadBank:
    global_controller = None
    load_list = None

    def __init__(self, global_controller):
        self.global_controller = global_controller
        columns = ['ID', 'Timestamp', 'OriginLatitude', 'OriginLongitude',
                   'DestinationLatitude', 'DestinationLongitude', 'Vehicle Type', 'Price', 'Mileage']
        self.load_list = pd.DataFrame(columns=columns)
    
    def DeleteAll(self):
        self.load_list = self.load_list.drop(self.load_list.index)
        print("Deleted all trucks!")

    # we won't really care abt sanitizing inputs until smt goes wrong
    def AddLoad(self, load):
        new_load = { 'ID': load["loadId"], 
                    'Timestamp': load["timestamp"],
                    'OriginLatitude': load["originLatitude"],
                    'OriginLongitude': load["originLongitude"],
                    'DestinationLatitude': load["destinationLatitude"],
                    'DestinationLongitude': load["destinationLongitude"],
                    'Vehicle Type': load["equipmentType"],
                    'Price': load["price"], 
                    'Mileage': load["mileage"], }
        
        if new_load['ID'] in self.load_list['ID'].values:
            raise Exception("[FATAL]: LOAD MAGICALLY CHANGED LOCATION????")
            return
            # self.load_list.loc[self.load_list["ID"] == new_row['ID']] = list(new_row.values())
            # print("Updated existing truck!")
        self.load_list = pd.concat([self.load_list, pd.DataFrame([new_load])], ignore_index=True)

    def DeleteLoad(self, load_id):
        # need to implement locking in future in case multiple truckers try to select at same time
        if load_id in self.load_list['ID'].values:
            raise Exception("[FATAL]: LOAD MAGICALLY DISAPPEARED????")
        
        self.load_list.drop(self.load_list.loc[self.load_list["ID"] == load_id], inplace=True)
