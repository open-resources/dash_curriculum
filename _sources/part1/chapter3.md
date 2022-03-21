# Chapter 3 - Dash Components and Layouts

## What you will learn

In this chapter we will explore Dash various **components**, how to add styling to them with **CSS**, and how to position them with **layout**
[starting_file.py](ch3_files/start.py)
[ending_file.py](ch3_files/app.py)

## Dash Components

**Components** are the building blocks of the app such as dropdown menus, buttons (radio, checkbox, etc...), slider bars, graphs, and many others.
We will learn a few common components in this chapter.

**Properties** are attributes of components (TODO: add more here)\

````{dropdown} Buttons
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
Buttons are clickable components that will be used to trigger other actions such as submitting a form or plotting data.  We will pass in a **child** property to give the button a name in the dashboard.


```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()
```

![button](../assets/p1_c3/button.gif)

````

````{dropdown} Checklist
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

Checklists display a set of options for the user to choose.
We will pass in a list of **options** when we create the checklist component below:


```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()

```

![checklist](../assets/p1_c3/checklist.gif)
  
````

````{dropdown} Radio items
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

  

Radio items are lists of options that a user can only select one option.
Similar to the checklst we will pass in a list of **options** when we create the component.

```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()

```

![radio_item](../assets/p1_c3/radio.gif)

````

````{dropdown} Dropdown
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

    
```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
                dropdown,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()

```

![drop_down](../assets/p1_c3/dropdown.gif)
  
````

````{dropdown} Slider
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    
```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 10, 1)

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
                dropdown,
                slider,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()

```

![slider](../assets/p1_c3/slider.gif)
````

## CSS

Next, we'll add styling to our application with a Cascading Style Sheets or **CSS**.
We will use the Bootstrap [stylesheet](https://www.w3schools.com/css/css_intro.asp) for this application.  

    
```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 10, 1)

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
                dropdown,
                slider,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()
```
 
![css_diff](../assets/p1_c3/style_comparison.png)


## Layout

So far, we've only organized our app **layout** in a `dbc.Container()` component without any further specifications:

```python
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
                dropdown,
                slider,
])
```

And we've seen that this will place our app components sequentually in one single column.  In order to neatly place the different components in a more functional and visually pleasing way, we'll have to introduce `dbc.Row()` and `dbc.Column()`. Together with `dbc.Container()` these are the main [Layout][components in dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout)

A `container` wraps the entire app, and a  `row` is a wrapper for `columns` than in turn contains elements such as controls, figures, tables, text and so on.  The layout of your app should thereofre be built as a series of rows of columns.

```{margin}
I'd like to take out this bold section and give the students a demonstration of the Rows/Columns immediately as I think the concept of **wrapper** or **wrapping** might confuse them

- SM
```
**The `col` component should always be used as an immediate child of Row and is a wrapper for your content that ensures it takes up the correct amount of horizontal space.
But let's get back to spacing and adjustments after we've seen how the already defined components `markdown`, `checklist`, `radio`, `slider` and `button` can all fit together with `rows` and `columns`.**

The following snippet will produce the app shown in the image below:

```python
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown)),
        dbc.Row([dbc.Col(dropdown), dbc.Col(slider)]),
        dbc.Row(dbc.Col(slider)),
        dbc.Row(dbc.Col(button)),
    ]
)
```

[app image](https://i.stack.imgur.com/M8j6q.png)

***missing: details about default width: 12***

```{margin}
Editor's Note: Discuss setting width to variable 3, 6, 8, 12 etc...

- FM
```

There are two main learning points here.
First, notice how you can freely put `dbc.Col(markdown)` as the only argument in the first `dbc.Row()` component.
If you have more than one element, like in the second `Row`, you'll have to encapsulate them in a list like this: `dbc.Row([dbc.Col(dropdown), dbc.Col(slider)])`.
Second, notice how the rows still appear sequentually in a vertical fashion, and that our two `Col` components withnin a `Row`  appear horizontally within the common `Row`:

[row_col](https://i.stack.imgur.com/3Yk7o.png)

***this paragraph possibly redundant by now???***

```{margin}
Editor's Note: I think it's fine to have a "Summary" section to review/recap

- FM
```

Best practices when constructing your layouts:

1. Wrap the entire app layout in a `Containter`
2. Only use `Row` and `Col` inside a Container 
3. `Rows` only contain `Col`
4. Components go inside `Col`

```{margin}
Editor's Note: Is a "Row component" and a "Col component" the right terminology? Should we use a different word to disambiguate Dash components?

- FM
```

![colored_app](../assets/p1_c3/app_colored.png)


```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 10, 1)

# App Layout 
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown, width=8)),
        dbc.Row(
            [
                dbc.Col(dropdown, width = 3), 
                dbc.Col(slider, width = 9),
            ]
        ),
        dbc.Row(dbc.Col(slider, width = 6)),
        dbc.Row(dbc.Col(button, width = 11)),
    ]
)

# Run the App 
if __name__ == '__main__':
    app.run_server()
```

## Summary
In this chapter we learned about Dash components, styling, and layout. **TODO: add more here**
