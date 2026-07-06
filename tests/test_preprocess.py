import pandas as pd
from src.preprocess import preprocess

def test_preprocess():
    df = pd.DataFrame({"date": ["2024-01-01"], "sales": [10], "revenue": [200]})
    df_clean = preprocess(df)
    assert "day_of_week" in df_clean.columns
