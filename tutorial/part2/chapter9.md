# Chapter 9

## What You Will Learn
In this chapter you will learn about `Dash DataTables' and how to use them to explore and edit data.

## 9.1 Intro to DataTables
`DataTables` are an [interactive table component designed for viewing, editing, and exploring large datasets](https://dash.plotly.com/datatable).  Let's create a basic `DataTable` with the [gapminder dataset](https://www.gapminder.org/data/).

```python
# Import libraries
from dash import Dash, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Import data into Pandas dataframe
df = px.data.gapminder()

# Create a Dash DataTable
dataTable = dash_table.DataTable(id="dataTable1", data=df.to_dict('records'))

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            dataTable
        ])
    ])
)

# Launch the app server
if __name__ == '__main__':
    app.run_server()
```

We see that this `DataTable` is huge let's filter for only a few countries and limit the rows shown to 10:

```python
# Import libraries
from dash import Dash, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Import data into Pandas dataframe
df = px.data.gapminder()

# Filter data with a list of countries we're interested in exploring
country_list = ['Canada', 'Brazil', 'Norway', 'Germany']
df = df[df['country'].isin(country_list)]

# Create a Dash DataTable
dataTable = dash_table.DataTable(id="dataTable1", data=df.to_dict('records'), page_size=10)

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            dataTable
        ])
    ])
)

# Launch the app server
if __name__ == '__main__':
    app.run_server()
```

## 9.2 Linking DataTable to a Graph

Now we will link the DataTable to a Graph and see that the graph changes when we edit data in the DataTable.

- For each `column` in the DataTable we need to set its `editable` property so our `DataTable` declaration changes from
`dataTable = dash_table.DataTable(id="dataTable1", data=df.to_dict('records'), page_size=10)`

to

`dataTable = dash_table.DataTable(id='dataTable1', 
                                data=df.to_dict('records'), 
                                columns=[{'name': i, 'id': i, 'editable':True} for i in df.columns]
                                )`
- 

```python
# Import libraries
from dash import Dash, dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px


# Import data into Pandas dataframe
df = px.data.gapminder()

# Filter data with a list of countries we're interested in exploring
country_list = ['Canada', 'Brazil', 'Norway', 'Germany']
df = df[df['country'].isin(country_list)]

# Create a Dash DataTable
dataTable = dash_table.DataTable(id='dataTable1', 
                                data=df.to_dict('records'), 
                                columns=[{'name': i, 'id': i, 'editable':True} for i in df.columns]
                                )

# Create a line graph of life expectancy over time
fig = px.line(df, x= 'year', y = 'lifeExp', color = 'country', markers=True)
graph1 = dcc.Graph(id='figure1', figure=fig)

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            graph1,
            dataTable,
        ])
    ])
)


# Link DataTable edits to the plot with a callback function
@app.callback(
    Output('figure1', 'figure'),
    Input('dataTable1', 'data'),
    Input('dataTable1', 'columns')
)
def display_output(rows, columns):
    # Create data frame from data table 
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    # Create a new figure to replace previous figure
    fig = px.line(df, x= 'year', y = 'lifeExp', color = 'country', markers=True)

    return fig

# Launch the app server
if __name__ == '__main__':
    app.run_server()
```

## 9.4 Other importnat DataTable props


## Summary
In this chapter we learned about `Dash DataTables`.  In the next chapter we will learn about **Advanced Callbacks**.
