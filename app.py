import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("DeepMarket Insight: Indian Stock Market Predictor")
st.write("A machine learning-based application to predict trends in the Indian stock market.")

st.sidebar.header("Stock Selection")
stock_symbol = st.sidebar.text_input("Enter the stock ticker (e.g., TCS.NS, INFY.NS):", "RELIANCE.NS")

st.sidebar.subheader("Select Date Range")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2023-01-01'))
end_date = st.sidebar.date_input("End Date", pd.to_datetime('today'))

@st.cache
def fetch_data(symbol, start, end):
    stock_data = yf.download(symbol, start=start, end=end)
    return stock_data

stock_data = fetch_data(stock_symbol, start_date, end_date)

st.subheader(f"Stock Data for {stock_symbol}")
st.write(stock_data.tail())

st.subheader("Stock Price Trend")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(stock_data['Close'], label='Close Price', color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Price (INR)")
ax.legend()
st.pyplot(fig)

def train_dummy_model(data):
    data = data.dropna()
    data['Days'] = np.arange(len(data))
    X = data[['Days']]
    y = data['Close']
    
    model = LinearRegression()
    model.fit(X, y)
    return model

st.subheader("Market Prediction")
if st.button("Predict Future Price"):
    model = train_dummy_model(stock_data)
    future_days = np.arange(len(stock_data), len(stock_data) + 30).reshape(-1, 1)
    future_prices = model.predict(future_days)
    
    prediction_df = pd.DataFrame({'Date': pd.date_range(start=end_date, periods=30), 'Predicted Close': future_prices})
    st.write(prediction_df)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(stock_data['Close'], label='Historical Prices', color='blue')
    ax.plot(prediction_df['Date'], prediction_df['Predicted Close'], label='Predicted Prices', color='red')
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (INR)")
    ax.legend()
    st.pyplot(fig)
else:
    st.write("Click the button to predict future prices.")

st.sidebar.write("Powered by DeepMarket Insight © 2024")
