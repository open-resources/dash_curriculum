# Chapter 10: Advanced Callbacks

## What you will learn

You have already learned about callbacks in chapter 4. Now, it is time to upskill and deal with more advanced callbacks. You will learn how to circumvent different components to trigger a callback action immediately as well as how to handle multiple outputs and inputs in one callback. Furthermore, we will see how to operate with buttons within a callback.

```{admonition} Learning Intentions
- Multiple outputs and inputs
- Buttons in callbacks
- States
```

## 10.1 Multiple outputs and inputs

You might want to have a graph that should be linked to more than one component, changing or affecting different dimensions of your graph. If you think the other way around, you might want to have several graphs that should be affected by the same component. Here is where multiple outputs and inputs come into play.

```{attention}
In addition to a much cleaner and shorter code, note that assigning two different callbacks the same component as an output argument is just not allowed by dash.
```

Let us see multiple inputs in action first. We take the final code from chapter 8 and add a markdown, some radio items and a slider, where both, the radio items as well as the slider, will affect the graph. Using multiple inputs we need to add them as arguments in the callback decorator as well as arguments in the callback function.

```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Setup data
df = px.data.gapminder()
dropdown_list = df['country'].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My first app')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
radio = dcc.RadioItems(id='our-radio', options=['line', 'scatter'], value='line')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row(
            [
                dbc.Col(dropdown, width=3),
                dbc.Col(radio, width=1)
            ]
        ),
        dbc.Row(dbc.Col(dcc.Graph(id='our-figure'))),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Input(component_id='our-dropdown', component_property='value'),
    Input(component_id='our-radio', component_property='value'),
)
def update_graph(value_dropdown, value_radio):
    df_sub = df[df['country'].isin([value_dropdown])]

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
### [ADD GIF, SHOWING THE ABOVE CODE IN ACTION]

Similarly, we are able to define multiple outputs in one callback. Herefore, let us take another example, where we want to trigger a graph and a table at the same time by a dropdown menu. Multiple outputs will be separated with a commata when returned by the callback function.

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
data_table = dash_table.DataTable(id='our-data-table', page_size=10)

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
### [ADD GIF, SHOWING THE ABOVE CODE IN ACTION]

## 10.2 Buttons within a callback

Now, that you know how to implement multiple inputs and outputs it's worth to take a closer look at buttons and how to approach them within a callback as you need to access different component properties than we have seen so far. Furthermore, we will see how to track how often a button has been clicked.

Besides the children and id property, buttons come with a property called `n_clicks`, which represents the number of times that the button has been clicked on. You can use this property either to count how many times a button has been clicked or to trigger one or multiple output components whenever the button is clicked. Let's see both in one simple example. Hereby, we are changing the title of our app depending if and how often the implemented button has been clicked.

```
# Import packages
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown')
button = html.Button(id='our-button', children='Update title')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row(dbc.Col(button))
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-button', component_property='n_clicks'),
)
def update_title(n_clicks):
    if n_clicks == 0:
        title = 'My first app. The button has not been clicked yet.'
    else:
        title = 'My first app with a button, that I have clicked {} times.'.format(n_clicks)
    return title


# Run the App
if __name__ == '__main__':
    app.run_server()
```
### [ADD GIF, SHOWING THE ABOVE CODE IN ACTION]

To give you some more flexibility on programming your future apps let's see two more facettes of how to use buttons within callbacks. First, let us see how to reset the n_clicks component property of a button. Herefore, let's adjust the above example by adding a second button. Whenever the second button will be clicked the component property n_clicks of the first button will be reset to 0.

```
# Import packages
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown')
button = html.Button(id='our-button', children='Update title')
button_reset = html.Button(id='reset-button', children='Reset')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row(
            [
                dbc.Col(button, width=2),
                dbc.Col(button_reset, width=2)
            ]
        )
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-button', component_property='n_clicks'),
)
def update_title(n_clicks):
    if n_clicks == 0:
        title = 'My first app. The button has not been clicked yet.'
    else:
        title = 'My first app with a button, that I have clicked {} times.'.format(n_clicks)
    return title


@app.callback(
    Output(component_id='our-button', component_property='n_clicks'),
    Input(component_id='reset-button', component_property='n_clicks'),
)
def update_title(n_clicks):
    if n_clicks >= 0:
        clicks = 0
    return clicks


# Run the App
if __name__ == '__main__':
    app.run_server()
```
### [ADD GIF, SHOWING THE ABOVE CODE IN ACTION]

To conclude this second part of the chapter, let us see how to implement a binary functionality of your button. This means you are triggering different outputs with clicking the button, depending if you have clicked it an even or an odd number of times. This can be easily handled with the modulo operator `%`.

```{tip}
For a comprehensive overview of the modulo operator and how to use it in Python, have a look at [Real Python](https://realpython.com/python-modulo-operator/).
```

```
# Import packages
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My first app')
button = html.Button(id='our-button', children='Update title')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row(dbc.Col(button))
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-button', component_property='n_clicks'),
)
def update_title(n_clicks):
    if n_clicks % 2 == 0:
        title = 'My first app'
    else:
        title = 'My first app, but with a changed title.'
    return title


# Run the App
if __name__ == '__main__':
    app.run_server()
```
### [ADD GIF, SHOWING THE ABOVE CODE IN ACTION]

## 10.3 States

So far, we had linked components of your app together which immediately affected each other. In a more advanced setup it might be useful though to circumvent this direct relationship. You might first want to have all of the input arguments together before your outpout is triggered. This could be helpful for any kind of forms. For this purpose there is a third argument that can be used within the callback decorator, the state. Formally, the state argument is used in the same way as the input argument.

Let's bring everything together in one final example. We will implement an app with a dropdown, some radio items and button which will trigger two output components, a graph and a table. However, we only want to trigger the output components when the button is clicked. This can be done with the state argument.

```{attention}
Note that you need to import the state argument the same way we are importing the input and output arguments at the beginning of your code.
```

```
# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

# Setup data
df = px.data.gapminder()
dropdown_list = df['country'].unique()

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My first app')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
radio = dcc.RadioItems(id='our-radio', options=['line', 'scatter'], value='line')
button = html.Button(id='our-button', children='Update data', n_clicks=0)
data_table = dash_table.DataTable(id='our-data-table', page_size=10)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row(
            [
                dbc.Col(dropdown, width=3),
                dbc.Col(radio, width=1),
                dbc.Col(button, width=3)
            ]
        ),
        dbc.Row(dbc.Col(dcc.Graph(id='our-figure'))),
        dbc.Row(dbc.Col(data_table))
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-figure', component_property='figure'),
    Output(component_id='our-data-table', component_property='data'),
    Input(component_id='our-button', component_property='n_clicks'),
    State(component_id='our-dropdown', component_property='value'),
    State(component_id='our-radio', component_property='value'),
)
def update_graph(n_clicks, value_dropdown, value_radio):
    if n_clicks >= 0:
        df_sub = df[df['country'].isin([value_dropdown])]
        data = df_sub.to_dict('records')

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

    return fig, data


# Run the App
if __name__ == '__main__':
    app.run_server()
```
### [ADD GIF, SHOWING THE ABOVE CODE IN ACTION]

## Summary

We have learned about how to link multiple input components with multiple output components. Furthermore, you know how to trigger certain inputs running after using the state argument in a callback. With the third learning on how to deal with buttons within callbacks you are now well equipped to build even more complex, fully interactive apps.
