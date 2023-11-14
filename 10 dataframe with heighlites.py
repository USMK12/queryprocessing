import pandas as pd
import numpy as np

np.random.seed(0)
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

def highlight_numbers(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

styled_df = df.applymap(highlight_numbers)
print(styled_df)
