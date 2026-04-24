secret = 7

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too Low")
    elif guess > secret:
        print("Too High")
    else:
        print("You Won!")
        break

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number:", reverse)

num = int(input("Enter a number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits:", count)

sales = [1200, 800, 1500, 400, 2000]

count = 0

print("Sales greater than 1000:")
for s in sales:
    if s > 1000:
        print(s)
        count += 1

print("Count:", count)

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    total += num

print("Total Sum:", total)