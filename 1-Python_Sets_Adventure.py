# Task 1: Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

intersection = our_routes.intersection(competitor_routes)
print(f"Destinations both airlines fly to: {intersection}")

difference = our_routes.difference(competitor_routes)
print(f"Destinations unique to our airline: {difference}")

symmetric_difference = our_routes.symmetric_difference(competitor_routes)
print(f"Destinations neither airline shares: {symmetric_difference}")