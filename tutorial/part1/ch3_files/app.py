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
        dbc.Row(dbc.Col(markdown, style={"background-color": '#636EFA'}, width=8)),
        dbc.Row(
            [
                dbc.Col(dropdown, style={"background-color": '#00CC96'}, width = 3), 
                dbc.Col(slider, style={"background-color": '#EF553B'}, width = 9),
            ]
        ),
        dbc.Row(dbc.Col(slider, style={"background-color": '#AB63FA'}, width = 6)),
        dbc.Row(dbc.Col(button, style={"background-color": '#00CC96'}, width = 11)),
    ]
)

# Run the App 
if __name__ == '__main__':
    app.run_server()