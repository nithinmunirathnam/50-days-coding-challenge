s = "abcabcbb"

char_set = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)

print("Longest Substring Length:", max_length)

lst = [1, 2, 2, 3, 4, 3, 5]

result = []
for num in lst:
    if num not in result:
        result.append(num)

print("List after removing duplicates:", result)

tup = (10, 5, 20, 8)

print("Maximum:", max(tup))
print("Minimum:", min(tup))

s = "programming"

freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequency:", freq)

words = ["cat", "dog", "elephant", "bat", "tiger"]

grouped = {}

for word in words:
    length = len(word)
    if length not in grouped:
        grouped[length] = []
    grouped[length].append(word)

print("Grouped Words:", grouped)