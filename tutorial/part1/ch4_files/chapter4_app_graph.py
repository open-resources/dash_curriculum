# Import packages
from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Prepare data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2]
})
fig = px.bar(df, x="Fruit", y="Amount")

# Initialise the app
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown(id='our-title', children='My First App', style={'textAlign': 'center'})
dropdown = dcc.Dropdown(id='our-drop', options=[1,2,3], value=3, clearable=False)
figure = dcc.Graph(id='our-graph', figure=fig)

# App layout
app.layout = dbc.Container([
    markdown,
    dropdown,
    figure
])

# Configure callback
@app.callback(
    Output(component_id='our-graph', component_property='figure'),
    Input(component_id='our-drop', component_property='value')
)
def update_output_div(value_drop):
    dff = df.copy()
    dff['Amount'][1] = dff['Amount'][1]*value_drop

    fig = px.bar(dff, x="Fruit", y="Amount")

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)