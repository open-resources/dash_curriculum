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
            if page["module"] != "pages.not_found_404" 
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
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),

)

app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
```

![img-repo](./ch14_files/multi-page.gif)

