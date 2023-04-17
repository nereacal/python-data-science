
import pandas as pd
import numpy as np

path = "../files/auto.csv"
df = pd.read_csv(path, header=None)

# headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
#          "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
#          "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
#          "peak-rpm","city-mpg","highway-mpg","price"]


# Normalize columns so they can have same mean and standard deviation
# Simple feature scaling:
df['normalized-losses'] = df['normalized-losses'] / df['normalized-losses'].mean()
# Min-max method:
df['normalized-losses'] = (df['normalized-losses'] - df['normalized-losses'].min()) / (df['normalized-losses'].max() - df['normalized-losses'].min())
# z-score:
df['normalized-losses'] = (df['normalized-losses'] - df['normalized-losses'].mean()) / df['normalized-losses'].std()
