

ids = [101, 102, 101, 103, 102, 104]

unique_ids = []
seen = set()

for i in ids:
    if i not in seen:
        unique_ids.append(i)
        seen.add(i)

print(unique_ids)



products = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for item in products:
    count[item] = count.get(item, 0) + 1

print(count)


marks = {"A": 85, "B": 92, "C": 88}

top_student = max(marks, key=marks.get)

print(top_student)


skills1 = ["Python", "SQL", "Excel"]
skills2 = ["SQL", "Power BI", "Python"]

common = list(set(skills1).intersection(set(skills2)))

print(common)

# Sort products by price

prices = {"apple": 50, "banana": 20, "orange": 30}

sorted_prices = sorted(prices.items(), key=lambda x: x[1])

print(sorted_prices)