# Chapter 12  Advanced Styling and Layout

```{admonition} What you will learn
- How to set a theme with a CSS stylesheet using `JupyterDash(external_stylesheets=[dbc.themes.SLATE])`
- How elements of a theme are styled through references to different classes in the stylesheet
- How you can change component layout through changing references to your stylesheet with `className` or `class_name` dending on library and version.
- A variety of classnames
  - text color `text-primary`
  - background color `bg-primary`
  - margin  `m-1`
  - padding `p-1`
  - rounded edges `rounded`
  - opacity `opacity-25`
- How multiple features are referenced in the same className call `"text-info bg-primary"`
- How the same component part can be referenced multiple times with `"bg-primary bg-opacity-25"`
- Special layout attributes for `dbc.Row()`
  - `justify = 'start'` # or center, end, between, around 
- Special layout attributes for `dbc.Container()`
  - `fluid = True`
- How to change the layout of a component directly with `style`
```

## 12.1 The theme of a Dash app

You can change the layout and add themes of your Plotly Dash app in many different ways you can . In this chapter you will learn how to set a theme with `external_stylesheets=[dbc.themes.<theme>]` where `'<theme>'` can by one of:

- `bootstrap`
- `cosmo`
- `cyborg`
- `darkly`
- `flatly`
- `grid`

For an exhaustive list, run `dir(dbc.themes)` and see which are available to your current version of Dash Bootstrap Components (`dbc`).
 
Your choice of theme will determine the look and feel of a variety of elements in your dashboard, ranging from the color of the background to the opacity of cards or the size of each component for different sizes of your device screen.

Here's how some elements will look like with the `bootstrap` theme:

[![enter image description here][1]][1]

And here's how the same elemets will look like with the `slate` theme:

[![enter image description here][2]][2]

You can study more themes and components in [dash-bootstrap-components][3].
 

## 12.2 Theme and the Cascading Style Sheet

You set up your Dash app and select a theme like this:

```python
app = Dash(external_stylesheets=[dbc.themes.SLATE])
```

What hides behind `dbc.themes.SLATE` is the link `https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css` which points to a certain cascading stylesheet or, `CSS`. For most web applicatoins, `CSS` goes hand in hand with `HTML`. In general, `HTML` is a language that lets you build web pages. and Plotly Dash can be regarded as a set of tools that lets you produce `HTML` components that look nice and act well togehter. A `CSS` file defines how these components look and behave with regards to the layout.

One such component can be the text container `dcc.Markdown()` that you can use as a title for your app or dashboard. If you use the `bootstrap` theme, the default font color of your heading will be of a dark grey type with the RGB code `(33, 37, 47)` and look like this:

[![enter image description here][4]][4]


 This particular color is mapped to `text-body` in the `CSS` file. And if you do a little search in the link above, you'll find *one* occurence of `text-body` in the `CSS` file:

    .text-body{--bs-text-opacity:1;color:rgba(var(--bs-body-color-rgb),var(--bs-text-opacity))

This is called a class. All classes are preceded with a period sign. And within the curly brackets we have multiple `property-value` pairs with a colon separating the `property` and `value`, and a semicolon between each pair. One such `property` is `color` with the corresponding value:
    
  
     var(--bs-body-color-rgb)
     
     
This points to a setting at the start of the document that reveals the `rgb()` code used by `text-body`:

    bs-body-color-rgb:33,37,43

You can use reources such as [RapidTables][5] to verfiy that you're lookin at the correct color:
    
[![enter image description here][6]][6]

The reason this whole thing is structured this way, is that you can use the same color code through a unique variable across several parts of the `CSS`. The next section in this chapter will describe how to edit these properties through the `className` attribute. At the end of the chapter you'll also learn how to design specific details through the `style` attribute of your components.
     
## 12.3 The `className` attribute

Most (or all?) Dash components have an attribute `className` that lets you reference the name of a class in a `CSS` file. This attribute will also let you change other layout features through selecting other class names than, for example, the default `text-body` for `dcc.Markdown()`.

```{warning}
In order to be able to change the layout through `classNaame`, a stylesheet *must*  be specified in 
    app = Dash(external_stylesheets=[dbc.themes.<theme>])
```

## 12.3.1 How to change font color

Some alternatives to `body` in `text-body` are:

- `primary`
- `secondary`
- `success`
- `danger`
- `info`

For other options, take a look at the cheatsheet at [pythonanywhere.com][7]. The following snippet builds on elements and principles of former chapters, and produces a markdown component that you can use as a header for your dasboards.¨

#### 12.3.1 - Code snippet 1

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [dcc.Markdown("# Dashboard title")],
                    width=10,
                )
            ]
        )
    ]
)

app.run_server(debug=True)
```
````

#### 12.3.1 - Code output 1

[![enter image description here][8]][8]

Below is the output with `Dasboard title` displayed as a heading in the colorcode we demonstrated earlier. Recall that this color corresponds to the color associated with `text-body` in the `CSS` file. In order to change the color, just include, for example, `class_name = "text-info"` in your `dcc.Markdwon()` function call.


#### 12.3.1 - Code snippet 2

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [dcc.Markdown("# Dashboard title", className="text-info")], width=10
                )
            ]
        )
    ]
)
app.run_server(debug=True)
```
````

#### 12.3.1 - Code output 2

[![enter image description here][9]][9]

```{admonition} Why all the extra components in the examples?
You might wonder why we've chosen to include the full `dbc.Container([dbc.Row([dbc.Col([dcc.Markdown()])])])` in these demonstrations. That's to comply with established standards of the former chapters. A `dbc.Contatiner()` forms the foundation of the app and holds one or more `dbc.Row` components. These can hold one or more `dbc.Col` components which in turn hold all our tables, figures and controls etc.

Also, all these components can offer slightly different functionalities on how to apply `className` and `style` depending on what you'd like to do. But we'll come back to that later.
```

## 12.3.2 How to change background color

Recall that the alternatives to `text-body` like `text-primary` and `text-secondary` aren't actual colors, but rather pointers to different colors set by the `CSS` file. So you can think of these options as different possible categories of the information you'd like to display. The same thing goes for other features of our `dcc.Markdown()` example like background color. The following snippet changes the white background of the `BOOTSTRAP` theme to a rich blue color. And if you'd like to know *exactly* which color that is, you already know how to find that out through studying the `CSS` file. Notice in the snippet below that all you have to do to change the background color is to include `bg-primary` in `className`. `bg` stands for *background*. Later we'll touch upon other abbreviations like `m` for *margin* and `p` for *padding*.

#### 12.3.2 - Code snippet
````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [dcc.Markdown("# Dashboard title", className="bg-primary")],
                    width=10,
                )
            ]
        )
    ]
)
app.run_server(debug=True)

```
````

#### 12.3.2 - Code output

[![enter image description here][10]][10]

Above we've only changed the background color, and let the text color remain `text-body`. The following sections will demonstrate how to edit multiple features at the same time.

```{warning}

Misspellings in `className` will *not* raise any errors. Any additions to `className` that can not be interpreted are simply ignored.

```

## 12.3.3 How to change font *and* background color

So far, the whole `CSS` thing can seem a bit complicated, but this particular section is where all suddenly (hopefully) makes sense. In order to change text color and background color at the same time, just include both `text-info` and `bg-primary` separated by `space` in `className`:

#### 12.3.3 Code snippet
````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "# Dashboard title", className="text-info bg-primary"
                        )
                    ],
                    width=10,
                )
            ]
        )
    ]
)
app.run_server(debug=True) 
```
````

#### 12.3.3 Code output

[![enter image description here][11]][11]


And you do not have to stop there. In the next subchapters you'll learn how to add controls that are contained in a `dbc.Card()` component, how to style that component, and how to make room for the different elements using padding `p-1`, and margin `m-1` in the `className` attribute. By "controls", we mean anything from buttons to dropdowns and input fields, as well as accompanying labels to describe what they do.


## 12.3.4 Spacing, margins and padding

Often, a `HTML` child component will take on the same size as its parent. This should mean that a `dbc.Col` contained by a `dbc.Row` component would span the entire height and width of the former. This is however not the case. If we add a color such as `bg-primary` to the `dbc.Row` component you'll see that there are margins on the right and left hand sides as well as at the bottom.

#### 12.3.4 Code snippet 1

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "# Dashboard title", className="text-info bg-primary mt-0"
                        )
                    ]
                )
            ],
            className="bg-secondary",
        )
    ]
)

app.run_server(debug=True)
```
````

#### 12.3.4 Code output 1

[![enter image description here][12]][12]

If we were to put this in `className` terms, this means the the default setting of the `dbc.Row` margin is `mt-0` which translates to `"margin at top is zero"`. This follows a naming convention `property-side-size`, where `property`, when it comes to [spacing][13], can be one of:

- `m` - `margin`, the space between a parent and a child component.
- `p` -  `padding`, component and features of that component such as text.


And `side` can be one of:

- `t` - `top` for classes that set margin-top or padding-top
- `b` - `bottom` for classes that set margin-bottom or padding-bottom
- `s` - `start` for classes that set margin-left or padding-left
- `e` - `end` for classes that set margin-right or padding-right
- `x` - for classes that set both *-left and *-right
- `y` - for classes that set both *-top and *-bottom
- *`blank`* - for classes that set a margin or padding on all 4 sides of the element

At last, `size` can be one of `0`, `1`, `2`, `3`, `4`, `5` where `0` eliminates the margin or padding. Take a look at [mdbootstrap.com][13] for more info on other size options. So far, you know enough to apply an arguably more visually appealing composition of these row and column components by replacing `m-0` with `m-1` or `m-2` in the `dbc.Row` className.

### 12.3.4 Code snippet 2

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "# Dashboard title", className="text-info bg-primary m-2"
                        )
                    ]
                )
            ],
            className="bg-secondary",
        )
    ]
)

app.run_server(debug=True)
```
````

### 12.3.4 Code output 2

[![enter image description here][14]][14]

## 12.3.5 Component placement

You should expect that different components from different libraries such as `dcc`, `dbc` and `HTML` come with different default settings with regards to margins, paddings and other features such as text alignment. This section will not go through all default settings for all relevant components, but rather demonstrate how to handle different settings and make sure your layout turns out the way you want it to. So lets take the setup that we've already got, and add a row with a `dbc.Label` component. Without defining any margins or padding, but with some background color to discern the different elements, the following snippet will produce the dashboard illustrated below.


### 12.3.5 Code snippet 1
````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title", className="text-info bg-primary"
                        )
                    ]
                )
            ],
            className="bg-secondary",
        ),
        dbc.Row(
            [dbc.Col([dbc.Label("Label 1", className="bg-warning")])],
            className="bg-secondary",
        ),
    ]
)
app.run_server(debug=True)
```
````

### 12.3.5 Code output 1

[![enter image description here][15]][15]

As it now stands, the dashboard isn't exactly very pleasing to the eye. The two rows have got the same widths, but the background color of the components they contain span *different* widths. In addition, the paddings for "Dashboard title" and "Label 1" look very different. In this case particular, we could overcome these obstacles by using the same component in both instances. But when you're going to build dashboards out in the wild, you're very likely going to need different components with different properties to align nicely. So let's take a look at the details on how to make it all visually pleasing.

The first thing we'll do is adding `p-1` in `className ="text-info bg-primary p-1"` for the `dcc.Markdown` component and `p-2` in `className = "bg-warning p-2"` for the `dbc.Label` component. This way we'll get approximately the same spacing around the texts `Dashboard title` and `Label 1`. The differnet font *sizes* still provide different emphasis to the content.

### 12.3.5 Code output 2.1 (snippet below)

[![enter image description here][16]][16]

Another result is that the markdown and label components no longer have a gap between them. If you'd like to keep the gap, you can choose to include it through either component. The image below shows the effect of including `"mt-2"` in `className = "bg-warning p-1 mt-2"` for the `dbc.Label` component:

### 12.3.5 Code output 2.2 (snippet below)

[![enter image description here][17]][17]

### 12.3.5 Code snippet 2

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title", className="text-info bg-primary"
                        )
                    ]
                )
            ],
            className="bg-secondary",
        ),
        dbc.Row(
            [dbc.Col([dbc.Label("Label 1", className="bg-warning p-1 mt-2")])],
            className="bg-secondary",
        ),
    ]
)

app.run_server(debug=True)
```
````

## 12.3.6 How to handle layout challenges with `style`

In the previous snippet, notice how `className ="bg-primary"` is set for `dcc.Markdown`, and how `className = "bg-warning"` is set for `dbc.Label` with very different results for the backgrounds. This is because the two components are set to "fill" the width of their parent components in different ways. In previous chapters, we've unsurprisingly set the width of `dbc.Col` components through the `width` attribute. However, if you run `help(dcc.Markdown)` and `help(dbc.Label)` you'll see that neither component has got a `width` attribute. This is where the `style` attribute comes into play if you'd like to align your components in a more visually pleasing way. With `style`, you can set the components widths to fill any percentage of the parent component, or to a certain amount of pixels. For the latter you'll use `style = {'width':'100px'}`, and for the former you can use either `style = {'width':'100%}` or `style = {'width':'100pc}`. Here's the same layout with `style = {'width':'75%}` for both components:

#### 12.3.6 Code snippet

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info bg-primary m-0",
                            style={"width": "75%"},
                        )
                    ]
                )
            ],
            className="bg-secondary ",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1", className="bg-warning", style={"width": "75%"}
                        )
                    ]
                )
            ],
            className="bg-secondary",
        ),
    ]
)
app.run_server(debug=True)
```
````

#### 12.3.6 Code output

[![enter image description here][18]][18]


```{note}

What you can do with `className` you can, for the most part, also do with `style` and vice versa. However, the attributes of your components are often referenced differently. One example is `"fw-bold"` for `className` and `"font-weight":"bold"` for `style`. The result will be the same, namely a bold font type for the object in question.
```

## 12.4 More components and more attributes

With some basic principles now firmly in place, all you'll need to put together a working and nice looking app is to increase the number of component types in your toolbox, as well as methods to include in `className`. In this section you'll learn how to build further on the previous examples and approach something that looks more like a complete dashboard by adding a `dbc.Button()` and a `dbc.Card()` component . The latter is often used to split a dashboard in different parts and as a container for more components. You'll also learn how to edit the appearance of your components with visual effects such as rounded edges and shadows.

## 12.4.1 A button and a card

For a more comprehensive list of boostrap components, refer to [this source][19]. For now we'll just add a `dbc.Button` in a new `dbc.Col` component next to our already existing `dbc.Label`. In addition, we'll include a `dbc.Card` in a `dbc.Col` component in a new `dbc.Row`.

#### 12.4.1 Code snippet

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info bg-primary",
                            style={"width": "100%"},
                        )
                    ]
                )
            ],
            className="text-info bg-secondary m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning m-0",
                            style={"width": "100%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="",
                    ),
                    width=4,
                ),
            ],
            className="bg-secondary m-0",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your content here",
                    className="",
                ),
                width=12,
            )
        ),
    ],
    className="",
)
app.run_server(debug=True, port=8118)
```
````

#### 12.4.1 Code output

[![enter image description here][20]][20]

## 12.4.2 Justify row components
In the previous snippet, we'ved used `width = 4` for both the `label` and the `button` which by default are placed at the start of the parent `row` component. To change this, you can include `justify = '<option>'` in the `row` component where your options are:

- `start`
- `center`
- `end`
- `around`
- `between`
- `evenly`

The image below shows the result for `justify = 'evenly'`. In additon we've included some margins and padding to make the title, label and button look a little nicer.

#### 12.4.2 Code snippet

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info bg-primary p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info bg-secondary m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="bg-secondary m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className="",
                ),
                width=12,
            )
        ),
    ],
    className="mt-2",
)
app.run_server(debug=True)
```
````

#### 12.4.2 Code output 

[![enter image description here][21]][21]

## 12.4.3 Set component height with `style = {'height':'200px'}`

Notice how we've cheated a bit by adding `'height':'65%'` for the `label` component style to make it align a bit better to the `button`. Before you're ready to fill your `card` with more components, it's often a good idea to increase the height of the card to give a better impression of how it will all look when your dashboard is nearing completeness. In the snippet below, we've included `'height':'200px'` for the `label` style attribute.

#### 12.4.3 Code snippet

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = rDash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info bg-primary p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info bg-secondary m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="bg-secondary m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-mt-2",
)
app.run_server(debug=True)
```
````

#### 12.4.3 Code output 1

[![enter image description here][22]][22]


## 12.4.4 Rounded edges

If you look closely at the edges of the `card`, you'll see that they are rounded by default. In order to apply rounded edges to other components, just include `"rounded"` in `className`. You can adjust the "weight" of the rounding by setting `rounded-{size}` where size can range from `0` to `3`. You can also specify which corners to round through `rounded-{corner}`, where `corner` can be:

- `top`
- `bottom`
- `start`
- `end`
- `circle`
- `pill`

The two last one will change not only the corners but the complete structure of the whole card to become circle or pill shaped.

```{tip}
When components come with rounded edges by default, you will sometimg have to include `rouned-0` before including `rounded-top` to round off the top *only*. This is the case with `dbc.Card`.
```

In the snippet below, we've rounded off the bottom of the card only, and set the weight to `3`.

#### 12.4.4 Code snippet

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info bg-primary p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info bg-secondary m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="bg-secondary m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="mt-1",
)
app.run_server(debug=True)
```
````

#### 12.4.4 Code output

[![enter image description here][23]][423]

## 12.4.5 Borders

So far, the background colors of the row and column components have served a purpose of visually discerning the various components rather than improving the aesthetics of the dashboard. So let's drop some of the background color, and rather separate the title from the components with a border. You can set the size of the border line with `border-{size}` where `size` can range from `1` to `5`. As with `rounded` you can set the position of the border with `border-{direction}` where `direction` can be:

- `top`
- `end`
- `bottom`
- `start`.

Don't forget that you can use a comnination of the list above with `className = " border-top border-bottom`.
In the snippet below we've added a thick grey border line below the title by adding `className = "border-top border-secondary border-3"` to the second `dbc.Row` component. We've also dropped the background colors for some of the components, and rather added a background color and some margins and padding to the `dbc.Container` itself with `className = 'bg-secondary mt-1 p-3'`


#### 12.4.5 Code snippet

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info bg-secondary m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary mt-1 p-3",
)
app.run_server(debug=True)
```
````

#### 12.4.5 Code output

[![enter image description here][24]][24]



## 12.4.6 Opacity

If you find that `bg-secondary` for the `db.Container` comes off as a bit too dominating, you can adjust the opacity of the background color with `opacity-{number}` where `number` can be `25`, `50` or `75`. Below we've used `bg-opacity-75` and also rounded off the `dbc.Container` corners with `className = 'bg-secondary bg-opacity-75 rounded-3 mt-1 p-3'`.

### 12.4.6 Code snippet
````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info bg-secondary m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 rounded-3 mt-1 p-3",
)
app.run_server(debug=True)
```
````

### 12.4.6 Code output
[![enter image description here][25]][25]

```{warning}
If you do not specify the context of `opacity`, like `bg-opacity`, *all* elements that are contained in your component will be affected.
```


## 12.4.7 Shadow

You can add a bit of depth to your dashboard by adding a shadow to your components with `shadow-{size}` where `size` can be left out all together, or set to:

- `none`
- `sm`
- `lg`

The last two options stand for `small` and `large`. Below we've included `shadow-lg` for the `dbc.Container` component.

### 12.4.7 Code snippet
````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 rounded-3 shadow-lg mt-1 p-3",
)
app.run_server(debug=True)
```
````

### 12.4.7 Code output

[![enter image description here][26]][26]

### 12.4.8 Gradient

Including `bg-gradient` will add additional depth to the background of your app through a smooth transition between two colors. Using the `className` approach in this case will however only let you illustrate subtle changes. The image below compares the snippet we have so far with and without `bg-gradient` in `className` for `dbc.Container` on the right and left-hand side, respectively. If you look closely, you'll notice that the top of the background in the right-hand image is slightly lighter. How this will look will also depend on which background color you're setting with `bg-{color}`.

#### 12.4.8 Code snippet 1

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 rounded-3 shadow-lg mt-1 p-3 bg-gradient",
)
app.run_server(debug=True)
```
````

#### 12.4.8 Code output 1

[![enter image description here][27]][27]

In order to add more flexibility to the gradient effect of the background color, you'll have to resort to the `style` attribute. As an example, you can set a background color that transitions from white to grey from the left to the right with:

```python
style={"background": "linear-gradient(90deg, white, grey"}
```

 `linear` in `linear-gradient` sets the gradient method. [Other alternatives][28] are `radial` and `conic`. `90` in `90deg` sets the direction through the degrees of the angle of the transition direction. Other options for `90` can be whatever you would like.

#### 12.4.8 Code snippet 2

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 rounded-3 shadow-lg mt-1 p-3",
    style={"background": "linear-gradient(90deg, white, grey"},
)
app.run_server(debug=True)
```
````

#### 12.4.8 Code Output 2

[![enter image description here][29]][29]



The color options are not limited to simple color names like `white` and `grey`. You can alose use `rgb` and even `rgba` to select any color with any grade of transparency you'd like. You can also use multiple colors at the same time to show multiple steps of the gradient. Below is an example that uses `red`, `yellow` and a transparent `blue` with `rgba(0, 0 , 255, 0.3)`. Notice also that we've included `70%` right after the `rgba` color. This sets the share of the last color compared to the rest of the colors.

#### 12.4.8 Code snippet 3

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Label 1",
                            className="bg-warning mt-2 p-2 overflow-auto",
                            style={"width": "100%", "height": "65%"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 rounded-3 shadow-lg mt-2 p-3",
    style={
        "background": "linear-gradient(125deg, red,  yellow, rgba(0, 0, 255, 0.3) 70%"
    },
)
app.run_server(debug=True)
```
````

#### 12.4.8 Code output 3

[![enter image description here][30]][30]


## 12.4.9 Overflow

So far we haven't filled any of the components with too much information. If we set the label to a fixed height of `45px` and add a text that's a bit too long, you'll see that the default behavioss of `dbc.Label` is to let the content flow over the component.

#### 12.4.9 Code output 1.1 (snippet below)

[![enter image description here][31]][31]


To change this behavior, include `overflow-{option}` in `className` where `option` can be:

- `auto`
- `hidden`
- `visible`
- `scroll`

Below is the same setup with `overflow-scroll` included. You can see that a slider with arrows has been added to the label component so that the content can be scrolled. The difference between `atuo` and `scroll` in this case is that the latter adds both vertical and horizontal sliders by default.

#### 12.4.9 Code output 1.2 (snippet below)

[![enter image description here][32]][32]

#### 12.4.9 Code snippet 1
````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Very important information that is too long for the component",
                            className="bg-warning mt-2 p-2 overflow-auto",
                            style={"width": "100%", "height": "45px"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 rounded-3 mt-1 p-3 bg-gradient",
)
app.run_server(debug=True)
```
````

## 12.5 Dashboard sizing

In our latest examples, the app fills up only a limited space of the background. You can adjust this in many ways depending on the functionalities of your app and screen size. This section will show you how to use the `fluid` attribute of `dbc.Container()` to make the app span the entire width of the screen, and how to use `style = {'height':100vh]` to fill the entire height of the screen.

### 12.5.1 `fluid` screen width

The image below shows how an app fills the avaiable screen space by default. There's no extra room on top, some extra room on both sides, and plenty of room below.

#### 12.5.1 Code output 1.1 (snippet below)

[![enter image description here][33]][33]

If you drag the screen to the any side, you'll see that the dashboard adjusts to still leave some room on either side. If you'd like to fill the entire available horizontal space, you can do so through setting `fluid = True` for the `dbc.Container` object.

#### 12.4.5 Code output 1.2 (snippet below)

[![enter image description here][34]][34]

#### 12.5.1 Code snippet 1
````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Very important information that is too long for the component",
                            className="bg-warning mt-2 p-2 overflow-auto",
                            style={"width": "100%", "height": "45px"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 p-3 bg-gradient",
    fluid=True,
)
app.run_server(debug=True)
```
````

Combining `fluid=True` with margin options in `className` can trigger some strange behavior. `me-4 ` will make the app still fill up the entire space to the right. `ms-4` will provide some space to the left of the app, but "push" the app to the right of the screen and trigger a horizontal scrollbar to appear. You can, however, safely add some space on top with `mt-2`

#### 12.5.1 Code snippet 2

````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Very important information that is too long for the component",
                            className="bg-warning mt-2 p-2 overflow-auto",
                            style={"width": "100%", "height": "45px"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 p-3 bg-gradient ms-4",
    fluid=True,
)
app.run_server(debug=True)
```
````

#### 12.5.1 Code output 2

[![enter image description here][35]][35]


### 12.5.2 Set component height

This subchapter introduces a new concept for style, the [viewport][36] height or `vh`. This is what you'll use to apply the same behaviour to the height of the app as we've seen for the *width* of the app with `fluid = True`.

#### 12.5.2 Code snippet
````{dropdown} See Code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            "#### Dashboard title",
                            className="text-info p-2",
                            style={"width": "100%"},
                        )
                    ],
                    className="mt-2",
                )
            ],
            className="text-info m-0",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            "Very important information that is too long for the component",
                            className="bg-warning mt-2 p-2 overflow-auto",
                            style={"width": "100%", "height": "45px"},
                        )
                    ],
                    width=4,
                ),
                dbc.Col(
                    dbc.Button(
                        "Click me",
                        className="m-2",
                    ),
                    width=4,
                ),
            ],
            className="border-top border-white border-3 m-0",
            justify="evenly",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    "Put your card content here",
                    className=" mt-2 rounded-0 rounded-bottom rounded-4",
                    style={"height": "200px"},
                ),
                width=12,
            )
        ),
    ],
    className="bg-secondary bg-opacity-75 p-3 bg-gradient",
    fluid=True,
    style={"height": "100vh"},
)
app.run_server(debug=True)
```
````


#### 12.5.2 Code output

[![enter image description here][37]][37]


```{warning}

You'll see the same strange behaviour with `mt-1` in `className` as you did for other margin options while using `fluid = True` for the app width. `mt-1` *will* provide space on the top, but also trigger a vertical scrollbar that has no real practical use.

```

#### 12.6 Studying layouts with your browser's development tools

By now you know how to assign different colors and formats to Dash components through `className` and `style`. You've also learnt how to study some of these settings in detail in the `CSS`. Instead of the `CSS` approach, you can also retrieve valuable information on colors and formatting by launching your browser's development tools. If you're using Edge or Chrome, you can do so with `Ctrl + Shift + I`. If you alsoe click the icon highlighted in the red rectangle below, you can hover over any element in your app and retrieve the associated information like this:

[![enter image description here][38]][38]


In the image above, we're hovering over the third `row` component. If you look at the associated `div class` information to the right you'll see:

```javascript
div class="border-top border-white border-3 m-0 justify-content-evenly row"
```
Notice how alle the `className` elements we've added can be found there. In addition, you'll see how using the `justify = 'evenly'` attribute for the `dbc.Row` compnent in effect adds `justify-content-evenly` to the very same component.

---

#### 12.7 Test your theme

The following screenshot shows a layout wiht the `bootstrap` theme with different settings for both `className` and `style` for several `dcc` and `dbc` components. The app is available on `<THIS LINK>`

# THEME TESTER APP - FINAL STAGES, SCREENSHOT

[![enter image description here][39]][39]

# THEME TESTER APP - FINALE STAGES, CODE 


```python

from jupyter_dash import JupyterDash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash import State, Input, Output, Dash, html, dcc

app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# card options
opts_className_1 = [{'label': 'text color', 'value': 'text-primary'},
                       {'label': 'background color', 'value': 'bg-primary'},
                       {'label': 'component margin', 'value': 'm-1'},
                       {'label': 'component padding', 'value': 'p-1'}]

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

opts_justify = ['start', 'center', 'end', 'around', 'between', 'evenly']

opts_justify = [{'label': k, 'value': k} for k in ['start', 'center', 'end', 'around', 'between', 'evenly']]

# card controls
ctrls_crd1 = [dbc.Row([dbc.Col([dbc.Label("Component"),
                                dcc.Markdown('Row 1',style={'marginTop' : '11px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('R1C1', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('dcc.MD', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('R2', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('R2C1', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('R2C2', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('dbc.Label 1', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('dbc.Label 2', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('Card', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                                dcc.Markdown('Container', style={'marginTop' : '12px', 'height': '30px', 'width': '200px'}),
                               ],
                              width = 1),
                       
                       dbc.Col([dbc.Label("Action"),
                                dcc.Dropdown(id='ddn_R1',
                                             options = opts_className_1,
                                             style={'marginTop' : '10px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_R1C1',
                                             options = opts_className_1,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_MD1',
                                             options = opts_ddn_scnd_title,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_R2',
                                             options = opts_className_1,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_R2C1',
                                             options = opts_className_1,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_R2C2',
                                             options = opts_className_1,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_LBL1',
                                             options = opts_className_1,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_LBL2',
                                             options = opts_className_1,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_CRD1',
                                             options = opts_className_1,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                dcc.Dropdown(id='ddn_CTR1',
                                             options = opts_className_1,
                                             style={'marginTop' : '12px', 'height': '30px'},
                                             clearable = True),
                                
                               ], #className = "bg-danger",
                              width = 2),
                       
                       dbc.Col([dbc.Label("CSS / className"),
                                dbc.Input(id = 'ipt_R1',
                                          placeholder="bg-primary border border-5 rounded-3",
                                          type="text",
                                          style={'marginTop' : '8px', 'height': '35px'}
                                         ),
                                dbc.Input(id = 'ipt_R1C1',
                                          placeholder="m-2 bg-info rounded-0 rounded-3",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'ipt_MD1',
                                          placeholder="bg-white m-4 rounded-3 p-2 opacity-75",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'ipt_R2',
                                          placeholder="bg-secondary bg-opacity-25",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'ipt_R2C1',
                                          placeholder="Ready",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'ipt_R2C2',
                                          placeholder="Ready",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'ipt_LBL1',
                                          placeholder="Ready",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'ipt_LBL2',
                                          placeholder="Ready",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'ipt_CRD1',
                                          placeholder="p-3 m-4 bg-secondary bg-opacity-50 fw-bold",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'ipt_CTR1',
                                          placeholder="rounded-3 mt-3",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                
                               ], #className = "bg-primary",
                              width =3, ),
                       
                        dbc.Col([dbc.Label("Width"),
                                dbc.Input(id = 'width_R1',
                                          placeholder="NA",
                                          disabled = True,
                                          # title = "Not an attribute. Adjust width in `Style` instead",
                                          type="text",
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'width_R1C1',
                                          placeholder="Default is 12",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'width_MD1',
                                          placeholder="NA",
                                          type="text",
                                          disabled = True,
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'width_R2',
                                          placeholder="NA",
                                          disabled = True,
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'width_R2C1',
                                          placeholder="Default is 12",
                                          type="text",
                                          # disabled = True,
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'width_R2C2',
                                          placeholder="Default is 12",
                                          type="text",
                                          # disabled = True,
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'width_LBL1',
                                          placeholder="Default is 12",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'width_LBL2',
                                          placeholder="Default is 12",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                 
                                dbc.Input(id = 'width_CRD1',
                                          placeholder="NA",
                                          disabled = True,
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'width_CTR1',
                                          placeholder="NA",
                                          type="text",
                                          disabled = True,
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                 
                               ], #className = "bg-primary",
                              width = 1, ),
                       
                        dbc.Col([dbc.Label("Justify"),
                                # dbc.Input(id = 'jfy_R1',
                                #           placeholder="None",
                                #           type="text",
                                #           style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                #          ),
                                # dcc.Dropdown(id = 'jfy_R1',
                                #           # placeholder="NA",
                                #           # type="text",
                                #           options = ['start', 'center', 'end', 'around', 'between', 'evenly'],
                                #           # className = 'text-success',
                                #           clearable = False,
                                #           style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                #          ),
                                dcc.Dropdown(id='jfy_R1',
                                             options = opts_justify,
                                             style={'marginTop' : '12px', 'height': '30px', 'width': '125px'},
                                             clearable = True),
                                 
                                 
                                dbc.Input(id = 'jfy_R1C1',
                                          disabled = True,
                                          placeholder="NA",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'jfy_MD1',
                                          placeholder="NA",
                                          type="text",
                                          disabled = True,
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                # dbc.Input(id = 'jfy_R2',
                                #           placeholder="Ready",
                                #           type="text",
                                #           # className = 'text-success',
                                #           style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                #          ),
                                dcc.Dropdown(id='jfy_R2',
                                             options = opts_justify,
                                             style={'marginTop' : '12px', 'height': '30px', 'width': '125px'},
                                             clearable = True),
                                dbc.Input(id = 'jfy_R2C1',
                                          placeholder="NA",
                                          disabled = True,
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'jfy_R2C2',
                                          placeholder="NA",
                                          disabled = True,
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'jfy_LBL1',
                                          placeholder="NA",
                                          disabled = True,
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'jfy_LBL2',
                                          placeholder="NA",
                                          disabled = True,
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                 
                                dbc.Input(id = 'jfy_CRD1',
                                          placeholder="NA",
                                          disabled = True,
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                dbc.Input(id = 'jfy_CTR1',
                                          placeholder="NA",
                                          disabled = True,
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '125px'},
                                         ),
                                 
                               ], #className = "bg-primary",
                              width = 1, ),
                       
                        dbc.Col([dbc.Label("Style"),
                                dbc.Input(id = 'style_R1',
                                          placeholder="{'width': '125px'}",
                                          # placeholder=None,
                                          type="text",
                                          style={'marginTop' : '8px', 'height': '35px'},
                                         ),
                                dbc.Input(id = 'style_R1C1',
                                          placeholder="{'width': '100%'}",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                dbc.Input(id = 'style_MD1',
                                          placeholder="{'height': '35px'}",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                dbc.Input(id = 'style_R2',
                                          placeholder="{'text-align': 'center'}",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                dbc.Input(id = 'style_R2C1',
                                          placeholder="{'marginTop' : '8px'}",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                dbc.Input(id = 'style_R2C2',
                                          placeholder="{'marginTop' : '8px'}",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                dbc.Input(id = 'style_LBL1',
                                          placeholder="Ready",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                dbc.Input(id = 'style_LBL2',
                                          placeholder="Ready",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                 
                                dbc.Input(id = 'style_CRD1',
                                          placeholder="{'width':'95%', 'background': 'linear-gradient(600deg, white 10%, rgba(75, 50, 250, 0.4)'}",
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                dbc.Input(id = 'style_CTR1',
                                          placeholder="{'width':'95%', 'height':'75vh', 'background': 'linear-gradient(45deg, white 10%, rgba(75, 50, 250, 0.4)'}",
                                          # placeholder = "{'width':'95%', 'height':'100vh', "background": "linear-gradient(25deg, white, rgba(0, 0, 250, 0.4)"}"
                                          type="text",
                                          # className = 'text-success',
                                          style={'marginTop' : '8px', 'height': '35px', 'width': '100%'},
                                         ),
                                 
                               ],
                              width = 4, )
                       
                      ],
                     # 
                     ),
             ]


app.layout = dbc.Container([dbc.Row([dbc.Col([dcc.Markdown('#### Dashboard title', id = "MD1" #className ="text-info bg-primary p-0",
                                                           #style={'height': '100%', 'width': '100%'},
                                                           
                                                           # justify = 'start'
                                                          )
                                             # COLUMN
                                             ], id = "R1C1",#className = "p-5 m-0 bg-success",  width = 12,  #style={'height': '100%', 'width': '20%'},
                                            ),
                                     
                                     
                                    # ROW 
                                    ],id = 'R1' #className = 'bg-danger m-2 p-2',
                                    #justify = 'start', #style={'height': '100%', 'width': '75%'}# m-0 g-0'
                                   ),
                            
                            dbc.Row([dbc.Col([dbc.Label("ClassName examples: {'width':'75%', 'height':'95vh', 'background':'linear-gradient(60deg, white 40%, rgba(0, 0, 200, 0.3))'}", id = 'LBL1' #className = "bg-warning m-0 p-2", style={'height': '100%', 'width': '50%'}
                                                       )
                                             # COLUMN 
                                             ], id = 'R2C1',
                                            ),
                                     dbc.Col([dbc.Label("Style examples: {'width':'75%', 'height':'95vh', 'background':'linear-gradient(60deg, white 40%, rgba(0, 0, 200, 0.3))'}", id = 'LBL2' #className = "bg-warning m-0 p-2", style={'height': '100%', 'width': '50%'}
                                                       )
                                             # COLUMN 
                                             ], id = 'R2C2',
                                            ),
                                     
                                     
                                    ], id = 'R2' #className = 'bg-secondary m-0 g-0', #style={"height": "100%"}
                                   ),
                            
                             dbc.Row([dbc.Col([dbc.Card(ctrls_crd1, id = 'CRD1'#Label 1', #className = "bg-warning m-0 p-2", style={'height': '100%', 'width': '50%'}
                                                       )
                                             ],  
                                            )
                                    ],#className = 'bg-secondary m-0 g-0', #style={"height": "100%"}
                                   ),
                            
                           ], #className = "bg-dark shadow-lg m-4 p-2", style={"height": "100vh"}, fluid = True
                            id = 'CTR1',
                            fluid = True
                          )
# CALLBAKCS
# Callbacks R1 ################################################################ 
# Set Row1 / R1 className through main_title_css chained to main_title_layout():
@app.callback(Output("ipt_R1", "value"),
              [Input("ddn_R1", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("R1", "className"),
              [Input("ipt_R1", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
# @app.callback(Output("R1", "width"),
#               [Input("width_R1", "value"),]
#              )
# def component_width(cName_element):
    return cName_element

# Set R1 Justify
@app.callback(Output("R1", "justify"),
              [Input("jfy_R1", "value"),]
             )
def component_justify(just):
    return just

# Set R2 Justify
@app.callback(Output("R2", "justify"),
              [Input("jfy_R2", "value"),]
             )
def component_justify(just):
    return just

# Set R1 style
@app.callback(Output("R1", "style"),
              [Input("style_R1", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)
    
# Callbacks R1C1 ################################################################ 
@app.callback(Output("ipt_R1C1", "value"),
              [Input("ddn_R1C1", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("R1C1", "className"),
              [Input("ipt_R1C1", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
@app.callback(Output("R1C1", "width"),
              [Input("width_R1C1", "value"),]
             )
def component_width(cName_element):
    return cName_element

# Set R1 Justify
# @app.callback(Output("R1C1", "justify"),
#               [Input("jfy_R1C1", "value"),]
#              )
# def component_justify(just):
#     return just

# Set R1 style
@app.callback(Output("R1C1", "style"),
              [Input("style_R1C1", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)    

# Callbacks MD1 ################################################################ 
@app.callback(Output("ipt_MD1", "value"),
              [Input("ddn_MD1", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("MD1", "className"),
              [Input("ipt_MD1", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
# @app.callback(Output("MD1", "width"),
#               [Input("width_MD1", "value"),]
#              )
# def component_width(cName_element):
#     return cName_element

# Set R1 Justify
# @app.callback(Output("MD1", "justify"),
#               [Input("jfy_MD1", "value"),]
#              )
# def component_justify(just):
#     return just

# Set R1 style
@app.callback(Output("MD1", "style"),
              [Input("style_MD1", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)
    
# Callbacks R2 ################################################################ 
@app.callback(Output("ipt_R2", "value"),
              [Input("ddn_R2", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("R2", "className"),
              [Input("ipt_R2", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
# @app.callback(Output("R2", "width"),
#               [Input("width_R2", "value"),]
#              )
# def component_width(cName_element):
#     return cName_element

# Set R1 Justify
# @app.callback(Output("R2", "justify"),
#               [Input("jfy_R2", "value"),]
#              )
# def component_justify(just):
#     return just

# Set R1 style
@app.callback(Output("R2", "style"),
              [Input("style_R2", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)

# Callbacks R2C1 ################################################################ 
@app.callback(Output("ipt_R2C1", "value"),
              [Input("ddn_R2C1", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("R2C1", "className"),
              [Input("ipt_R2C1", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
@app.callback(Output("R2C1", "width"),
              [Input("width_R2C1", "value"),]
             )
def component_width(cName_element):
    return cName_element

# Set R1 Justify
# @app.callback(Output("R2C1", "justify"),
#               [Input("jfy_R2C1", "value"),]
#              )
# def component_justify(just):
#     return just

# Set R1 style
@app.callback(Output("R2C1", "style"),
              [Input("style_R2C1", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)
    
# Callbacks R2C2 ################################################################ 
@app.callback(Output("ipt_R2C2", "value"),
              [Input("ddn_R2C2", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("R2C2", "className"),
              [Input("ipt_R2C2", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
@app.callback(Output("R2C2", "width"),
              [Input("width_R2C2", "value"),]
             )
def component_width(cName_element):
    return cName_element

# Set R1 Justify
# @app.callback(Output("R2C1", "justify"),
#               [Input("jfy_R2C1", "value"),]
#              )
# def component_justify(just):
#     return just

# Set R1 style
@app.callback(Output("R2C2", "style"),
              [Input("style_R2C2", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)   
    
# Callbacks LBL1 ################################################################ 
@app.callback(Output("ipt_LBL1", "value"),
              [Input("ddn_LBL1", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("LBL1", "className"),
              [Input("ipt_LBL1", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
@app.callback(Output("LBL1", "width"),
              [Input("width_LBL1", "value"),]
             )
def component_width(cName_element):
    return cName_element

# Set R1 Justify
# @app.callback(Output("LBL1", "justify"),
#               [Input("jfy_LBL1", "value"),]
#              )
# def component_justify(just):
#     return just

# Set R1 style
@app.callback(Output("LBL1", "style"),
              [Input("style_LBL1", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)

# Callbacks LBL2 ################################################################ 
@app.callback(Output("ipt_LBL2", "value"),
              [Input("ddn_LBL2", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("LBL2", "className"),
              [Input("ipt_LBL2", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
@app.callback(Output("LBL2", "width"),
              [Input("width_LBL2", "value"),]
             )
def component_width(cName_element):
    return cName_element

# Set R1 Justify
# @app.callback(Output("LBL1", "justify"),
#               [Input("jfy_LBL1", "value"),]
#              )
# def component_justify(just):
#     return just

# Set R1 style
@app.callback(Output("LBL2", "style"),
              [Input("style_LBL2", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)

# Callbacks CRD1 ################################################################ 
@app.callback(Output("ipt_CRD1", "value"),
              [Input("ddn_CRD1", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("CRD1", "className"),
              [Input("ipt_CRD1", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
# @app.callback(Output("CRD1", "width"),
#               [Input("width_CRD1", "value"),]
#              )
# def component_width(cName_element):
#     return cName_element

# Set R1 Justify
# @app.callback(Output("CRD1", "justify"),
#               [Input("jfy_CRD1", "value"),]
#              )
# def component_justify(just):
#     return just

# Set R1 style
@app.callback(Output("CRD1", "style"),
              [Input("style_CRD1", "value"),]
             )
def component_style(style):
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None)

# Callbacks CTR1 ################################################################ 
@app.callback(Output("ipt_CTR1", "value"),
              [Input("ddn_CTR1", "value"),]
             )
def component_layout(cName_element):
    return cName_element

@app.callback(Output("CTR1", "className"),
              [Input("ipt_CTR1", "value"),]
             )
def component_css(cName_element):
    return cName_element

# Set Row1 / R1 width
# @app.callback(Output("CTR1", "width"),
#               [Input("width_CTR1", "value"),]
#              )
# def component_width(cName_element):
#     return cName_element

# @app.callback(Output("CTR1", "justify"),
#               [Input("jfy_CTR1", "value"),]
#              )
# def component_justify(just):
#     return just

@app.callback(Output("CTR1", "style"),
              [Input("style_CTR1", "value"),]
             )
def component_style(style):
    # print(type(st))
    try:
        eval(style)
        return(eval(style))
    
    except:
        return(None) 
    


app.run_server(mode='external', port = 8009, debug = True)

```




#----------------------------------------------

---

# Everything beoynd this point is redundant and can safely be removed

## Unclear:


### className combinations:

- `" opacity-25 p-2 m-1 bg-primary bg-gradient text-light fw-bold rounded "`

- `" opacity-75 p-2 m-1 bg-success bg-opacity-25 text-light rounded-bottom "`


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

[![enter image description here][40]][40]

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
def crd2_layout(cName_element)
    return cName_element
@app.callback(Output("crd_2", "className"),
              [Input("ipt_crd_2", "value"),]
             )
def crd2_css(cName_element):
    return cName_element
                         
app.run_server(mode='external', port = 8032)                                              
```
[![enter image description here][41]][41]


 


  [1]: https://i.stack.imgur.com/Vunbd.png
  [2]: https://i.stack.imgur.com/EvbEU.png
  [3]: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
  [4]: https://i.stack.imgur.com/pHvGO.png
  [5]: https://www.rapidtables.com/web/color/RGB_Color.html
  [6]: https://i.stack.imgur.com/BFgvm.png
  [7]: https://dashcheatsheet.pythonanywhere.com/
  [8]: https://i.stack.imgur.com/iCkRA.png
  [9]: https://i.stack.imgur.com/d9pqj.png
  [10]: https://i.stack.imgur.com/vLWvz.png
  [11]: https://i.stack.imgur.com/dfjKw.png
  [12]: https://i.stack.imgur.com/muWaZ.png
  [13]: https://mdbootstrap.com/docs/standard/utilities/spacing/
  [14]: https://i.stack.imgur.com/PkwOL.png
  [15]: https://i.stack.imgur.com/Uu0Ee.png
  [16]: https://i.stack.imgur.com/UWulS.png
  [17]: https://i.stack.imgur.com/RylgH.png
  [18]: https://i.stack.imgur.com/jRrsW.png
  [19]: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
  [20]: https://i.stack.imgur.com/kTRZ4.png
  [21]: https://i.stack.imgur.com/UrTWh.png
  [22]: https://i.stack.imgur.com/B77Zv.png
  [23]: https://i.stack.imgur.com/xFYRI.png
  [24]: https://i.stack.imgur.com/PM6BH.png
  [25]: https://i.stack.imgur.com/UpEZe.png
  [26]: https://i.stack.imgur.com/4H9h8.png
  [27]: https://i.stack.imgur.com/VVPGV.png
  [28]: https://www.w3schools.com/css/css3_gradients.asp
  [29]: https://i.stack.imgur.com/tcSwu.png
  [30]: https://i.stack.imgur.com/J87m0.png
  [31]: https://i.stack.imgur.com/fkHbn.png
  [32]: https://i.stack.imgur.com/BdGEE.png
  [33]: https://i.stack.imgur.com/pay0z.png
  [34]: https://i.stack.imgur.com/OnxeJ.png
  [35]: https://i.stack.imgur.com/erqRS.png
  [36]: https://developer.mozilla.org/en-US/docs/Web/CSS/Viewport_concepts
  [37]: https://i.stack.imgur.com/IBPlh.png
  [38]: https://i.stack.imgur.com/1YYrX.png
  [39]: https://i.stack.imgur.com/dxVBF.png
  [40]: https://i.stack.imgur.com/NGfOi.png
  [41]: https://i.stack.imgur.com/EJw6S.png
