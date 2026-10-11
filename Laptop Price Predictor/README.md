# LapPulse AI ΓÇö Intelligent Laptop Price Predictor ≡ƒÆ╗ΓÜí

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![UI](https://img.shields.io/badge/UI-Cyber--Indigo%20Glassmorphism-6366F1?style=flat)](#-modern-ui-features)

An end-to-end Machine Learning web application designed to estimate and predict market prices for laptops based on granular hardware specifications (brand, CPU, GPU, RAM, screen resolution & PPI, storage drives, weight, and operating system).

---

## Γ£¿ Modern UI & App Highlights

- ≡ƒÄ¿ **Cyber-Indigo Glassmorphism Interface**: Deep slate theme (`#070A13`) with glowing gradient accents, frosted glass cards (`backdrop-filter: blur(16px)`), and micro-animations.
- ΓÜí **Real-Time Live Valuation**: Instant asynchronous valuation without full-page reloads, featuring smooth animated counter transitions.
- ≡ƒÄ» **1-Click Hardware Presets**:
  - ≡ƒÄ« **Gaming Rig** (Asus, 16GB RAM, Core i7, Dedicated Nvidia, 512GB SSD)
  - ≡ƒÆ╝ **Executive Ultrabook** (Apple, 16GB RAM, Core i5, 512GB SSD, 1.25kg)
  - ≡ƒÄô **Student Value** (HP, 8GB RAM, Core i5, 256GB SSD)
  - ≡ƒÄ¿ **Creator Studio** (Dell, 32GB RAM, 4K Screen, Core i7, 1TB SSD)
- ≡ƒÆ▒ **Multi-Currency Live Converter**: Instant toggle between Indian Rupee (**Γé╣ INR**), US Dollar (**$ USD**), and Euro (**Γé¼ EUR**).
- ≡ƒûÑ∩╕Å **Live Display PPI & Retina Indicator**: Calculates Pixels-Per-Inch (`PPI = ΓêÜ(w┬▓ + h┬▓) / diagonal`) in real time and classifies display clarity (Retina Ultra-Sharp, Hi-DPI, Full HD Standard).
- ΓÜû∩╕Å **Synced Range Sliders & Inputs**: Real-time slider and numeric box synchronization for chassis weight and display diagonal.
- ≡ƒôè **Dynamic Specification Sheet**: Live preview card with dynamic feature tags (*Dedicated GPU*, *Retina Clarity*, *Featherweight Nomad*, etc.) and market valuation tiers.
- ≡ƒöä **Dual Interaction Mode**: Supports both instant in-page AJAX prediction and full-page standard POST submission with complete shareable summary.

---

## ≡ƒ¢á∩╕Å Technology Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python, Flask, Jinja2 |
| **Machine Learning** | Scikit-learn (`Pipeline`, `RandomForestRegressor`, `OneHotEncoder`) |
| **Data Processing** | Pandas, NumPy |
| **Frontend UI** | HTML5, CSS3 (Modern Glassmorphism, CSS Grid & Flexbox), Vanilla JavaScript (ES6+) |
| **Typography** | Plus Jakarta Sans, Outfit, JetBrains Mono |

---

## ≡ƒôü Project Structure

```
laptop_price_prediction/
Γö£ΓöÇΓöÇ app.py                      # Core Flask web server & prediction endpoints
Γö£ΓöÇΓöÇ pipe.pkl                    # Trained Scikit-learn ML pipeline model
Γö£ΓöÇΓöÇ traineddata.csv             # Processed feature dataset for validation & dropdowns
Γö£ΓöÇΓöÇ laptop_data.csv             # Raw laptop dataset
Γö£ΓöÇΓöÇ requirements.txt            # Python dependencies
Γö£ΓöÇΓöÇ static/                     # Static styling and client scripts
Γöé   Γö£ΓöÇΓöÇ css/
Γöé   Γöé   ΓööΓöÇΓöÇ style.css           # Custom Cyber-Indigo glassmorphic stylesheet
Γöé   ΓööΓöÇΓöÇ js/
Γöé       ΓööΓöÇΓöÇ main.js             # Client controller (AJAX, presets, live PPI, currency)
Γö£ΓöÇΓöÇ templates/                  # Jinja2 HTML templates
Γöé   Γö£ΓöÇΓöÇ index.html              # Main configurator & live valuation dashboard
Γöé   ΓööΓöÇΓöÇ result.html             # Valuation result & shareable spec breakdown
Γö£ΓöÇΓöÇ Laptop Price Predictor.ipynb# Jupyter notebook for exploratory data analysis & training
ΓööΓöÇΓöÇ README.md                   # Project documentation
```

---

## ≡ƒÜÇ Installation & Getting Started

### 1. Prerequisites
- Python 3.8 or above installed on your system.

### 2. Clone / Open Directory
```bash
cd laptop_price_prediction
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Web Interface
Open your browser and navigate to:
```
http://localhost:5000
```
*(or `http://127.0.0.1:5000`)*

---

## ≡ƒºá Machine Learning Model Pipeline

The predictive engine uses a **Scikit-Learn Pipeline** trained on laptop hardware records:

1. **Preprocessing**:
   - Categorical columns encoded via `OneHotEncoder(drop='first', sparse_output=False)`:
     - `Company`, `TypeName`, `OpSys`, `CPU_name`, `Gpu brand`
   - Engineered features:
     - `PPI` (Pixels Per Inch) calculated from resolution and screen size
     - Storage split into dedicated `SSD` and `HDD` capacities (in GB)
     - Touchscreen and IPS display flags
2. **Regressor**:
   - `RandomForestRegressor` trained on log-transformed prices (`np.log(Price)`).
3. **Inference**:
   - Prediction is exponentiated back to price space (`np.exp(...)`) with confidence boundary (`┬▒ Γé╣1,500`).

### Features Expected by the Model:
1. `Company` ΓÇö Brand manufacturer (Apple, Dell, HP, Asus, Lenovo, Acer, MSI, etc.)
2. `TypeName` ΓÇö Form factor (Ultrabook, Notebook, Gaming, Workstation, 2 in 1 Convertible, Netbook)
3. `Ram` ΓÇö System memory (2 GB to 64 GB)
4. `OpSys` ΓÇö Operating system platform (Windows, Mac, Other)
5. `Weight` ΓÇö Chassis weight in kilograms
6. `TouchScreen` ΓÇö Touchscreen support (0 or 1)
7. `IPS` ΓÇö IPS display panel (0 or 1)
8. `PPI` ΓÇö Screen pixel density
9. `CPU_name` ΓÇö Processor tier (Intel Core i3, i5, i7, AMD Processor, Other Intel)
10. `HDD` ΓÇö Hard disk capacity in GB
11. `SSD` ΓÇö Solid-state drive capacity in GB
12. `Gpu brand` ΓÇö Graphics provider (Intel, AMD, Nvidia)

---

## ≡ƒöî API Endpoint

### `POST /predict`
Supports both JSON API payload and standard form-encoded data.

**Request Body (JSON):**
```json
{
  "company": "Apple",
  "type": "Ultrabook",
  "ram": 16,
  "weight": 1.25,
  "touchscreen": "No",
  "ips": "Yes",
  "screen_size": 13.3,
  "resolution": "2560x1600",
  "cpu": "Intel Core i5",
  "hdd": 0,
  "ssd": 512,
  "gpu": "Intel",
  "os": "Mac",
  "ajax": "true"
}
```

**Response (JSON):**
```json
{
  "success": true,
  "prediction": 88400,
  "min_price": 86900,
  "max_price": 89900,
  "specs": {
    "company": "Apple",
    "type": "Ultrabook",
    "ram": 16,
    "cpu": "Intel Core i5",
    "gpu": "Intel",
    "ssd": 512,
    "hdd": 0,
    "ppi": 227.0,
    "tier": "High-End Premium"
  }
}
```

---

## Γî¿∩╕Å Keyboard Shortcuts

- `Ctrl + Enter` (or `Cmd + Enter` on macOS): Instantly trigger price estimation.

---

## ≡ƒôä License

This project is open-source and available under the [MIT License](LICENSE).
