# 🌾 Farm Yield Optimization (SQL Project)

## 📌 Project Overview

This project focuses on analyzing agricultural data to optimize crop yield and resource utilization. Using SQL, we explore relationships between crop yield, irrigation, soil type, weather conditions, and farmer performance.

The objective is to derive actionable insights that help improve farm productivity and efficient water usage.


## 🗂️ Database Schema

The project consists of four tables:

### 👨‍🌾 farmers

* farmer_id (Primary Key)
* first_name
* last_name
* email
* hire_date

### 🌱 plots

* plot_id (Primary Key)
* plot_name
* farmer_id (Foreign Key)
* crop_type
* soil_type

### 🌾 yields

* yield_id (Primary Key)
* plot_id (Foreign Key)
* harvest_date
* yield_kg
* weather_condition

### 💧 irrigation_logs

* log_id (Primary Key)
* plot_id (Foreign Key)
* irrigation_date
* water_amount_liters

## 🔍 Key Analysis Performed

### 📊 1. Productivity & Performance

* Identified top 3 most productive plots based on average yield
* Calculated total water consumption per plot

### 🌦️ 2. Yield & Environmental Analysis

* Analyzed average yield by crop type and weather condition
* Identified highest-yielding plots for each soil type

### 👨‍🌾 3. Farmer & Resource Management

* Found farmers with lowest average water usage
* Calculated monthly harvest trends (last 12 months)

### 🚀 4. Advanced Analysis

* Identified inefficient plots:

  * Low yield compared to crop average
  * High water usage compared to crop average

## 🛠️ SQL Concepts Used

* SELECT, WHERE, GROUP BY, ORDER BY
* Aggregate Functions (SUM, AVG, MAX, COUNT)
* JOINs (INNER JOIN)
* Subqueries
* Window Functions (RANK)
* Date Functions (TO_CHAR, INTERVAL)

## 📊 Key Insights

* Water usage varies significantly across plots and impacts yield
* Certain crops perform better under specific weather conditions
* Soil type influences productivity
* Some plots consume more water but produce below-average yield (inefficient)

## 📌 Conclusion

This project demonstrates how SQL can be used to analyze agricultural data and support data-driven decision-making. It highlights the importance of optimizing both yield and resource consumption for sustainable farming.
