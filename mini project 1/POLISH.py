# Milestone 3(Polish): Cost Estimator for Flights

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
    total = (base_price * get_seasonality(month)) + (duration * 5)
    return round(total, 2)

def single_trip():
    destination = input("Enter your destination country: ")
    month = input("Enter your travel month: ")
    duration = get_duration()
    cost = estimate_cost(destination, month, duration)
    print(f"Estimated cost for a trip to {destination} in {month} for {duration} days is ${cost}")

def compare_trips():
    destinations = ["", "", ""]
    months = ["", "", ""]
    durations = [0, 0, 0]
    costs = [0, 0, 0]

    for i in range(3):
        print(f"Trip {i + 1}:")
        destinations[i] = input("Enter your destination country: ")
        months[i] = input("Enter your travel month: ")
        durations[i] = get_duration()
        costs[i] = estimate_cost(destinations[i], months[i], durations[i])

    print("\nCost Comparison:")
    for i in range(3):
        print(f"Trip {i + 1}: {destinations[i]} in {months[i]} for {durations[i]} days - Estimated Cost: ${costs[i]}")

    best_cost = costs[0]
    best_destination = destinations[0]
    for i in range(3):
        if costs[i] < best_cost:
            best_cost = costs[i]
            best_destination = destinations[i]
    print(f"\nThe most cost-effective trip is to {best_destination} with an estimated cost of ${best_cost}.")

def show_help():
    """
    This function allows for users to understand how we calculate the cost of a trip and how to use the platform appropriately.
    """
    print("\nHelp Section:")
    print("This platform provides an estimate for a round trip flight from the United States from a cost perspective.")
    print("For Single Trips, provide your desired destination, month of travel, and duration (in days) in order for us to provide a cost estimate.")
    print("For Trip Comparions, you can compare up to 3 destinations from a side by side perspective in order to find the most cost effective trip for you.")
    print("The price calculation is calculated from an economic class pricing perspective and there are adjustments based on how 'peak' the month you decide to travel.")
    print("June, July, August, and December are 'peak months' and are typically more costly.")
    print("The remaining months are not 'peak months' and are usually provided with a discount for our users.")

def show_banner():
    """
    This function creates a banner for our users and formally introduces them to our platform.
    """
    print("==================================")
    print(" Cost Estimator for Flights ")
    print(" An Avid Traveler's Best Friend ")
    print("==================================") 
    print("Type '3' as your option if you require assistance with respect to the operating system of this platform.\n")

def show_menu():
    """
    This function creates a menu to ensure aesthetics and a more professional, easy to use platform for our users.
    """
    print("1. Single Trip")
    print("2. Compare 3 Trips")
    print("3. Help")
    print("4. Quit")

show_banner()

while True:
    show_menu()
    choice = input("Please select an option (1-4): ")
    
    if choice == '1':
        single_trip()
    elif choice == '2':
        compare_trips()
    elif choice == '3':
        show_help()
    elif choice == '4':
        print("Thank you for using the Cost Estimator for Flights. Safe travels!")
        break
    else:
        print("Invalid option. Please select a valid option (1-4).")