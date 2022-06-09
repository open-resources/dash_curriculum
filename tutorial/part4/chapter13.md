# Chapter 13: Improving app performance

## What you will learn

By now, you have everything together to get your first app up and running using even advanced components, layouts and callbacks. As dashboards are designed for data analysis and visualisations at some point you might run into efficiency constraints when the amount of data you are working with gets growing. To circumvent any possible performance lacking this chapter will give you some insights on improving your app performance. You'll learn about the built-in Dash Developer Tools, how to plot massive amount of data with higher performing plotly graphs and how to use caching for improving the performance of your app. 

```{admonition} Learning Intentions
- Dash Developer Tools
- (Pre)Processing data
- Higher Performing Plotly graphs
- Caching
```

## 13.1 Dash Developer Tools
Dash Dev Tools is a set of tools to make debugging and developing Dash apps more productive & pleasant. These tools are enabled when developing your Dash app and are not intended when deploying your application to production. In this tutorial we focus on the Callback Graph. Dash displays a visual representation of your callbacks: which order they are fired in, how long they take, and what data is passed back and forth between the Dash app in the web browser and your Python code. For an overview over the other tools look at the [official documentation](https://dash.plotly.com/devtools).

The Dash Dev Tools Callback Graph provides Live Introspection, Profiling, and Live Debugging of your callback graph.
#### [ADD SCREENSHOT, THAT SHOWS THE DASH DEV TOOLS]

This includes:

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

## 13.2 (Pre)Processing data
Work in Progress:

- Transfer the example of section ''Let go of dataframes in request/response'' from the article [https://strange-quark.medium.com/improving-performance-of-python-dash-dashboards-54547d68f86b](https://strange-quark.medium.com/improving-performance-of-python-dash-dashboards-54547d68f86b) to the gapminder data set? Does this enhance performance? Need to restructure the gapminder data set?
- Using numpy for (numerical) calculations, examples on performance?

## 13.3 Higher Performing Plotly graphs
So far, we have used the `plotly.express` library to implement our graphs. This is a very easy and convenient way to do so. However, most plotly charts are rendered with SVG (Short for Scalable Vector Graphics). This provides crisp rendering, publication-quality image export as SVG images can be scaled in size without loss of quality, and wide browser support. Unfortunately, rendering graphics in SVG can be slow for large datasets (like those with more than 15k points). To overcome this limitation, `plotly.js` has WebGL (Short for Web Graphics Library) alternatives to some chart types. WebGL uses the GPU to render graphics which make them higher performing. Two WebGL alternatives are the following:

- [ScatterGL](https://plotly.com/python/line-and-scatter/#large-data-sets): A webgl implementation of the scatter chart type.
- [Pointcloud](https://plotly.com/python/reference/#pointcloud): A lightweight version of scattergl with limited customizability but even faster rendering.

### 13.3.1 ScatterGL

Let us have a closer look at the ScatterGL plot, which is a scatter plot. Against the scatter plots we have seen so far, the ScatterGL plot is a plotly `graph object`, in comparison to the plotly express scatter plot implemented in the previous chapters. The following App let's you compare the different durations for data loading.

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
#### [ADD GIF, THAT SHOWS APP IN ACTION AND COMPARES THE SPEED OF THE TWO SCATTER PLOTS FOR TWO DIFFERENT SLIDER VALUES]

### 13.3.2 Plotly Resampler

Even though the ScatterGL outperformes the px scatter plot, it is still rather slow for large data sets and is delayed when interacting with the data plot e.g., zoom in. That's where the package `plotly_resampler` comes in very handy. This package speeds up the figure by downsampling (aggregating) the data respective to the view and then plotting the aggregated points. When you interact with the plot (panning, zooming, ...), callbacks are used to aggregate data and update the figure.

```{admonition}
See also the [documenatation on Github](https://github.com/predict-idlab/plotly-resampler) for the plotly resampler package.
```

The following App let's you compare the different durations for data loading.

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
#### [ADD GIF, THAT SHOWS APP IN ACTION AND COMPARES THE SPEED OF THE SCATTER PLOTS FOR TWO DIFFERENT SLIDER VALUES AS WELL AS HOW TO ZOOM IN]

### 13.3.3 Datashader

Another high performing way of exploring correlations of large data sets is to use [datashader](https://plotly.com/python/datashader/) in combination with plotly. Datashader creates rasterized representations of large datasets for easier visualization, with a pipeline approach consisting of several steps: projecting the data on a regular grid aggregating it by count and creating a color representation of the grid. Usually, the minimum count will be plotted in black, the maximum in white, and with brighter colors ranging logarithmically in between.

Compared to the two plots above, the datashader differentiates not only in speed but in the method of visualisation of data. Instead of the actual data points it represents the occurence of the observed data, therefore letting you explore the correlation of your data set really fast. We stay with the introduced example above to introduce the datashader. Before use, make sure to install the datashader package.

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
df = px.data.gapminder()[['country', 'year', 'lifeExp']]
dropdown_list = df['country'].unique()

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
#### [ADD GIF, THAT SHOWS APP IN ACTION AND SELECTS TWO OR THREE DIFFERENT COUTNRIES FOR A HIGH SLIDER VALUE]

## 13.4 Caching

Caching, also known as Memoization, is a method used in computer science to speed up calculations by storing data so that future requests for that data can be served faster. Typically, this data stored in a cache is the result of an earlier computation. This way repeated function calls are made with the same parameters won't have to be calculated multiple times. One popular use case are recurvise functions.

```{admonition} Memoization
For an exemplary introduction to memoization and the implementation in Python also have a look at [Towards Data Science](https://towardsdatascience.com/memoization-in-python-57c0a738179a) or [Real Python](https://realpython.com/lru-cache-python/).
```

When working with callbacks, the easiest way implementing memoization is using the `flask_caching` module. See the [official documentation](https://dash.plotly.com/performance#memoization) for further reference.

## Other potential ideas if need be:

https://community.plotly.com/t/how-to-improve-the-loading-speed-of-my-page/17197

https://community.plotly.com/t/is-there-a-way-to-increate-the-performance-of-my-dash-web-app/23117/10

https://github.com/ijl/orjson

## Summary
