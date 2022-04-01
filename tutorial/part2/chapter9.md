# Chapter 9

Idea: Seeing Slider and Div style in action (* div would represent title of webpage): slider value would change font size 
    
Example:
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
