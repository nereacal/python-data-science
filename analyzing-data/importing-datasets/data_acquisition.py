import pandas as pd
import numpy as np
import requests

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data", names = headers)
print(df)

# Replace headers and recheck dataframe:
df.columns = headers
df.head(10)

# Replace '?' symbol with NaN so the dropna() can remove missing values
df1=df.replace('?',np.NaN)

#We can drop missing values along the column "price" as follows:
df=df1.dropna(subset=["price"], axis=0)
df.head(20)

# Save dataset
# index=False means the row names will not be written
df.to_csv("automobile.csv", index=False)


# Rename columns
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
# Or rename the existing DataFrame (rather than creating a copy) 
df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
