# Import Python libraries
from dash import Dash, html 
import dash_bootstrap_components as dbc

# Create a Dash application, pass in a stylesheet from Bootstrap
app = Dash( external_stylesheets=[dbc.themes.BOOTSTRAP] )

# Create the layout of the app
app.layout = dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.Div("Div 1", style={"outline": "2px dashed blue"})
                    ]),
                    dbc.Col([
                        html.Div("Div 2", style={"outline": "2px dashed red"})
                        ]),
                    ]),
            ],
            fluid=True # fill the horizontal space
            )

# Run the app
app.run_server()