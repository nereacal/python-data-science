# Linear regression will refer to one independent variable (predictor x) and one dependent variable (target y)
# y = b0 + b1x 
# b0 = the intercept
# b1 = the slope
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

# Define the predictor and target variables
x = df[['highway-mpg']]
y = df[['price']]

# Fit the model
lm.fit(x, y)

# Obtain the prediction
yhat = lm.predict(x)

# El intercept (b0) es un atributo de lm:
lm.intercept_

# El slope (b1) es un atributo de lm:
lm.coef_