import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

dropdown =  dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
        ],
        nav=True,
        label="More Pages",
        align_end=False,
    )

app.layout = dbc.Container(
    [dropdown, dash.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
