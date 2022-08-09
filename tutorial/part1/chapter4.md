# Chapter 4: Linking Dash components

## What you will learn

In Dash, "callbacks" allow you to link together the various components of your Dash app. App callbacks are necessary to build interactive apps, e.g. to have a component change what is displayed in a plot.

To better understand the notation of a callback, we will start with a short introduction to decorators in Python. We will then dive into the general structure of callbacks and finally see some examples in action.
After finishing this chapter you'll have a fully-operational interactive app that links together multiple components. 

```{admonition} Learning Intentions
- Decorators in Python
- Structure of callbacks
- Component ids & properties
- Additional examples of callbacks
```

By the end of this chapter you will know how to build this app:

![gif4-3](./ch4_files/gif-chap4-3.gif)

````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
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
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row(
            [
                dbc.Col([dropdown], width=3),
                dbc.Col([slider], width=9),
            ]
        ),
    ]
)


# Callbacks
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

````

[Click to download the complete code file for this chapter](https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part1/ch4_files/ch4_app.py)

## 4.1 Introduction to decorators in Python

Decorators can extend the behavior of a Python function without directly modifying the function's code. They "decorate" functions, that is, they wrap code around a function to enhance the function's capabilities. Decorators are usually called before defining the function that you want to decorate. 

For a comprehensive overview of the Python decorator, have a look at [Real Python](https://realpython.com/primer-on-python-decorators/).

## 4.2 Structure of app callbacks

Before we talk about the structure of a callback, let’s briefly discuss how callbacks will fit into your app. The callbacks will always fit after your app layout but before you actually run the app. Here’s the complete structure of what our apps will look like:

- Import packages
- Initialise the App
- Create app components
- App Layout
- **Configure callback(s)**
- Run the App

Let's take the app from the previous chapter, containing a markdown and a dropdown component. Extending this code with a simple callback gives us an app that links these two components together, where the selection of the dropdown value will update the title of the app.


```{attention}
Always make sure to import the packages 'Output' and 'Input' from the dash library at the beginning of your code when you are working with callbacks.
```

```
# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My First app')
dropdown = dcc.Dropdown(
    id='our-dropdown',
    options=['My First app', 'Welcome to the App', 'This is the title'],
    value='My First app'
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row([dbc.Col([dropdown], width=3)]),
    ]
)


# Callback
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

![gif4-1](./ch4_files/gif-chap4.1.gif)

Let’s go through this code step by step. Note that for linking components with each other, we have to uniquely identify them in order to distinguish between them. For this purpose, you should add the `id` property to each component, as we do above with the Dropdown and Markdown components. In addition to `id` property, we also include the `value` property for the dropdown. This will indicate the default value of the dropdown displayed on the page when loaded for the first time.

```{tip}
For a comprehensive overview of all the different properties of the Dash Core Components library, please have a look at the specific component in the [Official documentation](https://dash.plotly.com/dash-core-components).
```

Now, let's examine how the callback links the two components together. Despite the variety of usage of callbacks, they all share the same structure and are composed of two main elements: the callback decorator and the callback function:

```
# Callback decorator
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value')
)
# Callback function
def update_markdown(value_drop):
    title = value_drop
    return title
```

### 4.2.1 Callback Decorator

The callback decorator makes up the first part of the callback. Here you specify the components and their corresponding properties that you want to link together.

```
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value')
)
```

The decorator itself takes up two different arguments: `Output` and `Input`. Both of them again will take two arguments, the component id and the component property.

The meaning of the different arguments is as follows: 
  * The `Output` specifies the property of the component that will be modified; in this case, it's the `children` property of the Markdown component.
  * Accordingly, the `Input` specifies the property of the component that will activate the callback; in this case, it's the `value` property of the dropdown. 
  * Whenever the property of the `Input` component is changed by the user, it will immediately trigger the callback and update the property of the Output component, based on the returned value in the callback function. You might compare this behavior with two cells in excel which are linked together. 

### 4.2.2 Callback Function

The callback function makes up the second part of the callback. The function itself - like any arbitrary function in python - is composed of three different parts, namely

- The function signature
- The function body
- The return value (the output) of the function

```
def update_markdown(value_drop):  # Signature
    title = value_drop            # Body
    return title                  # Return value
```

Let's have a look at each of those in more detail.

The **function signature** specifies the name of the callback function and how many arguments it takes. The number of arguments should be the same as the number of `Input` components in the callback decorator. They should also be in the same order.

The **function body** is where you can work with the input data to build graphs and manipulate app data.

After the callback function has been executed, the **return value** of the function will be assigned to the `component_property` of the `Output` component. In our example, the title is assigned to the `children` property of the Markdown component, thereby updating the title of the page. 
Note, that you might work with multiple outputs in the callback decorator, in which case you would need to return the same number of values from the callback function.

## 4.3 Callbacks in action

Now that we have already seen a simple callback and understand how it is implemented, let's see a more complex example.

### 4.3.1 Change the style of a Markdown component using a slider

Here we will replace the dropdown from the previous example with a slider. In addition to the `children` property of the Markdown component we introduce another property called `style` which can be used for any kind of styling, e.g., the color or size of the font. [Chapter 9](../part3/chapter9.md) will give you some more insights on this topic.

We equip the slider introduced in the previous chapter with an `id` and add the `value` property with a default value to it. The respective value of the slider will then be responsible for modifying the size of the markdown. In this case, once the callback is triggered, we update the font size of the markdown to be the default value (12) plus twice the value chosen within the slider.

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
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row([dbc.Col([slider], width=9)]),
    ]
)


# Callback
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

Notice that we return the `markdown_style` object which is a dictionary type. We do this because the `style` property of the Markdown is of dictionary type.

![gif4-2](./ch4_files/gif-chap4-2.gif)

### 4.3.2 Bringing everything together

To end this chapter, let's tie everything together. Particularly, we want to show an example of how to use multiple callbacks in your app. In order to combine both callbacks implemented in section 4.2 and 4.3, we specify them in sequence in the code. Note that you need to insert space between the two callbacks, but there is no space between the callback decorator and the callback function.

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
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row(
            [
                dbc.Col([dropdown], width=3),
                dbc.Col([slider], width=9),
            ]
        ),
    ]
)


# Callbacks
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

![gif4-3](./ch4_files/gif-chap4-3.gif)

## Exercises
1.  Create a callback that, based on a color name (e.g. red) selected in a `RadioItems` component, updates the `style` property of a `Markdown` component to change the color of its text.
````{dropdown} See Solution
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
```
# Import packages
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
text_ = dcc.Markdown(id='our-markdown', children='Text', style={'textAlign': 'center'})
radioitems_ = dcc.RadioItems(id='our-radio', options=['red', 'orange', 'green'], value='red')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([text_], width=12)]),
        dbc.Row([dbc.Col([radioitems_], width=12)]),
    ]
)

# Callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='style'),
    Input(component_id='our-radio', component_property='value')
)
def update_markdown(value_radio):
    new_style = {'textAlign': 'center', 'color' : value_radio}
    return new_style

# Run the App
if __name__ == '__main__':
    app.run_server()
```
![solution_ex1](./ch4_files/chapter04_ex1.gif)
````
2.  Incorporate the callback we just built into the app code included in the "Bring everything together" section. The new app, besides allowing to change the title text and size, should also allow to change the title color, based on the `RadioItems` component. Locate the radio items component on a new row in the layout. Note that in the new app we will have two callbakcs both affecting the `style` of our title. You should know that callbacks can handle multiple inputs at the same time with the following code: `@app.callback(Output(), Input(), Input())`
````{dropdown} See Solution
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
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
radioitems_ = dcc.RadioItems(id='our-radio', options=['red', 'orange', 'green'], value='red')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row(
            [
                dbc.Col([dropdown], width=3),
                dbc.Col([slider], width=9),
            ]
        ),
        dbc.Row([dbc.Col([radioitems_], width=8)])
    ]
)


# Callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value')
)
def update_markdown(value_dropdown):
    title = value_dropdown
    return title

@app.callback(
    Output(component_id='our-markdown', component_property='style'),
    Input(component_id='our-slider', component_property='value'),
    Input(component_id='our-radio', component_property='value')
)
def update_markdown(value_slider, value_radio):
    new_style = {'fontSize': 12+2*value_slider, 'color' : value_radio}
    return new_style

# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)

```
![solution_ex2](./ch4_files/chapter04_ex2.gif)
````
## Summary

Congratulations! You are now able to build a simple app with various components, structure them within the app and understand the necessity of component ids and properties. You have also learned about the concept of app callbacks and how they upgrade your app by adding interactivity. Regardless if there is only one or multiple callbacks, you'll be able to manage your app by linking different components together.

Now it's your turn, try to link some of the other components you learned in chapter 3 and build your own interactive app.
In the next chapter we will learn how to deploy our app to the web.

