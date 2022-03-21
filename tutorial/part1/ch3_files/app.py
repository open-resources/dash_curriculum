# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 10, 1)

# App Layout 
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(markdown, width=8)),
        dbc.Row(
            [
                dbc.Col(dropdown, width = 3), 
                dbc.Col(slider, width = 9),
            ]
        ),
        dbc.Row(dbc.Col(slider, width = 6)),
        dbc.Row(dbc.Col(button, width = 11)),
    ]
)

# Run the App 
if __name__ == '__main__':
    app.run_server()