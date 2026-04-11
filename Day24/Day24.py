rides = (
    (101, "Ravi", "Bangalore", 250, 4.5),
    (102, "Anjali", "Hyderabad", 180, 4.2),
    (103, "Kiran", "Bangalore", 300, 4.8),
    (104, "Meena", "Chennai", 220, 4.0),
    (105, "Arjun", "Bangalore", 150, 3.9)
)
print(rides)

Total_rides=len("rides")
print("Total rides: ",Total_rides)

for ride in rides:
    if ride[2]=="Bangalore":
        print (ride)

total_revenue_bangalore = sum(ride[3] for ride in rides if ride[2] == "Bangalore")
print("\nTotal Revenue from Bangalore:", total_revenue_bangalore)

highest_rated = max(rides, key=lambda x: x[4])
print("\nHighest Rated Driver:", highest_rated)

city_ratings = {}
city_counts = {}

for ride in rides:
    city = ride[2]
    rating = ride[4]

    if city in city_ratings:
        city_ratings[city] += rating
        city_counts[city] += 1
    else:
        city_ratings[city] = rating
        city_counts[city] = 1


average_ratings = {}
for city in city_ratings:
    average_ratings[city] = round(city_ratings[city] / city_counts[city], 1)

print("\nAverage Rating per City:")
print(average_ratings)