# Milestone 2 (Core Features): Cost Estimator for Flights

def get_region(destination):
    oceania = ["australia", "new zealand", "fiji", "papua new guinea"]
    africa = ["south africa", "kenya", "morocco", "egypt", "ghana"]
    south_america = ["brazil", "colombia", "peru", "ecuador", "argentina"]
    asia = ["japan", "china", "south korea", "india", "thailand"]
    europe = ["france", "germany", "italy", "spain", "sweden"]
    
    destination = destination.lower()
    
    if destination in europe:
        return "europe"
    elif destination in asia:
        return "asia"
    elif destination in south_america:
        return "south_america"
    elif destination in africa:
        return "africa"
    elif destination in oceania:
        return "oceania"
    else:
        return "unknown"

def get_price(region):
    if region == "oceania":
        return 1300
    elif region == "africa":
        return 1100
    elif region == "south_america":
        return 550
    elif region == "asia":
        return 900
    elif region == "europe":
        return 750
    else:
        return 800 #baseline

def get_seasonality(month):
    """
    Based on the "peak" months of travel, this function allows for users to see how specific months either add or drop their price estimation.
    """
    peak = ["june", "july", "august", "december"]
    not_peak = ["january", "february", "march", "april", "may", "september", "october", "november"]

    if month.lower() in peak:
        return 1.4
    elif month.lower() in not_peak:
        return 0.75
    else:
        return 1 #baseline

def get_duration():
    duration = input("Enter trip duration in days: ")
    while not duration.isdigit():
        print("Please enter a valid number.")
        duration = input("Enter trip duration in days: ")
    return int(duration)

def estimate_cost(destination, month, duration):
    region = get_region(destination)
    base_price = get_price(region)
    total = (base_price * get_seasonality(month)) + (duration * 5) #$5 per travel day for easily accessible booking
    return round(total, 2)

def single_trip():
    destination = input("Enter your destination country:")
    month = input("Enter your travel month:")
    duration = get_duration()
    cost = estimate_cost(destination, month, duration)
    print(f"Estimated cost for a trip to {destination} in {month} for {duration} days is ${cost}")

def compare_trips():
    """
    This function allows for users to compare the cost of more than one trip to see which is more cost effective.
    """
    destinations = ["", "", ""]
    months = ["", "", ""]
    durations = [0, 0, 0]
    costs = [0, 0, 0]

    for i in range(3):
        print(f"Trip {i + 1}:")
        destinations[i] = input("Enter your destination country:")
        months[i] = input("Enter your travel month:")
        durations[i] = get_duration()
        costs[i] = estimate_cost(destinations[i], months[i], durations[i])
        
    print("\nTrip Comparisons:")
    for i in range(3):
        print(f"Trip {i + 1}: Estimated cost for a trip to {destinations[i]} in {months[i]} for {durations[i]} days is ${costs[i]}")

    best_cost = costs[0]
    best_destination = destinations[0]
    for i in range(3):
        if costs[i] < best_cost:
            best_cost = costs[i]
            best_destination = destinations[i]
    print(f"\nThe most cost effective trip is to {best_destination} with an estimated cost of ${best_cost}")

print("Welcome to the Cost Estimator for Flights: An Avid Traveler's Best Friend.")

while True:
    print("1. Single Trip 2. Compare Trips 3. Quit")
    choice = input("Enter your choice (1, 2, or 3):")

    if choice == "1":
        single_trip()
    elif choice == "2":
        compare_trips()
    elif choice == "3":
        print("Thank you for using our platform. Stay safe and enjoy your stay my friend.")
        break