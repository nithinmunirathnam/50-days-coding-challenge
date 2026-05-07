## 📌 Overview
This project is a beginner-friendly Python application that calculates the annual insurance premium for customers based on their age, policy type, and claim history. It helps learners understand how conditional statements, functions, and arithmetic operations are used in real-world applications.

---

## 🎯 Objective
To practice Python programming concepts by building an Insurance Premium Calculator using:

- Variables
- Input and Output
- Conditional Statements
- Functions
- Arithmetic Operations
- Validation Techniques

---

## ❓ Questions

### 1. Customer Information
Ask the user to enter:
- Customer Name
- Age
- Policy Type (`health`, `vehicle`, or `life`)
- Number of Claims Made

### 2. Base Premium
Assign the premium based on policy type:

| Policy Type | Base Premium |
|-------------|--------------|
| Health      | ₹8,000       |
| Vehicle     | ₹12,000      |
| Life        | ₹10,000      |

### 3. Age-Based Premium Adjustment
- If age is below 25 → Add 20%
- If age is between 25 and 45 → No change
- If age is above 45 → Add 15%

### 4. Claim-Based Adjustment
- If claims are more than 2 → Add 25%
- If claims are 0 → Give 10% discount

### 5. Validation
Display an error message if the user enters an invalid policy type.

### 6. Function Creation
Create a function:

calculate_premium(age, policy_type, claims)

The function should return the final premium amount.

---

## 🧾 Conclusion
This project helps beginners understand how real-world applications use conditions, functions, and calculations in programming. By developing this Insurance Premium Calculator, learners improve their logical thinking and gain practical experience with core Python concepts such as conditional statements, functions, arithmetic operations, and validation techniques.
