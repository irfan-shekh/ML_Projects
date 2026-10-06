# Car Selling Price Prediction

A machine learning project that predicts the selling price of used cars based on various features such as car specifications, usage history, and market conditions.

## 📁 Project Structure

```
car selling price prediction/
├── car_selling_price.ipynb    # Main Jupyter notebook with analysis and model
├── Car details.csv            # Dataset containing car specifications and prices
└── README.md                  # This file
```

## 📊 Dataset

The dataset (`Car details.csv`) contains the following features:

- **name**: Car model name
- **year**: Manufacturing year
- **selling_price**: Target variable - selling price in INR
- **km_driven**: Kilometers driven by the car
- **fuel**: Fuel type (Petrol, Diesel, LPG, etc.)
- **seller_type**: Type of seller (Individual, Dealer, etc.)
- **transmission**: Transmission type (Manual, Automatic)
- **owner**: Number of previous owners
- **mileage**: Fuel efficiency (kmpl or km/kg)
- **engine**: Engine displacement (CC)
- **max_power**: Maximum power output (bhp)
- **torque**: Torque specifications
- **seats**: Number of seats

## 🚀 Project Overview

This project demonstrates:
- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Feature engineering
- Machine learning model training and evaluation
- Price prediction for used cars

## 🛠️ Technologies Used

- **Python**: Programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib/Seaborn**: Data visualization
- **Scikit-learn**: Machine learning algorithms
- **Jupyter Notebook**: Interactive development environment

## 📈 Key Features

- **Data Analysis**: Comprehensive analysis of car features and their impact on selling price
- **Model Training**: Implementation of regression models for price prediction
- **Visualization**: Various plots and charts to understand data patterns
- **Feature Engineering**: Creation of meaningful features from raw data

## 🧠 Model Performance

The notebook includes evaluation metrics such as:
- R-squared (R²) score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## 📋 Requirements

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
```

## 🚀 Getting Started

1. Clone this repository
2. Navigate to the car selling price prediction folder
3. Install required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```
4. Open the Jupyter notebook:
   ```bash
   jupyter notebook "car_selling_price.ipynb"
   ```
5. Run the cells step by step to understand the analysis

## 📊 Results

The model provides predictions for used car prices based on historical data, helping buyers and sellers make informed decisions in the used car market.

## 👨‍💻 Author

**Madhur Yadav**
- Email: madhur.yadav7@gmail.com
- GitHub: madhurkgp

## 📄 License

This project is open source and available under the MIT License.
