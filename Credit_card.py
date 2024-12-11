# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:28:16 2024

@author: LAPTOPCOM
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
@st.cache_resource
def load_model():
    with open('fraud_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# App title
st.title("Credit Card Fraud Detection")

# Sidebar for user input
st.sidebar.header("User Input Features")

def user_input_features():
    # Example feature inputs (replace with your dataset features)
    V1 = st.sidebar.number_input("V1", min_value=-50.0, max_value=50.0, value=0.0)
    V2 = st.sidebar.number_input("V2", min_value=-50.0, max_value=50.0, value=0.0)
    V3 = st.sidebar.number_input("V3", min_value=-50.0, max_value=50.0, value=0.0)
    Amount = st.sidebar.number_input("Amount", min_value=0.0, max_value=10000.0, value=100.0)
    
    # Create a dictionary of inputs
    data = {
        'V1': V1,
        'V2': V2,
        'V3': V3,
        'Amount': Amount
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# Display user input
st.subheader("User Input Features")
st.write(input_df)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    
    # Display the results
    st.subheader("Prediction")
    st.write("Fraud" if prediction[0] == 1 else "Not Fraud")
    
    st.subheader("Prediction Probability")
    st.write(f"Not Fraud: {prediction_proba[0][0]:.2f}, Fraud: {prediction_proba[0][1]:.2f}")
