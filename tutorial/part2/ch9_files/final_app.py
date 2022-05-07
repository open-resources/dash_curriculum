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
        columns=[{'name': i, 'id': i,'selectable':True} for i in df.columns],
        page_size=10,
        column_selectable="single",
        selected_columns=['lifeExp'],
        editable=True
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
