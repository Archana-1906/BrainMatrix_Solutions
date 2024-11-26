# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:25:26 2024

@author: LAPTOPCOM
"""

import streamlit as st
import pandas as pd
import zipfile
import io

# App Title
st.title("CSV Data Analysis and Visualization")

# Upload File Section
st.sidebar.header("Upload Files")
fake_zip = st.sidebar.file_uploader("Upload Fake.csv.zip", type=["zip"])
true_zip = st.sidebar.file_uploader("Upload True.csv.zip", type=["zip"])

# Function to extract CSV from the uploaded ZIP file
def extract_csv_from_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as z:
        for filename in z.namelist():
            if filename.endswith('.csv'):
                with z.open(filename) as f:
                    return pd.read_csv(f)

# Load Data
if fake_zip and true_zip:
    try:
        fake_data = extract_csv_from_zip(fake_zip)
        true_data = extract_csv_from_zip(true_zip)
        
        # Display Dataframes
        st.subheader("Fake Data Preview")
        st.dataframe(fake_data.head())

        st.subheader("True Data Preview")
        st.dataframe(true_data.head())

        # Basic Stats
        st.subheader("Basic Statistics")
        fake_summary = fake_data.describe(include='all').T
        true_summary = true_data.describe(include='all').T
        
        st.write("**Fake Data Summary**")
        st.dataframe(fake_summary)
        
        st.write("**True Data Summary**")
        st.dataframe(true_summary)

        # Visualizations
        st.subheader("Data Visualizations")
        st.write("Select a dataset to visualize.")
        dataset_choice = st.radio("Choose a dataset", ("Fake", "True"))
        selected_data = fake_data if dataset_choice == "Fake" else true_data

        st.bar_chart(selected_data.select_dtypes(include='number'))

    except Exception as e:
        st.error(f"Error loading data: {e}")

else:
    st.info("Please upload both Fake.csv.zip and True.csv.zip files to proceed.")
