import streamlit as st
import pandas as pd
from src.predict import predict

st.title("Retail Sales ETL Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Input Data", df)
    preds = predict(df)
    st.write("Predicted Revenue", preds)
