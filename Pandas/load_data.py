import pandas as pd
df = pd.read_csv('sbux.csv')
print(type(df))
print(df.head(10))
print(df.tail())
print(df.info())