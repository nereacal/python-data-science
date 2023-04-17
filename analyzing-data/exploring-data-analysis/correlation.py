import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data", names = headers)
print(df)

# Find the correlation between the following columns: bore, stroke, compression-ratio, and horsepower.
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()

# Continuous numerical variables are variables that may contain any value within some range. 
# In order to start understanding the (linear) relationship between an individual variable and the price, we can use "regplot" which plots the scatterplot plus the fitted regression line for the data.
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
# Correlation between engine-size and price.
df[["engine-size", "price"]].corr()

# Highway mpg is a potential predictor variable of price. Let's find the scatterplot of "highway-mpg" and "price".
sns.regplot(x="highway-mpg", y="price", data=df)

# We can examine the correlation between 'highway-mpg' and 'price' and see it's approximately -0.704.
df[['highway-mpg', 'price']].corr()


# Weak Linear Relationship
sns.regplot(x="peak-rpm", y="price", data=df)
# Peak rpm does not seem like a good predictor of the price at all since the regression line is close to horizontal. Also, the data points are very scattered and far from the fitted line, showing lots of variability. Therefore, it's not a reliable variable.
df[['peak-rpm','price']].corr()

# Find the correlation between x="stroke" and y="price".
df[["stroke","price"]].corr()
#The correlation is 0.0823, the non-diagonal elements of the table.

# Given the correlation results between "price" and "stroke", do you expect a linear relationship?
#There is a weak correlation between the variable 'stroke' and 'price.' as such regression will not work well. We can see this using "regplot" to demonstrate this.
sns.regplot(x="stroke", y="price", data=df)



# Categorical variables: These are variables that describe a 'characteristic' of a data unit, and are selected from a small group of categories. The categorical variables can have the type "object" or "int64". A good way to visualize categorical variables is by using boxplots.
# Relationship between body-style and price.
sns.boxplot(x="body-style", y="price", data=df)

# We see that the distributions of price between the different body-style categories have a significant overlap, so body-style would not be a good predictor of price. Let's examine engine "engine-location" and "price":
sns.boxplot(x="engine-location", y="price", data=df)
# ere we see that the distribution of price between these two engine-location categories, front and rear, are distinct enough to take engine-location as a potential good predictor of price.
