# Chapter 12  Advanced Styling and Layout

## 12.1 The theme of a Dash app

There are many different ways you can change the layout and add themes to your Plotly Dash app. In this chapter you will learn how to set a theme with `external_stylesheets=[dbc.themes.<theme>]` when you set up an app like this:

```python
JupyterDash(external_stylesheets=[dbc.themes.SLATE])
```

What hides behind `dbc.themes.SLATE` is the link `https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/slate/bootstrap.min.css`. And the contents of that link is what will define the design of the components in your app. One such component can be a header `html.H1()`. If you use the `Slate` theme, the default font color of your heading will be of a light grey type with the RGB code `(170, 170, 170)`. In the context of the theme, this particular color is mapped to `text-body`. And if you do a little search in the link above, you'll find *one* occurence of `text-body` in the `css` file in the link above:

    text-body{--bs-text-opacity:1;color:rgba(var(--bs-body-color-rgb),var(--bs-text-opacity))
    
 When it comes to the color, the element we're interested in is this:
 
     var(--bs-body-color-rgb)
     
     
This points to a setting at the start of the document that reveals the `rgb()` code used by `text-body`:

    bs-body-color-rgb:170,170,170
    
[![enter image description here][1]][1]

Now we know how to set a theme with `external_stylesheets=[dbc.themes.SLATE]`, and we know that ...
The next section will describe how to edit these properties through `className` and `style`
     
## 12.2
    
---

## Unclear:

- how to change *complete* theme through callbacks on `JupyterDash(external_stylesheets=[dbc.themes.SLATE])`?
- can you set `order` of `dbc.Row()` co,ponents as you can with `dbc.Col()`. `align`?
- `external_stylesheets=[dbc.themes.SLATE]` < `className` < `style`?

## className details

### className elements

### className combinations:

- `" opacity-25 p-2 m-1 bg-primary text-light fw-bold rounded "`

- `" opacity-75 p-2 m-1 bg-success bg-opacity-25 text-light rounded-bottom "`

### className gotchas

Without a leading `space`, the first element `opacity-75` is ignored
Without a trailing `space`, the last element `rounded-bottom` will also likely be ignored, ***but*** the `bottom` property seems to be globally set by `[dbc.themes.SLATE]` and is uneditable???

## Resources:

https://bootswatch.com/
      
## I - Outline:      
## Advanced Styling with Dash Bootstrap Components

  - Introduction to [Dash Bootstrap themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/)
  - [Plotly Dash Theme Explorer App by Ann Marie](https://hellodash.pythonanywhere.com/)
  - Most common [styling components](https://dashcheatsheet.pythonanywhere.com/)
    - me, ms, mt, nb
    - text color, background color, border color
    - etc. 
  - Styling beyond DBC ("dbc offers you a lot, but for more customized styling you can use the `style` property in each dash component. For example `dcc.Markdown("App Title", style={'textAlign':'center'})`. To learn more go to this property see dash [docs](https://dash.plotly.com/layout#more-about-html-components)

## Advanced Styling of Dash DataTable

Recognizing that the DataTable is one of the most common Dash components, we'd like to show you a few examples on styling the DataTable, using a few DataTable properties, such as `style_cell`, `style_data_conditional`, `style_header`.

```python
# Create a Dash DataTable
data_table = dash_table.DataTable(
        id='dataTable1', 
        data=df.to_dict('records'), 
        columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
        sort_action='native',
        style_cell={'padding': '5px'},
        style_data_conditional=[
            {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(204, 230, 255)'},
            ],

        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'}
)
```

## Advanced Layout with Dash Bootstrap Components

 - Vertical alignment
 - Horizontal alignment
 - Container Fluid prop
 - adjusting columns by screen size:
```
      app.layout = dbc.Container([
          dbc.Row(
              [
              dbc.Col(
                  dcc.Markdown("left div", className="bg-primary"),
              xs=12, sm=12, md=3, lg=3, xl=3, # This sets the column width for different screen sizes
              ),
              dbc.Col(
                  my_table,
                  xs=12, sm=12, md=6, lg=6, xl=6, # This sets the column width for different screen sizes
              ),
              dbc.Col(
                  dcc.Markdown("right div", className="bg-primary"),
              xs=12, sm=12, md=3, lg=3, xl=3, # This sets the column width for different screen sizes
              ),

              ] ,className="g-0" #This allows to have no space between the columns. Delete if you want to have that breathing space
          )
      ])
```

## Dynamic app layout (I can help write this part, Arne, once you're done with the first draft of this chapter)
  - https://dash.plotly.com/live-updates#updates-on-page-load

# II - Outtakes:


     
 


A part of the file looks like this:

```
*/:root{--bs-blue:#007bff;--bs-indigo:#6610f2;--bs-purple:#6f42c1;--bs-pink:#e83e8c;--bs-red:#ee5f5b;--bs-orange:#fd7e14;--bs-yellow:#f89406;--bs-green:#62c462;--bs-teal:#20c997;--bs-cyan:#5bc0de;--bs-white:#fff;--bs-gray:#7a8288;--bs-gray-dark:#3a3f44;--bs-gray-100:#f8f9fa;--bs-gray-200:#e9ecef;--bs-gray-300:#dee2e6;--bs-gray-400:#ced4da;--bs-gray-500:#999;
```

And all those little details is what sets the colors, shapes and behaviour of your app. But all that is not written in stone. With a setup with this as a starting point, you can edit the layout and change the behaviour through two main ways:

1. The `className` attribute of the app components
2. The `style` attribute of the app components

This chapter will use `SLATE`, but you can study other options in the [themes explorer](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/)

When you've first defined a theme like the one above, you can edit the visual properties of, for example, a dropdown button like text color, background and text orientation through the `className` attribute of the dropdown.

# III - Theme Tester App

```python

import plotly.graph_objects as go
import plotly.express as px
from jupyter_dash import JupyterDash

import dash_core_components as dcc
import dash_html_components as html

app = JupyterDash(__name__)

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from dash import State, Input, Output, Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import json

# Initialise the App 
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app = JupyterDash(external_stylesheets=[dbc.themes.SLATE])



# data
df = px.data.gapminder()#.query('year == 2007')

# selections and specifications
    
colors = ['blue', 'green', 'red', 'black', 'yellow']
symbols = ['circle', 'circle-open', 'square', 'square-open', 'diamond', 'diamond-open', 'cross', 'x']

opts_columns_df = list(df.columns[:6])

opts_continent = [{'label': k, 'value': k} for k in list(df.continent.unique())]

opts_size = ['year', 'lifeExp', 'pop', 'gdpPercap'] + ['None']

opts_years = list(df.year.unique()) + ['All']

# opts_continent.extend([{'label': 'All', 'value': list(df.continent.unique())}])
# opts_continent.extend([{'label': 'All', 'value': ', '.join(list(df.continent.unique()))}])
opts_continent.extend([{'label': 'All', 'value': 'All'}])

# Set up well organized controls in a dbc.Card()
controls = dbc.Card([dbc.Row([dbc.Label("Continent"),
                                    dcc.Dropdown(id='ctrl_continent',
                                                 options= opts_continent,
                                                  value='All',
                                                  className = "text-danger"
                                                ),
                                   ],),
                     
                    dbc.Row([dbc.Label("X axis"),
                                   dcc.Dropdown(id='ctrl_xaxis',
                                                options=[{'label': k, 'value': k} for k in  opts_columns_df],
                                                value=df.columns[:6][0],
                                                ),
                                    ],),
                     
                    dbc.Row([dbc.Label("Y axis"),
                                   dcc.Dropdown(id='ctrl_yaxis',
                                                # options=[{'label': k, 'value': k} for k in [8,10,12,14,16]],
                                                options=[{'label': k, 'value': k} for k in  list(df.columns[:6])],
                                                value=list(df.columns[:6])[3],
                                                ),
                                    ],),
                     
                 
                    dbc.Row([dbc.Label("Size"),
                                   dcc.Dropdown(id='ctrl_size',
                                                # options=[{'label': k, 'value': k} for k in [8,10,12,14,16]],
                                                options=[{'label': k, 'value': k} for k in  opts_size],
                                                value=None,
                                                ),
                                    ],),
                     
                    dbc.Row([dbc.Label("Color"),
                                   dcc.Dropdown(id='ctrl_color',
                                                options=[{'label': k, 'value': k} for k in  list(df.columns[:6])],
                                                value=df.columns[:6][2],
                                                ),
                                    ],),
                     
                    dbc.Row([dbc.Label("Year"),
                                   dcc.Dropdown(id='ctrl_year',
                                                options=[{'label': k, 'value': k} for k in opts_years],
                                                value=df.year.max(),
                                                ),
                                    ],),
                    ],
                    body=True,
                    style = {'font-size': 'large'}
                    )

# controls_layout
opts_title_main = [{'label': k, 'value': k} for k in ["text-primary", "text-secondary", "text-success",
                                                      "text-danger", "text-warning"]]

controls_layout = dbc.Card([dbc.Row([dbc.Label("Color main title"),
                                     dcc.Dropdown(id='ctrl_dsgn_title_1',
                                                  options= opts_title_main,
                                                  # value='All'
                                                ),
                                     
                                     dcc.Dropdown(id='ctrl_dsgn_button',
                                                  options= opts_title_main,
                                                  # value='All'
                                                ),
                                     
                                   ],),
                    ],
                    body=True,
                    style = {'font-size': 'large'}
                    )

# Set up the app layout using dbc.Container(), dbc.Row(), and dbc.Col()
app.layout = dbc.Container([html.H1("Data selection and figure design", id='dsgn_title_1',  className="text-primary"),
                            html.Hr(),
                            dbc.Row([dbc.Col([controls],xs = 4),
                                     dbc.Col([dbc.Row([dbc.Col(dcc.Graph(id="fig_scatter_1")),])]),
                                    ]),
                            html.H1("Layout design", id='dsgn_title_2',  className="text-primary"),
                            html.Hr(),
                            dbc.Row([dbc.Col([controls_layout],xs = 4),
                                     # dbc.Col([dbc.Row([dbc.Col(dcc.Graph(id="fig_scatter_1")),])]),
                                    ]),
                            html.Br(),
                            ],
                            fluid=True,
                            )
# FIGURE 1 interactivity
@app.callback(
    Output("fig_scatter_1", "figure"),
    [   Input("ctrl_xaxis", "value"),
        Input("ctrl_yaxis", "value"),
        Input("ctrl_continent", "value"),
        Input("ctrl_size", "value"),
        Input("ctrl_color", "value"),
        Input("ctrl_year", "value"),
        # Input("ctrl_opac", "value"),
    ],
)
def history_graph(xval, yval, continent, size, color, year):
    df = px.data.gapminder()#.query('year == 2007')
    
    # handle subsetting of some or all continents
    if continent == 'All':
        df = df
    else:
        df = df[df.continent.isin([continent])] 
    
    # handle subsetting of one or all years
    if year == 'All':
        df = df
    else:
        df = df[df.year == year]
                  
    # df
    # global yval
    # print(yval)
    fig = px.scatter(df, x=xval, y=yval, size = None if size == 'None' else size,
                     color = color
                    )
    return fig


# MAIN TITLE interactivity
@app.callback(
    [Output("dsgn_title_1", "className"),Output("dsgn_title_2", "className")],
    # Output("dsgn_title_2", "className"),
    [   Input("ctrl_dsgn_title_1", "value"),
        # Input("ctrl_opac", "value"),
    ],
)
def title_main(text_color):
    print(text_color)
    # global fig

    return [text_color, text_color]

# Button design
@app.callback(
    Output("ctrl_continent", "className"),
    # Output("dsgn_title_2", "className"),
    [   Input("ctrl_dsgn_title_1", "value"),
        # Input("ctrl_opac", "value"),
    ],
)
def continent_button_style(text_color):
    print(text_color)
    # global fig

    return text_color


app.run_server(mode='external', port = 8011)


```

## Image of APP

[![enter image description here][2]][2]


  [1]: https://i.stack.imgur.com/XHoFx.png
  [2]: https://i.stack.imgur.com/NGfOi.png
