# 📊 Customer Orders Analysis using SQL JOINs

## 📌 Project Overview

This project focuses on analyzing customer orders, payments, and spending behavior using SQL JOIN operations. It simulates real-world e-commerce data analysis tasks commonly asked in interviews.


## 🗂️ Database Schema

### 1. Customers Table

* `customer_id` (Primary Key)
* `customer_name`
* `city`

### 2. Orders Table

* `order_id` (Primary Key)
* `customer_id` (Foreign Key)
* `order_date`
* `amount`

### 3. Payments Table

* `payment_id` (Primary Key)
* `order_id` (Foreign Key)
* `payment_status`


## 🎯 Objectives

* Understand and apply SQL JOINs:

  * INNER JOIN
  * LEFT JOIN
  * RIGHT JOIN
* Perform real-world business analysis
* Work with aggregate functions and grouping


## 📊 Tasks Covered

### ✅ Task 1: Customer Orders

Display customers who placed orders along with order details.

### ✅ Task 2: All Customers

Show all customers, including those without orders.

### ✅ Task 3: Invalid Orders

Find orders that do not have a valid customer.

### ✅ Task 4: Order Payment Status

Display order details with payment status (including missing payments).

### ✅ Task 5: Customers Without Orders

Identify customers who never placed any orders.

### ✅ Task 6: Orders Without Payment

Find orders that do not have a payment record.

### ✅ Task 7: Total Spending

Calculate total amount spent by each customer.

### ✅ Task 8: Fully Paid Customers

Identify customers whose all orders are completed.

### ✅ Task 9: Highest Order Per Customer

Find the highest order value for each customer.

### ✅ Task 10: Top Customers

Identify top 2 customers based on total spending.


## 🛠️ SQL Concepts Used

* JOINs (INNER, LEFT)
* GROUP BY
* HAVING
* Aggregate Functions (`SUM`, `MAX`, `COUNT`)
* CASE Statements
* ORDER BY
* NULL Handling


## 📈 Key Insights

* Helps identify high-value customers
* Detects missing or invalid data
* Tracks payment completion status
* Useful for business decision-making


## 💡 Learning Outcome

After completing this project, you will:

* Gain strong understanding of SQL JOINs
* Be able to solve real-world data analysis problems
* Improve your SQL skills for interviews and placements
