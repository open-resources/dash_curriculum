# Chapter 4: Linking Dash components

## What you will learn

After initializing a first simple app, learning about Dash components and setting a layout this chapter covers so called app callbacks, that will allow you to link various components in your Dash app. In other words, app callbacks are necessary to build truly interactive apps. This chapter aims at preparing you with the basics of callbacks. In order to not let you get confused by the notation of a callback there will be a short introduction to decorators in Python. We will then dive into the general structure of callbacks and finally see some examples in action.

```{admonition} Learning Intentions
- Decorators in Python
- Structure of callbacks
- Component ids & properties
- Simple examples for callbacks
```

When we finish this chapter you'll have a fully working app linking together two components. You can find the code already in the dropdown box below.

```{admonition} Click the button to reveal the end result of this chapter!
:class: dropdown



```

## 4.1 Introduction to decorators in Python



## 4.2 Structure of app callbacks

Before we talk about the structure of a callback, let's briefly discuss how callbacks in general will fit into your app. Referring to the structure of an app that we have discussed so far your callbacks will always fit after your app layout and before you actually run the app. Your app gets the following structure:

- Import packages
- Initialise the app
- Create app components
- App layout
- **Configure callback(s)**
- Run the app

Now, let's have a closer look at what a callback looks like. Despite the variety of usage of callbacks they all share the same basic structure. A generic callback will have the following structure and is composed of two main components, the callback decorator and the callback function:

```
# Callback decorator
@app.callback(
    Output(component_id='my-component-1', component_property='property-1'),
    Input(component_id='my-component-2', component_property='property-2')
)

# Callback function
def function_output(arg):
    output = arg
    return output
```

As there might be still some arguments you are not familiar with, we will go through the upper lines step by step.

### 4.2.1 Structure of Dash callback decorator

> The callback decorator makes up the first part of the callback. Here you specify the components and their corresponding properties that you want to link together.

The decorator itself takes up two different arguments: Output and Input. Both of them again will take two arguments, the component id and the component property.

```{admonition} Component id and property
We have already introduced different components of an app like a markdown or a dropdown. To work properly all of these components need at least one input argument like a children, a value or a list declaring several options. These arguments are also called properties. Furthermore, when you are building advanced dashboards you are probably using many of the same components. In order to identify them uniquely one optional argument every component takes is the id. Also when you are working with callbacks the id is necessary as you use it to refer which components you are linking.
```

The meaning of the different arguments is straight forward. The Output specifies what kind of property of which component of your app should be affected. Accordingly, the Input specifies what property of which other component of your app should trigger the Output. Note, that linking two different components establishes a direct relationship between them i.e., whenever the property of the input component is changed it will immediately trigger the selected property of the output component to change accordingly. You might compare this behavior with two cells in excel which are linked together.

In order to build more complex applications with Dash later we will introduce a third argument called State, which in some sense will allow to circumvent this direct relationship. Also the arguments Output and Input can take on different components to allow for advanced functionality. However, we'll come back to this in chapter 10.

### 4.2.2 Structure of Dash callback function

> The callback function makes up the second part of the callback. Here you process the input the way you want the otuput to be affected by.

The function itself - like any arbitrary function in python - is composed into three different parts, namely

- The function argument(s)
- The function body
- The return or output of the function

Let's have a look at those in more detail.

```{admonition} The function argument
The callback function takes as many arguments as there are input components. The order remains stable i.e., the component you enter first in the input argument of the callback decorator will be represented by the argument you enter first into the callback function.
```

```{admonition} The function body
The function body is the place where you can work with the input data to build graphs and manipulate app data.
```

```{admonition} The return or output of the function
At the end of the callback function the output that has been prepared in the function body gets returned i.e., that's the output of your function and therefore will be the output of your callback. Note, that later on when might working with multiple outputs in the callback decorator also the callback function needs to return the same amount of objects.
```

## 4.3 Callbacks in action

Now it's time to see some callbacks in action. For this chapter two examples should be discussed in detail.

### 4.3.1 Change a markdown by dropdown

Let's start of with linking a dropdown to a markdown. The markdown in this case could represent the title of the app.

```{attention}
Using callbacks always make sure to import the libraries 'Output' and 'Input' for the callback decorator.
```

Creating the app components we are using the markdown and the dropdown from the dash core components (dcc) library. The markdown gets assigned an id, a children and a style, whereas the dropdown gets assigned an id, some options and an initial value. The unique ids are necessary for implementing a working callback.

```
# Create app components
markdown = dcc.Markdown(id='our-title', children='My First App', style={'textAlign': 'center'})
dropdown = dcc.Dropdown(id='our-drop', options=['My First App', 'Another Title', 'Welcome to this App'], value='My First App')
```

The callback itself takes on the id as well as the children property of the markdown as output arguments in the decorator. As input arguments the id and the value of the dropdown. The value of the dropdown gets put into the callback function, saved into a basic variable and then gets returned.

```
# Configure callback
@app.callback(
    Output(component_id='our-title', component_property='children'),
    Input(component_id='our-drop', component_property='value')
)
def update_markdown(value_drop):
    title = value_drop
    return title
```

The complete code is shown below.

```
# Import packages
from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc

# Initialise the app
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown(id='our-title', children='My First App', style={'textAlign': 'center'})
dropdown = dcc.Dropdown(id='our-drop', options=['My First App', 'Another Title', 'Welcome to this App'], value='My First App')

# App layout
app.layout = dbc.Container([
    markdown,
    dropdown
])

# Configure callback
@app.callback(
    Output(component_id='our-title', component_property='children'),
    Input(component_id='our-drop', component_property='value')
)
def update_markdown(value_drop):
    title = value_drop
    return title


# Run the app
if __name__ == '__main__':
    app.run_server()
```

**[GIF, THAT SHOWS THE APP IN THE BROWSER IN ACTION I.E., SELECT A VALUE IN THE DROPDOWN TO CHANGE THE TITLE OF THE PAGE]**

### 4.3.2 Change a graph by dropdown

Now, that we have already changed the title of our app, let's get a little more sophisticated. We're keeping the dropdown but now want to link it to a simple graph. Linking dash core components like buttons, checkboxes, dropdowns or sliders to graphs is probably the most common usecase when working with dash. 

For this purpose we are extending our simple app by two more common libraries: plotly.express which we shorten by px and the pandas library which we shorten by pd. plotly.express is an easy to use library when plotting data, pandas is a very functional library when wrangling and analysing data, so both of these will probably accompany you from now on.

One of the best known functions from pandas is the so called DataFrame, which allows to structure a set of data. As an argument it'll take on a dictionary and give it a tabular structure. Now, you are set for performant data analysis which will be further discussed in the second part of this curriculum. In this example we give in a list of fruits, each of them assigned with a numeric value, which you may think of as an amount. The corresponding code is given below.

```
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2]
})
```

Next, we plot these data as a bar plot, with the fruits named on horizontal axis and the assigned values on the vertical axis. With plotly.express this will be as easy as the following line of code:

```
fig = px.bar(df, x="Fruit", y="Amount")
```

Bringing all pieces together gives the following simple app:

```
# Import packages
from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Prepare data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2]
})
fig = px.bar(df, x="Fruit", y="Amount")

# Initialise the app
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown(id='our-title', children='My First App', style={'textAlign': 'center'})
dropdown = dcc.Dropdown(id='our-drop', options=[1,2,3], value=3, clearable=False)
figure = dcc.Graph(id='our-graph', figure=fig)

# App layout
app.layout = dbc.Container([
    markdown,
    dropdown,
    figure
])

# Configure callback
@app.callback(
    Output(component_id='our-graph', component_property='figure'),
    Input(component_id='our-drop', component_property='value')
)
def update_output_div(value_drop):
    dff = df.copy()
    dff['Amount'][1] = dff['Amount'][1]*value_drop

    fig = px.bar(dff, x="Fruit", y="Amount")

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
```
**[GIF, THAT SHOWS THE APP IN THE BROWSER IN ACTION I.E., SELECT A VALUE IN THE DROPDOWN TO CHANGE THE BAR OF THE BARCHART]**
