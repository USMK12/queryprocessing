import pandas as pd
w_a_con = pd.read_csv(r"C:\Users\maheshpabbisetti\OneDrive\Documents\QPDS\19.world alcohol consumption.csv")
print("World alcohol consumption sample data:")
print(w_a_con.head())
print('\nShape of the dataframe: ',w_a_con.shape)
print('\nNumber of rows: ',w_a_con.shape[0])
print('\nNumber of column: ',w_a_con.shape[1])
print("\nExtract Column Names:")
print(w_a_con.columns)
