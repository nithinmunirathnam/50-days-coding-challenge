# 🏦 Banking Customer & Transaction Analytics Dashboard

## 📌 Project Overview

This project analyzes customer behavior, transaction patterns, and loan performance using **Power BI**. The dashboard provides interactive insights to help management make data-driven decisions.


## 📊 Dataset Description

The dataset contains banking-related information including:

* Customer_ID – Unique customer identifier
* Customer_Name – Customer name
* Age – Customer age
* Gender – Male/Female
* Account_Type – Savings, Current, Fixed Deposit, Loan
* Balance – Account balance
* Transaction_Date – Date of transaction
* Transaction_Type – Credit/Debit
* Transaction_Amount – Transaction value
* Loan_Status – Active, Closed, Default

## 🧹 Data Cleaning & Transformation

* Removed duplicate records
* Handled missing values (Loan_Status filled as *Unknown*)
* Created **Net Transaction Impact** (Credit = +, Debit = –)
* Created **Age Groups**:

  * 18–30 → Young
  * 31–50 → Adult
  * 51+ → Senior
* Standardized Account Types (SAV, CUR, FD, LN)


## 📐 Data Modeling

* Used single-table model
* Created **Calendar Table** for time-based analysis
* Built date hierarchy (Year → Quarter → Month)


## 🧮 DAX Measures

* Total Deposits
* Total Withdrawals
* Net Balance Growth
* Average Account Balance
* Loan Default Rate %
* Monthly Transaction Volume
* Customer Profitability Score


## 📊 Dashboard Features

### 🔹 Customer Overview

* Customer distribution by Age Group & Gender
* Total Customers KPI
* Conditional formatting for low balance accounts

### 🔹 Transaction Analysis

* Monthly transaction trend (Line chart)
* Heatmap (Day vs Hour analysis)
* Drill-through for customer transaction details

### 🔹 Loan Performance

* Loan status distribution (Pie chart)
* Loan Default Rate KPI (with color indicators)
* What-if parameter for interest rate simulation

### 🔹 Top Customers

* Top 10 customers by transactions
* Conditional formatting (highlight top performers)
* Tooltip showing average balance


## 🚀 Advanced Features Used

✔ Conditional Formatting
✔ Drill-through
✔ Tooltips
✔ What-if Parameters
✔ Slicers
✔ Date Hierarchy

## 📈 Key Insights

* Majority of customers belong to the **31–50 age group**
* Loan Default Rate is **~10.4%**, indicating moderate risk
* Transactions show **clear time-based patterns**
* Peak activity occurs during specific hours and days


## 🛠 Tools Used

* Power BI
* Power Query
* DAX
![Dashboard preview](https://github.com/nithinmunirathnam/50-days-coding-challenge/blob/96668f4f7d9969a0b3f25041f7a0b12cb16d0686/Day6/Day6.png)

## 📌 Conclusion

This dashboard provides a comprehensive view of customer behavior, financial activity, and loan risk, enabling better decision-making in the banking sector.


