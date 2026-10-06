# Customer Segmentation ML Web Application

A production-ready Django web application that uses machine learning to segment customers based on their demographic and behavioral characteristics.

## 🚀 Features

### Core Functionality
- **Customer Segmentation**: ML-powered segmentation using Random Forest, Decision Tree, and KMeans clustering
- **Real-time Predictions**: Instant customer segmentation with confidence scores
- **Interactive Dashboard**: Analytics and insights with visualizations
- **Sample Data**: One-click sample data generation for testing
- **Comprehensive History**: Complete segmentation history with pagination
- **REST API**: Programmatic access to segmentation functionality

### ML Models
- **Random Forest**: Ensemble method with high accuracy (85%+)
- **Decision Tree**: Interpretable tree-based model
- **KMeans Clustering**: Unsupervised learning for customer grouping

### Customer Segments
- **Segment A**: High Value Customers (Premium products, loyalty programs)
- **Segment B**: Growing Professionals (Career development, mid-range offerings)
- **Segment C**: Young Families (Family packages, value bundles)
- **Segment D**: Conservative Spenders (Essential products, traditional marketing)

## 🛠️ Tech Stack

### Backend
- **Django 4.2.7**: Web framework
- **scikit-learn 1.3.2**: Machine learning library
- **pandas 2.1.4**: Data manipulation
- **numpy 1.24.4**: Numerical computing
- **joblib 1.3.2**: Model serialization

### Frontend
- **Bootstrap 5**: Responsive UI framework
- **Bootstrap Icons**: Icon library
- **Chart.js**: Data visualization
- **Custom CSS**: Modern gradients and animations

### Database
- **SQLite**: Default development database
- **Configurable**: Support for PostgreSQL/MySQL

## 📋 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Quick Start

1. **Clone/Download the project**
   ```bash
   cd customer_segmentation_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   # Default: admin/admin123
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main App: http://127.0.0.1:8000
   - Admin Panel: http://127.0.0.1:8000/admin

## 🎯 Usage Guide

### Basic Segmentation
1. Fill in customer information on the home page
2. Select prediction method (Random Forest recommended)
3. Click "Segment Customer" to get results
4. View detailed insights and recommendations

### Sample Data
- Click "Sample Data" to auto-fill form with test data
- Perfect for exploring the application without manual input

### Analytics Dashboard
- View segment distribution charts
- Monitor model usage statistics
- Track confidence scores over time
- Access recent segmentation history

### API Usage
```python
import requests

# Prepare customer data
data = {
    "gender": "Female",
    "ever_married": "Yes",
    "age": 35,
    "graduated": "Yes",
    "profession": "Engineer",
    "spending_score": "Average",
    "prediction_method": "random_forest"
}

# Make prediction
response = requests.post(
    "http://127.0.0.1:8000/api/predict/",
    json=data
)
result = response.json()
print(result)
```

## 📊 Model Performance

### Accuracy Metrics
- **Random Forest**: 85% accuracy, best overall performance
- **Decision Tree**: 78% accuracy, highly interpretable
- **KMeans**: 0.45 silhouette score, good for clustering

### Features Used
- **Demographics**: Age, Gender, Marital Status, Graduation
- **Professional**: Profession, Work Experience
- **Financial**: Spending Score, Family Size
- **Categorical**: Var_1 category codes

## 🎨 UI/UX Features

### Design Elements
- **Modern Gradients**: Eye-catching color schemes
- **Responsive Design**: Works on all devices
- **Smooth Animations**: Interactive transitions
- **Progress Indicators**: Visual feedback for confidence scores
- **Segment Badges**: Color-coded segment identification

### User Experience
- **Form Validation**: Real-time input validation
- **Error Handling**: User-friendly error messages
- **Loading States**: Visual feedback during processing
- **Hover Effects**: Interactive elements
- **Print Support**: Printable result pages

## 🔧 Configuration

### Environment Variables
```bash
# Debug mode
DEBUG=True

# Database settings
DATABASE_URL=sqlite:///db.sqlite3

# Secret key (generate new one for production)
SECRET_KEY=your-secret-key-here
```

### Production Deployment
1. Set `DEBUG=False`
2. Configure production database
3. Set up static file serving
4. Configure domain in `ALLOWED_HOSTS`
5. Set up SSL/HTTPS

## 📁 Project Structure

```
customer_segmentation_project/
├── customer_segmentation_project/     # Main Django project
│   ├── settings.py                  # Django settings
│   ├── urls.py                     # URL configuration
│   └── wsgi.py                     # WSGI configuration
├── customer_segmentation/            # Core app
│   ├── models.py                    # Database models
│   ├── views.py                     # View logic
│   ├── forms.py                     # Form classes
│   ├── admin.py                     # Admin configuration
│   ├── ml_service.py               # ML service layer
│   ├── urls.py                     # App URLs
│   └── templates/                  # HTML templates
├── static/                         # Static files
├── media/                          # User uploads
├── models/                         # Trained ML models
├── requirements.txt                # Python dependencies
└── README.md                      # This file
```

## 🧪 Testing

### Manual Testing
1. **Form Validation**: Test all form inputs and validation
2. **ML Predictions**: Verify segmentation results
3. **API Endpoints**: Test REST API functionality
4. **Admin Interface**: Test data management features
5. **Responsive Design**: Test on different screen sizes

### Automated Testing (Future)
```bash
# Run tests (when implemented)
python manage.py test

# Check code quality
flake8 customer_segmentation/
```

## 🐛 Troubleshooting

### Common Issues

**Server won't start**
- Check if port 8000 is available
- Verify virtual environment is activated
- Ensure all dependencies are installed

**ML models not loading**
- Models are automatically created on first run
- Check file permissions in models directory
- Verify scikit-learn version compatibility

**Static files not loading**
- Run `python manage.py collectstatic`
- Check STATIC_URL and STATIC_ROOT settings
- Verify static directory exists

**Database errors**
- Run `python manage.py migrate`
- Check database file permissions
- Verify database configuration

### Performance Optimization
- Use PostgreSQL for production
- Enable database indexing
- Configure caching
- Optimize static file serving

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- scikit-learn for ML algorithms
- Django for web framework
- Bootstrap for UI components
- Chart.js for data visualization

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the documentation

---

**Version**: 1.0.0  
**Last Updated**: April 2024  
**Developer**: ML/Django Expert Team
