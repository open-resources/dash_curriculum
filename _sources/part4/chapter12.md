# Chapter 12  Advanced Styling and Layout

```{admonition} What you will learn

- How to set a theme with a CSS stylesheet using `JupyterDash(external_stylesheets=[dbc.themes.SLATE])`
- How elements of a theme are styled through references to the stylesheet
- How you can change component layout through changing references to your stylesheet with `className` or `class_name`.
- A variety of classnames
  - text color | `text-primary`
  - background color `bc-success`
  - margin `m-1`
  - padding `p-1`
  - rounded edges
  - opacity `opacity-25`
- Special layout attributes for `dbc.Col()`
- `no_gutters = bool` !!!=> is this removed for newer versions?
- `justify = 'start'` # or center, end, between, around 
- Special layout attributes for `dbc.Container()`
  - `fluid = True`
- How to change the layout of a component directly with `style`


```

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

The next section will describe how to edit these properties through `className` and `style`
     
## 12.2
    
---

## Unclear:

- how to change *complete* theme through callbacks on `JupyterDash(external_stylesheets=[dbc.themes.SLATE])`? => Only via clientside callback
- can you set `order` of `dbc.Row()` components as you can with `dbc.Col()`. `align`?
- `external_stylesheets=[dbc.themes.SLATE]` < `className` < `style`?
- when you set background color through `style={"height": "100%", "background-color": "grey"}`, where do the changes go? Directly in the component? Or through the css?

- Why isn't `dcc.Markdown()` affected by `justify = 'center' ` here ?:

```python
app.layout = dbc.Container(dbc.Row([dcc.Markdown('# CSS in action',
                                                 id = 'title_1',
                                                 className = 'text-body'),
                                    
                                    dbc.Col([dcc.Markdown('### Layout controls',
                                                          id = 'crd_concrol_title',
                                                          className = 'text-body'),


```

### className combinations:

- `" opacity-25 p-2 m-1 bg-primary bg-gradient text-light fw-bold rounded "`

- `" opacity-75 p-2 m-1 bg-success bg-opacity-25 text-light rounded-bottom "`

### className gotchas

Without a leading `space`, the first element `opacity-75` is ignored
Without a trailing `space`, the last element `rounded-bottom` will also likely be ignored, ***but*** the `bottom` property seems to be globally set by `[dbc.themes.SLATE]` and is uneditable???

## Resources:

https://bootswatch.com/

RGB

https://www.rapidtables.com/web/color/RGB_Color.html

Dash component row height

https://github.com/facultyai/dash-bootstrap-components/issues/286
      
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
import plotly.io as pio

import dash_core_components as dcc
import dash_html_components as html

# app = JupyterDash(__name__)

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from dash import State, Input, Output, Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import json

# Initialise the App 
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app = JupyterDash(external_stylesheets=[dbc.themes.SLATE])
# app = JupyterDash()



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
opts_fig_template = [{'label': k, 'value': k} for k in list(pio.templates)]

card_cols_width = 2
card_cols_offset = 2

# Set up well organized controls in a dbc.Card()
controls = dbc.Card([dbc.Row([dbc.Col([dbc.Label("Continent"),
                                      dcc.Dropdown(id='ctrl_continent',
                                                 options= opts_continent,
                                                  value='All',
                                                  # className = "text-danger"
                                                )], width = {'size':card_cols_width, 'offset':card_cols_offset}
                                      
                                      )
                             ], #width=2
                            ),
                     
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
#                     dbc.Row([dbc.Label("Button 1"),
#                                    dbc.Button(id='btn1',
#                                                 # # options=[{'label': k, 'value': k} for k in opts_years],
#                                               color = 'warning',
#                                               className = 'rounded'
#                                                 # value=df.year.max(),
                                              
#                                                 ),
#                                     ],),
                    dbc.Row([dbc.Label("Figure template"),
                                   dcc.Dropdown(id='fg_template',
                                                # # options=[{'label': k, 'value': k} for k in opts_years],
                                              # color = 'warning',
                                              # className = 'rounded''
                                              
                                              options = opts_fig_template,
                                              # value=opts_fig_template[0]
                                              
                                                ),
                                    ],),
                     
                        #  paper_bgcolor='rgba(0,0,0,0)',
                        # plot_bgcolor='rgba(0,0,0,0)'
                     
                     
                    dbc.Row([dbc.Label("Figure transparency"),
                                   dcc.Slider(id='fg_bg_transparency',
                                                # # options=[{'label': k, 'value': k} for k in opts_years],
                                              # color = 'warning',
                                              # className = 'rounded''
                                              min = 0,
                                              max = 100,
                                              value = 0, 
                                              # options = opts_fig_template,
                                              marks = {i*10: str(i*10) for i in range(11)}
                                              # value=opts_fig_template[0]
                                              
                                                ),
                                    ],),
                     
                     
                    ],
                    id='card_1', 
                    body=True,
                    # width = 2,
                    # className = "opacity-25 p-2 m-1 bg-primary text-light fw-bold rounded",
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
                                     
                                     # dcc.Dropdown(id='ctrl_dsgn_button',
                                     #              options= opts_title_main,
                                     #              # value='All'
                                     #            ),
                                     dbc.Label("dbc.Card className"),
                                     dcc.Input(id='ctrl_dsgn_button',
                                                  # options= opts_title_main,
                                                  type = 'text',
                                                  className = 'rounded'
                                                  # value='All'
                                                ),
                                     
                                     # dbc.Label("Figure template"),
                                     # dcc.Dropdown(id='fg',
                                     #              options= list(pio.templates),
                                     #              type = 'text',
                                     #              # className = 'rounded'
                                     #              # value='All'
                                     #            ),
                                     
                                   ],),
                    ],
                    body=True,
                    style = {'font-size': 'large'}
                    )

# Set up the app layout using dbc.Container(), dbc.Row(), and dbc.Col()
app.layout = dbc.Container([html.H1("Data selection and figure design", id='dsgn_title_1',  className="text-primary"),
                            html.Hr(),
                            dbc.Row([dbc.Col([controls],xs = 3),
                                     # dbc.Col([dbc.Row([dbc.Col(dcc.Graph(id="fig_scatter_1")),])]),
                                     # dbc.Col([(dcc.Graph(id="fig_scatter_1")),],style={"height": "100%", "background-color": "red"}),
                                       dbc.Col([(dcc.Graph(id="fig_scatter_1",
                                                          style={"height": "100%", "background-color": "yellow"}
                                                          )),],
                                               style={"height": "100%",
                                                      # "background-color": "red"
                                                     }, width = 6),
                                    ],style={"height": "55vh"}), # (vh is "viewport height", so 100vh means "100% of screen height", see
                            html.H1("Layout design", id='dsgn_title_2',  className="text-primary"),
                            html.Hr(),
                            dbc.Row([dbc.Col([controls_layout],xs = 3),
                                     # dbc.Col([dbc.Row([dbc.Col(dcc.Graph(id="fig_scatter_1")),])]),
                                    ]),
                            html.Br(),
                            ],
                            fluid=True,
                            # style={"height": "75vh"}
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
        Input("fg_template", "value"),
        Input("fg_bg_transparency", "value")
        # Input("ctrl_opac", "value"),
    ],
)
def history_graph(xval, yval, continent, size, color, year, template, transparency):
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
                  
    fig = px.scatter(df, x=xval, y=yval, size = None if size == 'None' else size,
                     color = color
                    )
    fig.update_layout(template = template)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,' + str(transparency / 100) + ')')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,' + str(transparency / 100) + ')')
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
    Output("card_1", "className"),
    # Output("dsgn_title_2", "className"),
    [   Input("ctrl_dsgn_button", "value"),
        # Input("ctrl_opac", "value"),
    ],
)
def continent_dropdown_style(text_color):
    print(text_color)
    # global fig

    return text_color


app.run_server(mode='external', port = 8031)
```

## Image of APP

[![enter image description here][2]][2]

# IV - APP / Dashboard CSS IN ACTION

```python

################################
# APP/DASHBOARD: CSS IN ACTION #
################################


################################
# APP/DASHBOARD: CSS IN ACTION #
################################

import plotly.graph_objects as go
import plotly.express as px
from jupyter_dash import JupyterDash
import plotly.io as pio

import dash_core_components as dcc
import dash_html_components as html

# app = JupyterDash(__name__)

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from dash import State, Input, Output, Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import json

# I - APP SETUP AND THEME SELECTION
app = JupyterDash(external_stylesheets=[dbc.themes.SLATE])

# options for control components (ctrls_crd1) in Card 1 (id = 'crd_1')
opts_ddn_main_title = [{'label': 'Set text color', 'value': 'text-primary'},
                       {'label': 'Set background color', 'value': 'bg-primary'},
                       {'label': 'Set component margin', 'value': 'm-1'},
                       {'label': 'Set component padding', 'value': 'p-1'},
                      ]

opts_ddn_scnd_title = [{'label': 'Set text color', 'value': 'text-primary'},
                       {'label': 'Set background color', 'value': 'bg-primary'},
                       {'label': 'Set component margin', 'value': 'm-1'},
                       {'label': 'Set component padding', 'value': 'p-1'},
                      ]

opts_ddn_crd_1 = [{'label': 'Set card margins', 'value': 'm-1'},
                  {'label': 'Set card padding', 'value': 'p-1'},
                 ]

opts_ddn_crd_2 = [{'label': 'Set card margins', 'value': 'm-1'},
                  {'label': 'Set card padding', 'value': 'p-1'},
                 ]

print(opts_ddn_crd_2)

# control components in Card 1 ()
ctrls_crd1 = [dbc.Row([dbc.Col([dbc.Label("Component"),
                                dcc.Markdown('Main title',
                                             style={'marginTop' : '10px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('Secondary titles'),
                                dcc.Markdown('Layout card'),
                                dcc.Markdown('Figure card'),
                               ],
                              width = 2),
                       
                       dbc.Col([dbc.Label("Action"),
                                dcc.Dropdown(id='ddn_main_title',
                                             options = opts_ddn_main_title,
                                             style={'marginTop' : '10px', 'height': '30px', 'width': '200px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_scnd_title',
                                             options = opts_ddn_scnd_title,
                                             style={'marginTop' : '10px', 'height': '30px', 'width': '200px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_crd_1',
                                             options = opts_ddn_crd_1,
                                             style={'marginTop' : '10px', 'height': '30px', 'width': '200px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_crd_2',
                                             options = opts_ddn_crd_2,
                                             style={'marginTop' : '10px', 'height': '30px', 'width': '200px'},
                                             clearable = True),
                                
                               ],
                              width = 4),
                       
                       dbc.Col([dbc.Label("CSS / className"),
                                dbc.Input(id = 'ipt_main_title',
                                          placeholder="Ready for action",
                                          type="text",
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '200px'},
                                         ),
                                dbc.Input(id = 'ipt_scnd_title',
                                          placeholder="Ready for action",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '200px'},
                                         ),
                                dbc.Input(id = 'ipt_crd_1',
                                          placeholder="Ready for action",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '200px'},
                                         ),
                                dbc.Input(id = 'ipt_crd_2',
                                          placeholder="Ready for action",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '200px'},
                                         ),
                               ],
                              width = 4, )
                      ],
                     # 
                     ),
             ]

# Resources for previous section
#
# dcc.Markdown: https://dash.plotly.com/dash-core-components/markdown
# dbc.Label: no direct link, but info available here: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/
# dcc.Dropdown: https://dash.plotly.com/dash-core-components/dropdown
# dcc.Dropdown, change height: https://community.plotly.com/t/dcc-dropdown-change-height/17464

# II - APP LAYOUT
app.layout = dbc.Container(dbc.Row([dcc.Markdown('# CSS in action',
                                                 id = 'title_1',
                                                 className = 'text-body'),
                                    
                                    dbc.Col([dcc.Markdown('### Layout controls',
                                                          id = 'crd_concrol_title',
                                                          className = 'text-body'),
                                             dbc.Card(ctrls_crd1,
                                                      id = 'crd_1',
                                                      # className = 'bg-danger'
                                                     ),
                                            ],
                                            width = {'size': 4},
                                            
                                           ),
                                    
                                    dbc.Col([dcc.Markdown('### Figure',
                                                          id = 'crd_figure_title',
                                                          className = 'text-secondary'),
                                             dbc.Card([dcc.Graph()],
                                                      id = 'crd_2')
                                            ],
                                            width = {'size': 4},
                                           )
                                   ], justify = 'around', # end, center, between, around
                                  ), fluid = True)

# Resources for previous section
#
# dbc.Card: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/

# III - CALLBACKS

# Callback group 1: 
# Set main title className through main_title_css chained to main_title_layout():
@app.callback(Output("ipt_main_title", "value"),
              [Input("ddn_main_title", "value"),]
             )
def main_title_layout(cName_element):
    return cName_element

@app.callback(Output("title_1", "className"),
              [Input("ipt_main_title", "value"),]
             )
def main_title_css(cName_element):
    return cName_element

# Callback group 2:
# Set card title classNames through scnd_title_css chained to scnd_title_layout():
@app.callback(Output("ipt_scnd_title", "value"),
              [Input("ddn_scnd_title", "value"),]
             )
def scnd_title_layout(cName_element):
    return cName_element

@app.callback([Output("crd_concrol_title", "className"),
               Output("crd_figure_title", "className")],
              [Input("ipt_scnd_title", "value"),]
             )
def scnd_title_css(cName_element):
    return cName_element, cName_element

# Callback group 3:
# Set Layout card component classNames through crd1_css chained to crd1_layout():
@app.callback(Output("ipt_crd_1", "value"),
              [Input("ddn_crd_1", "value"),]
             )
def crd1_layout(cName_element):
    return cName_element
@app.callback(Output("crd_1", "className"),
              [Input("ipt_crd_1", "value"),]
             )
def crd1_css(cName_element):
    return cName_element

# Callback group 4:
# Set Figure 1 card component classNames through crd2_css chained to crd2_layout():
@app.callback(Output("ipt_crd_2", "value"),
              [Input("ddn_crd_2", "value"),]
             )
def crd2_layout(cName_element):
    return cName_element
@app.callback(Output("crd_2", "className"),
              [Input("ipt_crd_2", "value"),]
             )
def crd2_css(cName_element):
    return cName_element
                         
app.run_server(mode='external', port = 8032)                                              
```
[![enter image description here][3]][3]


 
  [1]: https://i.stack.imgur.com/XHoFx.png
  [2]: https://i.stack.imgur.com/NGfOi.png
  [3]: https://i.stack.imgur.com/EJw6S.png
