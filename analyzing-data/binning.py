# Grouping the values into 'bins', for example bin 'age' into [0 to 5], [11 to 15]
# Convert numeric into canonical variable
# Group a set of numerical values into a set of bins
# Can improve accuracy of the predictive models
# Using bins we can categorize the price into three bins: low, medium, high

import numpy as np
import pandas as pd

path = "../files/auto.csv"
df = pd.read_csv(path, header=None)

# headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
#          "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
#          "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
#          "peak-rpm","city-mpg","highway-mpg","price"]

# Example:
# numpy function 'linspace()' to return  array 'bins_array' that contains 4 equally spaced numbers over the specified interval of the price
bins = np.linspace(min(df["price"]), max(df["price"]), 4)

# Create a list that contains bins names:
group_names = ["Low", "Medium", "High"]

# Function cut to segment and sort data values
df = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)