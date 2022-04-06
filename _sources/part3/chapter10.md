# Chapter 10: Advanced Callbacks

## What you will learn

You have already learned about callbacks in chapter 4. Now, it is time to upskill and deal with more advanced callbacks. You will learn how to circumvent different components to trigger a callback action immediately as well as how to handle multiple outputs and inputs in one callback.

```{admonition} Learning Intentions
- Multiple outputs and inputs
- States
```

## 10.1 Multiple outputs and inputs

You might want to have a graph that should be linked to more than one component, changing or affecting different dimensions of your graph. If you think the other way around, you might want to have several graphs that should be affected by the same component. Here is where multiple outputs and inputs come into play.

```{attention}
In addition to a much cleaner and shorter code, note that assigning two different callbacks the same component as an output argument is just not allowed by dash.
```

Let us see multiple inputs in action. We take the final code from chapter 8 and add the markdown, some radio items and a slider, where both, the radio items as well as the slider, will affect the graph.

```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Setup data
df = px.data.gapminder()
df = df[df['country'].isin(['Canada', 'Brazil', 'Norway', 'Germany'])]

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My First app')
radio = dcc.RadioItems(id='our-radio', options=['line', 'scatter'], value='line')
slider = dcc.Slider(
    id='our-slider',
    min=df['year'].min(),
    max=df['year'].max()-5,
    value=df['year'].min(),
    step=5,
    marks={str(year): str(year) for year in df['year'].unique()}
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row(dbc.Col(radio)),
        dbc.Row(dbc.Col(dcc.Graph(id='our-figure'))),
        dbc.Row(dbc.Col(slider)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Input(component_id='our-radio', component_property='value'),
    Input(component_id='our-slider', component_property='value'),
)
def update_graph(value_radio, value_slider):
    df_sub = df[df['year'] >= value_slider]

    if value_radio == 'scatter':
        fig = px.scatter(
            df_sub,
            x='year',
            y='lifeExp',
            color='country',
            symbol='continent',
            title='PX {} plot'.format(value_radio),
            template='plotly_white'
        )
    else:
        fig = px.line(
            df_sub,
            x='year',
            y='lifeExp',
            color='country',
            symbol='continent',
            title='PX {} plot'.format(value_radio),
            template='plotly_white'
        )
    return fig


# Run the App
if __name__ == '__main__':
    app.run_server()
```

Similarly, we are able to define multiple outputs in one callback. Herefore, let us take another example, where we want to trigger a graph and a table at the same time by a dropdown menu.

```
# Import packages
from dash import Dash, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Setup data
df = px.data.gapminder()
dropdown_list = df['country'].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My First app')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
data_table = dash_table.DataTable(id='our-data-table')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row(dbc.Col(dropdown, width=6)),
        dbc.Row(dbc.Col(dcc.Graph(id='our-figure'))),
        dbc.Row(dbc.Col(data_table)),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Output(component_id='our-data-table', component_property='data'),
    Input(component_id='our-dropdown', component_property='value'),
)
def update_graph(value_dropdown):
    df_sub = df[df['country'].isin([value_dropdown])]

    fig = px.line(
        df_sub,
        x='year',
        y='lifeExp',
        color='country',
        symbol='continent',
        title='PX line plot',
        template='plotly_white'
    )

    data = df_sub.to_dict('records')
    return fig, data


# Run the App
if __name__ == '__main__':
    app.run_server()
```

Feel free to practice and give your multiple inputs and outputs at the same time.

## 10.2 States

So far, we had linked components of your app together which immediately affected each other. In a more advanced setup it might be useful though to circumvent this direct relationship. You might first want to have all of the input arguments together before your outpout is triggered. This could be helpful for any kind of forms. For this purpose there is a third argument that can be used within the callback decorator, the state.

## Summary

Now you are well equipped to build a complex and fully interactive app, where you might link multiple input components with multiple output components. Furthermore, you know how to trigger certain inputs running after.
