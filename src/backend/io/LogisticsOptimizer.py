import json
import googlemaps
import os
from backend.structures import GlobalController


class LogisticsOptimizer:
    def __init__(self):
        with open('maps_connect.json', 'r') as json_file:
            api_key = json.load(json_file)
        self.maps_client = googlemaps.Client(key=api_key["apiKey"])

    def calculate_distance(self, origin, destination) -> (str, str):
        try:
            directions = self.maps_client.directions(origin, destination, mode="driving")
            distance_text = directions[0]['legs'][0]['distance']['text']
            distance_value = directions[0]['legs'][0]['distance']['value']
            duration_min = ((distance_value / 1609.34) / 65) * 60
            duration_hour_str = str(int(duration_min / 60))
            duration_hour = duration_min / 60
            duration_min_r = str(int(duration_min % 60))
            duration = duration_hour_str + ' hours ' + duration_min_r + ' min'
            print(f'Distance: {distance_text}')
            print(f'Estimated Travel Time: {duration}')
            return f'Distance: {distance_text}', f'Estimated Travel Time: {duration}', duration_hour

        except googlemaps.exceptions.ApiError as e:
            print(f'Error calculating distance using googlemaps library: {e}')

    def calculate_profit(self, truck, load):
        idle_distance = self.calculate_distance((truck[2], truck[3]), (load[2], load[3]))
        total_distance = idle_distance + load[8]
        expenses = total_distance * 1.38
        load_travel_time = (load[8]) / 65 + idle_distance[2]
        return (load[7] - expenses) / load_travel_time

    @staticmethod
    def check_preferences(truck, load):
        if int(load[8]) > 200:
            load_travel_type = "Long"
        else:
            load_travel_type = "Short"
        trucker_preference = truck[5]
        if trucker_preference == load_travel_type:
            return True
        else:
            return False

    def select_trucks(self, truck_bank, load):
        to_notify = []
        for truck in truck_bank:
            if (truck[5] != load[6]) or (self.check_preferences(truck, load)):
                continue
            else:
                if self.calculate_profit(truck, load) < 0:
                    continue
                else:
                    to_notify.append(truck)
        sorted_trucks = sorted(to_notify, key=self.calculate_profit, reverse=True)
        return sorted_trucks

    def select_loads(self, truck, load_bank):
        to_pick_up = []
        for load in load_bank:
            if (truck[5] != load[6]) or (self.check_preferences(truck, load)):
                continue
            else:
                if self.calculate_profit(truck, load) < 0:
                    continue
                else:
                    to_pick_up.append(load)
        sorted_loads = sorted(to_pick_up, key=self.calculate_profit, reverse=True)
        return sorted_loads


# Sample data for testing
sample_trucks = [
    # Sample truck data: [truck_id, truck_type, origin_lat, origin_lng, capacity, preference]
    [326, '2023-11-18T20:25:41', 32.736137, -85.289268, 'Flatbed', 'Short'],
    [339, '2023-11-18T20:26:48', 40.966309, -75.983070, 'Van', 'Short'],
    [101, '2023-11-18T20:28:01', 39.171665, -85.958260, 'Reefer', 'Long']
]

sample_loads = [
    [101, 'Goods', 34.0522, -118.2437, 34.0522, -118.2437, 'Long', 500, 300],
    [102, 'Furniture', 34.0522, -118.2437, 34.0522, -118.2437, 'Short', 800, 150],
    # Add more sample loads as needed
]

# Instantiate the LogisticsOptimizer class
logistics_optimizer = LogisticsOptimizer()

# Test the calculate_distance function
distance_result = logistics_optimizer.calculate_distance((34.0522, -118.2437), (34.0522, -118.2437))
print(distance_result)

# Test the calculate_profit function
profit_result = logistics_optimizer.calculate_profit(sample_trucks[0], sample_loads[0])
print(profit_result)

# Test the check_preferences function
preferences_result = logistics_optimizer.check_preferences(sample_trucks[0], sample_loads[0])
print(preferences_result)

# Test the select_trucks function
selected_trucks = logistics_optimizer.select_trucks(sample_trucks, sample_loads[0])
print(selected_trucks)

# Test the select_loads function
selected_loads = logistics_optimizer.select_loads(sample_trucks[0], sample_loads)
print(selected_loads)
