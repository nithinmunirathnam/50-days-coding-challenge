# 🚖 Ola Defect Analysis (String Operations Only)

## 📌 Project Overview

This project simulates a real-world **data cleaning and analysis task** for a ride-hailing platform like Ola.

The goal is to process complaint data provided as a **single string** and perform analysis using **only string operations in Python** (no lists, no pandas, no external libraries).


## 📂 Problem Statement

You are given complaint data in the form of a single string:

```
Ride101-Ramesh-Late Arrival-Bangalore, Ride102-Suresh-rude behavior-Hyderabad, Ride103-Mahesh-Late arrival-Bangalore
```

Your task is to clean and analyze this data using only string methods.


## ⚙️ Tasks Performed

### 1. Data Cleaning

* Convert entire string to lowercase

### 2. Count Total Complaints

* Count number of ride records

### 3. Count "Late Arrival" Issues

* Identify occurrences of "late arrival"

### 4. Bangalore Complaints

* Count complaints from Bangalore

### 5. Extract First Driver Name

* Extract driver name from first record

### 6. Standardize Issue Names

* Replace:

  * `rude behavior` → `rude_behavior`
  * `late arrival` → `late_arrival`

## 🧠 Concepts Used

* String manipulation
* Pattern counting using `.count()`
* String slicing
* `.find()` method
* `.replace()` method
* `.split()` method (minimal usage)

## 🚀 Key Takeaways

* Efficient data analysis can be done using basic string operations
* Helps build strong fundamentals for data preprocessing
* Useful for coding interviews and beginner-level data analytics tasks
