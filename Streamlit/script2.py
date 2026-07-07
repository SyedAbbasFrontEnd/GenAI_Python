# Capstone Project — Personal Finance Dashboard
# What the App Does: Users upload an expense CSV file and the app provides:

# • Expense summary metrics
# • Category-wise spending analysis
# • Monthly spending trends
# • Interactive filters
# • Clean dashboard layout

'''
Example Dataset
---
Date,Category,Amount,Payment_Mode,Description
2024-01-02,Food,250,UPI,Lunch
2024-01-03,Transport,120,Card,Metro
2024-01-05,Shopping,1500,Card,Clothes
2024-01-06,Food,400,Cash,Dinner
2024-01-08,Bills,2200,UPI,Electricity
---
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")

st.title("💰 Personal Finance Dashboard")
st.write("Upload your expense CSV file to analyze your spending habits.")

# Sidebar
st.sidebar.header("Upload Your Data")

uploaded_file = st.sidebar.file_uploader("Upload Expense CSV", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"])

    # Sidebar Filters
    st.sidebar.header("Filters")

    category_filter = st.sidebar.multiselect(
        "Select Category",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )

    payment_filter = st.sidebar.multiselect(
        "Payment Mode",
        options=df["Payment_Mode"].unique(),
        default=df["Payment_Mode"].unique()
    )

    filtered_df = df[
        (df["Category"].isin(category_filter)) &
        (df["Payment_Mode"].isin(payment_filter))
    ]

    # Top Metrics
    total_spent = filtered_df["Amount"].sum()
    avg_spent = filtered_df["Amount"].mean()
    max_spent = filtered_df["Amount"].max()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Spending", f"₹{total_spent:,.2f}")
    col2.metric("Average Transaction", f"₹{avg_spent:,.2f}")
    col3.metric("Highest Expense", f"₹{max_spent:,.2f}")

    st.divider()

    # Category Analysis
    st.subheader("📊 Spending by Category")

    category_data = filtered_df.groupby("Category")["Amount"].sum()

    # fig1, ax1 = plt.subplots()
    fig1, ax1 = plt.subplots(figsize=(4,2))
    category_data.plot(kind="bar", ax=ax1)
    ax1.set_ylabel("Amount Spent")
    ax1.set_xlabel("Category")

    # st.pyplot(fig1)
    st.pyplot(fig1, use_container_width=False)

    st.divider()

    # Monthly Trend
    st.subheader("📈 Monthly Spending Trend")

    filtered_df["Month"] = filtered_df["Date"].dt.to_period("M")

    monthly_data = filtered_df.groupby("Month")["Amount"].sum()

    # fig2, ax2 = plt.subplots()
    fig2, ax2 = plt.subplots(figsize=(4,2))
    monthly_data.plot(kind="line", marker="o", ax=ax2)
    ax2.set_ylabel("Amount")
    ax2.set_xlabel("Month")

    # st.pyplot(fig2)
    st.pyplot(fig2, use_container_width=False)

    st.divider()

    # Raw Data
    st.subheader("📄 Transaction Data")

    st.dataframe(filtered_df)

else:

    st.info("Please upload a CSV file to begin analysis.")