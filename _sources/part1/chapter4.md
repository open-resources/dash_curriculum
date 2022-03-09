# Chapter 4: Linking Dash components

## What you will learn

After initializing a first simple app, learning about Dash components and setting a layout this chapter covers so called app callbacks, that will allow you to link various components in your Dash app. In other words, app callbacks are necessary to build truly interactive apps. This chapter aims at preparing you with the basics of callbacks. In order to not let you get confused by the look of a callback there will be a short introduction to decorators in Python. We will then dive into the general structure of callbacks and finally see some examples in action.

```{admonition} Learning Intentions
- Decorators in Python
- Structure of callbacks
- Simple examples for callbacks
```

## Introduction to decorators in Python
 
 1. what are the advantages of decorators and basic structure  

## Structure of app callbacks

Despite the variety of usage of callbacks they all share the same basic structure. A generic callback will have the following structure and is composed of two main components, the callback decorator and the callback function:

```
# (1) Callback decorator
@app.callback(
    Output(component_id='my-comp-out', component_property='prop-out'),
    Input(component_id='my-comp-in', component_property='prop-in')
)

# (2) Callback function
def function_output(arg):
    return output
```

### Structure of Dash callback decorator

 1. Structure of a Dash callback decorator (*copy simple app from chapter 2 to refer to its callback here)
     1. Decorator arguments: Output, Input, component_id, component_property 

The callback decorator makes up the first part of the callback. The decorator itself takes up two different arguments: Output and Input. Both of them again will take two arguments, the component_id and the component_property. The meaning of the different arguments is straight forward. The Output specifies what kind of property of which component of your app should be affected. Accordingly, the Input specifies what property of which other component of your app should trigger the Output.

> In order to build more complex applications with Dash later we will introduce a third argument called State. Also the argument Input can take on different components.

```{attention}
The arguments of a callback decorator Output and Input need to be imported from the dash library on top of your app.
```

### Structure of Dash callback function

 1. Structure of Dash callback function
     1. function argument (*also mention multiple inputs require multiple arguments)
     2. function body (*a place where you can work with the input data to build graphs and manipulate app data)
     3. Return output of function (*also mention multiple outputs require multiple objects)

The callback function makes up the second part of the callback and is itself composed into three different parts:
- The function argument
The callback function takes as many arguments as there are input components. The order remains stable i.e., the component you enter first in the input argument of the callback decorator will be represented by the argument you enter first into the callback function.
- The function body
- The return or output of the function

## Callbacks in action

Now it's time to see some callbacks in action. For this chapter two examples should be discussed in detail.

### Change a graph by dropdown

  1. Seeing Graph and Dropdown in action (*copy simple app from chapter 3 to refer to its graph and dropdown components)
     1. Create a callback with the Dropdown and Graph from chapter 3
        1. add the graph figure and dropdown value in decorator as the component_property
        2. In callback function body: taking dropdown value to change bar graph 

Example code for section 4
```
from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout =html.Div([
    dcc.Dropdown(options=[1,2,3], value=3, id='my-dropdown', clearable=False),
    dcc.Graph(id='my-graph')
])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='my-dropdown', component_property='value')
)
def update_output_div(dropdown_value):
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2],
        # "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })
    dff = df.copy()
    dff['Amount'][1] = dff['Amount'][1]*dropdown_value

    fig = px.bar(dff, x="Fruit", y="Amount")

    return fig


if __name__ == '__main__':
    app.run_server(debug=False)
```

### Change a markdown by dropdown

  1. Seeing Dropdown and Div children in action: (* div would represent title of webpage)
     1. show reader how to control title of page: Dropdown with different text that will change the children of div
  2. Seeing Slider and Div style in action 
     1. slider value would change font size 
    
Example for section 5
```
from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout =html.Div([
    dbc.Row()
    html.Div(children="Our App Title", id='my-title'),
    dcc.Slider(min=10, max=100, step=5, value=10, id='my-slider'),
])

@app.callback(
    Output(component_id='my-title', component_property='style'),
    Input(component_id='my-slider', component_property='value')
)
def update_output_div(slider_v):
    title_size={'fontSize':slider_v}
    return title_size


if __name__ == '__main__':
    app.run_server(debug=False, port=8001)
```
