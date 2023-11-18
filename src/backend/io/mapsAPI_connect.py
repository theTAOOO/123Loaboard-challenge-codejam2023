import requests
import json

def ConnectAPI():
    with open('src/backend/io/maps_connect.json', 'r') as json_file:
        data = json.load(json_file)
    api_key = data["apiKey"]

    with open('file1.json', 'r') as startpoint:
        data1 = json.load(startpoint)

    with open('file2.json', 'r') as endpoint:
        data2 = json.load(endpoint)

    start_lat = data1["positionLatitude"]
    start_lng = data1["positionLongitude"]
    end_lat = data2["originLatitude"]
    end_lng = data2["originLongitude"]
    origin = 'start_lat,start_lng'
    destination = 'end_lat,end_lng'
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        distance_text = data['rows'][0]['elements'][0]['distance']['text']
        distance_value = data['rows'][0]['elements'][0]['distance']['value']

        print(f'Distance: {distance_text}')
        print(f'Distance Value: {distance_value} meters')
    else:
        print(f'Error: {response.status_code}')
        print(response.text)

connectedAPI = ConnectAPI()