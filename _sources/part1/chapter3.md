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

So far, we've only organized our app **layout** in a `dbc.Container()` component without any further specifications.  We've seen that this will place our app components sequentually in one single column.  To change the layout of components we'll use the [dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout) library layout components `dbc.Row()` and `dbc.Column()`.

Best practices when constructing your layout using **Dash Bootstrap Components**:

1. The entire app layout goes inside a `Containter`
2. 'Rows' go inside the `Container`
3. 'Cols' go inside 'Rows'
4. Components go inside `Cols`

![app image](https://i.stack.imgur.com/M8j6q.png)


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
        dbc.Row([dbc.Col(markdown)]),
        dbc.Row(
            [
                dbc.Col(dropdown), 
                dbc.Col(slider),
            ]
        ),
        dbc.Row([dbc.Col(slider)]),
        dbc.Row([dbc.Col(button)]),
    ]
)

# Run the App 
if __name__ == '__main__':
    app.run_server()
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
