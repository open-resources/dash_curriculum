# Chapter 3 - Dash Components and Layouts
## What you will learn

In this chapter we will explore Dash various **components** and how to position them with **layout** as well as add styling with **CSS**\
[p1c3_start.py](../assets/p1c2/p1c2_end.py)\
[p1c3_end.py](../assets/p1c3/p1c3_end.py)


## Dash Components

:::{dropdown} Buttons
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
:::

```{dropdown} Checklist
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
  
```

```{dropdown} Radio items
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

```

```{dropdown} Dropdown
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
  
```
