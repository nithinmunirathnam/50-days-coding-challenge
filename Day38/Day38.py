def calculate_premium(age, policy_type, claims):

    premiums = {
        "health": 8000,
        "vehicle": 12000,
        "life": 10000
    }

    if policy_type not in premiums:
        return None

    premium = premiums[policy_type]

    if age < 25:
        premium += premium * 0.20
    elif age > 45:
        premium += premium * 0.15

    if claims > 2:
        premium += premium * 0.25
    elif claims == 0:
        premium -= premium * 0.10

    return premium


name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
policy_type = input("Enter Policy Type (health/vehicle/life): ").lower()
claims = int(input("Enter Number of Claims: "))


final_premium = calculate_premium(age, policy_type, claims)


if final_premium is None:
    print("Error: Invalid policy type entered.")
else:
    base_premiums = {
        "health": 8000,
        "vehicle": 12000,
        "life": 10000
    }

    print("\n----- Insurance Premium Details -----")
    print("Customer Name:", name)
    print("Policy Type:", policy_type)
    print("Base Premium: ₹", base_premiums[policy_type])
    print("Final Premium: ₹", round(final_premium))