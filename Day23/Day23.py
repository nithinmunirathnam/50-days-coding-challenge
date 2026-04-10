data = "Ride101-Ramesh-Late Arrival-Bangalore, Ride102-Suresh-rude behavior-Hyderabad, Ride103-Mahesh-Late arrival-Bangalore"

data = data.lower()
print("cleaned data: ",data)

total_complaints=data.count("ride")
print("total_complaints: ",total_complaints)

late_arrivals=data.count("late arrival")
print("late_arrivals: ",late_arrivals)

Count_bangalore=data.count("bangalore")
print("bangalore appearance: ",Count_bangalore)

first_record=data[:data.find(",")]
first_name=first_record.split("-")[1]
print("First driver name: ",first_name)

data=data.replace("rude behaviour","rude_behaviour")
data=data.replace("late arrival","late_arrival")
print("Standardized Data: ",data)