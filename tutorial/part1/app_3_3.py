# Import Python libraries
from dash import Dash, html 
import dash_bootstrap_components as dbc

# Create a Dash application, pass in a stylesheet from Bootstrap
app = Dash( external_stylesheets=[dbc.themes.BOOTSTRAP] )

# Create the layout of the app
app.layout = dbc.Container([
                # Row 1
                dbc.Row([
                    dbc.Col([
                        html.Div("Div 1")
                    ],
                    style={"background-color": "blue"},
                    ),
                    dbc.Col([
                        html.Div("Div 2")
                        ]),
                    ],
                    style={"background-color": "green"},
                    className="h-75",
                    ),
                # Row 2
                dbc.Row([
                    dbc.Col([
                        html.Div("Div 3")
                    ],
                    style={"background-color": "pink"},
                    ),
                    dbc.Col([
                        html.Div("Div 4")
                        ]),
                    ],
                    style={"background-color": "yellow"},
                    className="h-25",
                    ),
            ],
            style={"height": "100vh"},
            )

# Run the app
app.run_server()