from src.data_loader import load_raw_data
from src.preprocess import preprocess
from src.train import train_model

def run_pipeline():
    print("🚀 Starting Retail Sales ETL Pipeline...")
    df = load_raw_data("data/raw/retail_sales.csv")
    print(f"Loaded {len(df)} rows from raw data.")
    df_clean = preprocess(df)
    print("Preprocessing complete.")
    train_model()
    print("Model training complete.")

if __name__ == "__main__":
    run_pipeline()
