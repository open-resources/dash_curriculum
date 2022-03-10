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
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
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
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 20)

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
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
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 20)
input_ = dcc.Input("Enter a value")

# Add components to app layout
app.layout = dbc.Container([
                button,
                checklist,
                dropdown,
                slider,
                input_
])

# Launch app
if __name__ == '__main__':
    app.run_server()
```
  
</details>



## Dash Layout
Dash applications are comprised of 2 parts:
- Layout: What the application looks like
- Callabacks: Interactivity of the application

***
The **layout** is made up of **components**.  Let's make a minimal Dash application to demonstrate this concept:
<details>
  <summary>Minimal Dash App</summary>
  
Create **app_3_1.py** in the `tutorial/part1` directory:

![Make app_3_1.py](../assets/p1_c3/make_app_3_1.png)

Copy/paste the minimal Dash app code:  
```python
# Import Python libraries
from dash import Dash, html 

# Create a Dash application
app = Dash()
# Create the layout of the app
app.layout = html.Div("This is a HTML Div component")
# Run the app
app.run_server()
```

Now **Run/Debug** the code:
![Running minimal Dash app](../assets/p1_c3/run_minimal.png)


Open a web browser, enter http://127.0.0.1:8050/ in the address bar, and you should see our minimal application:
![Display minimal Dash app](../assets/p1_c3/display_minimal.png)
</details>

***

Next, we'll add some styling with **CSS**.   We'll use a [stylesheet](https://www.w3schools.com/css/css_intro.asp) from the **Bootstrap** library.  
<details>
  <summary>CSS</summary>

Create **app_3_2.py** in the `tutorial/part1` directory:

![Make app_3_2.py](../assets/p1_c3/make_app_3_2.png)

Copy/paste the minimal Dash + CSS app code:  
```python
# Import Python libraries
from dash import Dash, html 
import dash_bootstrap_components as dbc

# Create a Dash application, pass in a stylesheet from Bootstrap
app = Dash( external_stylesheets=[dbc.themes.BOOTSTRAP] )
# Create the layout of the app
app.layout = html.Div("This is a HTML Div component with Bootstrap CSS theme", className="m-5")
# Run the app
app.run_server()
```

Run the code, open a web browser, enter http://127.0.0.1:8050/ in the address bar, and you should see our minimal application with a slightly different style this time:

![Display minimal Dash app](../assets/p1_c3/display_3_2.png)
vs
![no CSS comparison](../assets/p1_c3/display_minimal.png)

</details>

***

Let's continue to learn about **Bootstrap**, [the most popular CSS Framework for developing responsive and mobile-first websites](https://www.w3schools.com/whatis/whatis_bootstrap.asp).  We will be using the Dash Bootstrap Components library that makes it [easier to build consistently styled apps with complex, responsive layouts](https://dash-bootstrap-components.opensource.faculty.ai/)

<details>
  
  <summary>Dash Bootstrap Components</summary>
  
***
  
<details>

  <summary>Layout in Bootstrap</summary>
  
* [Layout in Bootstrap](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/) is controlled using the grid system. The Bootstrap grid has twelve columns
![Bootstrap layout](../assets/p1_c3/bootstrap_grid.png)
* 3 main layout components: Container, Row, and Column.
  * Container wraps the entire app
  * Rows only contain columns
  * Columns holds your components

Now let's add to our minimal, CSS styled app by using a Container, Rows, and Columns.  Create a new file called **app_3_3.py** and copy/paste the following code:
```python
# Import Python libraries
from dash import Dash, html 
import dash_bootstrap_components as dbc

# Create a Dash application, pass in a stylesheet from Bootstrap
app = Dash( external_stylesheets=[dbc.themes.BOOTSTRAP] )

# Create the layout of the app
app.layout = dbc.Container([
                # Row 1
                dbc.Row([
                    dbc.Col([
                        html.Div("Div 1")
                    ],
                    style={"background-color": "blue"},
                    ),
                    dbc.Col([
                        html.Div("Div 2")
                        ]),
                    ],
                    style={"background-color": "green"},
                    className="h-75",
                    ),
                # Row 2
                dbc.Row([
                    dbc.Col([
                        html.Div("Div 3")
                    ],
                    style={"background-color": "pink"},
                    ),
                    dbc.Col([
                        html.Div("Div 4")
                        ]),
                    ],
                    style={"background-color": "yellow"},
                    className="h-25",
                    ),
            ],
            style={"height": "100vh"},
            )

# Run the app
app.run_server()
```
Notice that a ```container``` which holds our app then we have 2 ```rows``` which hold 2 ```columns``` each, and each ```column``` containers a ```Div```. We added some CSS styling to change each column's ```background-color```.  The Rows also include some CSS styling to show how we can change the height of the Row.  Finally, we added CSS styling to make sure the Container expands to 100% of the height of the browser.

![Bootstrap layout](../assets/p1_c3/bootstrap_layout.png)
  
  </details>
  
***

