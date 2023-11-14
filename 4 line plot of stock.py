import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': [
        '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
        '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'
    ],
    'Close': [2700, 2720, 2750, 2765, 2778, 2782, 2790, 2805, 2815, 2820]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

start_date = '2023-01-03'
end_date = '2023-01-08'

filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.figure(figsize=(12, 6))
plt.plot(filtered_df['Date'], filtered_df['Close'], label='Alphabet Inc. Stock Price')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Historical Stock Prices of Alphabet Inc. (2023)')
plt.legend()
plt.grid(True)

plt.show()
