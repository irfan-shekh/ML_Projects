# Seasonal Agriculture Performance Analysis

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Project](https://img.shields.io/badge/VOIS%20AICTE-Major%20Project-green.svg)](https://aicte-india.org/)

An end-to-end data analytics project examining agricultural performance across **Kharif**, **Rabi**, and **Zaid** seasons. This project analyzes environmental factors, resource utilization, crop yields, water productivity, and financial outcomes across 4,000 farm profiles.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset Architecture](#-dataset-architecture)
- [Repository Structure](#-repository-structure)
- [Methodology & Workflow](#-methodology--workflow)
- [Visual Insights & Analysis](#-visual-insights--analysis)
- [Key Findings](#-key-findings)
- [Evidence-Based Recommendations](#-evidence-based-recommendations)
- [Setup & Execution](#-setup--execution)

---

## 🌾 Project Overview

Agricultural outcomes vary substantially across seasonal cycles due to changing rainfall patterns, ambient temperatures, soil moisture, and resource requirements. 

This project explores these seasonal dynamics using Python, rigorous exploratory data analysis (EDA), and statistical hypothesis testing to identify productivity bottlenecks and provide data-backed agricultural planning frameworks.

---

## 📊 Dataset Architecture

The project analyzes `seasonal_agriculture_performance_dataset.csv`, consisting of **4,000 records** and **28 features**:

| Domain | Key Attributes | Analytical Purpose |
| :--- | :--- | :--- |
| **Identifiers & Time** | `Farm_ID`, `State`, `District`, `Crop`, `Season` | Stratification across Kharif (1,779), Rabi (1,627), and Zaid (594). |
| **Environmental Conditions** | `Rainfall_mm`, `Avg_Temperature_C`, `Humidity_pct`, `Sunlight_Hours_Day`, `Soil_pH`, `Soil_Moisture_pct` | Characterizing climatic baseline and soil conditions. |
| **Nutrients & Inputs** | `Nitrogen_kg_ha`, `Phosphorus_kg_ha`, `Potassium_kg_ha`, `Fertilizer_kg_ha`, `Pesticide_Litre_ha`, `Seed_Quality_Score` | Evaluating input intensity and fertilizer management. |
| **Water Management** | `Irrigation_Method`, `Water_Used_m3`, `Water_Efficiency_t_per_1000m3` | Assessing irrigation efficiency (Drip, Flood, Rainfed, Sprinkler). |
| **Economic Performance** | `Yield_Tonnes_Ha`, `Production_Tonnes`, `Market_Price_INR_Tonne`, `Total_Cost_INR`, `Revenue_INR`, `Profit_INR`, `Disease_Pest_Risk_pct` | Quantifying yield productivity, margins, and pest vulnerability. |

---

## 📂 Repository Structure

```text
.
├── seasonal_agriculture_performance_analysis.ipynb  # End-to-end Jupyter analysis notebook
├── seasonal_agriculture_performance_dataset.csv     # Primary dataset (4,000 rows)
└── README.md                                        # Project documentation
