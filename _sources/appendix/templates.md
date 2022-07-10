# Dashboard Layouts
In this section we provide you with a series of layout templates for the purpose of...

## Control panels and graphs
- template1
- template2

### Template with control panel on the left

```
# Import packages
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Data
df = px.data.stocks()
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Figure
fig = px.line(df, x='date', y=['AAPL'], template='plotly_white', title='My Plotly Graph')

# Title
title = dcc.Markdown("My Dashboard", className="bg-light", style={'font-size': 40})

# Dropdown
dropdown = dcc.Dropdown(options=['AAPL','GOOG','MSFT'], value='AAPL')

# Date Picker
date_range = dcc.DatePickerRange(
    start_date_placeholder_text='start date',
    end_date_placeholder_text='end date',
    min_date_allowed=df.date.min(),
    max_date_allowed=df.date.max(),
    display_format='DD-MMM-YYYY',
    first_day_of_week=1
)

# Checklist
checklist = dbc.Checklist(
    options=[{'label': 'Dark theme', 'value': 1}],
    value=[],
    switch=True,
)

# Radio items
radio_items = dbc.RadioItems(
    options=[
        {'label': 'Red', 'value': 0}, 
        {'label': 'Green', 'value': 1}, 
        {'label': 'Blue', 'value': 2}
    ],
    value=2,
    inline=True
)

# Card content
card_content = [
    dbc.CardBody(
        [
            html.H5('My Control Panel'),
            html.P(
                '1) Select an option of the dropdown',
            ),
            dropdown,
            html.Br(),
            html.P(
                '2) Pick a date range from the form',
            ),
            date_range,
            html.Br(),
            html.Hr(),
            html.H6('Optional input'),
            html.P(
                '3) Enable dark theme of your graph',
            ),
            checklist,
            html.Br(),
            html.P(
                '4) Change the color of the graphs line',
            ),
            radio_items
        ]
    ),
]

# App Layout
app.layout = html.Div([
    dbc.Row([
        dbc.Col([title], style={'text-align': 'center', 'margin': 'auto'})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Row(dbc.Card(card_content, color="light")),
                ], width=4),
                dbc.Col(dbc.Card(dcc.Graph(id='figure1', figure=fig), color="light"), width=8),
            ]),
        ], width=10, style={'margin': 'auto'}),
    ])
])

# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
```

### Template with control panel on the bottom

## Navigation panels and Graphs
- template3
- template4

### Template witht navigation tabs on the top

### Template with navigation on the side

## Combining navigation and control panels
- template5
- template6

## Multipage app
- template7
- template8
