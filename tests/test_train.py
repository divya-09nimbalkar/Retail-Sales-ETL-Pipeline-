from src.train import train_model

def test_train_model():
    train_model()
    import os
    assert os.path.exists("models/sales_model.pkl")

