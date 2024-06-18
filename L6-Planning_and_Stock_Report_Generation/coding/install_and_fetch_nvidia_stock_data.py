# filename: install_and_fetch_nvidia_stock_data.py

import subprocess
import sys

# Install yfinance package
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yfinance'])

# Import yfinance after installation
import yfinance as yf
import pandas as pd

def fetch_stock_data(stock_ticker, start_date, end_date):
    # Fetch the historical data for the stock
    data = yf.Ticker(stock_ticker)
    historical_data = data.history(start=start_date, end=end_date)
    return historical_data

if __name__ == "__main__":
    # Nvidia's stock ticker symbol is "NVDA"
    ticker_symbol = "NVDA"
    # Calculate the past month date range
    end_date = pd.Timestamp.now()
    start_date = end_date - pd.DateOffset(30)  # 30 days back

    # Fetch data
    nvidia_data = fetch_stock_data(ticker_symbol, start_date, end_date)
    print(nvidia_data)