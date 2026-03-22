# 📊 Quality Control Dashboard – Power BI Project

## 📌 Overview

This project presents a **Quality Control Dashboard** built using Power BI to analyze production data and identify defect patterns. The dashboard helps monitor product quality, track defect trends, and evaluate performance across production lines and inspectors.

## 🎯 Objectives

* Calculate and visualize the **Overall Defect Rate**
* Identify **Top Defective Products**
* Analyze **Defect Trends Over Time**
* Evaluate defects by **Production Line and Inspector**
* Enable **interactive filtering** using date slicers


## 📂 Dataset Description

### 🔹 Production Data

* **Date** – Production date
* **ProductID** – Unique product identifier
* **BatchID** – Batch reference
* **Status** – Pass / Fail

### 🔹 Batch Data

* **BatchID** – Unique batch identifier
* **ProductionLine** – Manufacturing line
* **InspectorName** – Quality inspector


## 🔗 Data Modeling

* Established a **Many-to-One relationship** between:

* Followed **star schema approach** (no table merging)

## 📊 Dashboard Features

### 🔹 KPI Cards

* Total Items
* Defective Items
* Overall Defect Rate
* Daily Defect Rate

### 🔹 Visualizations

* 📌 **Top 5 Products by Defect Count** (Bar Chart)
* 📈 **Defect Rate Trend Over Time** (Line Chart)
* 📋 **Defects by Production Line & Inspector** (Matrix)

### 🔹 Interactivity

* 📅 **Date Slicer** to filter all visuals dynamically


## 🧠 Key Insights

* The overall defect rate is approximately **6%**, indicating stable production quality.
* **Product 3** has the highest defect count and requires further investigation.
* Certain inspectors are associated with more defects, highlighting potential quality gaps.
* **Line C** shows relatively higher defect occurrences.
* A slight upward trend in defects is observed toward the later dates.


## 🛠 Tools Used

* Power BI Desktop
* DAX (Data Analysis Expressions)
* Data Modeling (Star Schema)

## 📌 Conclusion

This dashboard provides actionable insights into product quality and helps identify areas for process improvement, enabling better decision-making in manufacturing operations.

![Dashboard preview](https://github.com/nithinmunirathnam/50-days-coding-challenge/blob/c927b5c9aa6a91784f6135cd3ef474edd3a1f252/Day7/Day7.png)


