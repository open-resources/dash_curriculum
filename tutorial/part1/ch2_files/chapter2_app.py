# (1) Import packages --------------------------------------------
from dash import Dash, dcc
import dash_bootstrap_components as dbc

# (2) Initialise the App --------------------------------------------
app = Dash(__name__)

# (3) App Layout --------------------------------------------
app.layout = dbc.Container([
    dcc.Markdown(children='My First App', style={'textAlign': 'center'})
])

# (4) Run the App --------------------------------------------
if __name__ == '__main__':
    app.run_server()
