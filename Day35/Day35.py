nested = [[1, 2], [3, 4], [5]]

flat_list = [item for sublist in nested for item in sublist]

print(flat_list)



s1 = "listen"
s2 = "silent"

result = sorted(s1) == sorted(s2)

print(result)



nums = [1, 2, 4, 5]

full_set = set(range(1, 6))
missing = full_set - set(nums)

print(missing.pop())

# Group words by their first letter

words = ["apple", "ant", "banana", "bat"]

grouped = {}

for word in words:
    grouped.setdefault(word[0], []).append(word)

print(grouped)



data = {"a": 1, "b": None, "c": 3, "d": None}

filtered_data = {k: v for k, v in data.items() if v is not None}

print(filtered_data)