import joblib
from sklearn.linear_model import LinearRegression
from src.data_loader import load_raw_data
from src.preprocess import preprocess

def train_model():
    df = load_raw_data("data/raw/retail_sales.csv")
    df = preprocess(df)

    X = df[["day_of_week", "sales"]].astype("category").cat.codes.values.reshape(-1,1)
    y = df["revenue"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "models/sales_model.pkl")
    print("✅ Model trained and saved.")

if __name__ == "__main__":
    train_model()
