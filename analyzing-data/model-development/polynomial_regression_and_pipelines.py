import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data", names = headers)


# generate a 3rd order polynomial regression
#f = np.polyfit(x, y, 3)
#p = np.poly1d(f)

pr=PolynomialFeatures(degree=2, include_bias=False)
pr.fit_transform([[1,2]])

# a medida que el la dimension del polinomio crece nos interesa normalizar multiple features usando scikit-learn
scale = StandardScaler()
scale.fit(x_data[['highway-mpg', 'horsepower']])
x_scale = scale.transform(x_data[['highway-mpg', 'horsepower']])

# usando pipeline library para simplicar el codigo
input = [('scale', StandardScaler()), ('poly', PolynomialFeatures(degree=2, include_bias=False),('mode', LinearRegression))]
pipe = Pipeline(input)
# train the pipeline
pipe.fit(df[['highway-mpg', 'horsepower']], y)

# produce prediction
yhat = pipe.predict(x[['highway-mpg', 'horsepower']])