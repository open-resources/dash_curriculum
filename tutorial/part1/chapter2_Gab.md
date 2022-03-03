# Chapter 2: Getting Started with Dash

- Structure of a Dash App
  - Dash apps are rendered and displayed in a web browser.
  - The are best practices to structure a Dash Apps. Following such best practices will simplify the development of the app. Let's take a simple Dash App example:

```
# (1) Required Python Libraries
from dash import Dash, html, dcc, Output, Input
import plotly.express as px

# (2) App Data
df = px.data.iris()

# (3) App object --------------------------------------------
app = Dash(__name__)

# (4) App Layout --------------------------------------------
app.layout =html.Div([
    html.Div(id='our-title', children='My First App', style={'textAlign': 'center'}),
    dcc.Graph(id='our-graph', figure=px.scatter(data_frame=df, x='sepal_length', y='petal_length'))
])

# (5) App Callback
#@app.callback(...)


# (6) Server Launch
if __name__ == '__main__':
    app.run_server()
```

  - As you can see in the code above, we can divide the app into 6 sections:
      -  (1) : Dash apps require some libraries to run
      -  (2) : Data is normally created / imported in a global section so that the whole App can use it as needed
      -  (3) : In this section, we initialise an app. This one row is pretty much static and fixed for any Dash app you may create.
      -  (4) : The app layout contains the structure of the app. There are a lot of elements that you can include in the app layout, normally they are encapsulated into html.Div() sections (within a "div" it is possible to specify its title (e.g. chiltren='My First App') and many other properties). In order to add a figure, we call dcc (which stands for "Dash Core Components"): in this example, we added a scatter plot.
      -  (5) : Callbacks will be covered in chapter XY. These elements define the user interaction with the Dashboard, e.g. defines what a filter does on a chart
      -  (6) : In order to display the app, we add these statements to Launch the server. Also this sectino is pretty much static and fixed for any Dash app you may create.
  - More complete app will include .css files (covered in Chapter XY) and may require additional files (for instance in order to allow multi page Apps).


Once we have a code ready, we need to launch this file in the following way:
- How to run the python file (via VS code)
--> add screenshot in VS code (.gif)
--> add screenshot of final output (.gif)


Console output --> mention that the app will be displayed on the URL
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'chpater2-code1' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off


- Live updates and debugging
  - how to stop your app (and why you should) (Ctrl+C)
  - how to update your app (Ctrl+C and then re-run)
  - how to turn on "live updating" (with debug=True) and what this means (i.e. what happens if you have a syntax error and your app crashes)
    - TIP > make sure debug=False before publishing the app
  - _error message if something is missing (example where we didn't import html)_


--> Suggest some "exercises"
Now that you know how to launch your first basic App, try to play around with it:
- Try to change the title of your App
- Try to change the scatter plot into a barchart (add a "tip" to link it with the documentation)
