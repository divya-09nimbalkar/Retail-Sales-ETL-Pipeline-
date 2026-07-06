import joblib
import pandas as pd
from src.preprocess import preprocess

def predict(df: pd.DataFrame):
    model = joblib.load("models/sales_model.pkl")
    df = preprocess(df)
    X = df[["day_of_week", "sales"]].astype("category").cat.codes.values.reshape(-1,1)
    return model.predict(X)
