# Chapter 2: Getting Started with Dash

## What you will learn
This chapter sets the foundation for the creation of Dash Applications. Starting from a minimal example, we'll explain the structure of a Dash app, how to interact with it, and how to update it. By the end of the chapter, you'll understand the following code and know how to launch your first Dash App:

```
# (1) Import packages --------------------------------------------
from dash import Dash, dcc
import dash_bootstrap_components as dbc

# (2) Initialise the App --------------------------------------------
app = Dash(__name__)

# (3) App Layout --------------------------------------------
app.layout = dbc.Container([
    dcc.Markdown(children='My First App', style={'textAlign': 'center'})
])

# (4) Run the App --------------------------------------------
if __name__ == '__main__':
    app.run_server()
```

[Download the code](tutorial/part1/ch2_files/chapter2_app.py)

---

## Structure of a Dash App
There are best practices to structure Dash Apps. Following these best practices will simplify the development of future applications. The recommended Dash App structure consists of the following sections:
1) Import packages
2) Initialise the App
3) App Layout
4) Run the App

### (1) Import packages
```
from dash import Dash, dcc
import dash_bootstrap_components as dbc
```
Dash apps require some libraries to run, this statement is importing them. Let's examine each library, one by one:
- Dash is the framework which is required to develop the App
> Dash is a python framework created by Plotly for creating interactive web applications. Dash is written on the top of Flask, Plotly. js and React. js.
- dcc stands for dash_core_components which is a module that give access to many interactive components that are used in Dash apps and will be introduced in Chapter 3.
- Via the dash_bootstrap_components module, it is possible to incorporates Boostrap components into the App making it easier to customise the app layout.

### (2) Initialise the App
```
app = Dash(__name__)
```
In this section, we initialise an app by creating a Dash instance and calling it "app".
This one line of code is pretty much static and fixed for any Dash app you may create. In later chapters, we'll need to specify more properties to create more complex apps (e.g. point to CSS files). 

### (3) App Layout
```
app.layout = dbc.Container([
    dcc.Markdown(children='My First App', style={'textAlign': 'center'})
])
```
The app layout contains the structure of the app. This represents what will be displayed on the web browser. There are a lot of elements that you can include in the app layout, normally they are encapsulated into a "Container". In this minimal example, one single component was added: the dcc.Markdown. This Dash Core Components gives you access to a markup language that makes it easier to format text for web pages. This component has been customized properties, such as:
- children : this is a common property shared by many Dash components and it allows to add textual content to it. In a Markdown, the "My First App" will be the content displayed on the web page.
- style : this is another common property shared by many Dash components and defines the look of the component. It requires a dictionary and in this case, a center alignment was set.

### (4) Run the App
```
if __name__ == '__main__':
    app.run_server()
```
In order to display the app through the browser, we add these statements to "Launch the server". 

{ !!! TO-DO !!! Add a bried explanation on why we need a server}

This section is pretty much static and fixed for any Dash app you may create.

Once we have the full code ready and saved in a .py file, we need to launch it:
[.gif showing how to launch the .py file of this chapter via VS code, displaying the Console output]

After launching the app, we will see the following console output:
```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'chpater2-code1' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
```
- In order to display the app, open the browser and navigate to the URL shown in the console, in this case: http://127.0.0.1:8050/

[.png with the App output from browser only]

---

## Interacting with the App
Once the app is launched and working, we can:
  - Stop the app: typing (Ctrl+C) on the console will stop the app. This is sometimes required as one App per port can be launched: if we forgot to stop the app and we launch a different app, an error message will be displayed.

[.png with the error message appearing when two apps are simultaneously launched]

  - Update the app: whenever we apply any change the app code, we may re-launch the app to display the new version of the code. A quicker alternative can be to activate the "live updating". Live update will refresh the app, from the browser, as you apply any modification to the corresponding .py file. In order to activate this functionality, the statement to Launch the server should be modified to:
```
if __name__ == '__main__':
    app.run_server(debug=True)
```

```{attention}
Make sure the live updating mode is deactivated (debug=False) before releasing/deploying the App. It is best practice to deactivate the debug mode, once the App is finalised
```

Now that you know how to create and launch your first basic App, try to play around with it:
- Try to change the content of your first Markdown of your App
- Try to add a new Markdown with a custom content

---
---

## Sections that will be covered in later chapters [ Move / Delete this section ]
In later chapters, we'll add features to our App, enhancing the App structure: we will include the following sections:

### Data Preparation
Data is normally created / imported in a global section of the app. In this way, the whole code can refer to and use it.
If you plan to perform any data wrangling tasks, you may want to add to section 1 dedicated libraries (import pandas as pd, ...)

### Callbacks Configuration
Callbacks define the user interaction with the dashboard. For example, a Dash app can have a callback that defines how a dropdown could affect a chart being displayed on the page. Callbacks will be covered in chapter 4.
