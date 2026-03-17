# 📊 Student Performance Analysis Dashboard

## 📌 Project Overview

* This project analyzes student data to understand how different factors affect academic performance.
* Focus areas include screen time, study hours, extracurricular activities, and age.
* The goal is to identify patterns and present insights using an interactive dashboard.


## 📂 Dataset Details

* Total Records: 200 students
* Features included:

  * Age (13–17 years)
  * Gender
  * Study Hours
  * Screen Time (hours/day)
  * Test Scores
  * Extracurricular Activity Hours


## 🧹 Data Preprocessing

* Removed duplicate records
* Handled missing values using average (mean) for numerical columns
* Retained original 0 values where present in raw data
* Ensured correct data types (numeric/text)
* Cleaned unwanted/extra columns


## ➕ New Columns Created

* **Screen_Time_Category**

  * Low (0–2 hrs)
  * Moderate (2–4 hrs)
  * High (4–6 hrs)
  * Extremely High (6+ hrs)

* **Performance_Category**

  * Excellent (≥90)
  * Very Good (80–89)
  * Good (70–79)
  * Average (60–69)
  * Poor (<60)


## 📊 Analysis Performed

* Screen Time Category vs Average Test Scores
* Screen Time vs Extracurricular Activity Trends
* Age vs Test Score Analysis
* Scatter Plot: Screen Time vs Test Scores (correlation check)


## 📈 Dashboard Features

* KPI Cards:

  * Total Students
  * Class Average
  * Max & Min Marks
  * Average Screen Time

* Charts Used:

  * Column Chart
  * Line Chart
  * Scatter Plot with Trendline

* Interactive Filters (Slicers):

  * Age
  * Screen Time Category
  * Performance Category

## 🧠 Key Insights

* No strong correlation between screen time and test scores
* Students with higher screen time show slightly higher extracurricular activity
* Study habits influence performance more than screen usage
* Age has minimal impact on academic performance
* Overall student performance is moderate with an average score of ~70.9

## 🏆 Conclusion

* Screen time alone does not negatively affect academic performance
* Balanced engagement in academics and extracurricular activities is observed
* Study hours play a key role in improving student outcomes


## 🛠 Tools Used

* Microsoft Excel
* Pivot Tables
* Data Cleaning Techniques
* Data Visualization (Charts & Dashboard)


## 📎 Project Outcome

* Developed a clean, interactive dashboard
* Derived meaningful insights from student data
* Demonstrated data analysis and visualization skills


![Dashboard Preview](https://github.com/nithinmunirathnam/50-days-coding-challenge/blob/06790db921d5712284c95b2370c112b5535668b5/Day_2/Dashboard_image.png)
