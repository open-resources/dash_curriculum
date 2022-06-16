# Chapter 13: Improving app performance

## What you will learn

By now, you have everything together to get your first app up and running using even advanced components, layouts and callbacks. As dashboards are designed for data analysis and visualisations at some point you might run into efficiency constraints when the amount of data you are working with gets growing. To circumvent any possible performance lacking this chapter will give you some insights on improving your app performance. You'll learn about the built-in Dash Developer Tools, how to plot massive amount of data with higher performing plotly graphs and how to use caching for improving the performance of your app. 

```{admonition} Learning Intentions
- Dash Developer Tools
- Higher Performing Plotly graphs
- Caching
```

## 13.1 Introduction

Let's kick off with a simple app where for a selected country we want to display the life expectation over the years as a scatter plot. To better understand how a growing data set affects the app performance we duplicate the underlying data set by a value of our choice using a range slider. With the growth of the underlying data set also the data points in the scatter plot will be resized. Last, we use the `datetime` package to stop the time our app is loading. All in all, we receive the following app:
#### [ADD GIF, THAT SHOWS THE APP IN ACTION SELECTING THREE DIFFERENT VALUES IN THE RANGE SLIDER]

````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import numpy as np
import pandas as pd
import plotly.express as px

# Setup data
df = px.data.gapminder()[['country', 'year', 'lifeExp']]
dropdown_list = df['country'].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
markdown_scatter = dcc.Markdown(id='markdown-scatter')
slider = dcc.Slider(id='our-slider', min=0, max=8500, marks=None, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown, width=3), dbc.Col(markdown, width=9)]),
        dbc.Row([dbc.Col(dcc.Graph(id='our-figure'))]),
        dbc.Row([dbc.Col(markdown_scatter)]),
        dbc.Row(dbc.Col(slider)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_markdown(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    title = 'Data points displayed: {:,}'.format(len(df_sub.index) * value_slider)
    return title


@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Output(component_id='markdown-scatter', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    df_new = pd.DataFrame(np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns)
    start_time = datetime.now()
    fig = px.scatter(
        df_new,
        x='year',
        y='lifeExp',
        title='PX scatter plot',
        template='plotly_white',
    )
    fig.update_traces(marker=dict(size=5 + (value_slider / 10000) * 25))
    end_time = datetime.now()
    subtitle = 'Duration for scatter plot loading: {} s'.format(round((end_time - start_time).total_seconds(), 2))
    return fig, subtitle


# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
```

````

When adjusting the range slider we obtain already huge performance differences. Right now, here we analyse about 100 k data points. To handle even much larger data sets you will learn about different graphs to work with as well as how to use stored data to improve app performance. Before that, Dash itself comes with a really handy built-in functionality to better analyse the performance of your app, the Dash Developer Tools. Let's go!

## 13.2 Dash Developer Tools
The Dash Developer Tools is a set of tools to make debugging and developing Dash apps more productive and pleasant. These tools are enabled when developing your Dash app and are not intended when deploying your application to production i.e., in order to make use of the Dash Developer Tools you must run your app with `debug=True`. When you do this your app will always display a blue circular button on the bottom right corner of your app with angle brackets in it. This button will grand you access to error messages or information on your callbacks.

In this tutorial we focus on the Callback Graph. The Dash Developer Tools display a visual representation of your callbacks: which order they are fired in, how long they take, and what data is passed back and forth between the Dash app in the web browser and your Python code.

```{admonition} Dash Developer Tools
For an overview over the other tools look at the [official documentation](https://dash.plotly.com/devtools).
```

The Dash Developer Tools Callback Graph provides Live Introspection, Profiling, and Live Debugging of your callback graph and looks as follows:

![Dash Developer Tools](./ch13_files/dash-dev-tools.png)

Let's go through the different items in more detail:

- The rounded green boxes represent your callback functions.
    - The top number represents the number of times the function has been called.
    - The bottom number represents how long the request took. This includes the network time (sending the data from the browser client to the backend and       back) and the compute time (the total time minus the network time or how long the function spent in Python).
- Click on a green box to see the detailed view about the callback. This includes:
    - `type` Whether the callback was a clientside callback or a serverside callback.
    - `call count` The number of times the callback was called during your session.
    - `status` Whether the callback was successful or not.
    - `time (avg milliseconds)` How long the request took. This is the same as the summary on the green box and is basically split up into the components       `total`, `compute` and `network`.
    - `data transfer (avg bytes)`
    - `outputs` A JSON representation of the data that was returned from the callback.
    - `inputs` A JSON representation of the data that was passed to your callback function as Input.
    - `state` A JSON representation of the data that was passed to your callback function as State.
- The blue boxes represent the input and output properties. Click on the box to see a JSON representation of their current values.
- The dashed arrows (not visible in the screenshot) represent State.
- The dropdown in the top right corner enables you to switch layouts

Now, that you know how to check for the performance of your app, let us learn about different higher performing graphs and how to incorporate them into you app.

## 13.3 Higher Performing Plotly graphs
So far, we have used the `plotly.express` library to implement our graphs. This is a very easy and convenient way to do so. However, most plotly charts are rendered with SVG (Short for Scalable Vector Graphics). This provides crisp rendering, publication-quality image export as SVG images can be scaled in size without loss of quality, and wide browser support. Unfortunately, rendering graphics in SVG can be slow for larger datasets as we have noticed in the first section. To overcome this limitation, in this section we explore the three most popular methods that will speed up your app when working with larger data sets.

### 13.3.1 ScatterGL

First, let us have a look at the [ScatterGL](https://plotly.com/python/line-and-scatter/#large-data-sets) plot which is a WebGL implementation of the scatter chart type. Against plotly charts rendered with SVG, `plotly.js` has WebGL (Short for Web Graphics Library) alternatives to some chart types. WebGL uses the GPU to render graphics which make them higher performing. The ScatterGL plot is the equivalent to the scatter plot you have already built dashboards with. To use it, you are required to import the `plotly.graph_objects` package. The following app let's you compare the different durations for data loading when using a ScatterGL plot.

#### [ADD GIF, THAT SHOWS APP IN ACTION AND COMPARES THE SPEED OF THE TWO SCATTER PLOTS FOR TWO DIFFERENT SLIDER VALUES]

````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Setup data
df = px.data.gapminder()[['country', 'year', 'lifeExp']]
dropdown_list = df['country'].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
markdown_scatter = dcc.Markdown(id='markdown-scatter')
markdown_gl = dcc.Markdown(id='markdown-gl')
slider = dcc.Slider(id='our-slider', min=0, max=50000, marks=None, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown, width=3), dbc.Col(markdown, width=9)]),
        dbc.Row([dbc.Col(dcc.Graph(id='our-figure')), dbc.Col(dcc.Graph(id='our-gl-figure'))]),
        dbc.Row([dbc.Col(markdown_scatter), dbc.Col(markdown_gl)]),
        dbc.Row(dbc.Col(slider)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_markdown(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    title = 'Data points displayed: {:,}'.format(len(df_sub.index) * value_slider)
    return title


@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Output(component_id='markdown-scatter', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    df_new = pd.DataFrame(np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns)
    start_time = datetime.now()
    fig = px.scatter(
        df_new,
        x='year',
        y='lifeExp',
        title='PX scatter plot',
        template='plotly_white',
    )
    fig.update_traces(marker=dict(size=5 + (value_slider / 30000) * 25))
    end_time = datetime.now()
    subtitle = 'Duration for scatter plot loading: {} s'.format(round((end_time - start_time).total_seconds(), 2))
    return fig, subtitle


@app.callback(
    Output(component_id='our-gl-figure', component_property='figure'),
    Output(component_id='markdown-gl', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    df_new = pd.DataFrame(np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns)
    start_time = datetime.now()
    fig = go.Figure(data=go.Scattergl(
        x=df_new['year'],
        y=df_new['lifeExp'],
        mode='markers',
        marker=dict(colorscale='Viridis', size=5 + (value_slider / 30000) * 25),
    ))
    fig.update_layout(
        title='GO gl-scatter plot',
        xaxis_title='year',
        yaxis_title='lifeExp',
    )
    end_time = datetime.now()
    subtitle = 'Duration for gl-scatter plot loading: {} s'.format(round((end_time - start_time).total_seconds(), 2))
    return fig, subtitle


# Run the App
if __name__ == '__main__':
    app.run_server()
```

````

### 13.3.2 Plotly Resampler

Even though the ScatterGL outperforms the px scatter plot, it is still rather slow for large data sets and is delayed when interacting with the data plot e.g., zoom in. That's where the `plotly_resampler` package comes in very handy. This package speeds up the figure by downsampling (aggregating) the data respective to the view and then plotting the aggregated points. When you interact with the plot (panning, zooming, ...), callbacks are used to aggregate data and update the figure.

```{admonition} Plotly Resampler
See also the [documentation on Github](https://github.com/predict-idlab/plotly-resampler) for the plotly resampler package.
```

The following app let's you compare the different durations for data loading when working with the plotly resampler.

#### [ADD GIF, THAT SHOWS APP IN ACTION AND COMPARES THE SPEED OF THE SCATTER PLOTS FOR TWO DIFFERENT SLIDER VALUES AS WELL AS HOW TO ZOOM IN]

````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly_resampler import FigureResampler

# Setup data
df = px.data.gapminder()[['country', 'year', 'lifeExp']]
dropdown_list = df['country'].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
markdown_scatter = dcc.Markdown(id='markdown-scatter')
markdown_gl = dcc.Markdown(id='markdown-gl')
markdown_resampler = dcc.Markdown(id='markdown-resample')
slider = dcc.Slider(id='our-slider', min=0, max=50000, marks=None, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown, width=3), dbc.Col(markdown, width=9)]),
        dbc.Row([dbc.Col(dcc.Graph(id='our-figure')),
                 dbc.Col(dcc.Graph(id='our-gl-figure')),
                 dbc.Col(dcc.Graph(id='our-resample-figure'))]),
        dbc.Row([dbc.Col(markdown_scatter),
                 dbc.Col(markdown_gl),
                 dbc.Col(markdown_resampler)]),
        dbc.Row(dbc.Col(slider)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_markdown(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    title = 'Data points displayed: {:,}'.format(len(df_sub.index) * value_slider)
    return title


@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Output(component_id='markdown-scatter', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    df_new = pd.DataFrame(np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns)
    start_time = datetime.now()
    fig = px.scatter(
        df_new,
        x='year',
        y='lifeExp',
        title='PX scatter plot',
        template='plotly_white',
    )
    fig.update_traces(marker=dict(size=5 + (value_slider / 30000) * 25))
    end_time = datetime.now()
    subtitle = 'Duration for scatter plot loading: {} s'.format(round((end_time - start_time).total_seconds(), 2))
    return fig, subtitle


@app.callback(
    Output(component_id='our-gl-figure', component_property='figure'),
    Output(component_id='markdown-gl', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    df_new = pd.DataFrame(np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns)
    start_time = datetime.now()
    fig = go.Figure()
    fig.add_trace(go.Scattergl(
        x=df_new['year'],
        y=pd.to_numeric(df_new['lifeExp']),
        mode='markers',
        marker=dict(colorscale='Viridis', size=5 + (value_slider / 30000) * 25),
    ))
    fig.update_layout(
        title='GO gl-scatter plot',
        xaxis_title='year',
        yaxis_title='lifeExp',
    )
    end_time = datetime.now()
    subtitle = 'Duration for gl-scatter plot loading: {} s'.format(round((end_time - start_time).total_seconds(), 2))
    return fig, subtitle


@app.callback(
    Output(component_id='our-resample-figure', component_property='figure'),
    Output(component_id='markdown-resample', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    df_new = pd.DataFrame(np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns)
    start_time = datetime.now()
    fig = FigureResampler(go.Figure())
    fig.add_trace(go.Scattergl(
        x=df_new['year'],
        y=pd.to_numeric(df_new['lifeExp']),
        mode='markers',
        marker=dict(colorscale='Viridis', size=5 + (value_slider / 30000) * 25),
    ))
    fig.update_layout(
        title='Plotly Resampler scatter plot',
        xaxis_title='year',
        yaxis_title='lifeExp',
    )
    end_time = datetime.now()
    subtitle = 'Duration for Plotly Resampler scatter plot loading: {} s'.format(round((end_time - start_time).total_seconds(), 2))
    return fig, subtitle


# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
```

````

### 13.3.3 Datashader

Another high performing way of exploring correlations of large data sets is to use the [datashader](https://plotly.com/python/datashader/) in combination with plotly. Datashader creates rasterized representations of large datasets for easier visualization, with a pipeline approach consisting of several steps: projecting the data on a regular grid aggregating it by count and creating a color representation of the grid. Usually, the minimum count will be plotted in black, the maximum in white, and with brighter colors ranging logarithmically in between.

Compared to the two methods above, the datashader differentiates not only in speed but in the way it visualises data. Instead of the actual data points it represents the occurence of the observed data, therefore letting you explore the correlation, especially any accumulations of your data set really fast. We stay with the bespoken example above to introduce the datashader but change the dropdown to select the continent instead of the country to really make use of the specifications of the datashader. Before use, make sure to install the `datashader` package.

```{attention}
As the datashader needs real numbers to process properly, we will use the numeric conversion that comes within the `pandas` package for the input years and life expectation i.e., we will set
- ``df_new['year'] = pd.to_numeric(df_new['year'])``
- ``df_new['lifeExp'] = pd.to_numeric(df_new['lifeExp'])``
```

Test the datashader in action with the following code:

#### [ADD GIF, THAT SHOWS APP IN ACTION AND SELECTS TWO OR THREE DIFFERENT CONTINENTS FOR A HIGH SLIDER VALUE]

````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import datashader as ds
from datetime import datetime
import numpy as np
import pandas as pd
import plotly.express as px

# Setup data
df = px.data.gapminder()[['continent', 'year', 'lifeExp']]
dropdown_list = df['continent'].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
markdown_scatter = dcc.Markdown(id='markdown-scatter')
slider = dcc.Slider(id='our-slider', min=0, max=50000, marks=None, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown, width=3), dbc.Col(markdown, width=9)]),
        dbc.Row([dbc.Col(dcc.Graph(id='our-figure'))]),
        dbc.Row([dbc.Col(markdown_scatter)]),
        dbc.Row(dbc.Col(slider)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_markdown(value_dropdown, value_slider):
    df_sub = df[df['continent'].isin([value_dropdown])]
    title = 'Data points aggregated: {:,}'.format(len(df_sub.index) * value_slider)
    return title


@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Output(component_id='markdown-scatter', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df['continent'].isin([value_dropdown])]
    df_new = pd.DataFrame(np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns)
    df_new['year'] = pd.to_numeric(df_new['year'])
    df_new['lifeExp'] = pd.to_numeric(df_new['lifeExp'])
    start_time = datetime.now()
    cvs = ds.Canvas(plot_width=100, plot_height=100)
    agg = cvs.points(df_new, 'year', 'lifeExp')
    zero_mask = agg.values == 0
    agg.values = np.log10(agg.values, where=np.logical_not(zero_mask))
    agg.values[zero_mask] = np.nan
    fig = px.imshow(agg, origin='lower', labels={'color': 'Log10(count)'})
    end_time = datetime.now()
    subtitle = 'Duration for scatter plot loading: {} s'.format(round((end_time - start_time).total_seconds(), 2))
    return fig, subtitle


# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
```

````

## 13.4 Caching

Caching, also known as Memoization, is a method used in computer science to speed up calculations by storing data so that future requests for that data can be served faster. Typically, this data stored in a cache is the result of an earlier computation. This way repeated function calls are made with the same parameters won't have to be calculated multiple times. One popular use case may be recurvise functions. More general, whenever you process repititive but difficult or time-consuming calculations within your app you might want to use caching as it allows you to store calculations to speed up your app performance.

```{admonition} Memoization
For an exemplary introduction to memoization and the implementation in Python also have a look at [Towards Data Science](https://towardsdatascience.com/memoization-in-python-57c0a738179a) or [Real Python](https://realpython.com/lru-cache-python/).
```

Let's stick with the example that we have used throughout this chapter but adding a repititve, time consuming functionality. Defining our own function `counting_string` we assure that whenever the callback for the graph gets triggered we delay the app performance by as many seconds as the selected country's name size. Here is when caching comes into play. By storing the functions' values for the selected countries, they do not have to be recalculated the next time. We will use the `lru_cache` (LRU for Least Recently Used) decorator from the `functools` package that goes infront our function and takes in the maximal size of values that can be stored as a parameter.

#### [ADD GIF, THAT SHOWS APP IN ACTION AND SELECTS A COUNTRY AND THEN WIHTIN THE SAME COUNTRY A DIFFERENT VALUE ON THE RANGE SLIDER]

````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
from functools import lru_cache
import numpy as np
import pandas as pd
import plotly.express as px
import time

# Setup data
df = px.data.gapminder()[['country', 'year', 'lifeExp']]
dropdown_list = df['country'].unique()


@lru_cache(maxsize=len(dropdown_list))
def counting_string(string):
    time.sleep(len(string))
    return string


# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
markdown_scatter = dcc.Markdown(id='markdown-scatter')
slider = dcc.Slider(id='our-slider', min=0, max=50000, marks=None, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(dropdown, width=3), dbc.Col(markdown, width=9)]),
        dbc.Row([dbc.Col(dcc.Graph(id='our-figure'))]),
        dbc.Row([dbc.Col(markdown_scatter)]),
        dbc.Row(dbc.Col(slider)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_markdown(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    title = 'Data points displayed: {:,}'.format(len(df_sub.index) * value_slider)
    return title


@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Output(component_id='markdown-scatter', component_property='children'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_dropdown, value_slider):
    df_sub = df[df['country'].isin([value_dropdown])]
    df_new = pd.DataFrame(np.repeat(df_sub.to_numpy(), value_slider, axis=0), columns=df_sub.columns)
    start_time = datetime.now()
    country = counting_string(value_dropdown)
    end_time = datetime.now()
    time_country = round((end_time - start_time).total_seconds(), 0)
    start_time = datetime.now()
    fig = px.scatter(
        df_new,
        x='year',
        y='lifeExp',
        title='PX scatter plot',
        template='plotly_white',
    )
    fig.update_traces(marker=dict(size=5 + (value_slider / 30000) * 25))
    end_time = datetime.now()
    subtitle = 'Duration for scatter plot loading: {} s. Duration to identify the country {}: {} s'.format(round((end_time - start_time).total_seconds(), 2), country, time_country)
    return fig, subtitle


# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
```

````

## Summary

This chapter gave an introduction on how to analyse large data sets with Dash as you will have to face performance issues at some point in time. The first functionality that will help you to understand the performance of your app are the built-in Dash Developer Tools. When it comes to implementing higher performance within your app you have learned about different ways of higher performing graphs: ScatterGL, Plotly Resampler and the Datashader. Last, memorising difficult as well as repetitive calculations can be handled storing the results in the cache. Combining everything you have learned so far you will be able to build dash apps not just functional but performant.
