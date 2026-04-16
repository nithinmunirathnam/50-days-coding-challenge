trips = (
    (101, "Bangalore", 12.5, 250),
    (102, "Hyderabad", 8.0, 180),
    (103, "Bangalore", 15.2, 300),
    (104, "Chennai", 5.5, 120),
    (105, "Bangalore", 7.8, 200)
)

print("Total Trips:", len(trips))

bangalore_trips = sum(1 for trip in trips if trip[1] == "Bangalore")
print("Bangalore Trips:", bangalore_trips)

total_revenue = sum(trip[3] for trip in trips)
print("Total Revenue:", total_revenue)

print("High Distance Trips:")
for trip in trips:
    if trip[2] > 10:
        print(trip)
highest_fare_trip = max(trips, key=lambda x: x[3])
print("Highest Fare Trip:", highest_fare_trip)

bangalore_fares = [trip[3] for trip in trips if trip[1] == "Bangalore"]
avg_fare = sum(bangalore_fares) / len(bangalore_fares)
print("Average Fare (Bangalore):", avg_fare)