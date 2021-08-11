import pandas as pd

col_val = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
data = pd.read_csv('teraterm.log', columns=col_val)
print(data)