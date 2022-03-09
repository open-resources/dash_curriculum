# Import required Python libraries
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Create the Dash app object
app = Dash(__name__)

# Create app components
button1 = html.Button("Button 1", id="button1")

# Add components to app layout
app.layout = dbc.Container([
                button1
])

# Launch app
if __name__ == '__main__':
    app.run_server()