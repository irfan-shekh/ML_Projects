# Mushroom Classification Web Application

A production-ready Django web application that classifies mushrooms as edible or poisonous using machine learning.

## 🍄 Features

- **ML-Powered Classification**: Uses trained scikit-learn models with PCA for accurate predictions
- **Modern UI**: Responsive, mobile-friendly interface with Bootstrap 5 and custom CSS
- **User-Friendly**: Intuitive form with clear categorization of mushroom characteristics
- **Sample Data**: One-click sample data filling for easy testing
- **Error Handling**: Comprehensive validation and user-friendly error messages
- **Professional Design**: Clean, modern interface with animations and visual feedback

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone/Download the project**

   ```bash
   cd mushroom_classification/Code/mysite
   ```

2. **Create and activate virtual environment**

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

4. **Run the application**

   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

## 📊 Model Details

### Features Used

The ML model uses 22 mushroom characteristics:

1. **Cap Characteristics**: Shape, Surface, Color, Bruises
2. **Sensory**: Odor
3. **Gill Characteristics**: Attachment, Spacing, Size, Color
4. **Stalk Characteristics**: Shape, Root, Surface (above/below ring), Color (above/below ring)
5. **Veil & Ring**: Type, Color, Number, Ring Type
6. **Spore & Habitat**: Spore Print Color, Population, Habitat

### Model Architecture

- **PCA Model**: `MushsPCA.pickle` - Dimensionality reduction
- **Classification Model**: `Mushs.pickle` - Main prediction model
- **Input Features**: 22 encoded categorical features
- **Output**: Binary classification (edible=0, poisonous=1)

## 🎯 Usage Guide

### Manual Classification

1. Fill in all required mushroom characteristics
2. Click "Classify Mushroom" to get prediction
3. View results with confidence indicators

### Quick Testing

1. Click "Fill Sample Data" to auto-populate form
2. Click "Classify Mushroom" to see sample prediction
3. Use "Classify Another" to reset and try new data

## 🔧 Technical Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5.3.0, Font Awesome 6.4.0
- **ML Libraries**: scikit-learn 1.3.2, pandas 1.5.3, numpy 1.24.3
- **Deployment**: Gunicorn 21.2.0 (production ready)

## 📁 Project Structure

```
mushroom_classification/Code/mysite/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── mysite/
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py           # WSGI configuration
└── polls/
    ├── __init__.py
    ├── views.py           # Main application logic
    ├── urls.py           # App URL configuration
    ├── models.py         # Database models
    ├── admin.py          # Admin interface
    ├── apps.py          # App configuration
    ├── templates/
    │   └── index.html   # Main template
    ├── Mushs.pickle     # Trained ML model
    └── MushsPCA.pickle # PCA transformation model
```

## 🛠 Configuration

### Development Settings

- **Debug Mode**: Enabled
- **Allowed Hosts**: 127.0.0.1, localhost, 0.0.0.0
- **Database**: SQLite3 (development)
- **Static Files**: Configured for local development

### Production Deployment

1. **Set DEBUG = False** in settings.py
2. **Configure ALLOWED_HOSTS** with your domain
3. **Set up production database** (PostgreSQL recommended)
4. **Configure static files serving**
5. **Set up HTTPS** with SSL certificate

## 🧪 Testing

### Manual Testing

1. **Form Validation**: Try submitting empty forms
2. **Sample Data**: Test the "Fill Sample Data" functionality
3. **Different Inputs**: Test various mushroom characteristics
4. **Error Handling**: Verify error messages display correctly

### Model Testing

Test with known mushroom types:

- **Edible Example**: Use sample data (should predict "edible")
- **Poisonous Example**: Modify odor to "foul" (should predict "poisonous")

## 🐛 Troubleshooting

### Common Issues

1. **Server won't start**
   - Check Python version (3.8+ required)
   - Verify virtual environment is activated
   - Install dependencies: `pip install -r requirements.txt`

2. **Model loading errors**
   - Ensure pickle files exist in `polls/` directory
   - Check file permissions
   - Verify model compatibility with scikit-learn version

3. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_URL and STATIC_ROOT settings
   - Verify Bootstrap CSS/JS links

4. **Form submission errors**
   - Check CSRF token is present
   - Verify all fields are filled
   - Check browser console for JavaScript errors

### Debug Mode

Enable debug logging in views.py:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Performance

### Optimization Tips

1. **Model Caching**: Load models once at startup
2. **Database Indexing**: Add indexes for frequent queries
3. **Static File Compression**: Enable gzip compression
4. **CDN**: Use CDN for Bootstrap/Font Awesome

### Expected Performance

- **Model Loading**: ~1-2 seconds (first time)
- **Prediction**: <100ms per request
- **Page Load**: <2 seconds with good internet

## 🔒 Security Considerations

1. **Input Validation**: All inputs are validated and sanitized
2. **CSRF Protection**: Django CSRF middleware enabled
3. **SQL Injection**: Django ORM prevents SQL injection
4. **File Upload**: No file uploads in current version
5. **Dependencies**: Regular security updates via requirements.txt

## 📱 Browser Compatibility

- **Chrome**: 90+ ✅
- **Firefox**: 88+ ✅
- **Safari**: 14+ ✅
- **Edge**: 90+ ✅
- **Mobile**: iOS Safari, Android Chrome ✅

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request

## 📄 License

This project is for educational purposes. Please ensure compliance with data usage and ML model deployment regulations in your jurisdiction.

## 📞 Support

For issues and questions:

1. Check troubleshooting section
2. Review Django documentation
3. Create GitHub issue with detailed description

---

**⚠️ Disclaimer**: This application is for educational purposes only. Never consume wild mushrooms based solely on app predictions. Always consult with expert mycologists and multiple reliable sources before consuming any wild mushrooms.
