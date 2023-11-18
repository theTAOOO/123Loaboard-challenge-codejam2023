import json
import googlemaps


def connectAPI() -> (str, str):
    with open('maps_connect.json', 'r') as json_file:
        api_key = json.load(json_file)

    with open('file1.json', 'r') as startpoint:
        data1 = json.load(startpoint)

    with open('file2.json', 'r') as endpoint:
        data2 = json.load(endpoint)

    maps_client = googlemaps.Client(key=api_key["apiKey"])
    start_lat = data1["positionLatitude"]
    start_lng = data1["positionLongitude"]
    end_lat = data2["originLatitude"]
    end_lng = data2["originLongitude"]

    origin = (start_lat, start_lng)
    destination = (end_lat, end_lng)

    try:
        directions = maps_client.directions(origin, destination, mode="driving")
        distance_text = directions[0]['legs'][0]['distance']['text']
        distance_value = directions[0]['legs'][0]['distance']['value']
        duration_min = ((distance_value / 1609.34) / 65) * 60
        duration_hour = str(int(duration_min / 60))
        duration_min_r = str(int(duration_min % 60))
        duration = duration_hour + ' hours ' + duration_min_r + ' min'
        print(f'Distance: {distance_text}')
        print(f'Estimated Travel Time: {duration}')
        return f'Distance: {distance_text}', f'Estimated Travel Time: {duration}'

    except googlemaps.exceptions.ApiError as e:
        print(f'Error calculating distance using googlemaps library: {e}')


connectAPI()

