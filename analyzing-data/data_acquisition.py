import pandas as pd
import matplotlib
import scipy
import numpy as np
import requests

async def download(url, filename):
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    response = requests.request("GET", url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
            

async def load_data(path):
    await download(path, "auto.csv")
    df = pd.read_csv(path, header=None)
    return df

path = "../files/auto.csv"
df = load_data(path)
print("The first 5 rows of the dataframe") 
df.head(5)

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

# Replace headers and recheck dataframe:
df.columns = headers
df.head(10)


# Replace '?' symbol with NaN so the dropna() can remove missing values
df1=df.replace('?',np.NaN)

#We can drop missing values along the column "price" as follows:
df=df1.dropna(subset=["price"], axis=0)
df.head(20)

# Save dataset
df.to_csv("automobile.csv", index=False)
