# Chapter 9: DataTables

## What You Will Learn
In this chapter you will learn about `Dash DataTables` and how to use them to explore and edit data.

## 9.1 Intro to DataTables
`DataTables` are an interactive table designed for viewing, editing, and exploring large datasets.  Let's create a basic `DataTable` with the gapminder dataset.

```python
# Import libraries
from dash import Dash, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Import data into Pandas dataframe
df = px.data.gapminder()

# Create a Dash DataTable
data_table = dash_table.DataTable(id="dataTable1", data=df.to_dict('records'))

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            data_table
        ])
    ])
)

# Launch the app server
if __name__ == '__main__':
    app.run_server()
```

![intro datatable](../assets/p2_c9/datatable_intro.png)

We see that this dataset is huge so let's use the `page_size` property of `DataTables` to limit the rows shown to 10.  We'll also filter the dataset to only look at a few countries
and remove columns we're not interested in:

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

# Filter columns we want to use
df.drop(['continent', 'iso_alpha', 'iso_num'], axis=1, inplace=True)

# Create a Dash DataTable
data_table = dash_table.DataTable(id="dataTable1", data=df.to_dict('records'), page_size=10)

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            data_table
        ])
    ])
)

# Launch the app server
if __name__ == '__main__':
    app.run_server()
```

![filtered datatable](../assets/p2_c9/datatable_filtered.png)
## 9.2 Linking DataTable to a Graph

Now we will link the DataTable to a Graph and see that the graph changes when we edit data in the DataTable.

### 9.2.1 Line Plot

Creating the `DataTable` becomes more complicated because we need to make each column's `editable` and `selectable` property `true`.  We'll modify the `columns` and `columns_selectable` properties of the DataFrame.

We also add a `Callback` function that will be triggered when data is changed or the user selects a column.  The callback then takes in all the data from the table and return an updated figure.

```python
# Import libraries
from dash import Dash, dash_table, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


# Import data into Pandas dataframe
df = px.data.gapminder()

# Filter data with a list of countries we're interested in exploring
country_list = ['Canada', 'Brazil', 'Norway', 'Germany']
df = df[df['country'].isin(country_list)]

# Filter columns we want to use
df.drop(['continent', 'iso_alpha', 'iso_num'], axis=1, inplace=True)

# Create a Dash DataTable
data_table = dash_table.DataTable(
        id='dataTable1', 
        data=df.to_dict('records'), 
        columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
)

# Create a line graph of life expectancy over time
fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
graph1 = dcc.Graph(id='figure1', figure=fig)

# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            graph1,
            data_table,
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
    fig = px.line(df, x='year', y=sel_col[0], color='country', markers=True)

    return fig

# Launch the app server
if __name__ == '__main__':
    app.run_server()
```

![data table with line plot](../assets/p2_c9/datatable_plot_link.gif)

### 9.2.2 Histogram

Let's explore the data further using a `Histogram` that we'll animate to show population change over time:

```python
# Import libraries
from dash import Dash, dash_table, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


# Import data into Pandas dataframe
df = px.data.gapminder()

# Filter data with a list of countries we're interested in exploring
country_list = ['Canada', 'Brazil', 'Norway', 'Germany']
df = df[df['country'].isin(country_list)]

# Filter columns we want to use
df.drop(['continent', 'iso_alpha', 'iso_num'], axis=1, inplace=True)

# Create a Dash DataTable
data_table = dash_table.DataTable(
        id='dataTable1', 
        data=df.to_dict('records'), 
        columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
)

# Create a line graph of life expectancy over time
fig1 = px.line(df, x='year', y='lifeExp', color='country', markers=True)
graph1 = dcc.Graph(id='figure1', figure=fig1)

# Create an animated histogram of population growth
fig_bar = px.histogram(df, x="country", y="pop", color="country",
                 animation_frame="year", animation_group="country", 
                 range_y=[0,200000000],
)
graph2 = dcc.Graph(id='figure2', figure=fig_bar)


# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            graph1,
        ]),
        dbc.Col([
            graph2,
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            data_table,
        ]),
    ]),  
])


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
    fig = px.line(df, x='year', y=sel_col[0], color='country', markers=True)

    return fig


# Link DataTable edits to the plot with a callback function
@app.callback(
    Output('figure2', 'figure'),
    Input('dataTable1', 'data'),
    Input('dataTable1', 'columns'),
    Input('dataTable1', 'selected_columns')
)
def display_output(rows, columns, sel_col):
    # Create data frame from data table 
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    # Create a new figure to replace previous figure
    # Create an animated histogram of population growth
    fig = px.histogram(df, x="country", y="pop", color="country",
                    animation_frame="year", animation_group="country", 
                    range_y=[0,200000000],
    )

    return fig
# Launch the app server
if __name__ == '__main__':
    app.run_server()
```

![datatable histogram link](../assets/p2_c9/datatable_hist_link.gif)

## 9.3 Other Important DataTable props

Let's take a look at some useful `DataTable` props:

### 9.3.1 Sorting
First let's add `sorting`:
```python
# Create a Dash DataTable
data_table = dash_table.DataTable(
        id='dataTable1', 
        data=df.to_dict('records'), 
        columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
        sort_action='native',
)
```
![data table sorting](../assets/p2_c9/datatable_sort.gif)

### 9.3.2 Filtering
We can also add the option to filter the columns of data.  In this example we will only use **>** or **<**:

![datatable filter](../assets/p2_c9/datatable_filter.gif)

```python
# Import libraries
from dash import Dash, dash_table, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


# Import data into Pandas dataframe
df = px.data.gapminder()

# Filter data with a list of countries we're interested in exploring
country_list = ['Canada', 'Brazil', 'Norway', 'Germany']
df = df[df['country'].isin(country_list)]

# Filter columns we want to use
df.drop(['continent', 'iso_alpha', 'iso_num'], axis=1, inplace=True)

# Create a Dash DataTable
data_table = dash_table.DataTable(
        id='dataTable1', 
        data=df.to_dict('records'), 
        columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
        sort_action='native',
        filter_action='native',
)

# Create a line graph of life expectancy over time
fig1 = px.line(df, x='year', y='lifeExp', color='country', markers=True)
graph1 = dcc.Graph(id='figure1', figure=fig1)

# Create an animated histogram of population growth
fig_bar = px.histogram(df, x="country", y="pop", color="country",
                 animation_frame="year", animation_group="country", 
                 range_y=[0,200000000],
)
graph2 = dcc.Graph(id='figure2', figure=fig_bar)


# Create the Dash application with Bootstrap CSS stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            graph1,
        ]),
        dbc.Col([
            graph2,
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            data_table,
        ]),
    ]),  
])

# Take a filter string and apply it to a dataframe. Return a Plotly figure
def parse_filter(filter, df):
    # Parse the string to get the filter and target column
    lst = filter.split("s")
    col_name = lst[0][1:-2]
    op = lst[1].split(" ")
    # perform > or < filter of df column
    if op[0] == ">":
        df = df[df[col_name]> float(op[1])] 
    elif op[0] == "<":
        df = df[df[col_name]< float(op[1])] 
        
    # Create a new figure to replace previous figure
    fig = px.line(df, x='year', y=col_name, color='country', markers=True)

    return fig


# Link DataTable edits to the plot with a callback function
@app.callback(
    Output('figure1', 'figure'),
    Input('dataTable1', 'data'),
    Input('dataTable1', 'columns'),
    Input('dataTable1', 'selected_columns'),
    Input('dataTable1', "filter_query")
)
def display_output(rows, columns, sel_col, flter):

    # Create data frame from data table 
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])

    # Apply the filter if selected
    if flter:
        fig = parse_filter(flter,df)
        return fig
    # Use the selected column if the user chose one
    elif sel_col:
        # Create a new figure to replace previous figure
        fig = px.line(df, x='year', y=sel_col[0], color='country', markers=True)
        return fig
    else:
        # Create a new figure to replace previous figure
        fig = px.line(df, x='year', y='lifeExp', color='country', markers=True) 
        return fig


# Link DataTable edits to the plot with a callback function
@app.callback(
    Output('figure2', 'figure'),
    Input('dataTable1', 'data'),
    Input('dataTable1', 'columns'),
    Input('dataTable1', 'selected_columns')
)
def display_output(rows, columns, sel_col):
    # Create data frame from data table 
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    # Create a new figure to replace previous figure
    # Create an animated histogram of population growth
    fig = px.histogram(df, x="country", y="pop", color="country",
                    animation_frame="year", animation_group="country", 
                    range_y=[0,200000000],
    )

    return fig
# Launch the app server
if __name__ == '__main__':
    app.run_server()
```


### 9.3.3 Delete Columns
Datasets will often contain much more data than we care about.  Let's allow the user to delete columns in the `DataTable` that they are not interested in:
```python
# Create a Dash DataTable
data_table = dash_table.DataTable(
        id='dataTable1', 
        data=df.to_dict('records'), 
        columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True, 'deletable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
        sort_action='native',
        filter_action='native',
)
```
**TODO: gif of deleting columns**

### 9.3.4 Styling DataTable

Now let's add some `styling` to the DataTable

```python
# Create a Dash DataTable
data_table = dash_table.DataTable(
        id='dataTable1', 
        data=df.to_dict('records'), 
        columns=[{'name': i, 'id': i, 'editable':True, 'selectable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
        sort_action='native',
        style_cell={'padding': '5px'},
        style_data_conditional=[
            {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(204, 230, 255)'},
            ],

        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'}
)
```

**TODO: picture of datatable**

## Summary
In this chapter we learned about `Dash DataTables`.  In the next chapter we will learn about **Advanced Callbacks**.
