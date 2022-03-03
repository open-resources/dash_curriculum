# Chapter 2: Getting Started with Dash

- Structure of a Dash App
  - Dash apps are rendered and accessible in a web browser and require the developer to follow some folder structure and naming conventions.
  - The are best practices for a structure of a simple Dash App. Take this app as an example:

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
      -  (1) : xxx
      -  (2) : data
      -  (3) : "App" object
      -  (4) the app layout: i.e. the objects that we intend to show in the dashboards
      -  (5) functions that can be defined to enable user interaction, e.g. allow the user to filter a chart by geography
      -  (6) some statements to run the app (run_server)
  - More complete app will include ... any other additional app asset such as: "css" files (Chapter...)  to further customise the layout  


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
