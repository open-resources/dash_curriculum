# Chapter 3 - Dash Components and Layouts
## What you will learn

In this chapter we will explore Dash various **components** and how to position them with **layout** as well as add styling with **CSS**\
[p1c3_start.py](../assets/p1c2/p1c2_end.py)\
[p1c3_end.py](../assets/p1c3/p1c3_end.py)


## Dash Components

````{dropdown} Buttons
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

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()
```
````

````{dropdown} Checklist
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

**Add gif of checklist function**

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

**Insert picture of checklist and button together**
  
````

````{dropdown} Radio items
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

  

**Add gif of radio item function**

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

````

````{dropdown} Dropdown
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

  
**Add gif of dropdown function**
  
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
  
````

````{dropdown} Slider
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    
**Add gif of slider function**

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
````

## CSS

Next, we'll add styling to our application with a Cascading Style Sheets or **CSS**.   We will use the Bootstrap [stylesheet](https://www.w3schools.com/css/css_intro.asp) for this application.  

````{dropdown} CSS
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    
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
 
**pictures/gif showing the difference CSS stylesheet makes**

````

## Layout

Now let's learn about layout and how to place the components at specific locations on the page instead.  We will use **Dash Bootstrap Components** to do this.  **Bootstrap** is [the most popular CSS Framework for developing responsive and mobile-first websites](https://www.w3schools.com/whatis/whatis_bootstrap.asp).

````{dropdown} Dash Bootstrap Components
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
* [Layout in Bootstrap](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/) is controlled using the grid system. The Bootstrap grid has twelve columns
![Bootstrap layout](../assets/p1_c3/bootstrap_grid.png)
* 3 main layout components: Container, Row, and Column.
  * Container wraps the entire app
  * Rows only contain columns
  * Columns holds your components

````
Running the code we have so far would produce an app with the following layout:

[![enter image description here][1]][1]

Here, the elements are organized in a `dbc.Component()` component (?) without any further specifications. This means that they will appear sequentually in one single column. In order to neatly place the different components in a more functional and visually pleasing way, we'll have to introduce `dbc.Row()` and dbc.Column(). The three componenst mentioned so far are the three main [Layout][2] components in dash-bootstrap-components.

The Row component is a wrapper for columns. The layout of your app should be built as a series of rows of columns. The Col component should always be used as an immediate child of Row and is a wrapper for your content that ensures it takes up the correct amount of horizontal space.

Now, lets set up the existing app with the markdown element on top, followed by a row with the button and checklist in two different columns. Then we'll follow up with a row with the radio, and dropdown components in two different columns. At the very bottow, we'll place the slider in a row that fills up the space of one single column. Here's the same app with a new layout:

[![enter image description here][3]][3]

And here's the corresponding snippet:

    app.layout = dbc.Container(
        [
            dbc.Row(dbc.Col(markdown)),
            dbc.Row([dbc.Col(button), dbc.Col(checklist)]),
            dbc.Row([dbc.Col(radio), dbc.Col(dropdown)]),
            dbc.Row(dbc.Col(slider)),
        ]
    )

Be aware that `dbc.Row()` requires the affiliated components like `dbc.Col(button)` to be organized in a list ***if*** there are more than one element. So `dbc.Row(dbc.Col(markdown))` will not raise an error, but `dbc.Row([dbc.Col(button), dbc.Col(checklist)])` will. 

For best results, also make sure you adhere to the following two rules when constructing your layouts:

1. Only use Row and Col inside a Container. A single Container wrapping your entire app's content is fine.

2. The immediate children of any Row component should always be Col components. Your further content should go inside the Col components.


  [1]: https://i.stack.imgur.com/8wTPR.png
  [2]: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout
  [3]: https://i.stack.imgur.com/VpcDJ.png
