# Specialized visualization tools


## [Pie Charts](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@155e435d066a4a22a2c7a2994308e709/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@d88b0f7488fe4b0b99d06d7d4c2f43c3)
------

A pie chart is a circular statistical graphic divided into slices to illustrate numerical proportion.  
How to generate a pie chart:  
```
df.plot(kind='pie')
```


## [Box Plots](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@d0cea537238c47a0ac4835e1463a3c7d/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@f40e5aa8a6f74e80a69d8e56d19a7239)
--------

A boxplot is a way of statistically representing the distribution of given data through 5 main dimensions:
- 1D is minimum: smallest number of the sorted data. Its value can be obtained by subtracting 1.5 times the IQR where IQR is interquartile range
from the first quartile.
- 2D is first quartile (25%) of the sorted data. In other words, 1/4 of the data points are less than this value.
- 3D is the median
- 4D is the third quartile (75%). In other words, 3/4 of the data points are less than this value.
- 5D is maximum which is the highest number of the sorted data where
maximum equals third quartile summed with 1.5 multiplied by IQR.

How to generate a boxplot:  
```
df.plot(kind='box')
```

![](https://github.com/nereacal/python-data-science/blob/main/visualizing-data/images/boxplots.jpeg)


## [Scatter Plots](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@8f960392dacc48bebb8230b9efad3f8b/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@082bdf544064463fb862d141807ee4a3)
----
A scatter plot is a type of plot that displays values pertaining to
typically two variables against each other. Usually it is a dependent variable
to be plotted against an independent variable in order to determine if any
correlation between the two variables exists.

How to generate a boxplot:  
```
df.plot(kind='scatter', x='year', y='total')
```