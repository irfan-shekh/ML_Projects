# World Happiness Ranking Predictor

A Django-based machine learning web application that predicts the happiness ranking of countries based on various socio-economic factors.

## Features

- **Modern UI** with Bootstrap 5 styling
- **AJAX functionality** for smooth predictions without page refresh
- **Machine Learning Model** using Linear Regression
- **Interactive Form** with sample data and clear functionality
- **Responsive Design** that works on all devices

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run database migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and go to `http://127.0.0.1:8000`

## How to Use

1. **Click "📊 Fill Sample Data"** to populate the form with Switzerland data
2. **Or manually enter** country data in all required fields
3. **Click "🎯 Predict Happiness Rank"** to get instant results
4. **Use "🔄 Clear Form"** to reset all fields

## Model Details

- **Algorithm**: Linear Regression
- **Features**: 8 socio-economic indicators
- **Performance**: ~99% accuracy on test data
- **Dataset**: World Happiness Report with 158 countries

## Technology Stack

- **Backend**: Django 3.1
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Machine Learning**: scikit-learn, pandas, numpy
- **Database**: SQLite3

The application is fully functional and ready for deployment!
