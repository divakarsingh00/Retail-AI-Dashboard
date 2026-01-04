# 🛍️ Retail AI: Customer Segmentation Dashboard

An end-to-end Machine Learning and Web application that uses **Unsupervised Learning** to segment customers based on 500,000+ real-world transactions.

## 🚀 Business Problem
Small and large-scale retailers often struggle to identify which customers are high-value and which are likely to churn (leave). This project solves that by automating **RFM Analysis** (Recency, Frequency, Monetary) to drive data-driven marketing decisions.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Machine Learning:** Scikit-Learn (K-Means Clustering)
* **Data Processing:** Pandas, Openpyxl
* **Web Framework:** Streamlit
* **Dataset:** UCI Machine Learning Repository (Online Retail Dataset)

## 🧠 Features
- **Data Cleaning Pipeline:** Handles "messy" real-world data including cancellations, missing values, and outliers.
- **RFM Engineering:** Calculates Recency, Frequency, and Monetary scores for every unique customer.
- **ML Clustering:** Uses **StandardScaler** and **K-Means** to group customers into 3 tiers:
    - **VIP / High Value:** Frequent shoppers who spend the most.
    - **Regular:** Average shopping habits.
    - **At Risk:** High-spending customers who haven't returned recently.
- **Interactive Search:** Real-time lookup of customer status via a web-based dashboard.

## 📦 Installation & Usage
1. Clone the repository: `git clone [YOUR_LINK]`
2. Install dependencies: `pip install pandas scikit-learn openpyxl streamlit`
3. Run the app: `python -m streamlit run app.py`

## 📊 Results & Impact
By segmenting the 4,000+ unique customers in this dataset, this tool allows businesses to:
1. Target **VIPs** with loyalty rewards.
2. Send re-engagement campaigns to **At-Risk** users.
3. Optimize marketing spend by focusing on high-revenue segments.