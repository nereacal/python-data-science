import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data")
print(df)

# Normalize columns so they can have same mean and standard deviation
# Simple feature scaling:
df['normalized-losses'] = df['normalized-losses'] / df['normalized-losses'].mean()
# Min-max method:
df['normalized-losses'] = (df['normalized-losses'] - df['normalized-losses'].min()) / (df['normalized-losses'].max() - df['normalized-losses'].min())
# z-score:
df['normalized-losses'] = (df['normalized-losses'] - df['normalized-losses'].mean()) / df['normalized-losses'].std()
