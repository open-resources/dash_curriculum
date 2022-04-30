# Chapter 12  Advanced Styling and Layout
      
## Advanced Styling with Dash Bootstrap Components

  - Introduction to [Dash Bootstrap themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/)
  - Most common [styling components](https://dashcheatsheet.pythonanywhere.com/)
    - me, ms, mt, nb
    - text color, background color, border color
    - etc. 
  - Styling beyond DBC ("dbc offers you a lot, but for more customized styling you can use the `style` property in each dash component. For example `dcc.Markdown("App Title", style={'textAlign':'center'})`. To learn more go to this property see dash [docs](https://dash.plotly.com/layout#more-about-html-components)

## Advanced Styling of Dash DataTable

Recognizing that the DataTable is one of the most common Dash components, we'd like to show you a few examples on styling the DataTable, using a few DataTable properties, such as `style_cell`, `style_data_conditional`, `style_header`.

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

## Dynamic app layout (I can help write this part, Arne, once you're done with the first draft of this chapter)
  - https://dash.plotly.com/live-updates#updates-on-page-load

