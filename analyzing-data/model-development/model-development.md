# Model development

- Simple and multiple linear regression
- model evaluation using visualization
- Polynomial regression and pipelines
- R-squared and MSE for In-Sample Evaluation
- Prediction and decision making
  
Model development: mathematical equation used to predict a value given one or more values. Relating one or more independent variables to dependent variables.
In a regression plot, the horizontal axis represents the independent variable and the vertical axis represents the dependent variable.


## Linear Regression
-----
First we fit a simple linear model and then we obtain a prediction.  
Define the predictor variable and target variable:  
```
X = df[['highway-mpg']]
Y = df['price']
```   
Then use lm.fit(X,Y) to fit the model  
```
lm.fit(X,Y)
```  
Obtain the prediction  
``` 
Yhat = lm.predict(X)
``` 


## Multiple Linear Regression
----
Used to explain relationships between one continuous target y variable and 2 or more predictor x variables.  
Extract 4 predictor variables and store them in z variable then train the model and obtain the prediction:
```
z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(z, df['price'])
Yhat = lm.predict(X)
```


## Model Evaluation using Visualization
---

**Regression plot**:  
Gives a good estimate of the relationship between 2 variables, the strength of the correlation and the direction of the relationship (positive or negative).  
With function regplot, the first argument x is the independent variable and the second argument y is the name of the column that contains the name of the dependent variable or target. The parameter data is the name of the dataframe. The result is the given plot.
```
sns.regplot(x = "highway-mpg", y="price",data=df)
plt.ylim(0,)
```  


**Residual plot**:  
Represents the error between the actual value.  
A residual plot is a graph that shows the residuals on the vertical axis and the independent variable on the horizontal axis. If the points in a residual plot are randomly dispersed around the horizontal axis, a linear regression model is appropriate for the data; otherwise, a nonlinear model is more appropriate.

Use seaborn to create a residual plot:
```
sns.residplot(df['highway-mpg'], df['price'])
```
The first parameter is a series of dependent variable or feature.
The second parameter is a series of dependent variable or target.
We see in this case, the residuals have a curvature.
A distribution plot counts the predicted value versus the actual value.


**Distribution plots:**  
A distribution plot counts the predicted value versus the actual value.
The code for distribution plots:
```
ax1 = sns.distplot(df['price'], hist=False, color='r', label='Actual Value')
sns.distplot(Yhat, hist=False, color='b', label='Fitted Values', ax=ax1)
```


## Polynomial Regression and Pipelines
----  
The polynomial regression is a special case of the general linear regression model and useful for describes curvilinear relationships (is what you get by squaring or getting higher order terms of the predictor variables in the model transforming the data).  
Types of polynomial regression:  
- Quadratic - 2nd order: the predictor variable in the model is squared.
- Cubic - 3rd order: the predictor variable in the model is cubed.
- Higher order: when a good fit hasn't been archived by second or third.

Example of third order:  
```
f = np.polyfit(x, y, 3)
p = np.polyld(f)
print(p)
```

We can also have multi dimensional polynomial linear regression.  
Example of a 2 dimensional second order polynomial:  
Create a polynomial feature object, the constructor takes the degree of the polynomial as a parameter
```
from sklearn.prepocessing import PolynomialFeatures
pr = PolynomialFeatures(degree=2, include_bias=False)
pr.fit_transform([[1,2]])
```

As the dimension of the data gets larger, we may want to normalize multiple features in scikit-learn. 
Instead we can use the preprocessing module to simplify many tasks.  
For example, we can standardize each feature simultaneously.
We import StandardScaler. We train the object, fit the scale object,
then transform the data into a new data frame on array x_scale.
```
from sklearn.preprocessing import StandardScaler
SCALER = StandardScaler()
SCALER.fit(x_data[['horsepower', 'highway-mpg']])
x_scale = SCALER.transform(x_data[['horsepower', 'highway-mpg']])
```


### Pipeline
We can simplify our code by using a pipeline library. Pipeline sequencially perform a series of transformations (Normalization, Polynomial Transform, Linear regression)
First create a list of tuples, first element is the name of the estimator model, second element contains the model constructor. Then input the list in the pipeline constructor. We can train the pipeline by applying the train method to the pipeline object.  

```
from sklearn.prepocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(degree=2), 'mode', LinearRegression())]

pipe = Pipeline(input)
```

We can also produce a prediction. The method normalizes the data, performs a polynomial transform, then outputs a prediction.
```
pipe.fit(df[['horsepower', 'highway-mpg', 'curb-weight', 'engine-size']], y)
yhat = pipe.predict(x[['horsepower', 'highway-mpg', 'curb-weight', 'engine-size']])
```