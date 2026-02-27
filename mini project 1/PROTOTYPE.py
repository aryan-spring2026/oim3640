# Milestone 1 (Prototype): Cost Estimator for Flights

def get_region(destination):
    """ 
    With the chosen country of travel, a region (continent) is returned to align with the travel plan. If the country or region is not on the platform, the term "unknown" will be showcasd to the user.
    """
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
    """
    Showcases to the user the price of a round trip to the region of their choosing. These prices are derived from the United States mean economy flights.
    """
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

def estimate_cost(destination, month, duration):
    """
    This function calculates the estimate for a round trip flight cost.
    """
    region = get_region(destination)
    base_price = get_price(region)
    flexibility_fee = duration * 5 #$5 per travel day for easily accessible booking

    total = base_price + flexibility_fee
    return total

def display_result(destination, month, duration, cost):
    """
    Displays the trip cost estimate to the user.
    """
    print(f"Estimated cost for a trip to {destination} in {month} for {duration} days is ${cost}")

destination = input("Enter your destination country:")
month = input("Enter your travel month:")
duration = int(input("Enter the duration of your trip in day(s):"))

cost = estimate_cost(destination, month, duration)
display_result(destination, month, duration, cost)