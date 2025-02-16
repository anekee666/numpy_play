import pandas as pd
df = pd.read_csv('sbux.csv')
print(df.columns)
# columns can be assigned
df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'name']
print(df.columns)
print(df['open'])
print(df[['open', 'close']])
print(type(df['open'])) # pandas.core.series.Series
print(type(df[['open', 'close']])) #pandas.core.frame.DataFrame
print(df.iloc[0])
print(df.loc[0])
df2 = pd.read_csv('sbux.csv', index_col='date')
print(df2.head())
print(df2.loc['2013-02-08'])
print(type(df2.loc['2013-02-08'])) #pandas.core.series.Series
print(df[df['open'] > 64])
print(df[df['name'] != 'SBUX'])
# don't want "objects" when we're doing math!
print(df.values)
A = df[['open', 'close']].values
print(type(A)) #numpy.ndarray
# write a dataframe to file
smalldf = df[['open', 'close']]
# what if we don't want an index column?
smalldf.to_csv('output.csv', index=False)