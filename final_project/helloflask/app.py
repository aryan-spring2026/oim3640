from flask import Flask, request, render_template

app = Flask(__name__)

"""
Adding multiplers per month, which showcasing based on the season how does your travel month impact the price.
"""

MONTH_MULTIPLIER = {
    "January": 0.90,
    "February": 0.85,
    "March": 0.95,
    "April": 1.00,
    "May": 1.00,
    "June": 1.15,
    "July": 1.15,
    "August": 1.20,
    "September": 1.00,
    "October": 0.90,
    "November": 0.85,
    "December": 1.50,
}

"""
Adding the arrival airport function to ensure that the location of departure is taken into consideration when planning the price estimate.
"""

DESTINATIONS = {
    "London, United Kingdom":{
        "flight": 700,
        "living": 100,
        "food": 45,
        "transportation": 30,
    },
    "Venice, Italy": {
        "flight": 600,
        "living": 100,
        "food": 35,
        "transportation": 15,
    },
    "Kyoto, Japan": {
        "flight": 1200,
        "living": 100,
        "food": 50,
        "transportation": 25,
    },
    "Seoul, South Korea": {
        "flight": 1000,
        "living": 95,
        "food": 45,
        "transportation": 30,
    },
    "Toronto, Canada": {
        "flight": 300,
        "living": 50,
        "food": 25,
        "transportation": 10,
    },
}

"""
Adding the price of departing airport so consumers can compare prices from departing airport.
"""
AIRPORT_MULTIPLIER = {
    "BOS": 1.15,
    "JFK": 1.00,
    "EWR": 1.10,
    "LAX": 1.08,
    "MIA": 1.25,
    "ATL": 1.20,
    "Other": 1.08,
}

def format_money(amount):
    return "${:,.2f}".format(amount)

def calculate_trip(destination, month, travelers, days, airport):
    data = DESTINATIONS[destination]

    flight_cost = (
        data["flight"]
        * MONTH_MULTIPLIER[month]
        * AIRPORT_MULTIPLIER[airport]
        * travelers
    )

    nights = days - 1
    living_cost = data["living"] * nights
    food_cost = data["food"] * days * travelers
    transportation_cost = data["transportation"] * days * travelers

    total_cost = flight_cost + living_cost + food_cost + transportation_cost

    return {
        "destination": destination,
        "month": month,
        "travelers": travelers,
        "days": days,
        "flight_cost": format_money(flight_cost),
        "living_cost": format_money(living_cost),
        "food_cost": format_money(food_cost),
        "transportation_cost": format_money(transportation_cost),
        "total_cost": format_money(total_cost),
        "cost_per_person": format_money(total_cost / travelers),
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compare", methods=["POST"])
def compare():
    airport = request.form["airport"]
    month = request.form["month"]
    travelers = int(request.form["travelers"])
    days = int(request.form["days"])

    selected_destinations =request.form.getlist("destinations")

    trips = []

    for destination in selected_destinations:
        trip = calculate_trip(destination, month, travelers, days, airport)
        trips.append(trip)

    best_trip = trips[0]

    for trip in trips:
        total_number = float(trip["total_cost"].replace("$", "").replace(",", ""))

        best_number = float(best_trip["total_cost"].replace("$", "").replace(",", ""))

        if total_number < best_number:
            best_trip = trip
    
    return render_template(
        "results.html",
        trips=trips,
        best_trip=best_trip
    )

if __name__ == "__main__":
    app.run(debug=True)