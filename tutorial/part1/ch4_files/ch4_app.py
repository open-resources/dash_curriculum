# Import packages
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(id='our-markdown', children='My First app', style={'fontSize': 12})
dropdown = dcc.Dropdown(id='our-dropdown', options=['My First app', 'Welcome to the App', 'This is the title'], value='My First app')
slider = dcc.Slider(id='our-slider', min=0, max=10, step=1, value=0)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row(
            [
                dbc.Col([dropdown], width=3),
                dbc.Col([slider], width=9),
            ]
        ),
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value')
)
def update_markdown(value_dropdown):
    title = value_dropdown
    return title


@app.callback(
    Output(component_id='our-markdown', component_property='style'),
    Input(component_id='our-slider', component_property='value')
)
def update_markdown(value_slider):
    title_size = {'fontSize': 12+2*value_slider}
    return title_size


# Run the App
if __name__ == '__main__':
    app.run_server()
