import streamlit as st
import numpy as np
import os

st.title("🚀 Tesla Stock Price Predictor")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pred_1_day = np.load(os.path.join(BASE_DIR, 'models', 'pred_1_day.npy'))
pred_5_days = np.load(os.path.join(BASE_DIR, 'models', 'pred_5_days.npy'))
pred_10_days = np.load(os.path.join(BASE_DIR, 'models', 'pred_10_days.npy'))

option = st.selectbox(
    "Select Prediction Days",
    [1, 5, 10]
)

if option == 1:
    st.write(pred_1_day)
elif option == 5:
    st.line_chart(pred_5_days)
else:
    st.line_chart(pred_10_days)