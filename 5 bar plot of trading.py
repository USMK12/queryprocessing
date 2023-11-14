import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': [
        '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
        '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'
    ],
    'Volume': [1000000, 1200000, 1500000, 1350000, 1400000, 1250000, 1100000, 1300000, 1400000, 1150000]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

start_date = '2023-01-03'
end_date = '2023-01-08'

filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.figure(figsize=(12, 6))
plt.bar(filtered_df['Date'], filtered_df['Volume'], label='Trading Volume', color='blue')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Trading Volume of Alphabet Inc. Stock (2023)')
plt.legend()
plt.grid(axis='y')

plt.show()
