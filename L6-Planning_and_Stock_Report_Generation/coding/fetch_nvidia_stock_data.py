# filename: fetch_nvidia_stock_data.py
import yfinance as yf

# Define the ticker symbol and the time frame
ticker_symbol = "NVDA"
start_date = "2024-03-23"
end_date = "2024-04-23"

# Fetch the historical data
nvda_data = yf.download(ticker_symbol, start=start_date, end=end_date)
print(nvda_data)