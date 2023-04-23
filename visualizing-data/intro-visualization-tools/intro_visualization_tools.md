# Introduction to Visualization tools


## [Matplotlib Architecture](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@0bbe2601174649b78e44d5721ab666b7/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@3e2878d4fdcb432c8033e0c67881db2a)
-------------------

Matplotlib **architecture** composed of:
- Backend layer (FigureCanvas, Renderer, Event)
- Artist layer (Artist)
- Scripting layer (pyplot)


> ### Backend Layer
> 3 built-in abstract interfaces classes:
> - ``matplotlib.backend_bases.FigureCanvas``: Ecomposses the area onto which the figure is drawn
> - ``matplotlib.backend_bases.Renderer``: Knows how to draw on the FigureCanvas
> - ``matplotlib.backend_bases.Event``: Handles user inputs such as keyboard strokes and mouse clicks.
> </br>  

> ### Artist Layer
> 1 main object: Artist. Knows how to use the Renderer to draw the canvas.  
> Everything on a figure is an artist (Title, lines, images...), they are artist instances  
> 2 type of objects:
> - Primitive: Line2D, Rectangle, Circle and text
> - Composite: Axis, Tick, Axes and Figure. Each composite artist may contain other composite artists as well as primitive artists.  
> Example to generate histogram of some data:
>> ```
>> from matplotlib.backends.backend_agg import FigureCanvas
>> from matplotlib.figure import Figure
>> fig = Figure()
>> canvas = FigureCanvas(fig)
>> 
>> import numpy as np
>> x = np.random.randn(1000)
>> 
>> ax = fig.add_subplot(111) # create an axes artist
>> ax.hist(x, 100) #generate a histogram of the 1000 numbers
>> ax.set_title('Normal distribution with $\mu=0, \sigma=1$') #set the title
>> ```
>> ![](https://github.com/nereacal/python-data-science/blob/main/visualizing-data/images/artist_layer.jpeg)
> </br> 

> ### Scripting Layer
> 1 scripting interface - **pyplot**: automates the process of defining a canvas and defining a figure artist instance and connecting them.
>> ```
>> from matplotlib.pyplot import plt
>> import numpy as np
>> 
>> x = np.random.randn(1000)
>> plt.hist(x ,100)
>> plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
>> plt.show()
>> ```
> </br> 

## [Matplotlib - Plot Function](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@5954a0d4016a4346b83ff34bd5edef84/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@b23f8327de4a41f8b34323f5f7aae695)
-------

How to with pyplot:  
```
%matplotlib inline # to perform code in the same page browser
import matplotlib.pyplot as plt

plt.plot(5, 5, 'o') # plot circular mark at the position(5, 5)
plt.show()

# When using pandas and there is a DataFrame:
data_frame_name["column_name"].plot(kind="hist")
```

  
  ## [Line Plot](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@570a870ea5764dbf85ed5c91a915648e/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@0fdf3503de7f4904b550a0bcca1f0301)
  -----
Line plot is a type of plot which displays information as a series of data points called 'markers' connected by straight line segments.  
Example: 
```
import matplotlib as mpl
import matplotlib.pyplot as plt

years = list(map(str, range(1980, 2014)))
df_canada.loc['Haiti', years].plot(kind='line')
plt.title('Inmigration from Haiti')
plt.xlabel('Years')
plt.ylabel('Number of inmigrants')
plt.show()
```

