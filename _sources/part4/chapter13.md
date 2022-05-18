# Chapter 13: Improving app performance

## What you will learn

By now, you have everything together to get your first app up and running using even advanced components, layouts and callbacks. As dashboards are designed for data analysis and visualisations at some point you might run into efficiency constraints when the amount of data you are working with gets growing. To circumvent any possible performance lacking this chapter will give you some insights on improving your app performance.

```{admonition} Learning Intentions
- Preprocessing data
- Higher Performing Plotly graphs
- Caching
```

## 13.1 Preprocessing data
the main idea is to give two examples on data wrangling. Once where the data wrangling takes place before initializing the app, once after or during a callback. The plan is to show some difference in processing time.

## 13.2 Higher Performing Plotly graphs
So far, we have used the `plotly.express` library to implement our graphs. This is a very easy and convenient way to do so. However, most plotly charts are rendered with SVG (Short for Scalable Vector Graphics). This provides crisp rendering, publication-quality image export as SVG images can be scaled in size without loss of quality, and wide browser support. Unfortunately, rendering graphics in SVG can be slow for large datasets (like those with more than 15k points). To overcome this limitation, `plotly.js` has WebGL (Short for Web Graphics Library) alternatives to some chart types. WebGL uses the GPU to render graphics which make them higher performing. Two WebGL alternatives are the following:

- [ScatterGL](https://plotly.com/python/line-and-scatter/#large-data-sets): A webgl implementation of the scatter chart type.
- [Pointcloud](https://plotly.com/python/reference/#pointcloud): A lightweight version of scattergl with limited customizability but even faster rendering.

Another high performing way of exploring correlations of large data sets is to use [datashader](https://plotly.com/python/datashader/) in combination with plotly. Datashader creates rasterized representations of large datasets for easier visualization, with a pipeline approach consisting of several steps: projecting the data on a regular grid aggregating it by count and creating a color representation of the grid. Usually, the minimum count will be plotted in black, the maximum in white, and with brighter colors ranging logarithmically in between.

### 13.2.1 ScatterGL

Let us have a closer look at the ScatterGL plot, which is a scatter plot. Against the scatter plots we have seen so far, the ScatterGL plot is a plotly `graph object`, in comparison to the plotly express scatter plot implemented in the previous chapters. The following App let's you compare the different duration for data loading.

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

### 13.2.2 Datashader

## 13.3 Caching

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
