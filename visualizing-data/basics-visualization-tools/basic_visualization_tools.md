# Visualization Tools


## [Area Plots](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@2d204ac4fa3143048a998da7e53702d7/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@bc103d3618c54b20891e959ff7e8842b)
-------
An extension of the line plot. Area plot is an area chart of graph that depicts accumulated totals using numbers or percentages over time.  Used when trying to compare 2 or more quantities.  

Generate area plots:
```
import matplotlib as mpl
import matplotlib.pyplot as plt

df.plot(kind='area')
```

## [Histograms](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@6c377c9edbc6442c8612bee3250e9639/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@e9711cfbbbe1467f844fbfed9ec3f9c7)
------
Is a way of representing the frequency distribution of a variable.  
 The way it works is it partitions the spread of the numeric data into bins, assigns each datapoint in the dataset to a bin, and then counts the number of datapoints that have been assigned to each bin. So the vertical axis is actually the frequency or the number of datapoints in each bin.
Generate area plots:
```
import matplotlib as mpl
import matplotlib.pyplot as plt

df.plot(kind='hist')
```
If bins are not aligned to the tick marks on the horizontal axis:
```
import numpy as np

count, bing_edges = np.histogram(df_canada['2013'])
df_canada['2013'].plot(kint='kist', xticks=bin_edges)
```
What this function is going do is it is going to partition the spread of the data in column 2013 into 10 bins of equal width, compute the number of datapoints that fall in each bin, and then return this frequency of each bin which we're calling count here and the bin edges which we're calling bin_edges.


## [Bar Charts](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@87a6f38e1c6f407b86a1aabbb5e326c2/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@576c4c9c1344484eb87be592ad4e8ced)
------
Is a type of plot where lenght of each bar is proportional to the values of a variable at a given point of time.
```
df.plot(kind='bar')
```

