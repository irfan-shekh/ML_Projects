# Artist Sculpture Cost Prediction

A production-ready Django web application that uses machine learning to predict the cost of custom sculptures and artwork based on various features.

## 🎨 Features

- **ML-Powered Predictions**: Uses a Random Forest model with 84.1% test accuracy
- **Modern UI**: Responsive, professional interface with smooth animations
- **Real-time Processing**: Instant cost predictions based on 15 features
- **Form Validation**: Comprehensive input validation with user-friendly error messages
- **Sample Data**: One-click sample data for easy testing
- **Mobile Responsive**: Works seamlessly on all device sizes

## 📊 Model Performance

- **Training Accuracy**: 97.53%
- **Test Accuracy**: 84.14%
- **Model Type**: Random Forest Regressor
- **Features**: 15 input parameters
- **Training Samples**: 2,765 sculptures

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Artist Sculpture Cost prediction/mysite"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:8000`

## 📋 Input Features

The model uses the following 15 features for prediction:

### Required Fields
- **Artist Name**: Name of the artist (for identification)
- **Artist Reputation**: Float value between 0.0 - 1.0
- **Height**: Sculpture height in meters
- **Width**: Sculpture width in meters  
- **Weight**: Weight in grams
- **Material**: Material type (Aluminium, Brass, Bronze, Clay, Marble, Stone, Wood)
- **Base Sculpture Price**: Base price in USD
- **Base Shipping Price**: Shipping cost in USD
- **Waiting Time**: Days between scheduled and delivery date

### Optional Fields
- **International Shipping**: Yes/No
- **Express Shipment**: Yes/No
- **Installation Included**: Yes/No
- **Transport Method**: Airways/Roadways/Waterways
- **Fragile Item**: Yes/No
- **Customer Type**: Wealthy/Working Class
- **Remote Location**: Yes/No

## 🎯 Usage Examples

### Sample Data 1: Bronze Sculpture
```
Artist Name: John Smith
Reputation: 0.75
Height: 1.8m
Width: 1.2m
Weight: 8500g
Material: Bronze
Base Price: $2500
Shipping: $150
Express Shipment: Yes
Installation: Yes
Transport: Airways
Fragile: Yes
Customer: Wealthy
Remote: No
Waiting: 7 days
```

### Sample Data 2: Marble Statue
```
Artist Name: Maria Garcia
Reputation: 0.85
Height: 2.1m
Width: 0.9m
Weight: 12000g
Material: Marble
Base Price: $3500
Shipping: $200
Express Shipment: No
Installation: Yes
Transport: Roadways
Fragile: Yes
Customer: Wealthy
Remote: Yes
Waiting: 14 days
```

## 🏗️ Project Structure

```
Artist Sculpture Cost prediction/
├── mysite/
│   ├── mysite/
│   │   ├── __init__.py
│   │   ├── settings.py          # Django settings
│   │   ├── urls.py            # Main URL configuration
│   │   ├── wsgi.py            # WSGI configuration
│   │   └── asgi.py            # ASGI configuration
│   ├── polls/
│   │   ├── __init__.py
│   │   ├── views.py           # Main prediction view
│   │   ├── urls.py            # App URL configuration
│   │   ├── models.py          # Database models
│   │   ├── admin.py           # Django admin
│   │   ├── apps.py            # App configuration
│   │   ├── templates/
│   │   │   └── index.html    # Main template
│   │   └── Artist.pickle      # Trained ML model
│   ├── static/
│   │   └── css/
│   │       └── styles.css    # Modern CSS styles
│   ├── manage.py              # Django management script
│   └── requirements.txt       # Python dependencies
├── Artist Sculpture Cost.csv   # Training dataset
├── ArtistSculpture.ipynb     # Jupyter notebook (model training)
└── README.md                 # This file
```

## 🔧 Technical Details

### Machine Learning Pipeline

1. **Data Preprocessing**
   - Removed null values and negative costs
   - Applied outlier removal (Height < 53m, Width < 22m, Price < $4000, Cost < $25000)
   - Label encoded categorical variables
   - Calculated waiting time from dates

2. **Feature Engineering**
   - Created 'Waiting time' feature from scheduled/delivery dates
   - Label encoded materials and categorical variables
   - Removed unnecessary columns (Customer ID, Artist Name, Location)

3. **Model Training**
   - Algorithm: Random Forest Regressor
   - Estimators: 200
   - Test split: 80/20
   - Random state: 42

### Web Application Architecture

- **Backend**: Django 4.2.7 with Python 3.8+
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **ML Framework**: scikit-learn 1.3.0
- **Data Processing**: pandas 2.0.3, numpy 1.24.3
- **Model Format**: Pickle (.pickle)

## 🐛 Troubleshooting

### Common Issues

1. **Server won't start**
   ```bash
   # Check Django installation
   python -c "import django; print(django.get_version())"
   
   # Check dependencies
   pip list
   ```

2. **Model loading error**
   - Ensure `Artist.pickle` exists in `polls/` directory
   - Check file permissions

3. **Static files not loading**
   ```bash
   # Collect static files
   python manage.py collectstatic
   ```

4. **Prediction errors**
   - Verify all required fields are filled
   - Check numeric input ranges
   - Ensure material is selected

### Error Messages

- **"Please enter the artist name"**: Artist name field is empty
- **"Artist reputation must be between 0 and 1"**: Reputation value out of range
- **"Height, width, and weight must be positive numbers"**: Invalid dimension values
- **"Model file not found"**: ML model file missing or corrupted

## 📱 Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🚀 Deployment

### Production Settings

1. **Update `settings.py`**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

2. **Environment Variables**:
   ```bash
   export SECRET_KEY='your-secret-key'
   export DEBUG=False
   ```

3. **Static Files**:
   ```bash
   python manage.py collectstatic --noinput
   ```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 📈 Model Improvement

### Potential Enhancements

1. **Feature Engineering**
   - Add artist historical pricing data
   - Include market demand indicators
   - Add material cost fluctuations

2. **Model Optimization**
   - Hyperparameter tuning
   - Ensemble methods
   - Neural network approaches

3. **Data Quality**
   - Increase training dataset size
   - Add more diverse materials
   - Include regional pricing variations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is for educational and demonstration purposes.

## 📞 Support

For issues and questions:
- Check the troubleshooting section
- Review the error messages
- Verify input data formats

---

**Built with ❤️ using Django, scikit-learn, and modern web technologies**
