# Chapter 3 - Dash Components and Layouts

## What you will learn

In this chapter we will explore Dash various **components** and how to position them within the app **layout**

[starting_file.py](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part1/ch2_files/chapter2_app.py)

[ending_file.py](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part1/ch3_files/app.py)

## 3.1 Dash Components

**Components** are the building blocks of the app such as dropdown menus, buttons (radio, checkbox, etc...), slider bars, graphs, and many others.
We will learn a few common components in this chapter.

**Properties** are attributes of components such as their `id` or `children`.  We will learn more about properties in [chapter 4](./chapter4.md)

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
markdown = dcc.Markdown(children='My First app')
button = html.Button(children="Button")

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
markdown = dcc.Markdown(children='My First app')
button = html.Button(children="Button")
checklist = dcc.Checklist(options=['New York City', 'Montréal', 'San Francisco'])

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
markdown = dcc.Markdown(children='My First app')
button = html.Button(children="Button")
checklist = dcc.Checklist(options=['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(options=['New York City', 'Montréal', 'San Francisco'])

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
    
Dropdowns allow the user to select from a list of option. Similar to the checklst we will pass in a list of **options** when we create the component.
    
```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown(children='My First app')
button = html.Button(children="Button")
checklist = dcc.Checklist(options=['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(options=['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(options=['NYC', 'MTL', 'SF'])

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
    
Sliders allow the user to select a value by moving an indicator.  We pass in the (**start**, **end**, **increment**) `properties` to this component.

```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown(children='My First app')
button = html.Button(children="Button")
checklist = dcc.Checklist(options=['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(options=['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(options=['NYC', 'MTL', 'SF'])
slider = dcc.Slider(min=0, max=10, step=1)

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

## 3.2 Layout

So far, we've only organized our app **layout** in a `dbc.Container()` component without any further specifications.  We've seen that this will place our app components sequentually in one single column.  To change the layout of components we will use the [dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout) library components `dbc.Row()` and `dbc.Column()`.

Best practices when constructing your layout using **Dash Bootstrap Components**:

1. The entire app layout goes inside a `Containter`
2. `Rows` go inside the `Container`
3. `Cols` go inside `Rows`
4. Components go inside `Cols`

```{admonition} Note
- There are **12 Columns** in each Row
- In the code below we define the `width` property of the `Column`
```

```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(children='My First app')
button = html.Button(children="Button")
checklist = dcc.Checklist(options=['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(options=['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(options=['NYC', 'MTL', 'SF'])
slider = dcc.Slider(min=0, max=10, step=1)

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
        dbc.Row(
            [
                dbc.Col(checklist, width = 6),
                dbc.Col(radio, width = 6),
            ]
        ),
        dbc.Row(dbc.Col(button, width = 11)),
    ]
)

# Run the App 
if __name__ == '__main__':
    app.run_server()
```

![colored_app](../assets/p1_c3/app_colored.png)

We see there are 4 rows with columns of various `widths` which contain components.  You can play around with the `width` value of the column to see how it changes the app layout.

```{admonition} Note
- We will learn about `external_stylesheets` in later chapters
- The colors above are for demonstration purposes, you will not see them in your local dashboard
```

## Summary
In this chapter we learned about Dash **components** and **layout**. In the next chapter we will learn how to create an interactive app by linking the components together.
