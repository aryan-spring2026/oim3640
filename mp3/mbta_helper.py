import os
import math
import requests
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")


SPORTS_VENUES = [
    ("Fenway Park", 42.3467, -71.0972),
    ("TD Garden", 42.3662, -71.0621),
    ("Agganis Arena", 42.3522, -71.1177),
    ("Harvard Stadium", 42.3664, -71.1269),
    ("Nickerson Field", 42.3533, -71.1200),
    ("Alumni Stadium", 42.3351, -71.1665),
    ("Gillette Stadium", 42.0909, -71.2643)
]


def get_coordinates(place_name):
    if MAPBOX_TOKEN is None:
        raise ValueError("Missing Mapbox token.")

    url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + place_name + ".json"

    params = {
        "access_token": MAPBOX_TOKEN,
        "limit": 1,
        "proximity": "-71.0589,42.3601"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if len(data["features"]) == 0:
        raise ValueError("Location not found.")

    coordinates = data["features"][0]["center"]
    longitude = coordinates[0]
    latitude = coordinates[1]

    return latitude, longitude


def calculate_distance(lat1, lon1, lat2, lon2):
    radius = 3958.8

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    difference_lat = lat2 - lat1
    difference_lon = lon2 - lon1

    a = (
        math.sin(difference_lat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2)
        * math.sin(difference_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = radius * c
    return distance


def find_nearest_venue(user_lat, user_lon):
    nearest_name = ""
    nearest_lat = 0
    nearest_lon = 0
    shortest_distance = None

    for venue in SPORTS_VENUES:
        name = venue[0]
        lat = venue[1]
        lon = venue[2]

        distance = calculate_distance(user_lat, user_lon, lat, lon)

        if shortest_distance is None or distance < shortest_distance:
            shortest_distance = distance
            nearest_name = name
            nearest_lat = lat
            nearest_lon = lon

    return nearest_name, nearest_lat, nearest_lon, round(shortest_distance, 2)

def find_top_venues(user_lat, user_lon, number_of_venues):
    venues_with_distances = []

    for venue in SPORTS_VENUES:
        name = venue[0]
        lat = venue[1]
        lon = venue[2]

        distance = calculate_distance(user_lat, user_lon, lat, lon)

        venue_info = {
            "name": name,
            "lat": lat,
            "lon": lon,
            "distance": round(distance, 2)
        }

        venues_with_distances.append(venue_info)

    venues_with_distances.sort(key=lambda venue: venue["distance"])

    return venues_with_distances[:number_of_venues]

def get_nearest_stop(lat, lon):
    url = "https://api-v3.mbta.com/stops"

    params = {
        "filter[latitude]": lat,
        "filter[longitude]": lon,
        "sort": "distance",
        "page[limit]": 1
    }

    headers = {}

    if MBTA_API_KEY:
        headers["x-api-key"] = MBTA_API_KEY

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if "data" not in data:
        print(data)
        raise ValueError("MBTA API did not return stop data.")

    if len(data["data"]) == 0:
        raise ValueError("No nearby MBTA stops found.")

    stop = data["data"][0]
    attributes = stop["attributes"]

    stop_name = attributes["name"]
    wheelchair_boarding = attributes["wheelchair_boarding"]

    if wheelchair_boarding == 1:
        accessible = "Yes"
    elif wheelchair_boarding == 2:
        accessible = "No"
    else:
        accessible = "Unknown"

    stop_lat = attributes["latitude"]
    stop_lon = attributes["longitude"]

    return stop_name, accessible, stop_lat, stop_lon


def find_trip(place_name):
    user_lat, user_lon = get_coordinates(place_name)

    venue_name, venue_lat, venue_lon, venue_distance = find_nearest_venue(
        user_lat,
        user_lon
    )

    top_venues = find_top_venues(user_lat, user_lon, 3)
    
    stop_name, accessible, stop_lat, stop_lon = get_nearest_stop(
        venue_lat,
        venue_lon
    )

    result = {
        "search_location": place_name,
        "user_lat": user_lat,
        "user_lon": user_lon,
        "venue_name": venue_name,
        "venue_lat": venue_lat,
        "venue_lon": venue_lon,
        "venue_distance": venue_distance,
        "top_venues": top_venues,
        "stop_name": stop_name,
        "accessible": accessible,
        "stop_lat": stop_lat,
        "stop_lon": stop_lon
    }

    return result


def main():
    place_name = input("Enter your location: ")

    try:
        result = find_trip(place_name)

        print()
        print("Sports Venue Transit Finder")
        print("---------------------------")
        print("Search location:", result["search_location"])
        print("Closest sports venue:", result["venue_name"])
        print("Distance to venue:", result["venue_distance"], "miles")
        print("Nearest MBTA stop:", result["stop_name"])
        print("Wheelchair accessible:", result["accessible"])

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()