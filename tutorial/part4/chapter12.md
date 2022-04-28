# Chapter 12  Advanced Layout and Styling

## Advanced Layout with Dash Bootstrap Components

 - Vertical alignment
 - Horizontal alignment
 - Container Fluid prop
 - adjusting columns by screen size:
```
      app.layout = dbc.Container([
          dbc.Row(
              [
              dbc.Col(
                  dcc.Markdown("left div", className="bg-primary"),
              xs=12, sm=12, md=3, lg=3, xl=3, # This sets the column width for different screen sizes
              ),
              dbc.Col(
                  my_table,
                  xs=12, sm=12, md=6, lg=6, xl=6, # This sets the column width for different screen sizes
              ),
              dbc.Col(
                  dcc.Markdown("right div", className="bg-primary"),
              xs=12, sm=12, md=3, lg=3, xl=3, # This sets the column width for different screen sizes
              ),

              ] ,className="g-0" #This allows to have no space between the columns. Delete if you want to have that breathing space
          )
      ])
```
      
## Advanced Styling with Dash Bootstrap Components

  - Introduction to [Dash Bootstrap themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/)
  - Most common [styling components](https://dashcheatsheet.pythonanywhere.com/)
    - me, ms, mt, nb
    - text color, background color, border color
    - etc. 
  - Dark them or light theme app

## Creating a component inside a callback
  - suppress_callback_exceptions

## Dynamic app layout
  - https://dash.plotly.com/live-updates#updates-on-page-load


## Styling DataTable

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
