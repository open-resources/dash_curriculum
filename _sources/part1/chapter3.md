# Chapter 3 - Dash Components and Layouts
## What you will learn

In this chapter we will explore Dash various **components** and how to position them with **layout** as well as add styling with **CSS**\
[p1c3_start.py](../assets/p1c2/p1c2_end.py)\
[p1c3_end.py](../assets/p1c3/p1c3_end.py)


## Dash Components
<details>
  <summary>Checklist</summary>
  
**Add gif of checklist function**
  
```python
# Import required Python libraries
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Create the Dash app object
app = Dash(__name__)

# Create app components
button = html.Button("Button 1", id="button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
])

# Launch app
if __name__ == '__main__':
    app.run_server()
```
**Insert picture of checklist and button together**
  
</details>


<details>
  <summary>Radio Item</summary>
  
**Add gif of radio item function**

```python
# Import required Python libraries
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Create the Dash app object
app = Dash(__name__)

# Create app components
button = html.Button("Button 1", id="button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
                radio
])

# Launch app
if __name__ == '__main__':
    app.run_server()
```
  
  
</details>

<details>
  <summary>Dropdown</summary>
  
**Add gif of dropdown function**
  
```python
# Import required Python libraries
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Create the Dash app object
app = Dash(__name__)

# Create app components
button = html.Button("Button 1", id="button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
                radio,
                dropdown,
])

# Launch app
if __name__ == '__main__':
    app.run_server()
```
  
</details>

<details>
  <summary>Slider</summary>
  
**Add gif of slider function**

```python
# Import required Python libraries
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Create the Dash app object
app = Dash(__name__)

# Create app components
button = html.Button("Button 1", id="button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 20)

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
                radio,
                dropdown,
                slider
])

# Launch app
if __name__ == '__main__':
    app.run_server()
```

</details>

<details>
  <summary>Input</summary>
  
**Add gif of input function**

```python
# Import required Python libraries
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Create the Dash app object
app = Dash(__name__)

# Create app components
button = html.Button("Button 1", id="button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 20)
input_ = dcc.Input("Enter a value")

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
                radio
                dropdown,
                slider,
                input_
])

# Launch app
if __name__ == '__main__':
    app.run_server()
```
  
</details>



## CSS

Next, we'll add styling to our application with a Cascading Style Sheets or **CSS**.   We will use the Bootstrap [stylesheet](https://www.w3schools.com/css/css_intro.asp) for this application.  
<details>
  <summary>CSS</summary>
 
```python
# Import required Python libraries
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Create the Dash app object
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
button = html.Button("Button 1", id="button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 20)
input_ = dcc.Input("Enter a value")

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
                radio,
                dropdown,
                slider,
                input_
])

# Launch app
if __name__ == '__main__':
    app.run_server()
```
 
**pictures/gif showing the difference CSS stylesheet makes**

</details>

***

## Layout

Now let's learn about layout and how to place the components at specific locations on the page instead.  We will use **Dash Bootstrap Components** to do this.  **Bootstrap** is [the most popular CSS Framework for developing responsive and mobile-first websites](https://www.w3schools.com/whatis/whatis_bootstrap.asp).

<details>
  
  <summary>Dash Bootstrap Components</summary>
  
* [Layout in Bootstrap](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/) is controlled using the grid system. The Bootstrap grid has twelve columns
![Bootstrap layout](../assets/p1_c3/bootstrap_grid.png)
* 3 main layout components: Container, Row, and Column.
  * Container wraps the entire app
  * Rows only contain columns
  * Columns holds your components

</details>
  
