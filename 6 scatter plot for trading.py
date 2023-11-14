import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': [
        '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
        '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'
    ],
    'Open': [2700, 2720, 2750, 2765, 2778, 2782, 2790, 2805, 2815, 2820],
    'High': [2710, 2740, 2778, 2780, 2785, 2800, 2810, 2820, 2830, 2840],
    'Low': [2685, 2710, 2748, 2760, 2772, 2778, 2785, 2795, 2805, 2810],
    'Close': [2705, 2735, 2770, 2775, 2780, 2795, 2805, 2820, 2815, 2820],
    'Adj Close': [2690, 2720, 2755, 2760, 2775, 2790, 2800, 2815, 2810, 2825],
    'Volume': [1000000, 1200000, 1500000, 1350000, 1400000, 1250000, 1100000, 1300000, 1400000, 1150000]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 6))
plt.scatter(df['Volume'], df['Close'], c='blue', marker='o', alpha=0.7)
plt.xlabel('Volume')
plt.ylabel('Stock Price (Close)')
plt.title('Scatter Plot of Trading Volume vs. Stock Prices (2023)')
plt.grid(True)

plt.show()
