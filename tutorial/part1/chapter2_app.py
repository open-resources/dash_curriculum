# (1) Import packages --------------------------------------------
from dash import Dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc

# (2) Prepare Data --------------------------------------------

# (3) Initialise the App --------------------------------------------
app = Dash(__name__)

# (4) App Layout --------------------------------------------
app.layout = dbc.Container([
    dcc.Markdown(id='our-title', children='My First App', style={'textAlign': 'center'})
])

# (5) Configure Callbacks --------------------------------------------
#@app.callback(...)


# (6) Run the App --------------------------------------------
if __name__ == '__main__':
    app.run_server()
