# For model training only take number as input
# Problem: Most statistical models cannot take object or strings as input

import numpy as np
import pandas as pd

path = "../files/auto.csv"
df = pd.read_csv(path, header=None)

# Example: Fuel of a car can be gas or fuel, both strings.
# For fuel analysis, values should be converted to numberical format.
# Create encoding for the values by adding features corresponding to each unique value (0, 1). When value occurs, set value to 1. This technique is called 'One-Hot Encoding'.
# With pandas, use get_dummies() function to create one-hot encoding.

pd.get_dummies(df['Fuel_Type'])