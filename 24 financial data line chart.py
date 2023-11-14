import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/maheshpabbisetti/OneDrive/Documents/QPDS/24.financial data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Open'], label='Open', color='blue', marker='o')
plt.plot(df.index, df['High'], label='High', color='green', marker='o')
plt.plot(df.index, df['Low'], label='Low', color='red', marker='o')
plt.plot(df.index, df['Close'], label='Close', color='purple', marker='o')
plt.title('Alphabet Inc. Stock Prices (Oct 3, 2016 - Oct 7, 2016)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
