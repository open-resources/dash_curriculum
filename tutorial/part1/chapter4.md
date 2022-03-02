# Chapter 4: Linking Dash components

 1. Introduction to decorators in Python
     1. what are the advantages of decorators and basic structure  
 2. Structure of a Dash callback decorator (*copy simple app from chapter 2 to refer to its callback here)
     1. Decorator arguments: Output, Input, component_id, component_property 
 3. Structure of Dash callback function
     1. function argument (*also mention multiple inputs require multiple arguments)
     2. function body (*a place where you can work with the input data to build graphs and manipulate app data)
     3. Return output of function (*also mention multiple outputs require multiple objects)

  4. Seeing Graph and Dropdown in action (*copy simple app from chapter 3 to refer to its graph and dropdown components)
     1. Create a callback with the Dropdown and Graph from chapter 3
        1. add the graph figure and dropdown value in decorator as the component_property
        2. In callback function body: taking dropdown value to change bar graph 
  5. Seeing Dropdown and Div children in action: (* div would represent title of webpage)
     1. show reader how to control title of page: Dropdown with different text that will change the children of div
  6. Seeing Slider and Div style in action 
     1. slider value would change font size 

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
