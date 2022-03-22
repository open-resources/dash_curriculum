# Chapter 4: Linking Dash components

## What you will learn

After initializing a first simple app, learning about Dash components and setting a layout this chapter covers so called app callbacks, that will allow you to link various components in your Dash app. In other words, app callbacks are necessary to build truly interactive apps. This chapter aims at preparing you with the basics of callbacks. In order to not let you get confused by the notation of a callback there will be a short introduction to decorators in Python. We will then dive into the general structure of callbacks and finally see some examples in action.

```{admonition} Learning Intentions
- Decorators in Python
- Structure of callbacks
- Component ids & properties
- Simple examples for callbacks
```

When we finish this chapter you'll have a fully-operational interactive app that links together different components. [Download the code](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part1/ch4_files/ch4_app.py)

## 4.1 Introduction to decorators in Python

Decorators provide extensions to the behavior of Python functions without modifying the functions' code.

```{tip}
For a comprehensive overview of the Python decorator, have a look at [Real Python](https://realpython.com/primer-on-python-decorators/).
```

## 4.2 Structure of app callbacks

Before we talk about the structure of a callback, let's briefly discuss how callbacks in general will fit into your app. Referring to the structure of an app that we have discussed so far your callbacks will always fit after your app layout and before you actually run the app. Your app gets the following structure:

- Import packages
- Initialise the App
- Create app components
- App Layout
- **Configure callback(s)**
- Run the App

Let's start of with an easy example. For this purpose let's take the app from the previous chapter, containing a markdown and a dropdown. Extending this code by a simple callback we get an app that links these two components together.

**[GIF, THAT SHOWS THE APP IN THE BROWSER IN ACTION I.E., SELECT A VALUE IN THE DROPDOWN TO CHANGE THE TITLE OF THE PAGE]**

The corresponding code will look as follows.

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
        dbc.Row(dbc.Col(markdown, width=8)),
        dbc.Row(dbc.Col(dropdown, width=3)),
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

Let's go through this step by step. Note first, that linking components with each other, in general we have to be able to uniquely identify them in order to distinguish between different of the same components in an app e.g., different dropdowns. This way we can specify which components should influence each other. For this purpose for every component you want to add a component `id`.

More general, the id of a component is also called a property of a component. Besides an id every component has multiple properties which can be used to specify the component. In the example above we introduce the `children` property for the markdown as well as the `options` and the `value` property for the dropdown.

```{tip}
For a comprehensive overview of all the different properties for the components of the dash core components library please have a look at the specific component in the [Official documentation](https://dash.plotly.com/dash-core-components).
```

Now, that we have assigned different properties and ids to the components we can actually link them together. This is done within the callback. Despite the variety of usage of callbacks they all share the above structure and are composed of two main components, the callback decorator and the callback function:

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

Let's break further down these two components.

### 4.2.1 Structure of Dash callback decorator

The callback decorator makes up the first part of the callback. Here you specify the components and their corresponding properties that you want to link together.

The decorator itself takes up two different arguments: Output and Input. Both of them again will take two arguments, the component id and the component property.

```{attention}
Always make sure to import the packages 'Output' and 'Input' from the dash library at the beginning of your code when you are working with callbacks.
```

The meaning of the different arguments is straight forward. The Output specifies what kind of property of which component of your app should be affected e.g., the `children` property of the markdown. Accordingly, the Input specifies what property of which other component of your app should trigger the Output e.g., the `value` property of the dropdown. Note, that linking two different components establishes a direct relationship between them i.e., whenever the property of the input component is changed it will immediately trigger the selected property of the output component to change accordingly. You might compare this behavior with two cells in excel which are linked together.

In order to build more complex applications with Dash later we will introduce a third argument called State, which in some sense will allow to circumvent this direct relationship. Also the arguments Output and Input can take on different components to allow for advanced functionality. However, we'll come back to this in [chapter 10](../part3/chapter10.md).

### 4.2.2 Structure of Dash callback function

The callback function makes up the second part of the callback. Here you process the input the way you want the otuput to be affected by.

The function itself - like any arbitrary function in python - is composed into three different parts, namely

- The function argument(s)
- The function body
- The return or output of the function

Let's have a look at those in more detail.

```{admonition} The function argument
The callback function takes as many arguments as there are input components. The order remains stable i.e., the property of the component you enter first in the input argument of the callback decorator will be represented by the argument you enter first into the callback function.
```

```{admonition} The function body
The function body is the place where you can work with the input data to build graphs and manipulate app data.
```

```{admonition} The return or output of the function
At the end of the callback function the output that has been prepared in the function body gets returned i.e., that's the output of your function and therefore will be the output of your callback. Note, that later on when might working with multiple outputs in the callback decorator also the callback function needs to return the same amount of objects.
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

**[GIF, THAT SHOWS THE APP IN THE BROWSER IN ACTION I.E., SELECT A VALUE IN THE SLIDER AND DROPDOWN (AND OTHER WAY AROUND) TO CHANGE THE MARKDOWN]**

The code looks as follows.

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

## Summary

Congratulations! You are now able to build a simple app with variuos components, structure them within the app and understand the neccessity of component ids and properties. You have also learned about the concept of app callbacks and how they upgrade your app by adding interactivity. No matter if only one or multiple callbacks, you'll be able to manage your app linking different components together. 

Now it's your turn, try yourself to link other components you already know and build your own first interactive app.
