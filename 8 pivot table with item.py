import pandas as pd

data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Sale': [100, 200, 150, 300, 250, 120, 180, 220, 130, 280]
}

sales_data = pd.DataFrame(data)


pivot_table = sales_data.pivot_table(index='Item', values='Sale', aggfunc='sum')


pivot_table.reset_index(inplace=True)

pivot_table.columns = ['Item', 'Unit Sold']

print(pivot_table)
