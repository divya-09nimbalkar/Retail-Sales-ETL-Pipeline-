from src.data_loader import load_raw_data

def test_load_raw_data():
    df = load_raw_data("data/raw/retail_sales.csv")
    assert not df.empty
