from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the trained model with error handling
try:
    with open('pipe.pkl', 'rb') as f:
        rf = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    rf = None

# Load the training data for dropdown options
try:
    data = pd.read_csv("traineddata.csv")
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")
    data = None

@app.route('/')
def home():
    if data is None:
        return "Error: Could not load training data", 500
    
    # Get unique values for dropdowns
    companies = data['Company'].unique()
    types = data['TypeName'].unique()
    os_options = data['OpSys'].unique()
    cpus = data['CPU_name'].unique()
    gpus = data['Gpu brand'].unique()
    resolutions = ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440']
    
    return render_template('index.html', 
                         companies=companies,
                         types=types,
                         os_options=os_options,
                         cpus=cpus,
                         gpus=gpus,
                         resolutions=resolutions)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form data
            company = request.form['company']
            type_name = request.form['type']
            ram = int(request.form['ram'])
            weight = float(request.form['weight'])
            touchscreen = request.form['touchscreen']
            ips = request.form['ips']
            screen_size = float(request.form['screen_size'])
            resolution = request.form['resolution']
            cpu = request.form['cpu']
            hdd = int(request.form['hdd'])
            ssd = int(request.form['ssd'])
            gpu = request.form['gpu']
            os = request.form['os']
            
            # Convert categorical values
            touchscreen = 1 if touchscreen == 'Yes' else 0
            ips = 1 if ips == 'Yes' else 0
            
            # Calculate PPI
            X_resolution = int(resolution.split('x')[0])
            Y_resolution = int(resolution.split('x')[1])
            ppi = ((X_resolution**2)+(Y_resolution**2))**0.5/(screen_size)
            
            if rf is not None:
                # Use the trained model - features must match training data order exactly
                # Order: Company, TypeName, Ram, Gpu, OpSys, Weight, TouchScreen, IPS, PPI, CPU_name, HDD, SSD, Gpu brand
                
                # Extract GPU brand from full GPU name
                gpu_brand = gpu.split()[0] if ' ' in gpu else gpu
                
                # Create DataFrame with proper column names
                query_data = {
                    'Company': [company],
                    'TypeName': [type_name], 
                    'Ram': [ram],
                    'Gpu': [gpu],
                    'OpSys': [os],
                    'Weight': [weight],
                    'TouchScreen': [touchscreen],
                    'IPS': [ips],
                    'PPI': [ppi],
                    'CPU_name': [cpu],
                    'HDD': [hdd],
                    'SSD': [ssd],
                    'Gpu brand': [gpu_brand]
                }
                query_df = pd.DataFrame(query_data)
                
                prediction = int(np.exp(rf.predict(query_df)[0]))
            else:
                # Fallback: simple price estimation based on key features
                base_price = 25000
                
                # RAM pricing
                ram_price = ram * 1500
                
                # Storage pricing
                storage_price = (ssd * 10) + (hdd * 2)
                
                # Brand pricing
                brand_multiplier = {'Apple': 2.5, 'Dell': 1.2, 'HP': 1.1, 'Lenovo': 1.1, 'Asus': 1.0, 'Acer': 0.9, 'MSI': 1.3}
                brand_price = base_price * brand_multiplier.get(company, 1.0)
                
                # Type pricing
                type_multiplier = {'Ultrabook': 1.3, 'Gaming': 1.8, 'Workstation': 2.0, 'Notebook': 1.0, 'Netbook': 0.7, '2 in 1 Convertible': 1.4}
                type_price = base_price * type_multiplier.get(type_name, 1.0)
                
                # CPU pricing (simplified)
                if 'i7' in cpu:
                    cpu_price = 8000
                elif 'i5' in cpu:
                    cpu_price = 5000
                elif 'i3' in cpu:
                    cpu_price = 3000
                elif 'Ryzen' in cpu:
                    cpu_price = 6000
                else:
                    cpu_price = 2000
                
                # GPU pricing
                gpu_multiplier = {'Nvidia': 1.5, 'AMD': 1.3, 'Intel': 1.0}
                gpu_price = 3000 * gpu_multiplier.get(gpu, 1.0)
                
                # Screen features
                screen_price = (touchscreen * 2000) + (ips * 1500) + (ppi * 10)
                
                prediction = int(base_price + ram_price + storage_price + brand_price + type_price + cpu_price + gpu_price + screen_price)
            
            min_price = prediction - 1000
            max_price = prediction + 1000
            
            return render_template('result.html', 
                                 min_price=min_price,
                                 max_price=max_price,
                                 prediction=prediction)
        except Exception as e:
            return f"Error during prediction: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
