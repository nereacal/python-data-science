# Exploring data analysis (EDA)
Approach to analyze data in order to summarize main characteristics of the data gain better understanding of the data set, uncovering relationships between different variables, and extract important variables. For example, try to get which characteristics have more impact on the price car.


## Modules

> ### Descriptive statistics  
> ------------------------
> To obtain a short summary about the sample and measures of the data.  
> - **describe()** funtion in panda and appliying it to a dataframe will automatically compute basic statistics for all numberical variables.  
> Any NaN values will be skipped  
> - **value_counts()** function to summarize the quantity of each value in the dataframe.  
> - **boxplot()** function display outliers as individuals dots that occur outside the upper and lower extremes.


> ### GroupBy  
> ------------------------
> To obtain a short summary about the sample and measures of the data.  
> Can be used to know if there is any relationship between one variable and another or to know which category of a variable can add more value to the object.  
>> **groupBy()** is used on categorical variables, groups the data into subsets according to different categories of that variable.  
>> Can group by single or multi variable passing variable names  
>> We would pick out the data columns that we are interested in:  
>> ``df_test = df[['drive-wheels', 'body-style', 'price']]``  
>> Group reduced data according to drive-wheels and body style:  
>> ``df_grp = df_test.groupby(['drive-wheels', body-style'] as_index=False).mean()``  
>> The data is now grouped into subcategories and only the average price of each category is shown.  
>
>> **pivot()** to convert table to a pivot table. A pivot table has one variable displayed along the columns and the other variable displayed along the rows.  
>> ``df_pivot = df_grp.pivot(index='drive-wheels', columns='body-style')``  
>
>> **heatmap()** takes a rectangular grid of data and assigns a color intensity based on the data value at the grid points.  
>> ``plt.pcolor(df_pivot, cmap='RdBu')``  
>> ``plt.colorbar()``  
>> ``plt.show()``  
>

> ### Correlation  
> ------------- 
> statistical metric for measuring to what extent different variables are interdependent. Or in other words, to see how if one variable changes over time how will affect the other variable.
> Visualize 2 variables using scatter plot and an added linear line called a regression line, which indicates the relationship between the 2. 
> We will see whether the engine size has any impact on the price.  
> ``sns.regplot(x="engine-size", y="price", data=df)``  
> ``plt.ylim(0,)``  
> Use seaborn.regplot to create the scatter plot.  
> *A weak positive correlation indicates that, although both variables tend to go up in response to one another, the relationship is not very strong.*  
> *A strong negative correlation, on the other hand, indicates a strong connection between the two variables, but that one goes up whenever the other one goes down.*  
> ![](https://github.com/nereacal/python-data-science/blob/main/analyzing-data/images/StrongWeak_Positive_Correlation.jpeg)  
>

> ### Correlation statistics
> -------------  
> Measure the strength of the correlation between 2 features.
> Pearson's correlation will give 2 values: the correlation coefficient and the P-value.  
>> **Correlation coefficients**:  
>> - Close to +1: Large Positive relationship
>> - Close to -1: Large Negative relationship 
>> - Close to 0: No Relationship
>
>> **P-value**:  
>> - P-value < 0.001 Strong certainly in the result.  
>> - P-value < 0.05 Moderate certainly in the result. 
>> - P-value < 0.1 Weak certainly in the result.
>> - P-value > 0.1 No certainly in the result.  
>
>> **Strong correlation**: 
>> - Correlation coefficient close to 1 or -1
>> - P value less than 0.001  
>
> ``pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])``
>




