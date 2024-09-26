# DeepMarket Insight: Indian Stock Market Predictor

**DeepMarket Insight** is a Streamlit-based web application designed to predict trends in the Indian stock market using basic machine learning techniques. The application leverages historical stock data to provide predictions for future stock prices.

## Features

- **Real-time Stock Data:** Fetches up-to-date stock data using the Yahoo Finance API.
- **Customizable Date Range:** Users can select the date range for analysis.
- **Visualization:** Displays historical closing prices of the selected stock.
- **Machine Learning Prediction:** Provides a simple linear regression model to predict the future stock price for the next 30 days.
- **Interactive Interface:** Users can easily select stocks, choose date ranges, and visualize both historical data and predictions.

## Installation

To run this application locally, follow these steps:

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/deepmarket-insight.git
    cd deepmarket-insight
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Stock Selection:** 
    - Enter the stock ticker symbol in the sidebar (e.g., `RELIANCE.NS` for Reliance Industries).
    - Default stock symbol is set to `RELIANCE.NS`.

2. **Select Date Range:**
    - Choose the start and end dates for which you want to analyze the stock data.
    - The default start date is set to `2023-01-01`, and the end date is set to today's date.

3. **View Stock Data:**
    - The application will display the most recent stock data in a table format.

4. **Visualize Stock Trend:**
    - A plot of the stock's closing prices over the selected date range will be displayed.

5. **Predict Future Prices:**
    - Click the "Predict Future Price" button to generate and display predictions for the next 30 days based on a linear regression model.

## File Structure

- **`app.py`**: Main application file containing the Streamlit code.
- **`requirements.txt`**: Lists the Python packages required to run the application.
- **`README.md`**: This file, providing an overview of the project.

## Dependencies

The following Python libraries are required to run this application:

- `streamlit`: For creating the web interface.
- `yfinance`: To fetch stock data from Yahoo Finance.
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib`: For plotting data.
- `scikit-learn`: For the linear regression model.




## Future Improvements

- **Advanced Machine Learning Models:**  
  Incorporate more sophisticated models like LSTM or ARIMA to enhance prediction accuracy.

- **Multiple Stock Comparison:**  
  Enable users to compare predictions for multiple stocks simultaneously.

- **Technical Indicators:**  
  Add support for technical analysis indicators such as RSI, MACD, and Bollinger Bands.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
