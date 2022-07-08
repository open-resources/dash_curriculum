# Chapter 14: Introduction to Multi-page Apps

## What you will learn
In this chapter we will introduce multi-page apps which will allow us to build more complex apps.
```{admonition} Learning Intentions
- How to structure multi-page apps project
- Navigate between apps
```

## Why separate app into multiple pages?
  - <b>Advantages</b>
    - Easy to develop small apps and features
    - Easy to troubleshoot bugs
    - New apps can be built on to old apps
  - <b>Disadvantages</b>
    - Extra infrastructure is required
    - Slightly more complex apps

## Basics of Multi-page Apps

Multi-page apps have a simple structure:  
  - One main file commonly named `app.py`
  - One sub-folder, which <b>must</b> be named `pages`, that contains all of the seperate apps
  - Another sub-folder called 'assets' which will hold all the pictures and files our app uses

Let's start exploring `multi-page apps` by walking through the example in [Dash documentation](https://dash.plotly.com/urls).  

First, create a root directory folder called `dash_multi_page`.  Within the `dash_multi_page` directory create the main app file called `app.py` and the `/pages` subdirectory:

![app_structure](ch14_files/app_structure.png)

Next, we'll create the `app.py` file and copy over the example code:

```python
from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
	html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)
```

There are several requirements for the `app.py` file:
  - `use_pages=True` must be included when creating the `app` object
  - `for page in dash.page_registry.values()` will crawl through the `/pages` directory to allow access to all of our sub-apps
  - `dash.page_container` component must be included in the `app.layout`
    - This is where the sub-apps will be displayed
  
Next, let's create the `home` page for the app.  Create `home.py` in the `/pages` subdirectory.  Notice in the code below that we specify the `path` when calling `dash.register_page()`.  This will make the `home.py` page the landing page for our multi-page app.

```python
import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='This is our Home page'),

    html.Div(children='''
        This is our Home page content.
    '''),

])
```
We'll create 2 more pages to complete this basic multi-page example:  `analytics.py` and `archive.py`.

Here is the code for `analytics.py`:

```python
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='This is our Analytics page'),
	html.Div([
        "Select a city: ",
        dcc.RadioItems(['New York City', 'Montreal','San Francisco'],
        'Montreal',
        id='analytics-input')
    ]),
	html.Br(),
    html.Div(id='analytics-output'),
])


@callback(
    Output(component_id='analytics-output', component_property='children'),
    Input(component_id='analytics-input', component_property='value')
)
def update_city_selected(input_value):
    return f'You selected: {input_value}'
```
Here is the code for `archive.py`:

```python
import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='This is our Archive page'),

    html.Div(children='''
        This is our Archive page content.
    '''),

])
```
![basic-app](./ch14_files/multi-page_basic.gif)

## More Advanced Multi-Page app

Now let's create a more advanced `multi-page` app.  We'll use a `dropdown` component to navigate between apps.  For the apps themselves we'll use examples from previous chapters.

First, create the `app.py` file and paste the following code:

```python
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

dropdown =  dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
        ],
        nav=True,
        label="More Pages",
        align_end=False,
    )

app.layout = dbc.Container(
    [dropdown, dash.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
```
The `dropdown` menu will display the different apps that users can navigate to.


We can now create our `home.py` file:

```python
import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='This is our Home page'),

    html.Div(children='''
        This is our Home page content.
    '''),
])
```

Next we need to create the individual apps. The first app will be `8.2.3` from Chapter 8.  To make this app work with our multi-page example we need to add `dash.register_page(__name__)` and remove all references to `app` because it should only be declared in the main `app.py` file :

```python
import dash
from dash import dcc, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc


dash.register_page(__name__)

# Data
df = px.data.gapminder()

# App Layout
layout = dbc.Container([
    dcc.Markdown("# Interactive Dash App with Line Chart"),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='country-dropdown',
                         options=[x for x in df.country.unique()],
                         multi=True,
                         value=['Canada', 'Brazil'])
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='figure1')
        ], width = 8)
    ])
])


# Configure Callback
@callback(
    Output('figure1','figure'),
    Input('country-dropdown', 'value')
)
def udpate_graph(countries_selected):
    df_filtered = df[df.country.isin(countries_selected)]
    fig = px.line(df_filtered, x='year', y='lifeExp', color='country')

    return fig
```

For our second app we will use the final `Chapter 10` code:

```python
# Import packages
from dash import Dash, dash_table, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

dash.register_page(__name__)

# Setup data
df = px.data.gapminder()
dropdown_list = df['country'].unique()

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='# My first app')
dropdown = dcc.Dropdown(id='our-dropdown', options=dropdown_list, value=dropdown_list[0])
radio = dcc.RadioItems(id='our-radio', options=['line', 'scatter'], value='line')
button = html.Button(id='our-button', children='Update data', n_clicks=0)
data_table = dash_table.DataTable(id='our-data-table', page_size=10)

layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row(
            [
                dbc.Col(dropdown, width=3),
                dbc.Col(radio, width=3),
                dbc.Col(button, width=3)
            ]
        ),
        dbc.Row(dbc.Col(dcc.Graph(id='our-figure'))),
        dbc.Row(dbc.Col(data_table))
    ]
)


# Configure callbacks
@callback(
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
```

![img-repo](./ch14_files/multi-page.gif)

