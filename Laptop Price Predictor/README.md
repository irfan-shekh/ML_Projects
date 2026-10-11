# LapPulse AI — Intelligent Laptop Price Predictor 💻⚡

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![UI](https://img.shields.io/badge/UI-Cyber--Indigo%20Glassmorphism-6366F1?style=flat)](#-modern-ui-features)

An end-to-end Machine Learning web application designed to estimate and predict market prices for laptops based on granular hardware specifications (brand, CPU, GPU, RAM, screen resolution & PPI, storage drives, weight, and operating system).

---

## ✨ Modern UI & App Highlights

- 🎨 **Cyber-Indigo Glassmorphism Interface**: Deep slate theme (`#070A13`) with glowing gradient accents, frosted glass cards (`backdrop-filter: blur(16px)`), and micro-animations.
- ⚡ **Real-Time Live Valuation**: Instant asynchronous valuation without full-page reloads, featuring smooth animated counter transitions.
- 🎯 **1-Click Hardware Presets**:
  - 🎮 **Gaming Rig** (Asus, 16GB RAM, Core i7, Dedicated Nvidia, 512GB SSD)
  - 💼 **Executive Ultrabook** (Apple, 16GB RAM, Core i5, 512GB SSD, 1.25kg)
  - 🎓 **Student Value** (HP, 8GB RAM, Core i5, 256GB SSD)
  - 🎨 **Creator Studio** (Dell, 32GB RAM, 4K Screen, Core i7, 1TB SSD)
- 💱 **Multi-Currency Live Converter**: Instant toggle between Indian Rupee (**₹ INR**), US Dollar (**$ USD**), and Euro (**€ EUR**).
- 🖥️ **Live Display PPI & Retina Indicator**: Calculates Pixels-Per-Inch (`PPI = √(w² + h²) / diagonal`) in real time and classifies display clarity (Retina Ultra-Sharp, Hi-DPI, Full HD Standard).
- ⚖️ **Synced Range Sliders & Inputs**: Real-time slider and numeric box synchronization for chassis weight and display diagonal.
- 📊 **Dynamic Specification Sheet**: Live preview card with dynamic feature tags (*Dedicated GPU*, *Retina Clarity*, *Featherweight Nomad*, etc.) and market valuation tiers.
- 🔄 **Dual Interaction Mode**: Supports both instant in-page AJAX prediction and full-page standard POST submission with complete shareable summary.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python, Flask, Jinja2 |
| **Machine Learning** | Scikit-learn (`Pipeline`, `RandomForestRegressor`, `OneHotEncoder`) |
| **Data Processing** | Pandas, NumPy |
| **Frontend UI** | HTML5, CSS3 (Modern Glassmorphism, CSS Grid & Flexbox), Vanilla JavaScript (ES6+) |
| **Typography** | Plus Jakarta Sans, Outfit, JetBrains Mono |

---

## 📁 Project Structure

```
Laptop Price Predictor/
├── app.py                      # Core Flask web server & prediction endpoints
├── pipe.pkl                    # Trained Scikit-learn ML pipeline model
├── traineddata.csv             # Processed feature dataset for validation & dropdowns
├── laptop_data.csv             # Raw laptop dataset
├── requirements.txt            # Python dependencies
├── static/                     # Static styling and client scripts
│   ├── css/
│   │   └── style.css           # Custom Cyber-Indigo glassmorphic stylesheet
│   └── js/
│       └── main.js             # Client controller (AJAX, presets, live PPI, currency)
├── templates/                  # Jinja2 HTML templates
│   ├── index.html              # Main configurator & live valuation dashboard
│   └── result.html             # Valuation result & shareable spec breakdown
├── Laptop Price Predictor.ipynb# Jupyter notebook for exploratory data analysis & training
└── README.md                   # Project documentation
```

---

## 🚀 Installation & Getting Started

### 1. Prerequisites
- Python 3.8 or above installed on your system.

### 2. Navigate to Project Directory
```bash
cd "Laptop Price Predictor"
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

## 🧠 Machine Learning Model Pipeline

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
   - Prediction is exponentiated back to price space (`np.exp(...)`) with confidence boundary (`± ₹1,500`).

### Features Expected by the Model:
1. `Company` — Brand manufacturer (Apple, Dell, HP, Asus, Lenovo, Acer, MSI, etc.)
2. `TypeName` — Form factor (Ultrabook, Notebook, Gaming, Workstation, 2 in 1 Convertible, Netbook)
3. `Ram` — System memory (2 GB to 64 GB)
4. `OpSys` — Operating system platform (Windows, Mac, Other)
5. `Weight` — Chassis weight in kilograms
6. `TouchScreen` — Touchscreen support (0 or 1)
7. `IPS` — IPS display panel (0 or 1)
8. `PPI` — Screen pixel density
9. `CPU_name` — Processor tier (Intel Core i3, i5, i7, AMD Processor, Other Intel)
10. `HDD` — Hard disk capacity in GB
11. `SSD` — Solid-state drive capacity in GB
12. `Gpu brand` — Graphics provider (Intel, AMD, Nvidia)

---

## 🔌 API Endpoint

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

## ⌨️ Keyboard Shortcuts

- `Ctrl + Enter` (or `Cmd + Enter` on macOS): Instantly trigger price estimation.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
