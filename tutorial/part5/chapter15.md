# Chapter 15: Advanced Features of Multi-page Apps

## What you will learn
In this chapter we will build a more advanced multi page App, starting from the framework introduced in the previous chapter. We'll learn how to:
```{admonition} Learning Intentions
- Navigate the `page_registry`
- Customise several features of multi-page Apps such as: page name, order, meta tags
- Include images into multi-page Apps
```
By the end of this chapter, you'll be able to build the following App:

## 15.1 Advanced multi-page App Introduction
As a starting point for the chapter, let's start by building a multi-page App structure with all the knowledge from the previous chapter. Starting from this template, we'll be adding a couple of features in every section.

Our starting template is the following, you can download it [here](ch15_files/app_v1.zip) (the .zip file will need to be uncompressed):
![app_structure](ch15_files/app_baseline.gif)

The App structure consists in: 
- `app.py` file
- `assets` folder, which is currently empty
- `pages` folder with the following pages: `Home`, `Graphs`, `Extras`, `About`.

We want to build an App with a website-looking layout and therefore we've customised the `app.py` file in the following way:
- Our header is represented by a `dbc.Navbar` component containing the title of our App and one `dbc.NavLink` for each page in our registry. From the registry, we exclude one page ``if page["module"] != "pages.not_found_404"``. This is a default page that is used when the user tries to reach an invalid URL. In the next section we'll see how it works and how we can customise it.
- Below the header, we've included a `theme_toggle` which is a theme switcher. We've picked two themes from `dbc.themes` and the switcher will allow to switch between the two
- Note that when instatiating our `app`, we've enabled the `use_pages=True` option and used the `external_stylesheets` to define the default theme (which is `url_theme2`) together with enhanced fonts with the option `dbc.icons.FONT_AWESOME`.

The obtained `app.py` is the following:

````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
```
from dash import Dash, html
import dash_bootstrap_components as dbc
import dash
from dash_bootstrap_templates import ThemeSwitchAIO

# Configure Themes
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY
theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[url_theme2, url_theme1],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

# App
app = Dash(__name__, use_pages=True, external_stylesheets=[[url_theme2, dbc_css], dbc.icons.FONT_AWESOME])

header = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row([
                    dbc.Col(dbc.NavbarBrand("Multi page app | Advanced"))
                ],
                align="center"),
            href="/",
            style={"textDecoration": "none"}
            ),
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([
                        dbc.NavLink(page["name"], href=page["path"])
                        for page in dash.page_registry.values() if page["module"] != "pages.not_found_404"
                    ])
            ])
        ],
        fluid=True,
    ),
    dark=True,
    color='dark'
)

app.layout = dbc.Container([header, theme_toggle, dash.page_container], fluid=True)

if __name__ == '__main__':
	app.run_server(debug=False)
```

````

Each page code is very basic and will be enhanced in the following sections.

## 15.2 Default and Custom 404
Multi pages Apps include, by default, a landing page whenever the user tries to reach an invalid URL.
The default 404-page looks like the following:
![app_structure](ch15_files/app_404_default.gif)

The 404-page can be customised, in order to do so we need to create a new page which must be named `not_found_404.py` with the desired layout and it should be included into the `pages` folder.
Let's create the following 404 custom page and see it in use:
```
import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='Page not found'),

    html.Div(children='''
        This is a custom 404 page layout
    '''),
])
```
By adding this page into the `pages` folder from the app shown in the previous section, we will get the following:
![app_structure](ch15_files/app_404_custom.gif)

## 15.3 Navigating the page registry
Let's now examine the page registry.
The `dash_labs` module has a function called `print_registry()` which allows to print the registry into the terminal.

In the `extras.py` page from the App, we've used this function which is triggered by a button.
````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
```
import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc
from dash_labs import print_registry

dash.register_page(__name__)

layout = dbc.Container(
    [
    dbc.Row([html.H1(children='Extras')]),
    dbc.Row([html.H3(children='Visualising the App Registry')]),
    dbc.Row(
        [dbc.Col(dbc.Button(children="Print Registry to Console", id='print-reg'), width = 10)]
         ),
    dbc.Row(
        [html.P(id='res-')]
         )
    ],
    fluid=True
)

@callback(
    Output(component_id='res-', component_property='children'),
    Input(component_id='print-reg', component_property='n_clicks')
)
def print_reg(n):
    if n is not None:
        print_registry(exclude="layout")
        return 'Check the console'
```

````
If we then examine the page registry into the terminal, we will see the following output (for each page of the App; we've just included a couple of pages in the screenshot):

![printregistry](ch15_files/print_registry.png)

As we can see, the registry stores a lot of information for each page, let's focus on some properties (for the full list, [click here](https://dash.plotly.com/urls#dash.register_page())):
- `path`: is the URL of the page. We can see that the homepage has url '/'.
- `name`: name of the page to be displayed in the URL. If null, the app filename will be used.
- `order`: the order of the pages in our App. The page with path '/' will receive order 0, then the remaining pages are sorted alphabetically. This is why, if we look at our App, we can see that the pages are sorted alphabetically (after Home) in the navbar.
- `title`: name of the page to be displayed into the browser tab. If null, the app filename will be used.
- `description` and `image` are extra properties that, if specified, allow to add meta information to our App URL when shared. `image` should contain the image filename located into the assets folder.
- the registry also contain the full `layout` of each page. We've disabled the print out of this property by calling the function in this way: `print_registry(exclude="layout")`

When we register each page of our app with the `dash.register_page()` function, we can define the above properties and improve our App. Let's see some examples.

## 15.4 Customising multi-page name and order
By looking at the App we have so far, we notice that the order of pages is alphabetical (after Home) and that our pages are named after the respective .py filenames.
However, our Graph filename contains some versioning (hence the page name `Graphs v2 fin`). This doesn't look professional, but can be easily adjusted by properly calling the `dash.register_page()` function.

We can obtain a much better result by specifying the following props when calling `dash.register_page(__name__)` for each page. In the version of the app displayed below, we've introduced the following adjustments for each page:
- pages/home.py : `dash.register_page(__name__, path='/', order='0', name='Home', title='Home')`
- pages/about.py : `dash.register_page(__name__, order='3')`
- pages/extras.py : `dash.register_page(__name__, order='2')`
- pages/graphs_v2_fin.py : `dash.register_page(module = __name__, order='1', name='Graphs', title='Dash App | Graphs')`. In the gif below, pay attention to the name displayed in the navbar and the name displayed into the browser tab for this page. This is the difference between `name` and `title` props

![app_structure](ch15_files/app_fix01.gif)

## Content:
- Show and describe the following App as the baseline
- Go through the following enhancements to the app:
  - Creation of a button which print out the registry on the console and examine it
  - Add assets folder with images and show them
  - Rename URLs
  - Sort pages differently (e.g. Graph page before Extras)
  - Add a meta tag example


