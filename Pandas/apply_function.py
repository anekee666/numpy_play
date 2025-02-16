import pandas as pd
df = pd.read_csv('sbux.csv')

def date_to_year(row):
  return int(row['date'].split('-')[0])

df.apply(date_to_year, axis=1)
df['year'] = df.apply(lambda row:int(row['date'].split('-')[0]), axis=1)
print(df.head())