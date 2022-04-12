# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(children='My First app')
button = html.Button(children="Button")
checklist = dcc.Checklist(options=['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(options=['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(options=['NYC', 'MTL', 'SF'])
slider = dcc.Slider(min=0, max=10, step=1)

# App Layout 
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row(
            [
                dbc.Col([dropdown], width = 3), 
                dbc.Col([slider], width = 9),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([checklist], width = 6),
                dbc.Col([radio], width = 6),
            ]
        ),
        dbc.Row([dbc.Col([button], width = 11)]),
    ]
)

# Run the App 
if __name__ == '__main__':
    app.run_server()
