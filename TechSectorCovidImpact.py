
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Close']  # returning only the 'Close' prices

start_date = '2020-11-01'
end_date = '2021-02-01'

# Fetching data
nvidia_data = fetch_stock_data('NVDA', start_date, end_date)
apple_data = fetch_stock_data('AAPL', start_date, end_date)
microsoft_data = fetch_stock_data('MSFT', start_date, end_date)

# Plotting data
plt.figure(figsize=(14,7))
nvidia_data.plot(label='Nvidia', legend=True)
apple_data.plot(label='Apple', legend=True)
microsoft_data.plot(label='Microsoft', legend=True)

plt.title('COVID Impact on the Tech Sector at Pandemic Peak')
plt.ylabel('Stock Price')
plt.xlabel('Date')
plt.grid(True)
plt.show()
