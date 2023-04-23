import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv", names = headers)
df.describe()

# question 1
df.dtypes

# question 2
df.drop("id", axis = 1, inplace=True)
df.drop("Unnamed: 0", axis = 1, inplace=True)
df.describe()

# question 3
df['floors'].value_counts().to_frame()

# question 4
sns.boxplot(x="waterfront", y="price", data=df)

# question 5
sns.regplot(x="sqft_above", y="price", data=df)

# question 6
X = df[['sqft_living']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)

# question 7
# Normalize bedrooms
avg_val_bedrooms = df["bedrooms"].astype("float").mean(axis=0)
df["bedrooms"].replace(np.nan, avg_val_bedrooms, inplace = True)
# Normalize bathrooms
avg_val_bathrooms = df["bathrooms"].astype("float").mean(axis=0)
df["bathrooms"].replace(np.nan, avg_val_bathrooms, inplace = True)
# Fit
X = df[['floors', 'waterfront', 'lat', 'sqft_basement', 'view', 'sqft_living15', 'sqft_above', 'grade', 'sqft_living', 'bathrooms', 'bedrooms']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)

# question 8
Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(X, Y)
pipe.score(X, Y)

# question 9
ridge_object = Ridge(alpha=0.1)
ridge_object.fit(X, Y)
ridge_object.score(X, Y)

# question 10
pr = PolynomialFeatures(degree=2)
x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.fit_transform(x_test)
ridge_object_pr = Ridge(alpha=0.1)
ridge_object_pr.fit(x_train_pr, y_train)
print("Test data R^2: ",ridge_object_pr.score(x_test_pr, y_test))
print("Train data R^2: ",ridge_object_pr.score(x_train_pr, y_train))