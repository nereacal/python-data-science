# Plot a regression plot

from sklearn.linear_model import LinearRegression
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data", names = headers)

# x es el nombre de las column que contiene la variable indepenient y la variable dependent
sns.regplot(x = "num-of-doors", y = "normalized-losses", data =df)
plt.ylim(0,)

# Residual plot represents the error between the actual model value.

# create a residual plot
sns.residplot(df['highway-mpg'], df['price'])

lm = LinearRegression()
x = df[['highway-mpg']]
y = df[['price']]
lm.fit(x, y)
yhat = lm.predict(x)

# Distributed plot counts the predicted value versus the acutal value.
# Create a distributed plot
ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.displot(yhat, hist=False, color="g", label="Fitted Values", ax=ax1)