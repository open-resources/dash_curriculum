# Import packages
from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc

# Initialise the app
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown(id='our-title', children='My First App', style={'textAlign': 'center'})
dropdown = dcc.Dropdown(id='our-drop', options=['My First App', 'Another Title', 'Welcome to this App'], value='My First App')

# App layout
app.layout = dbc.Container([
    markdown,
    dropdown
])

# Configure callback
@app.callback(
    Output(component_id='our-title', component_property='children'),
    Input(component_id='our-drop', component_property='value')
)
def update_markdown(value_drop):
    title = value_drop
    return title


# Run the app
if __name__ == '__main__':
    app.run_server()