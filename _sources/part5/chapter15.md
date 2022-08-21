# Chapter 15: Advanced Features of Multi-page Apps

## What you will learn
In this chapter we will cover more advanced features of Dash Pages, as we build a professional multi-page App.
```{admonition} Learning Intentions
- Add a custom 404 page
- Navigate the `page_registry`
- Customise order of pages, title and urls
- Include meta tags
```

By the end of this chapter, you'll be able to build this app:

![app_structure](ch15_files/app_baseline.gif)

[Click to download the complete code file for this chapter](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part5/ch15_files/app_vfin.zip?raw=true).

```{attention} 
To run this app successfully, you will need to install the `dash_bootstrap_templates` and the `dash-labs` packages.

> pip install dash-bootstrap-templates

> pip install dash-labs
```

## 15.1 Default and Custom 404
Multi pages Apps include, by default, a landing page whenever the user tries to reach an invalid URL.
The default 404-page looks like the following:
![app_structure](ch15_files/app_404_default.gif)

However, the 404-page can be customised. In order to do so, we need to create a new file named `not_found_404.py` inside the pages folder and add the desired layout content.

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

Then, by adding the below line of code to the `app.py` file, we ensure that the 404 page does not show up as a link in the navbar. 

`for page in dash.page_registry.values() if page["module"] != "pages.not_found_404"`

Now, run the app, and try to type a fake name in the url to see the new 404 page displayed:

![app_structure](ch15_files/app_404_custom.gif)

## 15.2 Navigating the page registry
The `dash_labs` module has a function called `print_registry()` which allows to print the registry into the terminal to see the meta data of each registered page.

Un-hashtag the below line of code in the `apps.py` file, and rerun your app.

`print_registry(exclude="layout")`

If you examine your terminal, you will see the following output (we've included only a couple of pages in the screenshot. The complete output includes the same properties for every page):

![printregistry](ch15_files/print_registry.png)

As we can see, the registry stores a lot of information for each page, let's focus on some properties ([see the docs for the full list](https://dash.plotly.com/urls#reference-for-dash.register_page))

- `path`: is the URL of the page. We can see that the homepage has url '/'.
- `name`: name of the link. If null, the app filename will be used.
- `order`: the order of the pages in the app - commonly used when creating the page links in the app.py file (Navlink in our case). If order of pages is not supplied, the page with path '/' will receive order 0, then the remaining pages are sorted alphabetically.
- `title`: name of the page to be displayed into the browser tab. If null, the app filename will be used.
- `description` and `image` are extra properties that, if specified, allow the adding of meta information to our App URL when shared. `image` should contain the image filename located into the `assets` folder. We'll see an example of this feature later.


## 15.3 Customising multi-page order
By looking at the App we have so far, you'll notice that the order of the links in the Navbar are Home, Graphs, and About, from left to right. This is because we assigned the number 0 to the `order` propertye of the home.py file, the number 1 to the graphs_v2_fin.py file and the number 2 to the about.py file. Had we chosen not to supply an order, the app would have displayed the pages in an alphabetical order: "Home" first since it's the home page, "About" second, and "Graphs" third.

Here's what the current app looks like: 
- pages/home.py : `dash.register_page(__name__, path='/', order='0')`
- pages/about.py : `dash.register_page(__name__, order='2')`
- pages/graphs_v2_fin.py : `dash.register_page(module = __name__, order='1')`

Get your feet wet. Try to change the order of the home page so it appears last (far right) in the Navbar. 


## 15.4 Customising names, titles, and URLs of pages
Our App can be further improved by renaming several elements of the app. To modify the name of the page that appears on the browsers tab, you will need to assign the desired name to the `title` property of the page registry. To 

. By looking at the Navbar, we can see that our pages are named after the respective .py filenames.
However, our Graph filename contains some versioning (hence the page name "Graphs v2 fin"). This doesn't look professional, but can be easily adjusted: we can obtain a much better result by specifying the following props when calling `dash.register_page(__name__)` for each page. 
In the version of the app displayed below, we've introduced the following adjustments for some pages:
- pages/home.py : `dash.register_page(__name__, path='/', order='0', name='Home', title='Home')`
- pages/graphs_v2_fin.py : `dash.register_page(module = __name__, order='1', name='Graphs', title='Dash App | Graphs')`.

In the gif below, pay attention to the name displayed in the navbar and the name displayed into the browser tab for each page. This is the difference between `name` and `title` props and it is particularly evident for the "graphs" page:

![app_structure](ch15_files/app_fix02_names.gif)

Now try this yourself: go into the pages files and update the `title` and `name` props with other values.

## 15.5 Updating the default `pages` directory
We can further customise our app by renaming the folder which contains all pages. By default, the folder should be named `pages`, however, we can simply specify a custom name when instantiating our `app`.
Let's suppose we want to rename the folder to `app sections`. We can do so by using the `pages_folder` prop when instantiating:
`app = Dash(__name__, use_pages=True, external_stylesheets=[[url_theme2, dbc_css], dbc.icons.FONT_AWESOME], pages_folder='app sections')`.

```{note}
When renaming the `pages` directory, all parts of the code which are using the `pages` folder should be updated with the new name. An example of this is the code used in our template to build the `Navbar`. When we rename the folder, we should also change our code
- from: `for page in dash.page_registry.values() if page["module"] != "pages.not_found_404"`
- to: `for page in dash.page_registry.values() if page["module"] != "app sections.not_found_404"`
```

## 15.7 Metatags
When sharing the link to a page of our app (on chat app or social networks), it is possible, thanks to metatags, to display a card with a preview of our page consisting of: a `title`, a `description` and an `image`.
To test this feature, we would need the app to be published; here's an example of a published app which includes metatags: [example of metatags](https://www.trainerhill.com/blog/power-creep).

![metatags_example](ch15_files/metatags_example.jpg)

Metatags information can be specified by customising the `dash.register_page()` call of each page. In particular, we can specify:
- a `title`, like we did above
- any textual `description`
- an `image`, which should contain the filename of the image we would like to include into our metatags and which should be placed into the `assets` folder of our app.
So, if we write: 
```
dash.register_page(module = __name__,
		order='1',
		name='Graphs',
		title='Dash App | Graphs',
		description='Graphs of several analyisis of the gapminder dataset.',
		image=graph_preview.png)
```
then we would need to have an image file called  `graph_preview.png` into our `assets` folder.

## 15.X Advanced multi-page App Introduction
As a starting point for the chapter, let's build a multi-page App structure with all the knowledge from the previous chapter. We'll build on this template, by adding a couple of features to it in every section of this chapter.

The template is the following, you can download it [here](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part5/ch15_files/app_v1.zip?raw=true) (the .zip file will need to be uncompressed):
![app_structure](ch15_files/app_baseline.gif)

The App structure consists in: 
- `app.py` file
- `assets` folder, which is currently empty. This is where pictures, media files, and style sheets might be stored
- `pages` folder with the following pages: `Home`, `Graphs`, `Extras`, `About`.

We want to give this app a more professional look; therefore we've customised the `app.py` file in the following way:
- Our header is represented by a `dbc.Navbar` component containing the title of our App and one `dbc.NavLink` for each page in our registry. From the registry, we exclude one page ``if page["module"] != "pages.not_found_404"``. This is a default page that is used when the user tries to reach an invalid URL. In the next section we'll see how it works and how we can customise it.
- Below the header, we've included a `theme_toggle` which allow to switch between two themes. We've picked two themes from `dbc.themes` (tipically a dark and a light one) and the switcher will allow to switch between the two.
- Note that when instantiating our `app`, we've enabled the `use_pages=True` option and used the `external_stylesheets` to define the default theme (which is `url_theme2`) together with enhanced fonts with the option `dbc.icons.FONT_AWESOME`.

**App.py file:**

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

## Summary
In this chapter, we have gone through several features that are specific to multi page apps. There are additional functionalities and examples that can be found in the [Dash documentation](https://dash.plotly.com/urls).

This also concludes the section dedicated to multi page apps.
