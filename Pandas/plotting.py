import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
df = pd.read_csv('sbux.csv')
df['open'].hist()
plt.show()
df['open'].plot()
plt.show()
df[['open', 'high', 'low', 'close']].plot.box()
plt.show()
scatter_matrix(df[['open', 'high', 'low', 'close']],
               alpha=0.2, figsize=(6, 6))
plt.show()