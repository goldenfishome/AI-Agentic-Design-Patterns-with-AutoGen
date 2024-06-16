# filename: analysis_and_plot_nvidia_stock.py
import pandas as nut
import matplotlib.pyplot as plt

# Data, previously retrieved and output shown
data = {
    'Date': ['2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-04-01',
             '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-08',
             '2024-04-09', '2024-04-10', '2024-04-11', '2024-04-12', '2024-04-15',
             '2024-04-16', '2024-04-17', '2024-04-18', '2024-04-19', '2024-04-22'],
    'Adj Close': [94.994194, 92.553398, 90.242584, 90.348579, 90.355576,
                  89.444656, 88.956688, 85.897942, 88.000778, 87.125847,
                  85.346985, 87.031853, 90.608551, 88.178757, 85.993935,
                  87.407822, 84.028099, 84.664040, 76.193741, 79.511467]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate daily returns
df['Daily Return'] = df['Adj Close'].pct_change()

# Compute overall return
overall_return = (df['Adj Close'].iloc[-1] - df['Adj Close'].iloc[0]) / df['Adj Close'].iloc[0]

# Plotting the adjusted close price
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Adj Close'], marker='o', linestyle='-')
plt.title('Nvidia Stock Performance from March 23, 2024, to April 23, 2024')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.grid(True)
plt.show()

print("Overall performance over the period:", overall_return * 100, "%")