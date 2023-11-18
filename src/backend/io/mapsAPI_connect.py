import json
import googlemaps

def connectAPI():
    with open('maps_connect.json', 'r') as json_file:
        api_key = json.load(json_file)

    with open('src/backend/io/file1.json', 'r') as startpoint:
        data1 = json.load(startpoint)

    with open('src/backend/io/file2.json', 'r') as endpoint:
        data2 = json.load(endpoint)

    maps_client = googlemaps.Client(key=api_key["apiKey"])
    start_lat = data1["positionLatitude"]
    start_lng = data1["positionLongitude"]
    end_lat = data2["originLatitude"]
    end_lng = data2["originLongitude"]

    origin = (start_lat, start_lng)
    destination = (end_lat, end_lng)

    # Using googlemaps library to get directions
    directions = maps_client.directions(origin, destination, mode="driving")

    if directions:
        distance_text = directions[0]['legs'][0]['distance']['text']
        distance_value = directions[0]['legs'][0]['distance']['value']

        print(f'Distance: {distance_text}')
        print(f'Distance Value: {distance_value} meters')
    else:
        print('Error calculating distance using googlemaps library')

connectAPI()
