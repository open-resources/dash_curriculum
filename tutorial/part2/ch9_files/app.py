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
        columns=[{'name': i, 'id': i, 'selectable':True, 'deletable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
        sort_action='native',
        filter_action='native',
        row_deletable=True,
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