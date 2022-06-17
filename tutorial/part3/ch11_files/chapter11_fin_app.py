# Import packages
from dash import Dash, Input, Output, State, html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import base64


# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

image_filename = 'plotly.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
img = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))
offcanvas_doc = dcc.Link("Off-Canvas documentation", id='oc_doc', target='_blank',href='https://dash-bootstrap-components.opensource.faculty.ai/docs/components/offcanvas/')
link_doc = dcc.Link("Link documentation", id='link_doc', target='_blank',href='https://dash.plotly.com/dash-core-components/link')


offcanvas_layout = dbc.Container(
    [
        dbc.Row([dbc.Col(img)]),
        dbc.Row([dbc.Col(offcanvas_doc)]),
        dbc.Row([dbc.Col(link_doc)]),
    ]
)
offcanvas = html.Div(
    [
        dbc.Button("Open Offcanvas", id="open-offcanvas", n_clicks=0),
        dbc.Offcanvas(
            [offcanvas_layout],
            id="offcanvas",
            title="Off-Canvas",
            is_open=False,
        ),
    ]
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(offcanvas)])
    ]
)



@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
)
def toggle_offcanvas(n1):
    if n1:
        return True
    


# Run the App
if __name__ == '__main__':
    app.run_server()
