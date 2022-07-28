# Chapter 14: Introduction to Multi-page Apps

## What you will learn
In this chapter we will introduce multi-page apps which will allow us to build more complex apps.
```{admonition} Learning Intentions
- How to structure multi-page apps project
- Navigate between pages
```

## Why build multi-page apps?
  - <b>Advantages</b>
    - Easier to scale our apps by adding smaller individual pages, rather than developing one large app
    - Easier to troubleshoot bugs
    - Better Search Engine Optimization because each page can have its own meta tags and rendering content
    - Usage statistics available for each page allows us to analyze user behavior for separate sections of the app
  - <b>Disadvantages</b>
    - Extra code infrastructure is usually required
    - Single-page apps are more mobile-friendly than multi-page
    - Slightly more complex to build than single-page apps

## Basics of a Multi-page App

Multi-page apps have a simple structure:  
  - One main file commonly named `app.py`
  - One sub-folder, named `pages`, that contains all of the seperate pages of the app
  - Another sub-folder called 'assets' which will hold the pictures and style sheets our app might use

Let's start exploring `multi-page apps` by walking through the example in [Dash documentation](https://dash.plotly.com/urls).  

First, create a root directory folder called `dash_multi_page`.  Within the `dash_multi_page` directory create the main file called `app.py` as well as the `/pages` and `/assets` subdirectories:

![app_structure](ch14_files/app_structure.png)
  
Next, let's create the `home` page for our app.  Create `home.py` in the `/pages` subdirectory.  Notice in the code below that we specify the `path` with a forward slash when calling `dash.register_page()`.  This will make the `home.py` page the landing page for our multi-page app.

You might also see that we don't declare an `app` object as we normally do in `Dash` apps - `app = Dash(__name__)`.  This is because the `app` object is declared in the `app.py` file which we will build shortly.

#### home.py
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
We'll create 2 more pages for this basic multi-page app example:  `analytics.py` and `archive.py`. Notice how the`layout` and `@callback` are written. Unlike single-page Dash apps, which would have `app.layout` and `@app.callback`, with multi-page apps, the pages do not use the app object. 

#### analytics.py

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

#### archive.py

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

Finally, we'll create the `app.py` file which incorporates all three pages into the app.

#### app.py
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
  - `for page in dash.page_registry.values()` will crawl through the `/pages` directory to find all the names and links of each page
  - `dash.page_container` component must be included in the `app.layout`. This is where the content of each page will be displayed

![basic-app](./ch14_files/multi_page_basic.gif)

## More Advanced Multi-Page app

Now let's create a more advanced `multi-page` app, building on examples from previous chapters.  We'll use a `dropdown` component to navigate between pages instead of the `dcc.Link` that we used above.

First, create the `app.py` file and use the following code:

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
The `dropdown` menu will display the different pages that users can navigate to.


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

Next we need to create the individual pages. The first page will be `8.2.3` from Chapter 8.  To make this page work with our multi-page example we need to add `dash.register_page(__name__)` and remove all references to `app` because it should only be declared in the main `app.py` file :

```python
import dash
from dash import dcc, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc


dash.register_page(__name__)

# Data
df = px.data.gapminder()

# Page Layout
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

For our second page we will use the final `Chapter 10` code:

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

