# Chapter 2: Getting Started with Dash

- Structure of a Dash App
  - Dash apps are rendered and displayed in a web browser.
  - The are best practices to structure Dash Applications. Following such best practices will simplify the development of the app. Let's take a simple Dash App example:

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
      1) Dash apps require some libraries to run, the first statement is importing them
      2) Data is normally created / imported in a global section so that the whole App can use it as needed
      3) In this section, we initialise an app. This one row is pretty much static and fixed for any Dash app you may create.
      4) The app layout contains the structure of the app. There are a lot of elements that you can include in the app layout, normally they are encapsulated into html.Div() sections (within a "div" it is possible to specify its title (e.g. chiltren='My First App') and many other properties). In this example, we added a scatter plot: to add a figure, we call dcc (which stands for "Dash Core Components") and then specify which figure we want to use. (Chapter 3 will go through all the components)
      5) Callbacks define the user interaction with the dashboard, e.g. defines what a filter does on a chart. (These elements will be covered in chapter 4)
      6) In order to display the app, we add these statements to Launch the server. This section is pretty much static and fixed for any Dash app you may create.
  - More complete app will include more sections: such as .css files (covered in Chapter 3).
  - This is an initial template that can be used as a starting point for your dashboard. 


Once we have a code ready, we need to launch the corresponding .py file in the following way:
- How to run the python file (via VS code)
- [add screenshot in VS code (.gif)]
- [add screenshot of final output (.jpg)]

After launching the app, we have two outputs:
- The console will show the following message
```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'chpater2-code1' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
```
- In order to display the app, open the browser and navigate to the URL shown in the console: http://127.0.0.1:8050/

Once the app is launched and working, we can:
  - Stop the app: type (Ctrl+C) on the console and this will stop the app. ( ? and why you should)
  - Update the app: once we change the app code, we may re-launch the app to display the new version of the code or activate the "live updating". Live update will refresh the app, from the browser, as you apply any modification on the .py file. In order to activate this functionality, the statement to Launch the server should be modified to:
```
# (6) Server Launch
if __name__ == '__main__':
    app.run_server(debug=True)
```
```{attention} Make sure the live updating mode is deactivated (debug=False) before releasing/deploying the App. It is best practice to deactivate the debug mode, once the App is finalised.
```
? (i.e. what happens if you have a syntax error and your app crashes)  - _error message if something is missing (example where we didn't import html)_


Now that you know how to launch your first basic App, try to play around with it:
- Try to change the title of your App
- Try to change the scatter plot into a barchart (add a "tip" to link it with the documentation)
