🛍️ Retail AI: Inventory & Customer Dashboard
An end-to-end Machine Learning web application that transforms raw transactional data into actionable business intelligence. This tool automates Demand Forecasting and Customer Tiering using a dataset of 500,000+ real-world transactions.
🚀 Business Problem
Retailers often struggle with two major inefficiencies:

Inventory Waste: Overstocking items that do not sell.

Generic Marketing: Treating one-time shoppers the same as high-value VIPs.

This project solves these issues by using Supervised Learning to predict stock needs and Unsupervised Learning to segment the customer base for targeted marketing.
🛠️ Tech Stack
Language: Python 3.x

Machine Learning: Scikit-Learn (Linear Regression & K-Means Clustering)

Data Processing: Pandas, NumPy, Openpyxl

Web Framework: Streamlit

Dataset: UCI Machine Learning Repository (Online Retail Dataset)
🧠 Core Features & ML Logic
📊 Smart Inventory Forecasting (Linear Regression)
Logic: Analyzes daily quantity trends using a LinearRegression model.

Function: Uses a Time-Index as the feature to predict total units needed for the Next 7 Days.

Goal: Aims for a 15-20% reduction in waste by aligning supply with predicted demand.
👥 Customer Segmentation (K-Means Clustering)
Logic: Implements the KMeans algorithm with StandardScaler to group unique customers.

Function: Analyzes transactional behavior to identify:

VIP / High Value: Frequent shoppers who spend the most.

Regulars: Average shopping habits.

At-Risk: Customers who haven't returned recently.
🚨 Real-time Inventory Alerts
Automated Pipeline: Handles data cleaning for cancellations ('C' Invoice prefixes), missing values, and outliers.

Low Stock Warnings: Instantly identifies items with critically low quantities to prevent lost sales.
Installation & Usage
Clone the repository:
git clone [https://github.com/divakarsingh00]
cd retail-ai-dashboard
Install dependencies:
pip install pandas scikit-learn openpyxl streamlit numpy
Run the application:
streamlit run app.py
📊 Results & Impact
Efficiency: Optimized data handling using @st.cache_data to manage 500,000+ rows efficiently.

Strategic Marketing: Provides a data-driven foundation for loyalty rewards and re-engagement campaigns.

Operational Readiness: Built a robust cleaning pipeline to transform "messy" real-world data into a structured ML format.
