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

We see that this `DataTable` is huge so let's filter for only a few countries and limit the rows shown to 10:

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

Now we will link the DataTable to a Graph and see that the graph changes when we edit data in the DataTable.\

Creating the `DataTable` becomes more complicated because we need to make each column's `editable` and `selectable` property `true`.  We also add a `Callback` function that will be triggered when data is changed or the user selects a column.  The callback then takes in all the data from the table and return an updated figure.

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
                                columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
                                page_size=10,
                                column_selectable="single",
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
    Input('dataTable1', 'columns'),
    Input('dataTable1', 'selected_columns')
)
def display_output(rows, columns, sel_col):
    # Create data frame from data table 
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    # Create a new figure to replace previous figure
    fig = px.line(df, x= 'year', y = sel_col[0], color = 'country', markers=True)

    return fig

# Launch the app server
if __name__ == '__main__':
    app.run_server()
```

## 9.4 Other Important DataTable props

Let's take a look at some useful `DataTable` props:

First let's add `sorting`:
```python
# Create a Dash DataTable
dataTable = dash_table.DataTable(id='dataTable1', 
                                data=df.to_dict('records'), 
                                columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
                                page_size=10,
                                column_selectable="single",
                                sort_action='native',
                                )
```

Now let's add some styling:

```python
# Create a Dash DataTable
dataTable = dash_table.DataTable(id='dataTable1', 
                                data=df.to_dict('records'), 
                                columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
                                page_size=10,
                                column_selectable="single",
                                sort_action='native',
                                style_cell={'padding': '5px'},
                                style_data_conditional=[{
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'}],
                                style_header={
                                    'backgroundColor': 'rgb(230, 230, 230)',
                                    'fontWeight': 'bold'}
)
```




## Summary
In this chapter we learned about `Dash DataTables`.  In the next chapter we will learn about **Advanced Callbacks**.
