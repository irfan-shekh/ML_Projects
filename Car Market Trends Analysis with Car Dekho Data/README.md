# Used Car Price Exploratory Data Analysis (EDA)

An exploratory data analysis (EDA) project on the **CarDekho Used Car Dataset** using Python, pandas, seaborn, and matplotlib. This repository contains the analysis notebook and dataset to inspect vehicle pricing factors, market distributions, fuel types, and ownership patterns.

---

## Repository Files

- `Car_Dekho_Data.ipynb` – Jupyter / Google Colab notebook containing all data loading, inspections, statistical summaries, and visualization plots.
- `Car Dekho Data.csv` – Raw dataset containing 301 used vehicle listings.
- `README.md` – Project documentation.

---

## Dataset Overview

The dataset contains **301 records** and **9 columns** with **0 missing values**:

| Feature | Type | Description |
| :--- | :--- | :--- |
| `Car_Name` | Categorical | Brand/model of the car (98 unique models) |
| `Year` | Numerical | Year of manufacture (2003 – 2018)[cite: 1] |
| `Selling_Price` | Numerical | Selling price (in Lakhs ₹)[cite: 1] |
| `Present_Price` | Numerical | Current ex-showroom price (in Lakhs ₹)[cite: 1] |
| `Kms_Driven` | Numerical | Distance driven in kilometers[cite: 1] |
| `Fuel_Type` | Categorical | Fuel type: `Petrol`, `Diesel`, or `CNG`[cite: 1] |
| `Seller_Type` | Categorical | Seller category: `Dealer` or `Individual`[cite: 1] |
| `Transmission` | Categorical | Transmission type: `Manual` or `Automatic`[cite: 1] |
| `Owner` | Numerical | Number of previous owners (0, 1, or 3)[cite: 1] |

---

## Key Analysis & Findings

- **Data Completeness:** No null or NaN values found across all 301 rows[cite: 1].
- **Fuel Distribution:**
  - **Petrol:** 79.4% (239 vehicles)[cite: 1]
  - **Diesel:** 19.9% (60 vehicles)[cite: 1]
  - **CNG:** 0.7% (2 vehicles)[cite: 1]
- **Most Listed Vehicles:** The most frequent cars in the dataset are the **City** (26), **Corolla Altis** (16), **Verna** (14), **Fortuner** (11), and **Brio** (10)[cite: 1].
- **Price Statistics:**
  - **Selling Price:** Average is **4.66 Lakhs**, ranging from **0.10 Lakhs** to **35.00 Lakhs**[cite: 1].
  - **Present Price:** Average is **7.63 Lakhs**, ranging from **0.32 Lakhs** to **92.60 Lakhs**[cite: 1].
- **Mileage (`Kms_Driven`):** Average distance driven is **~36,947 km**, with a minimum of **500 km** and a maximum of **500,000 km**[cite: 1].

---

## How to Run

1. Clone or download this repository:
   ```bash
   git clone [[https://github.com/](https://github.com/)<your-username>/<your-repo-name](https://github.com/irfan-shekh/ML_Projects/tree/main/Car%20Market%20Trends%20Analysis%20with%20Car%20Dekho%20Data)>.git
   cd <ML_Projects>
