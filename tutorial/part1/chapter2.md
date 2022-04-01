# Chapter 2: Getting Started with Dash

## What you will learn
This chapter sets the foundation for the creation of Dash Applications. Starting from a minimal example, we'll explain the structure of a Dash app, how to interact with it, and how to update it. By the end of the chapter, you'll understand the following code and know how to launch your first Dash App:

```
# (1) Import packages --------------------------------------------
from dash import Dash, dcc
import dash_bootstrap_components as dbc

# (2) Initialise the App --------------------------------------------
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# (3) App Layout --------------------------------------------
app.layout = dbc.Container([
    dcc.Markdown(children='My First App', style={'textAlign': 'center'})
])

# (4) Run the App --------------------------------------------
if __name__ == '__main__':
    app.run_server()
```

[Download the file](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part1/ch2_files/chapter2_app.py) 

---

## 2.1 Structure of a Dash App
There are best practices to structure Dash Apps. Following these best practices will simplify the development of future applications. The recommended Dash App structure consists of the following sections:
1) Import packages
2) Initialise the App
3) App Layout
4) Run the App

### 2.1.1 Import packages
```
from dash import Dash, dcc
import dash_bootstrap_components as dbc
```
Dash apps require some libraries to run, which we import in the above code. Let's examine each library, one by one:
- **Dash** is the framework which is required to develop the App
- **dcc** stands for dash_core_components which is a module that gives access to many interactive components that are used in Dash apps and will be introduced in Chapter 3.
- Via the **dash_bootstrap_components** module, it is possible to incorporate Boostrap components into the App making it easier to customise the app layout and giving you access to additional components not found in Dash Core Components

### 2.1.2 Initialise the App
```
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
```
In this section, we initialise an app by creating a Dash instance and calling it "app".
This one line of code is pretty much static and fixed for any Dash app you may create. In later chapters, we'll talk about external stylesheets and show you how to to specify more properties to create more complex apps. 

### 2.1.3 App Layout
```
app.layout = dbc.Container([
    dcc.Markdown(children='My First App', style={'textAlign': 'center'})
])
```
The app layout represents what will be displayed on the web browser. There are a lot of elements that you can include in the app layout, normally they are encapsulated into a "Container". In this minimal example, one single component was added: the dcc.Markdown. This Dash Core Component gives you access to a markup language that makes it easier to format text for web pages. This component has a few props, such as `children` and `style`:
- **Children** : this is a common prop shared by many Dash components and it allows the adding of textual content. In a Markdown, the "My First App" will be the content displayed on the web page.
- **Style** : this is another common prop shared by many Dash components and defines the look of the component. It requires a dictionary, where the key represents the styling feature you would like to modify, while the value represents how this feature would be modified. In this app, we want to modify the alignment of the text, by centering it.

### 2.1.4 Run the App
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

## 2.2 Interacting with the App
Once the app is launched and working, we can:
  - **Stop the app**: typing ('Ctrl+C' on Windows, 'Command+C' on Mac) on the console will stop the app. This is sometimes helpful when trying to update an app or when running multiple apps at the same time. Dash apps automatically run on the same browser port 8050, unless specified otherwise. As a result, if we forgot to stop the app and we launch a different app, with the same port number, an error message will be displayed.

[.png with the error message appearing when two apps are simultaneously launched]

  - **Update the app**: whenever we apply changes to the app code, we may first stop the app and re-launch it after making the changes in order to display the new version of the app. A quicker alternative can be to activate the "live updating". Live update will refresh the app, from the browser, as you apply any modification to the app's code. This way, you don't need to stop the app prior to modifying the code. In order to activate this functionality, the statement to Launch the server should be modified to:
```
if __name__ == '__main__':
    app.run_server(debug=True)
```

```{attention}
Make sure the live updating mode is deactivated (debug=False) before releasing/deploying the App. It is best practice to deactivate the debug mode, once the App is finalised
```

Now that you know how to create and launch your first basic App, try to play around with it:
- Try to change the content of the Markdown in your App
- Try to add a new Markdown with custom content

## Summary
In this chapter we learned about what is a Dash App and what is its recommended sturture. We have also explored each building block and their core properties, learning how to modify them.  Finally, we learned how to launch the App, stop and update the App.

In the next chapter, we will discover additional the Dash components and examine how to position them in the layout.

---
---

## Sections that will be covered in later chapters [ Move / Delete this section ]
In later chapters, we'll add features to our App, enhancing the App structure: we will include the following sections:

### Data Preparation
Data is normally created / imported in a global section of the app. In this way, the whole code can refer to and use it.
If you plan to perform any data wrangling tasks, you may want to add to section 1 dedicated libraries (import pandas as pd, ...)

### Callbacks Configuration
Callbacks define the user interaction with the dashboard. For example, a Dash app can have a callback that defines how a dropdown could affect a chart being displayed on the page. Callbacks will be covered in chapter 4.
