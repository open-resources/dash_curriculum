# Chapter 11: Advanced Components

## What you will learn
In this chapter we will introduce several advanced components that go beyond what we have seen so far, but that are necessary for advanced apps.

```{admonition} Learning Intentions
- How to look for additional components
- Familiarize with some of the most common advanced components
```

## 11.1 Introducing advanced components
Dash libraries include a lot of components that serves multiple purposes. It may be a bit overwhelming to navigate through all components, in search for the one that works for our needs. In this chapter we will provide some structure around the components you may include in your app.

We will broke down components into categories, grouping together components that serve the same purpose. For each category, we will present some of the most common components in detail.

All advanced components that will be presented come from these three very common libraries. By clicking on the links, you'll be able to access to each library documentation:
- dcc : [Dash core components](https://dash.plotly.com/dash-core-components)
- dbc : [Dash boostrap components](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/)
- dmc : [Dash mantine components](https://dash-mantine-components.herokuapp.com/)

In the links above, it is possible to search for keywords and find the components we need. Once we've identified the components that we want to include in our app, [this cheatsheet](https://dashcheatsheet.pythonanywhere.com/) is another powerful tool that helps us understanding how components can be customised.


## 11.2 Data Display Components

### 11.2.1 Upload
The `Upload` component allows us to upload a file to the dashboard.  For this example we will upload a [CSV file](https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/) and plot the data:

```python
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objects as go
import base64
import io
from dash.dash import no_update


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

upload = dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag & Drop or Click to Select CSV file'
                    ]),
                    style={
                        'width': '100%',
                        'height': '10%',
                        'lineHeight': '60px',
                        'borderStyle': 'dashed',
                        'textAlign': 'center',
                    }
                )
graph = dcc.Graph(id='graph1')



# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(upload)),
        dbc.Row(dbc.Col(graph))
    ]
)

@app.callback(Output('graph1', 'figure'),
              Input('upload-data', 'filename'))
def update_output(filename):
    if 'csv' in filename:
        fig = go.Figure()
        df = pd.read_csv(filename)
        time_col = df.columns[0]
        for col in df.columns:
            if time_col in col:
                pass
            else:
                fig.add_trace(go.Scattergl(x=df[time_col], y=df[col], mode='lines+markers', name=col))
        fig.update_layout(xaxis_title="Time (ms)", yaxis_title="Degrees rotation")
        return fig
    return no_update


# Launch the app server
if __name__ == '__main__':
    app.run_server()

```

![upload component](ch11_files/upload.gif)

## 11.3 Feedback Components

## 11.4 Filtering & Input Components

### 11.4.1 DatePicker
The DatePicker component allows the user of the app to select a date, that can then be used in our callbacks.
There are two types of date pickers, both part of the DCC library:
- ```DatePickerSingle``` consists of one single date selection that the user can input. By clicking on the object a calendar will pop-up, allowing the user to pick a date
- ```DatePickerRange``` is similar to the previous component, but includes two date selections, which should be read as "start" and "end" dates.

The two components have very similar properties - the complete list is available [here](https://dash.plotly.com/dash-core-components/datepickerrange); the main ones are:
- min_date_allowed : minimum date the user can choose from
- max_date_allowed : maximum date the user can choose from
- start_date : default start date, before the user makes any selection
- end_date : default end date, before the user makes any selection

Let's see an example of this component in action. In the following app a DatePickerRange is used as a filter for a line chart.
Based on the user selection, a dataframe will be filtered and the chart updated.
As min_date_allowed and max_date_allowed, the min and max dates from the dataframe have been selected.

```python
# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import plotly.express as px

# Import data
df = px.data.stocks()
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
date_range = dcc.DatePickerRange(id='date-range',
    start_date_placeholder_text='start date',
    end_date_placeholder_text='end date',
    min_date_allowed=df.date.min(),
    max_date_allowed=df.date.max(),
    display_format='DD-MMM-YYYY',
    first_day_of_week = 1)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([date_range], width=8)]),
        dbc.Row(dbc.Col([dcc.Graph(id='stock-line')], width=8))
    ]
)

# Configure callback
@app.callback(
    Output(component_id='stock-line', component_property='figure'),
    Input(component_id='date-range', component_property='start_date'),
    Input(component_id='date-range', component_property='end_date')
)
def plot_dt(start_date, end_date):
    df_plot = df
    if start_date is not None:
        df_plot = df_plot.loc[(df_plot['date']>=start_date), :]
    if end_date is not None:
        df_plot = df_plot.loc[(df_plot['date']<=end_date), :]
    fig = px.line(df_plot, x='date', y=['GOOG','AAPL','AMZN','FB','NFLX','MSFT'], template='plotly_white')

    return fig

# Run the App
if __name__ == '__main__':
    app.run_server()
```
![DatePickerRange_Example](./ch11_files/chap11-DatePicker.JPG)

## 11.5 Navigation Components

## 11.6 Layout Components



---
---
---
## Previous Notes (To be removed)

## Topics to cover
- Components to unveil additional content
- Components for filtering (e.g. date picker)
- Components for navigation
- Components for media content (carousel…)

## Individual components we're thinking to add
### DCC components
- RangeSlider (required)
- Datepicker (required)
- Interval (required)
- Store (required)
- Upload
### DBC components
- Drop down
- Modal
- Offcanvas too?
- Navbar
- Tabs
- Carousel

### DMC components
[Mantine](https://www.dash-mantine-components.com/)
