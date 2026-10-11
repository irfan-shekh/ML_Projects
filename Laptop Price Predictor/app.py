from flask import Flask, render_template, request, jsonify
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
    companies = sorted(data['Company'].unique())
    types = sorted(data['TypeName'].unique())
    os_options = sorted(data['OpSys'].unique())
    cpus = sorted(data['CPU_name'].unique())
    gpus = sorted(data['Gpu brand'].unique())
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
    try:
        # Determine source (JSON payload or form encoded)
        if request.is_json:
            form = request.get_json()
        else:
            form = request.form

        # Extract features
        company = form.get('company')
        type_name = form.get('type')
        ram = int(form.get('ram', 8))
        weight = float(form.get('weight', 1.5))
        touchscreen_val = form.get('touchscreen', 'No')
        ips_val = form.get('ips', 'No')
        screen_size = float(form.get('screen_size', 15.6))
        resolution = form.get('resolution', '1920x1080')
        cpu = form.get('cpu')
        hdd = int(form.get('hdd', 0))
        ssd = int(form.get('ssd', 256))
        gpu = form.get('gpu')
        os = form.get('os')
        
        # Convert categorical flags
        touchscreen = 1 if touchscreen_val in ['Yes', '1', 1, True] else 0
        ips = 1 if ips_val in ['Yes', '1', 1, True] else 0
        
        # Calculate PPI
        X_res, Y_res = map(int, resolution.split('x'))
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        
        gpu_brand = gpu.split()[0] if gpu and ' ' in gpu else (gpu or 'Intel')

        if rf is not None:
            # Order: Company, TypeName, Ram, OpSys, Weight, TouchScreen, IPS, PPI, CPU_name, HDD, SSD, Gpu brand
            query_data = {
                'Company': [company],
                'TypeName': [type_name], 
                'Ram': [ram],
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
            # Fallback estimation
            base_price = 25000
            ram_price = ram * 1500
            storage_price = (ssd * 10) + (hdd * 2)
            brand_multiplier = {'Apple': 2.5, 'Dell': 1.2, 'HP': 1.1, 'Lenovo': 1.1, 'Asus': 1.0, 'Acer': 0.9, 'MSI': 1.3}
            brand_price = base_price * brand_multiplier.get(company, 1.0)
            type_multiplier = {'Ultrabook': 1.3, 'Gaming': 1.8, 'Workstation': 2.0, 'Notebook': 1.0, 'Netbook': 0.7, '2 in 1 Convertible': 1.4}
            type_price = base_price * type_multiplier.get(type_name, 1.0)
            
            if cpu and 'i7' in cpu:
                cpu_price = 8000
            elif cpu and 'i5' in cpu:
                cpu_price = 5000
            elif cpu and 'i3' in cpu:
                cpu_price = 3000
            elif cpu and 'Ryzen' in cpu:
                cpu_price = 6000
            else:
                cpu_price = 2000
                
            gpu_multiplier = {'Nvidia': 1.5, 'AMD': 1.3, 'Intel': 1.0}
            gpu_price = 3000 * gpu_multiplier.get(gpu_brand, 1.0)
            screen_price = (touchscreen * 2000) + (ips * 1500) + (ppi * 10)
            prediction = int(base_price + ram_price + storage_price + brand_price + type_price + cpu_price + gpu_price + screen_price)
        
        # Round prediction nicely
        prediction = max(10000, round(prediction / 100) * 100)
        min_price = max(8000, prediction - 1500)
        max_price = prediction + 1500
        
        # Price tier classification
        if prediction < 35000:
            tier = "Budget Friendly"
        elif prediction < 65000:
            tier = "Mid-Range Mainstream"
        elif prediction < 110000:
            tier = "High-End Premium"
        else:
            tier = "Enthusiast / Flagship"

        specs_info = {
            'company': company,
            'type': type_name,
            'ram': ram,
            'weight': weight,
            'touchscreen': 'Yes' if touchscreen else 'No',
            'ips': 'Yes' if ips else 'No',
            'screen_size': screen_size,
            'resolution': resolution,
            'cpu': cpu,
            'hdd': hdd,
            'ssd': ssd,
            'gpu': gpu_brand,
            'os': os,
            'ppi': round(ppi, 1),
            'tier': tier
        }
        
        is_ajax = (
            request.is_json or 
            request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 
            request.headers.get('Accept') == 'application/json' or 
            form.get('ajax') == 'true' or
            request.args.get('format') == 'json'
        )
        
        if is_ajax:
            return jsonify({
                'success': True,
                'prediction': prediction,
                'min_price': min_price,
                'max_price': max_price,
                'specs': specs_info
            })
            
        return render_template('result.html', 
                             min_price=min_price,
                             max_price=max_price,
                             prediction=prediction,
                             specs=specs_info)
    except Exception as e:
        if request.is_json or form.get('ajax') == 'true' or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': str(e)}), 400
        return f"Error during prediction: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
