import pandas as pd

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich sales data."""
    df = df.dropna()
    df["date"] = pd.to_datetime(df["date"])
    df["day_of_week"] = df["date"].dt.day_name()
    return df
