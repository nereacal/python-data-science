# [Model evaluation](https://learning.edx.org/course/course-v1:IBM+DA0101EN+2T2021/block-v1:IBM+DA0101EN+2T2021+type@sequential+block@55c6b7920eca44d0a0e0fe4aed2d557d/block-v1:IBM+DA0101EN+2T2021+type@vertical+block@db264a515adf4a558de5d37ac6dd52c7)

In-sample evaluation tells us how well our model fits the data already given to train it. In-sample data or training data to train the model. The rest of the data called Test Data is used as out-of-sample data.
Test data is used to approximate how the model performs the real world. For that we split the dataset of data and the larger portion of data is used for training the smallest part is used for testing.
Ex: 70% to train and 30% to test.

A function to split datasets is ``train_test_split()``. This function randomly splits the dataset into training and testing subsets.
```
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=0)
```

x_data = features or independetn vairables  
y_data = data target  
x_train y y_train = parts of available data as training  
x_test y y_test = parts of available data as test  
test_size = percentage of data for testing (30%)  
random_state = number generator used for random sampling  


## Generalization performance
----------
Generalization error is measure of how well our data does at predicting previosly unseed data. the error obtained using our testing data is an approximation of this error.

If fewer data points are used to train the model and more to test the model, the accuracy of the generalization performance will be less, but the model will have a good prediction.  
If error estimates points are relatively together but they are futher away from the true generalization, then this is called **cross-validation**.  
To apply cross-validation we used:  
```
from sklearn.model_selection import cross_val_score

scores = cross_val_score(lr, x_data, y_data, cv=3)
np.mean(scores)
```
lr is the linear regression model or object  
x_data is the predictive variable data  
y_data is the target variable data  
cv is the number of partitions  
The function returns an array of scores  
mean() function to average the result together to estimate out of sample R^2  

*What if we want to know the actual predicted values supplied by our model before the r squared values are calculated?*  
To do this, we use the cross_ val_predict function.
The input parameters are exactly the same as the cross_val_score function,
but the output is a prediction.  
```
from sklearn.model_selection import cross_val_predict

yhat = cross_val_predict(lr, x_data, y_data, cv=3)
```

  

## [Overfitting, Underfitting, and model selection](https://learning.edx.org/course/course-v1:IBM+DA0101EN+2T2021/block-v1:IBM+DA0101EN+2T2021+type@sequential+block@03bd4d2f86e749969eb6ebf6f9ff46a5/block-v1:IBM+DA0101EN+2T2021+type@vertical+block@d72ad6117a524ad784dbefd6ae46eb5e)
---------

In this section, we will discuss how to pick the best polynomial order and problems that arise when selecting the wrong order polynomial.  
The goal of Model Selection is to determine the order of the polynomial to provide the best estimate of the function y(x).  
When the model is to simple to fit the data we call it ***underfitting***.  
![](https://github.com/nereacal/python-data-science/blob/main/analyzing-data/images/underfitting.jpeg) 


With the following picture we can see an 8th order polynomial, the model does extremely well at tracking the training point but performs poorly at estimating the function. This is specially apparent where there is little training data. The estimated function oscillates not tracking the function. This is ***Overfitting***  
![](https://github.com/nereacal/python-data-science/blob/main/analyzing-data/images/overfitting.jpeg)  

---
***Overfitting** occurs when a function is too closely fit to the training data points and captures the noise of the data.   
**Underfitting** refers to a model that can't model the training data or capture the trend of the data.*

-------

![](https://github.com/nereacal/python-data-science/blob/main/analyzing-data/images/model_selection.jpeg) 

Calculate different R^2 values as follows:
```
rsqu_test = []
order = [1, 2, 3, 4]

for n in order:
    pr = PolynomialFeatures(degree=n)
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])
    lr.fit(x_train_pr, y_train)
    rsqu_test.append(lr.score(x_test_pr, y_test))

```
First we create an empty list to store the values  
We create a list containing different polynomial orders  
We then iterate through the the list  
We create a polynomial feature object with the order of the polynomial as a parameter  
We transform the training and test data into a polynomial using the fit transform function  
We fit the regression model using the transform data  
We then calculate the R^2 using the test dta and store in the array  
  

## [Ridge Regression](https://learning.edx.org/course/course-v1:IBM+DA0101EN+2T2021/block-v1:IBM+DA0101EN+2T2021+type@sequential+block@6143fb2d7d9349f7a802d87df7f76115/block-v1:IBM+DA0101EN+2T2021+type@vertical+block@74e0abcb7419407787be07de56b886fd)
--------
Prevents overfitting. Overfitting is a big problem when you have multiple independent variables or features.  
  
***Ridge regression** is a regression that is employed in a Multiple regression model when Multicollinearity occurs.*


***Alpha*** is the parameter we select before fitting or training the model to control the magnitude of the polynomial.  
As alpha increases, the parameters get smaller.
This is most evident for the higher order polynomial features.  
Make a prediction using ridge regression:
```
from sklearn.linear_model import Ridge
ridge_model = ridge(alpha=0.1)
ridge_model.fit(x, y)
yhat = ridge_model.predict(x)
```

***When there are signs of non flexibility in a graph, then underfitting starts. When alpha gets higher, then underfitting appears.***


## [Grid Search](https://learning.edx.org/course/course-v1:IBM+DA0101EN+2T2021/block-v1:IBM+DA0101EN+2T2021+type@sequential+block@ff80025726d347febbdcd363af9d213b/block-v1:IBM+DA0101EN+2T2021+type@vertical+block@03d4011dcf10495cba43a0e9f66d77a2)
------
Grid Search allows us to scan through multiple free parameters with few lines of code.  
The value of your Grid Search is a Python list that contains a Python dictionary.
The key is the name of the free parameter.
The value of the dictionary is the different values of the free parameter:
```
parameters = [{'alpha':[1, 10, 100, 1000]}]
```
To create an object of grid search takes on the scoring method, in this case:
- R^2 the number of folds
- The model or object
- the free parameters values

```
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

parameters = [{'alpha':[1, 10, 100, 1000, 10000, 100000]}]
rr = Ridge()
grid1 = GridSearchCV(rr, parameters, cv=4)
grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpt']], y_data)
grid1.best_estimator_
scores = grid1.cv_results_
scores['mean_test_score']
```
We create a ridge regression object or model.  
We then create a GridSearchCV object.
The inputs are the ridge regression object, the parameter values, and the number of folds. We will use R-squared.  This is the default scoring method.  
We fit the object.  
Find the best values for the free parameters using the attribute best estimator.  
We can also get information like the mean score on the validation data using the attribute CV result.  

We can print out the score for the different free parameter values:
```
for param, mean_val, mean_test in inzip(scores['params'], scores['mean_val'], scores['mean_test']):
    print(param, "R^2 on test data: ", mean_test,"R^2 on train data: ", mean_val)
```