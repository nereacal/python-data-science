# Obtain relationship between one continuous target y variable and 2 or more predictor x variables.
# y = b0 + b1*x1 + b2*x2 +... + bn*xn

from sklearn.linear_model import LinearRegression
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

lm = LinearRegression()

# Extract predictor x variables and store in z
z = df[['horsepower','peak-rpm','city-mpg','highway-mpg']]

# train the model
lm.fit(z, df['price'])

# obtain the prediction
yhat = lm.predict(z)