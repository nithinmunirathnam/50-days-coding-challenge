# 📊 Customer Segmentation Using SQL

## 📌 Project Overview

This project focuses on analyzing customer data and segmenting customers based on their spending behavior using basic SQL operations.

The goal is to practice and demonstrate core SQL concepts such as filtering, sorting, aggregation, grouping, and segmentation using real-world-like data.


## 🗂 Dataset Information

### Table: `customers`

| Column Name      | Data Type     | Description                 |
| ---------------- | ------------- | --------------------------- |
| customer_id      | INT           | Unique ID for each customer |
| customer_name    | VARCHAR(50)   | Name of the customer        |
| city             | VARCHAR(50)   | City of the customer        |
| age              | INT           | Age of the customer         |
| total_spent      | DECIMAL(10,2) | Total amount spent          |
| number_of_orders | INT           | Number of orders placed     |


## 🛠 SQL Concepts Used

* SELECT
* WHERE
* ORDER BY
* GROUP BY
* CASE
* HAVING
* Aggregate Functions (SUM, AVG, COUNT)

## 📈 Tasks Performed

### 🔹 Level 1: Basic Filtering

* Retrieved customers from a specific city
* Filtered customers based on spending
* Selected customers within an age range

### 🔹 Level 2: Sorting & Aggregation

* Sorted customers by total spending
* Calculated total revenue
* Found average spending per customer

### 🔹 Level 3: Grouping

* Calculated total spending per city
* Counted number of customers in each city

### 🔹 Level 4: Customer Segmentation (Core Task)

Customers were segmented into:

* **High Value Customers** → Spending > 50,000
* **Medium Value Customers** → Spending between 20,000 and 50,000
* **Low Value Customers** → Spending < 20,000

### 🔹 Level 5: Advanced Filtering

* Identified cities with total spending greater than 50,000 using HAVING clause


## 📊 Key Insights

* Bangalore and Mumbai contribute significantly to total revenue
* High-value customers form a smaller group but generate maximum revenue
* Low-value customers are more in number but contribute less individually
* Customer segmentation helps businesses target the right audience

3. Run the SQL queries provided in this project.

## 🎯 Learning Outcomes

* Strong understanding of SQL basics
* Ability to perform data analysis using SQL
* Hands-on experience in customer segmentation
* Improved problem-solving skills for real-world datasets


## 📌 Conclusion

This project demonstrates how SQL can be effectively used for customer analysis and segmentation. It lays a strong foundation for advanced analytics and data-driven decision-making.

