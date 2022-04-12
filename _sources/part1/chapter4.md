# Chapter 4: Linking Dash components

## What you will learn

This chapter will cover the callback. The callback will allow you to link the various components in your Dash app. App callbacks are necessary to build truly interactive apps.

To better understand the notation of a callback, there will be a short introduction to decorators in Python. We will then dive into the general structure of callbacks and finally see some examples in action.

```{admonition} Learning Intentions
- Decorators in Python
- Structure of callbacks
- Component ids & properties
- Simple examples for callbacks
```

When we finish this chapter you'll have a fully-operational interactive app that links together multiple components. 

[Download the code](./ch4_files/ch4_app.py)

## 4.1 Introduction to decorators in Python

Decorators provide extensions to the behavior of Python functions without modifying the functions' code.

```{tip}
For a comprehensive overview of the Python decorator, have a look at [Real Python](https://realpython.com/primer-on-python-decorators/).
```

## 4.2 Structure of app callbacks

Before we talk about the structure of a callback, let’s briefly discuss how callbacks will fit into your app. The callbacks will always fit after your app layout but before you actually run the app. Here’s the complete structure:

- Import packages
- Initialise the App
- Create app components
- App Layout
- **Configure callback(s)**
- Run the App

Let's start off with an easy example. For this purpose let's take the app from the previous chapter, containing a markdown and a dropdown. Extending this code by a simple callback we get an app that links these two components together.

```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My First app')
dropdown = dcc.Dropdown(id='our-dropdown', options=['My First app', 'Welcome to the App', 'This is the title'], value='My First app')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row([dbc.Col([dropdown], width=3)]),
    ]
)


# Configure callback
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value')
)
def update_markdown(value_dropdown):
    title = value_dropdown
    return title


# Run the App
if __name__ == '__main__':
    app.run_server()
```

**[GIF, THAT SHOWS THE APP IN THE BROWSER IN ACTION I.E., SELECT A VALUE IN THE DROPDOWN TO CHANGE THE TITLE OF THE PAGE]**

Let’s go through this step by step. Note that for linking components with each other, we have to uniquely identify them in order to distinguish between them. For this purpose, you should add the `id` property to each component, as we do above with the Dropdown and Markdown components.

In addition to `id` property, we also include the `value` property for the dropdown. This will indicate the default value of the dropdown displayed on the page when loaded for the first time.

```{tip}
For a comprehensive overview of all the different properties of the Dash Core Components library, please have a look at the specific component in the [Official documentation](https://dash.plotly.com/dash-core-components).
```

Now, let’s link the components together. This is done within the callback. Despite the variety of usage of callbacks, they all share the same structure and are composed of two main elements: the callback decorator and the callback function:

```
# Configure callback
@app.callback(                                                          ###---------------###
    Output(component_id='our-markdown', component_property='children'), #     Callback      #
    Input(component_id='our-dropdown', component_property='value')      #     decorator     #
)                                                                       ###---------------###
def update_markdown(value_drop):                                        ###---------------###
    title = value_drop                                                  # Callback function #
    return title                                                        ###---------------###
```

### 4.2.1 Callback Decorator

The callback decorator makes up the first part of the callback. Here you specify the components and their corresponding properties that you want to link together.

```
@app.callback(                                                          
    Output(component_id='our-markdown', component_property='children'), 
    Input(component_id='our-dropdown', component_property='value')      
)   
```

The decorator itself takes up two different arguments: Output and Input. Both of them again will take two arguments, the component id and the component property.

```{attention}
Always make sure to import the packages 'Output' and 'Input' from the dash library at the beginning of your code when you are working with callbacks.
```

The meaning of the different arguments is straight forward. 
  * The Output specifies the property of the component that will be modified; in this case, it's the `children` property of the markdown. 
  * Accordingly, the Input specifies the property of the component that will activate the callback; in this case, it's the `value` property of the dropdown. 
  * Whenever the property of the Input component is changed by the user, it will immediately trigger the callback and update the property of the Output component, based on the returned value in the callback function. You might compare this behavior with two cells in excel which are linked together. 

### 4.2.2 Callback Function

The callback function makes up the second part of the callback. The function itself - like any arbitrary function in python - is composed of three different parts, namely

- The function argument(s)
- The function body
- The return or output of the function

```
def update_markdown(value_drop):
    title = value_drop
    return title
```

Let's have a look at those in more detail.

```{admonition} The function argument
The callback function takes as many arguments as there are Input components. The order remains stable. That is, the property of the component you enter first in the Input argument of the callback decorator will be represented by the argument you enter first into the callback function.
```

```{admonition} The function body
The function body is the place where you can work with the input data to build graphs and manipulate app data.
```

```{admonition} The return or output of the function
At the end of the callback function, the object returned will be assigned to the component property of the Output. In our example, the title is assigned to the children of the Markdown, thereby, updating the title of the page. 
Note, that you might work with multiple outputs in the callback decorator, in which case you would need to return the same number of objects in the callback function.
```

## 4.3 Callbacks in action

Now, that we have already seen a simple callback and understand how it is implemented, let's grade things up a little.

### 4.3.1 Change the style of a markdown by a slider

After linking together a markdown and a dropdown, let's replace the dropdown by a slider. Instead of the children property of the markdown we introduce another property called `style` which can be used for any kind of styling e.g., the color of the markdown or the font size. [Chapter 9](../part3/chapter9.md) will give you some more insights on this topic.

We equip the slider introduced in the previous chapter with an `id` and add the `value` property with a default value to it. The respective value of the slider will then be responsible for seizing the markdown. In this case, we change the font size of the markdown to be the default value added by twice the value choosen within the slider.

The following snippet shows the corresponding code.

```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My First app', style={'fontSize': 12})
slider = dcc.Slider(id='our-slider', min=0, max=10, step=1, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown, width=8)),
        dbc.Row(dbc.Col(slider, width=9)),
    ]
)


# Configure callback
@app.callback(
    Output(component_id='our-markdown', component_property='style'),
    Input(component_id='our-slider', component_property='value')
)
def update_markdown(value_slider):
    markdown_style = {'fontSize': 12+2*value_slider}
    return markdown_style


# Run the App
if __name__ == '__main__':
    app.run_server()
```

In action, you will now have programmed the following interactive app:

**[GIF, THAT SHOWS THE APP IN THE BROWSER IN ACTION I.E., SELECT A VALUE IN THE SLIDER TO CHANGE THE FONT SIZE OF THE MARKDOWN]**

### 4.3.2 Bringing everything together

To end this chapter, let's tie everything together. Especially, we want to make you aware, how to use mutliple callbacks in your app. Therefore, this paragraph brings everything together we have achieved in this chapter. In order to combine both callbacks implemented above just put both of them behind each other in your code. Hereby the order doesn't matter, just make sure you have all components defined and assigned the right ids and properties. Merging everything together will give you the final app for this chapter.

```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My First app', style={'fontSize': 12})
dropdown = dcc.Dropdown(id='our-dropdown', options=['My First app', 'Welcome to the App', 'This is the title'], value='My First app')
slider = dcc.Slider(id='our-slider', min=0, max=10, step=1, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown, width=8)),
        dbc.Row(
            [
                dbc.Col(dropdown, width=3),
                dbc.Col(slider, width=9),
            ]
        ),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value')
)
def update_markdown(value_dropdown):
    title = value_dropdown
    return title


@app.callback(
    Output(component_id='our-markdown', component_property='style'),
    Input(component_id='our-slider', component_property='value')
)
def update_markdown(value_slider):
    title_size = {'fontSize': 12+2*value_slider}
    return title_size


# Run the App
if __name__ == '__main__':
    app.run_server()
```

**[GIF, THAT SHOWS THE APP IN THE BROWSER IN ACTION I.E., SELECT A VALUE IN THE SLIDER AND DROPDOWN (AND OTHER WAY AROUND) TO CHANGE THE MARKDOWN]**

## Summary

Congratulations! You are now able to build a simple app with variuos components, structure them within the app and understand the neccessity of component ids and properties. You have also learned about the concept of app callbacks and how they upgrade your app by adding interactivity. No matter if only one or multiple callbacks, you'll be able to manage your app linking different components together. 

Now it's your turn, try yourself to link other components you already know and build your own first interactive app.
