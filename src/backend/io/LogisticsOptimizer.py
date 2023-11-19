import json
import googlemaps
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
