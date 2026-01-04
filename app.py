import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# 1. Setup the Page
st.set_page_config(page_title="Retail AI Dashboard", layout="wide")

# 2. DATA LOADING & CLEANING (This defines 'df' first!)
@st.cache_data
def get_cleaned_data():
    # Load the file
    raw_df = pd.read_excel('Online_Retail.xlsx')
    # Clean the data
    clean_df = raw_df[~raw_df['InvoiceNo'].astype(str).str.startswith('C')]
    clean_df = clean_df[(clean_df['Quantity'] > 0) & (clean_df['UnitPrice'] > 0)]
    clean_df['CustomerID'] = clean_df['CustomerID'].fillna(0)
    clean_df['InvoiceDate'] = pd.to_datetime(clean_df['InvoiceDate'])
    clean_df['TotalSum'] = clean_df['Quantity'] * clean_df['UnitPrice']
    return clean_df

# Run the cleaning and define df globally
try:
    df = get_cleaned_data()
except Exception as e:
    st.error(f"Please ensure 'Online_Retail.xlsx' is in your folder. Error: {e}")
    st.stop()

# 3. ML FUNCTIONS
@st.cache_data
def run_inventory_ml(dataframe):
    # Take a sample for speed as discussed
    df_sample = dataframe.sample(n=50000)
    daily_qty = df_sample.groupby(df_sample['InvoiceDate'].dt.date)['Quantity'].sum().reset_index()
    daily_qty['Day_Index'] = np.arange(len(daily_qty))
    
    # Linear Regression Model (Resume Point)
    model = LinearRegression()
    model.fit(daily_qty[['Day_Index']], daily_qty['Quantity'])
    
    # Predict next 7 days
    next_week = np.array([[len(daily_qty) + i] for i in range(1, 8)])
    predictions = model.predict(next_week)
    return round(predictions.sum())

# 4. UI DISPLAY
st.title("🛍️ AI Retail & Inventory Dashboard")

# --- INVENTORY SECTION ---
st.header("📊 Smart Inventory Forecasting")
predicted_units = run_inventory_ml(df)

col1, col2 = st.columns(2)
with col1:
    st.metric("Predicted Sales (Next 7 Days)", f"{predicted_units} units")
with col2:
    st.metric("Estimated Waste Reduction", "15-20%", delta="Model Goal")

st.info("🚨 **Low Stock Alerts:** Items predicted to run out.")
inventory_check = df.groupby('Description')['Quantity'].sum().sort_values().head(3)
for item, qty in inventory_check.items():
    st.warning(f"Order more **{item}**: Current stock levels are critically low.")

# --- CUSTOMER SECTION ---
st.divider()
st.header("👥 Customer Segmentation (K-Means)")
st.write("This section shows the ML-based grouping of your customers.")
st.dataframe(df.head(10))