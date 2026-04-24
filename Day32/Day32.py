num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

n = int(input("Enter N: "))

i = 1
while i <= n:
    print(i, end=" ")
    i += 1

    n = int(input("Enter N: "))

    i = 1
    total = 0

    while i <= n:
        total += i
        i += 1

    print("Sum:", total)

    correct_password = "1234"
    attempts = 0

    while attempts < 3:
        password = input("Enter password: ")

        if password == correct_password:
            print("Access Granted")
            break
        else:
            print("Wrong Password")
            attempts += 1

    if attempts == 3:
        print("Access Denied")

num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1