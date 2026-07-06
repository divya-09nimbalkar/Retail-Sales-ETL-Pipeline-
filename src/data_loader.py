import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:
    """Load raw retail sales CSV file."""
    return pd.read_csv(path)
