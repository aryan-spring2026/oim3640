import os
import requests

from dotenv import load_dotenv
from flask import Flask, request, render_template

load_dotenv(dotenv_path=".env")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

MONTH_MULTIPLIERS = {
    "January": 0.95,
    "February": 0.90,
    "March": 1.00,
    "April": 1.05,
    "May": 1.10,
    "June": 1.25,
    "July": 1.35,
    "August": 1.30,
    "September": 1.05,
    "October": 0.95,
    "November": 0.90,
    "December": 1.40,
}

def format_money(amount):
    return "${:,.2f}".format(amount)

def get_airport_multiplier(airport):
    airport = airport.upper().strip()

    if airport in ["JFK", "LGA", "EWR"]:
        return 0.95

    elif airport in ["BOS", "PHL", "DCA"]:
        return 1.00

    elif airport in ["ORD", "ATL", "DFW", "IAH"]:
        return 1.03

    elif airport in ["LAX", "SFO", "SEA", "SAN"]:
        return 1.08

    elif airport in ["MIA", "MCO", "TPA"]:
        return 0.98

    else:
        return 1.10

def get_destination_estimate(destination):
    destination = destination.lower()

    if (
        "london" in destination
        or "paris" in destination
        or "venice" in destination
        or "rome" in destination
        or "prague" in destination
    ):
        return {"flight": 750, "hotel": 145, "food": 55, "transport": 18}

    elif (
        "tokyo" in destination
        or "kyoto" in destination
        or "seoul" in destination
        or "bangkok" in destination
    ):
        return {"flight": 1100, "hotel": 130, "food": 45, "transport": 16}

    elif (
        "toronto" in destination
        or "mexico" in destination
        or "vancouver" in destination
    ):
        return {"flight": 450, "hotel": 100, "food": 35, "transport": 12}

    else:
        return {"flight": 800, "hotel": 120, "food": 45, "transport": 15}

def get_weather(destination):
    if WEATHER_API_KEY is None:
        return {
            "available": False,
            "message": "Weather API key is missing."
        }

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": destination,
        "appid": WEATHER_API_KEY,
        "units": "imperial"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {
            "available": False,
            "message": "Weather unavailable for this destination."
        }

    data = response.json()

    return {
        "available": True,
        "city": data["name"],
        "country": data["sys"]["country"],
        "current_temp": round(data["main"]["temp"]),
        "feels_like": round(data["main"]["feels_like"]),
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"].title(),
    }

def calculate_trip(destination, month, travelers, days, airport):
    data = get_destination_estimate(destination)

    airport_multiplier = get_airport_multiplier(airport)
    month_multiplier = MONTH_MULTIPLIERS[month]

    flight_cost = data["flight"] * airport_multiplier * month_multiplier * travelers
    nights = days - 1
    hotel_cost = data["hotel"] * nights
    food_cost = data["food"] * days * travelers
    transport_cost = data["transport"] * days * travelers

    total_cost = flight_cost + hotel_cost + food_cost + transport_cost

    weather = get_weather(destination)

    return {
        "destination": destination.title(),
        "airport": airport.upper(),
        "month": month,
        "travelers": travelers,
        "days": days,
        "flight_cost": format_money(flight_cost),
        "hotel_cost": format_money(hotel_cost),
        "food_cost": format_money(food_cost),
        "transport_cost": format_money(transport_cost),
        "total_cost": format_money(total_cost),
        "raw_total": total_cost,
        "cost_per_person": format_money(total_cost / travelers),
        "cost_per_day": format_money(total_cost / days),
        "weather": weather,
    }
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compare", methods=["POST"])
def compare():
    airport = request.form["airport"]
    travelers = int(request.form["travelers"])
    days = int(request.form["days"])
    month = request.form["month"]

    selected_destinations = []

    for destination in request.form.getlist("destinations"):
        if destination.strip() != "":
            selected_destinations.append(destination.strip())

    trips = []

    for destination in selected_destinations:
        trip = calculate_trip(destination, month, travelers, days, airport)
        trips.append(trip)

    if len(selected_destinations) == 0:
        return render_template("index.html")

    best_trip = trips[0]

    for trip in trips:
        if trip["raw_total"] < best_trip["raw_total"]:
            best_trip = trip
    
    return render_template(
        "results.html",
        trips=trips,
        best_trip=best_trip
    )

if __name__ == "__main__":
    app.run(debug=True)