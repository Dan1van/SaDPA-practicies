import flightradar24
import json
from urllib.request import Request, urlopen
import folium


def main():
    fr = flightradar24.Api()
    flight = fr.get_flight('CZ300')

    flight_id = flight['result']['response']['data'][0]['identification']['id']
    timestamp = flight['result']['response']['timestamp']

    json_file = get_json(flight_id, timestamp)
    coordinates = parse_coordinates(json_file)

    draw_the_flight(coordinates)


def get_json(flight_id: str, timestamp: int):
    track_request_link = f'https://api.flightradar24.com/common/v1/flight-playback.json?flightId={flight_id}&timestamp={timestamp}&token=&pk'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(track_request_link, headers=headers)
    track_request = urlopen(req).read().decode('utf-8')
    json_file = json.loads(track_request)
    return json_file


def parse_coordinates(json_file: dict):
    coordinates = []
    track = json_file['result']['response']['data']['flight']['track']

    for coordinate in track:
        coordinates.append((coordinate['latitude'], coordinate['longitude']))
    return coordinates


def draw_the_flight(coordinates: list):
    map = folium.Map()
    folium.PolyLine(coordinates, color='#cc473d').add_to(map)
    map.save('x.html')


if __name__ == '__main__':
    main()
