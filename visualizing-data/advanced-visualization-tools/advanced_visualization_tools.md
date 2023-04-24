# Advanced Visualization Tools

## [ Seaborn and Regression Plots](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@ee60a97bbc384edfbd7a5fc0a7040c47/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@a7cca2aca5514978bceffda2cedab9f0)
------
Is a visualization library based on Matplotlib. Can generate plots with code that is 5 times less than with Matplotlib.

How to generate a regression plot with seaborn:
```
import seaborn as sns

ax = sns.regplot(x='year', y='total', data=df, color='black', marker='+')
```
Params used:
- color: to change the color of the line in the regression plot
- marker: to change the marker
