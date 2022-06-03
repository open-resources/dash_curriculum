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

There are many different ways you can change the layout and add themes to your Plotly Dash app. In this chapter you will learn how to set a theme with `external_stylesheets=[dbc.themes.<theme>]` where `'<theme>'` can by any of `['BOOTSTRAP',  'CERULEAN', 'COSMO', 'CYBORG', 'DARKLY', 'FLATLY', 'GRID'. For an exhaustive list, run `dir(dbc.themes)` and see which are available for your current versions of Dash Bootstrap components.
 
Your choice of theme will determine the look and feel of a variety of elements in your dashboard, ranging from the color of the background to the opacity of cards or the size of each component for different sizes of your device screen.

Here's how some elements will look like with `'BOOTSTRAP'`:

[![enter image description here][1]][1]

And here's how the same elemets will look like with `'SLATE'`:

[![enter image description here][2]][2]

You can study more themes and more components in [dash-bootstrap-components][3]
 

## 12.2 Theme and the cascading style sheet, or CSS


You set up your Dash app and select a theme like this:

```python
Dash(external_stylesheets=[dbc.themes.SLATE])
```

What hides behind `dbc.themes.SLATE` is the link `https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css` which points to a cascading styleshett or `CSS`. For most web applicatoins, `CSS` goes hand in hand with `HTML`. In genereal, `HTML` is a language that let's you build web pages. In short, Plotly Dash is a set of tools that let's you produce `HTML` components that look nice and act well togehter. And a `CSS` file defines how these components look and behave with regards to the layout.

One such component can be a header `dcc.Markdown()` that you can use as a title for your app or dashboard. If you use the `BOOTSTRAP` theme, the default font color of your heading will be of a dark grey type with the RGB code `(33, 37, 47)` and look like this:


 In the context of the theme, this particular color is mapped to `text-body`. And if you do a little search in the link above, you'll find *one* occurence of `text-body` in the `css` file:

    .text-body{--bs-text-opacity:1;color:rgba(var(--bs-body-color-rgb),var(--bs-text-opacity))

In the world of `CSS`, this is called a class. All classes are preceded with a period sign. And within the curly brackets we have multiple `property-value` pairs with a colon separating the `property` and `value` with a semicolon between each pair. One such `property` is `color` with the corresponding value:
    
  
     var(--bs-body-color-rgb)
     
     
This points to a setting at the start of the document that reveals the `rgb()` code used by `text-body`:

    bs-body-color-rgb:33,37,43

    
[![enter image description here][4]][4]

The reason this whole thing is structured this way, is that you can use the same color code through a unique variable across several sections of the `CSS`. The next section in this chapter will describe how to edit these properties through the `class_name` attribute. At the end of the chapter you'll also learn how to design specific details through the `style` attribute of your components.
     
## 12.3 The `class_name` attribute

Most (or all?) Dash components have an attribute `class_name` that let's you reference the name of a class in a `CSS` file. This attribute will also let you change other layout features through selecting other class names than, for example, the default `text-body` for `dcc.Markdown()`.

```{warning}

In order to be able to change the layout through `class_name`, a stylesheet *must*  be specified in 

    app = Dash(external_stylesheets=[dbc.themes.<theme>])

```


## 12.3.1 How to change font color

Some alternatives to `body` in `text-body` are `primary`, `secondary`, `success`, `danger`, and `info`. For other options, take a look at the cheatsheet at [pythonanywhere.com][5]. The following snippet builds on elements and principles of former chapters, and produces a markdown component that you can use as a header for your dasboards.

```python

from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([dbc.Row([dbc.Col([dcc.Markdown('# Dashboard title', className ="text-info bg-primary")], width = 10)])])

app.run_server(mode='inline', port = 9000) 

```

[![enter image description here][6]][6]

Below is the output with `Dasboard title` displayed as a heading in the colorcode we demonstrated earlier. Recall that this color corresponds to the color associated with `text-body` in the `CSS`-file. In order to change the color, just incldue, for example, `class_name = "text-info"` in your `dcc.Markdwon()` function call:

```python
from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([dbc.Row([dbc.Col([dcc.Markdown('# Dashboard title', className ="text-info")], width = 10)])])

app.run_server(mode='inline', port = 9000)  
```

[![enter image description here][7]][7]

```{admonition} Why all the extra components?

You might wonder why we've chosen to include the full `dbc.Container([dbc.Row([dbc.Col([dcc.Markdown()])])])` in these demonstrations. That's to comply with established standards of the former chapters. A `dbc.Contatiner()` forms the foundation of the app and holds one or more `dbc.Row()` components. These can hold one or more `dbc.Col()` components which in turn holds all our tables, figures and callbacks etc.

Also, all these components can offer slightly different functionalities on how to apply `className` and `style` depending on what you'd like to do. But we'll come back to that later.

```

## 12.3.2 How to change background 

Recall that the alternatives to `text-body` like `text-primary` and `text-secondary` aren't actual colors, but points to different colors set by the `CSS` file. So you can think of these options as different categories of the information you'd like to display. The same thing goes for other features of our `dcc.Markdown()` example as well as all other Dash components, like background color. The following snippet changes the white background of the BOOTSTRAP theme to a rich blue color. And if you'd like to know *exactly* which color that is, you already know how to find that out through studying the `CSS` file. Notice in the snippet below that all you have to do to change the background color is to include `bg-primary` in `className`. `bg` stands for *background*. Later we'll touch upon other abbreviations like `m` for *margin* and `p` for *padding*.

```python
from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([dbc.Row([dbc.Col([dcc.Markdown('# Dashboard title', className ="bg-primary")], width = 10)])])

app.run_server(mode='inline', port = 9000) 

```

[![enter image description here][8]][8]

Above we've only changed the background color, and let the text color remain `text-body`. The following sections will demonstrate how to do edit multiple features at the same time.

## 12.3.3 How to change font *and* background color

So far, the whole `CSS` thing can seem a bit complicated, but this particular section is where all suddenly (hopefully) makes sense. In order to change text color and background color at the same time, just include both `text-info` and `bg-primary` separated by `space` in `className`:

```python

from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([dbc.Row([dbc.Col([dcc.Markdown('# Dashboard title', className ="text-info bg-primary")], width = 10)])])

app.run_server(mode='inline', port = 9000)  


```

And you do not in any way have to stop there. In the next subchapters you'll learn how to add controls that are contained in a `dbc.Card()` component, how to style that component, and how to make room for the different elements using padding `p-1`, and margin `m-1` in the `className` attribute. By "controls", we mean anything from buttons to dropdowns and input fields, as well as accompanying labels to describe what they do.

[![enter image description here][9]][9]


## 12.3.4 Spacing, margins and padding

Often, a `HTML` child component will take on the same size as its parent. This should mean that a `dbc.Col()` contained by a `dbc.Row()` component would span the entire height and width of the former. This is however not the case. If we add a color such as `bg-primary` to the `dbc.Row` component you'll see that there are margins on the right and left hand sides as well as at the bottom.

[![enter image description here][10]][10]



```python

from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([dbc.Row([dbc.Col([dcc.Markdown('# Dashboard title', className ="text-info bg-primary mt-0")
                                             ]
                                            )
                                    ],className = 'bg-secondary')])

app.run_server(mode='inline', port = 9000)

```

If we were to put this is `className` terms, this means the the default setting of the `dbc.Row` margin is `mt-0`. This follows a naming convention `property-side-size`, where `property`, when it comes to [spacing][11], can be one of:

- `m` - `margin`, the space between a parent and a child component.
- `p` -  `padding`, component and features of that component such as text.


`side` can be one of:

- `t` - `top` for classes that set margin-top or padding-top
- `b` - `bottom` for classes that set margin-bottom or padding-bottom
- `s` - `start` for classes that set margin-left or padding-left
- `e` - `end` for classes that set margin-right or padding-right
- `x` - for classes that set both *-left and *-right
- `y` - for classes that set both *-top and *-bottom
- *`blank`* - for classes that set a margin or padding on all 4 sides of the element

`size` can be one of `0`, `1`, `2`, `3`, `4`, `5` where `0` eliminates the margin or padding. Take a look at [mdbootstrap.com][11] for more info on other size options. So far, you know enough to apply an arguably more visually appealing composition of these row and column components by replacing `m-0` with `m-1` or `m-2` in the `dbc.Row` className:

[![enter image description here][12]][12]

```python

from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([dbc.Row([dbc.Col([dcc.Markdown('# Dashboard title', className ="text-info bg-primary m-2")
                                             ]
                                            )
                                    ],className = 'bg-secondary')])

app.run_server(mode='inline', port = 9000)

```

## 12.3.5 Component placement

You should expect that different components from different libraries such as `dcc`, `dbc` and `HTML` come with different default settings with regards to margins, paddings and other features such as text alignment. This section will not go through all default settings for all relevant components, but rather demonstrate how to handle different settings and make sure your layout turns out the way you want it to. So lets take the setup that we've already got, and add a row with a `dbc.Label` component. Without defining any margins or padding, but with some background color to discern the different elements, the snippet below will produce the dashboard illustrated in this image:

[![enter image description here][13]][13]



```python

from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([dbc.Row([dbc.Col([dcc.Markdown('#### Dashboard title', className ="text-info bg-primary")])], className = 'bg-secondary'),
                            dbc.Row([dbc.Col([dbc.Label('Label 1', className = "bg-warning")])],className = 'bg-secondary')])

app.run_server(mode='inline', port = 9008)

```

As it now stands, the dashboard isn't exaclty very pleasing to the eye. The two rows have got the same widths, but the background color of the components they contain span different widths. In addition, the paddings for "Dashboard title" and "Label 1" look very different. In this case, we could overcome these obstacles by using the same component in both instances. But when you're going to build dashboards out in the wild, you're very likely going to need different components with different properties to align nicely. So let's take a look at the details on how to make it all visually pleasing. For the remainder of this section, we will only show the changes we've made in stand-alone code snippets, and then show the whole thing in a complete snippet at the end.

The first thing we'll do is add `p-1` in `className ="text-info bg-primary p-1")` for the `dcc.Markdown` component and `p-2` in `className = "bg-warning p-2"` for the `dbc.Label` component. This way we'll get approximately the same space around the texts `Dashboard title` and `Label 1`, while the font sizes provide different emphasis to the content:

[![enter image description here][14]][14]


## 12.3.6 How to handle layout challenges with `style`












## 12.3.5 A rounded, transparent card

## 12.3.6 








    
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

[![enter image description here][15]][15]

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
[![enter image description here][16]][16]


 


  [1]: https://i.stack.imgur.com/Vunbd.png
  [2]: https://i.stack.imgur.com/EvbEU.png
  [3]: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
  [4]: https://i.stack.imgur.com/BFgvm.png
  [5]: https://dashcheatsheet.pythonanywhere.com/
  [6]: https://i.stack.imgur.com/iCkRA.png
  [7]: https://i.stack.imgur.com/d9pqj.png
  [8]: https://i.stack.imgur.com/vLWvz.png
  [9]: https://i.stack.imgur.com/dfjKw.png
  [10]: https://i.stack.imgur.com/muWaZ.png
  [11]: https://mdbootstrap.com/docs/standard/utilities/spacing/
  [12]: https://i.stack.imgur.com/PkwOL.png
  [13]: https://i.stack.imgur.com/Uu0Ee.png
  [14]: https://i.stack.imgur.com/UWulS.png
  [15]: https://i.stack.imgur.com/NGfOi.png
  [16]: https://i.stack.imgur.com/EJw6S.png
