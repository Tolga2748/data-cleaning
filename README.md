# ☕ Cafe Sales Data Cleaning & Exploration Project

This project focuses on cleaning and exploring a real-world cafe sales dataset. The project consists of two main Python scripts, and works with both raw and cleaned data files.

---

## 📁 Project Structure

cafe_sales_project/
├── data_cleaning.py # Cleans the raw cafe sales data
├── data_exploration.py # Explores and analyzes the cleaned data
├── dirty_cafe_sales.csv # Original dataset (contains dirty data)
├── cleaned_cafe_sales.csv # Cleaned dataset after processing
└── README.md # Project description



---

## 🔧 1. Data Cleaning (`data_cleaning.py`)

This script performs the following tasks:

- Reads the raw CSV data (`dirty_cafe_sales.csv`)
- Checks for missing values
- Fixes formatting issues (date, capitalization, etc.)
- Standardizes column names
- Removes duplicates
- Exports the cleaned data to `cleaned_cafe_sales.csv`

---

## 📊 2. Data Exploration (`data_exploration.py`)

This script includes:

- Summary of the dataset
- Visualization of trends (optional)
- Insights into most sold items, busiest hours, etc.
- Statistics about revenue, item counts, and customer behavior

---

## 📈 Dataset Overview

- **dirty_cafe_sales.csv**: A CSV file containing raw cafe sales data with missing values, inconsistent formats, and duplicates.
- **cleaned_cafe_sales.csv**: The cleaned version of the dataset ready for analysis.

---

## 💻 How to Run

1. Make sure you have Python and `pandas` installed:
   ```bash
   pip install pandas

Run the cleaning script:

python data_cleaning.py

Then run the exploration script:

python data_exploration.py

Requirements
Python 3.x
pandas

Author

Tolga Agaçkesen
Project: Cafe Sales Data Cleaning & Analysis
For learning and practice in Data Science & Pytho
