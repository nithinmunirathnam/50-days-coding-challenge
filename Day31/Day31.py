# Smart Expense Analyzer

# Given data
salary = 50000
rent = 12000
food = 8000
transport = 3000
entertainment = 4000

# Task 1: Total Expenses
total_expenses = rent + food + transport + entertainment
print("Total Expenses:", total_expenses)

# Task 2: Savings Calculation
savings = salary - total_expenses
print("Savings:", savings)

# Task 3: Expense Comparison
print("Is rent greater than food?", rent > food)
print("Is transport less than entertainment?", transport < entertainment)

# Task 4: Financial Condition Check
if savings > 10000:
    print("Financial Status: Good Saving")
elif savings >= 5000 and savings <= 10000:
    print("Financial Status: Average Saving")
else:
    print("Financial Status: Low Saving")

# Task 5: Bonus Update
salary += salary * 0.10
print("Updated Salary after 10% bonus:", salary)