# Laptop Price Predictor

A machine learning web application that predicts laptop prices based on various specifications like brand, RAM, CPU, GPU, and other hardware features.

## 🚀 Features

- **Interactive Web Interface**: User-friendly Flask-based web application
- **Real-time Predictions**: Get instant price predictions for laptop configurations
- **Comprehensive Features**: Supports multiple laptop specifications including:
  - Brand/Company
  - Laptop Type (Ultrabook, Notebook, Gaming, etc.)
  - RAM configurations (2GB to 64GB)
  - Operating Systems
  - Screen specifications (size, resolution, touchscreen, IPS)
  - CPU and GPU options
  - Storage configurations (HDD/SSD)

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, Bootstrap-inspired styling
- **Model**: Random Forest Regressor (pre-trained)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

1. **Clone or download the project**
   ```bash
   cd laptop_price_prediction
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app_flask_fixed.py
   ```

4. **Access the application**
   - Open your web browser and go to: `http://localhost:5000`

## 📁 Project Structure

```
laptop_price_prediction/
├── app_flask_fixed.py          # Main Flask application
├── requirements.txt            # Python dependencies
├── pipe.pkl                   # Trained machine learning model
├── traineddata.csv            # Processed training data
├── laptop_data.csv            # Original dataset
├── templates/                 # HTML templates
│   ├── index.html            # Main input form
│   └── result.html           # Prediction results page
├── Laptop Price Predictor.ipynb  # Original Jupyter notebook
└── README.md                  # This file
```

## 🎯 How to Use

1. **Start the application** by running `python app_flask_fixed.py`
2. **Open your browser** and navigate to `http://localhost:5000`
3. **Fill in the laptop specifications**:
   - Select the laptop brand
   - Choose the laptop type
   - Specify RAM size
   - Select operating system
   - Enter weight
   - Choose display options (touchscreen, IPS)
   - Specify screen size and resolution
   - Select CPU and GPU
   - Configure storage (HDD/SSD)
4. **Click "Predict Price"** to get the estimated price range
5. **View the results** showing the predicted price range

## 🤖 Model Information

- **Algorithm**: Random Forest Regressor
- **Training Data**: 1,302 laptop configurations
- **Features**: 12 specification parameters
- **Price Range**: Predictions include ±₹1,000 confidence interval

## 📊 Features Used for Prediction

1. **Company** - Laptop manufacturer (Apple, Dell, HP, etc.)
2. **TypeName** - Laptop category (Ultrabook, Notebook, Gaming, etc.)
3. **Ram** - Memory size in GB
4. **Weight** - Laptop weight in kg
5. **TouchScreen** - Touchscreen capability (Yes/No)
6. **IPS** - IPS display panel (Yes/No)
7. **PPI** - Pixels per inch (calculated from resolution and screen size)
8. **CPU_name** - Processor model
9. **HDD** - Hard disk drive capacity in GB
10. **SSD** - Solid state drive capacity in GB
11. **Gpu brand** - Graphics processor manufacturer
12. **OpSys** - Operating system

## 🔧 Dependencies

- `flask` - Web framework
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `scikit-learn` - Machine learning library

## 📈 Model Performance

The model was trained on a comprehensive dataset of laptop configurations and achieves reliable price predictions across different laptop categories and specifications.

## 🐛 Troubleshooting

**Common Issues:**

1. **Model Loading Error**: Ensure `pipe.pkl` and `traineddata.csv` are in the same directory
2. **Port Already in Use**: Change the port in the last line of `app_flask_fixed.py`
3. **Missing Dependencies**: Run `pip install -r requirements.txt` to install all required packages

## 🤝 Contributing

This project is for educational purposes. Feel free to:
- Improve the model with additional features
- Enhance the user interface
- Add more laptop specifications
- Deploy to cloud platforms

## 📝 License

This project is open source and available under the MIT License.

## 📞 Contact

For questions or issues regarding this project, please refer to the original Jupyter notebook for detailed implementation and data processing steps.

---

**Note**: The original Jupyter notebook (`Laptop Price Predictor.ipynb`) contains the complete data exploration, preprocessing, and model training pipeline. The Flask application provides a user-friendly interface to use the trained model for predictions.
