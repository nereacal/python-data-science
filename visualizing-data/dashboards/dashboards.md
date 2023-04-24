# Creating dashboards with Plotly and Dash

## [Dashboarding overview](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@fdc7444acb784622b44dde577475affd/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@3043c80e72204cba89c25f48417dfa1b)
------

- Real-time visuals
- Undesrtanding business moving parts
- Visually track, analyze and display key performance indicators(KPI)
- Reduce hours of analyzing

Web-based dashboarding tools:
- Dash: Framework for building web analytic app.
- Panel: make plotting libraries instantly viewable
- Voila: turns Jupyter notebooks into standalone web applications.
- Streamlit: python scripting, treat widgets as variables, and reuse data and computation.

Other dashboard tools:
- Bokeh: is a plotting library, a widget and app library. It acts as a server for both
plots and dashboards.
- ipywidgets: provides an array of Jupyter-compatible widgets
and an interface supported by many Python libraries, but sharing as a dashboard requires a separate deployable server like Voila.
- Matplotlib: is a comprehensive library for creating static, animated, and interactive visualizations in Python.
- Bowtie: allows users to build dashboards in pure Python.
- Flask: is a Python-backed web server that can be used to build arbitrary web sites, including those with Python plots that function as flask dashboards.


## [Plotly](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@e2f3c70616cf4855a2dcc065c02a284b/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@4b1c9e8935f147f6894d0add18a0c808)
-----
Interactive plotting library. Includes charts types like statistical, financial, maps, scrientific and 3D data.  
Plotly submodules:
- Graph objects: low-level interface to figures, traces and layout.
- Express: High-level wrapper.


## [Dash](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@4a88065df2134adfb8295157a895e1f2/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@520f1680aa354be38ad3e6a0b732c09c)
------
Dash applications are web servers running Flask and communicating JSON packets over HTTP requests.
Dash’s frontend renders components using React.js. It is easy to build a Graphical User Interface
using dash as it abstracts all technologies required to build the applications.  
Dash components:
- Core components
- HTML components
  

## [Dash Interactive components](https://learning.edx.org/course/course-v1:IBM+DV0101EN+1T2021/block-v1:IBM+DV0101EN+1T2021+type@sequential+block@84fc4ee3ea1a478d8cca76e57861fbb2/block-v1:IBM+DV0101EN+1T2021+type@vertical+block@738f526d68b24f678248b9823189b7cd)
------
A callback function is a python function that is automatically called by Dash whenever an input component's property changes.
Callback function is decorted and tells whenever there is a change in the input component value.  
Decorate the callback function with @app.callback decorator.
This takes two parameters:
- Output : This sets result returned from the callback function to a component id 
- Input: This set input provided to the callback function to a component id