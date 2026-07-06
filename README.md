
---

# Retail Sales ETL Pipeline 🛒

## 📌 Overview
This project implements an **ETL (Extract, Transform, Load) pipeline** for retail sales data. It is designed to:
- Extract raw sales data from CSV files
- Transform and clean the data (date parsing, feature engineering)
- Load the processed data into structured outputs
- Train a simple machine learning model to predict revenue
- Provide an interactive dashboard using **Streamlit**

---

## 📂 Project Structure
```
Retail_Sales_ETL_Pipeline/
│
├── data/
│   ├── raw/                # raw input CSVs (retail_sales.csv)
│   └── processed/          # cleaned outputs
│
├── docs/                   # documentation
│
├── models/                 # trained ML models (sales_model.pkl)
│
├── notebooks/              # Jupyter notebooks for exploration
│   └── exploration.ipynb
│
├── src/
│   ├── __init__.py
│   ├── dashboard.py        # Streamlit dashboard
│   ├── data_loader.py      # extract raw CSVs
│   ├── main.py             # pipeline entry point
│   ├── predict.py          # prediction logic
│   ├── preprocess.py       # cleaning & feature engineering
│   ├── run_pipeline.py     # orchestrates ETL + training
│   └── train.py            # training script
│
├── tests/                  # unit tests
│   ├── test_data_loader.py
│   ├── test_preprocess.py
│   └── test_train.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Retail_Sales_ETL_Pipeline.git
   cd Retail_Sales_ETL_Pipeline
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 1. Prepare Data
Place your raw CSV in:
```
data/raw/retail_sales.csv
```

Required columns:
- `date`
- `store_id`
- `product_id`
- `sales`
- `revenue`

---

### 2. Run ETL Pipeline
```bash
python -m src.main
```
This will:
- Load raw data
- Clean and transform it
- Save processed data to `data/processed/retail_sales_clean.csv`
- Train a simple ML model (`models/sales_model.pkl`)

---

### 3. Run Dashboard
Start Streamlit:
```bash
python -m streamlit run src/dashboard.py
```
Upload a CSV with the required columns, and the dashboard will show predictions.

---

## 📓 Exploration Notebook
Open:
```bash
jupyter notebook notebooks/exploration.ipynb
```
This notebook demonstrates:
- Data loading
- Preprocessing
- Exploratory plots
- Correlation analysis

---

## 🧪 Testing
Run unit tests:
```bash
pytest tests/
```

---


