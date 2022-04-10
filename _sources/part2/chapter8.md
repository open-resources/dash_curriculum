# Chapter 8: Data Visualization

```{admonition} What you will learn

- Principles of Effective Visualizations
- How to incorporate a Plotly Figure Object in your Dash App.
- How Plotly Express (`px`) is the preferred way to create a Plotly Figure Object.
- An introduction to the powers of `px`.
- How `px` uses attributes such as `color` and `symbol` to illustrate multiple dimensions of a dataset.
- How `px` uses the attributes `animation_frame` and `animation_group` to create animations.
- How to create chart types like  `line`, `scatter`, `bar`, `histogram`, `box`, `facet`, `maps` and`treemap`.

```
## 8.1 Principles of Effective Visualizations

`Firas`

## 8.2 Incorporting Plotly Figures in a Dash app

We've earlier talked about how a `dbc.Col` component resides in a `dbc.Row` component and serves as a wrapper for other components. One such component can be a `dcc.Graph()` component, which in turn is a wrapper (is this a correct description?) for a Plotly figure object in `figure = fig`:

```python
app.layout = dbc.Container([dbc.Row(dbc.Col(dcc.Graph(id='figure1', figure=fig), width = 4))])
```

There's almost no end to what such a figure object can be as we'll describe in more detail in a bit. But as an example of how to include figures in your dash APP, consider the following snippet where we load a dataset from `px.data.gapminder()` and make a figure with `px.line()`. The function call `px.line()` in this snippet will contain attributes and arguments that you will learn more about in the following subsections.

### 8.2.1 How to create a Plotly Express Figure for your Dash APP

```python
df = px.data.gapminder()
df = df[df['country'].isin(['Canada', 'Brazil', 'Norway', 'Germany'])]

# figure
fig = px.line(df, x= 'year', y = 'lifeExp', color = 'country',
                  symbol = 'continent',
                  title = "PX line plot",
                  template = 'plotly_white'
                  )
fig.show()
```

[![enter image description here][1]][1]

### 8.2.2 How to incorporate the Figure in your Dash APP

This figure can then be incorporated in the following snippet that loads a dataset, creates a Plotly Figure object, and displays it in a Dash app.

### Complete code

```python
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
import dash_bootstrap_components as dbc

# data
df = px.data.gapminder()
df = df[df['country'].isin(['Canada', 'Brazil', 'Norway', 'Germany'])]

# figure
fig = px.line(df, x= 'year', y = 'lifeExp', color = 'country', symbol = 'continent',
                  title = "PX line plot",
                  template = 'plotly_white'
                  )

# Dash App
app = dash.Dash()

# App Layout 
app.layout = dbc.Container([dbc.Row(dbc.Col(dcc.Graph(id='figure1', figure=fig), width = 4))])

app.run_server(debug=True, use_reloader=False)
```

### App

[![enter image description here][2]][2]

The following sections will show you how you can put almost any type of figure in a Dash App using Plotly Express

### Should we have a callback here as well !?!

## 8.3 Introduction to the powers of Plotly Express

The [plotly.express module][3] (usually imported as px) contains functions that can create entire figures at once, and is referred to as Plotly Express or `px`. Plotly Express is a built-in part of the plotly library, and is the recommended starting point for creating most common figures like [line][4], [scatter][5], [bar][6],  and [timeline][7] figures. We'll go through some of them in this chapter, and you can study more in the docs. But first, let's unveil the powers you can unleash with a multi-dimensinal dataset like `px.data.gapminder()` and a simple plotly express function like `px.line()`

### 8.3.1 About the gapminder dataset

The gapminder dataset available through `px.data.gapminder()` is provided by [Gapminder.org][8]. Here you'll find `1704` rows of data and the following columns `['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap' 'iso_alpha', 'iso_num']`. Life expectancy at birth is stored in `lifeExp`, population by country is `pop`, and `gdpPercap` is the per capita GDP. The data is an excerpt of data found in specific spreadsheets on [Gapminder][8] circa 2010. The data has a so-called long (or  tidy) format. Long-form data has one row per observation, and one column per variable. This is suitable for storing and displaying multivariate data (more dimensions than 2). 
PX also handles data of [other formats][9].


### 8.3.2 A basic line chart with `px.line()`


As a minimal example, consider life expectancies in Canada in a period from 1962 to 2007:

[![enter image description here][10]][10]


This figure is produced using only these lines of code where the most essential part is [`px.line()`][11]:

```python
import plotly.express as px
import pandas as pd

# sample data 
df = px.data.gapminder()

# data subset 1
df = df[df['country'].isin(['Canada'])]

# 8.1.1 line chart
fig = px.line(df, x= 'year', y = 'lifeExp',
                  title = "PX Line plot",
                  template = 'plotly_white'
                  )
fig.show()
```

Let's look at the applied arguments of `px.line()` one by one.

1. `df` is a reference to the imported dataset.
2. `x='year'` defines the `year` column in `df` to appear on the x-axis
3. `y='lifeExp` defines the `lifeExp` column in `df` to appear on the y-axis
4.  `title = "PX Line plot"` is optional, and creates a title in the top left corner.
5. `template = 'plotly_white'` is also optional, and creates a minimal figure layout with a white background.

```{tip}
You do not *have* to use the setup above with `fig = px.line([...])`. Just calling `px.line([...])` without the assignment to `fig` will also produce a [Plotly Graph Object](https://plotly.com/python/graph-objects/). Depending on your IDE, this function call will also display the figure. However, running `fig = px.line([...])` is considered standard notation (?) and will make the figure available for further editing and methods like `fig.show()`
```


### 8.3.3 Adding multiple lines with different colors
So far so good, but the dataset includes data for a lot more countries that could be brought into the light. The way you add data from another country can seem a bit strange at first, but it's also an important part of what makes Plotly Express so powerful and flexible. The following figure is produced by the snippet below where we've included some other countries in the dataset with `df = df[df['country'].isin(['Canada',  'Norway', 'Germany'])]`

[![enter image description here][12]][12]

```python
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# sample data
df = px.data.gapminder()

# data subset 2
df = df[df['country'].isin(['Canada',  'Norway', 'Germany'])]

# 8.2.1 Line chart
fig = px.line(df, x= 'year', y = 'lifeExp', color = 'country' 
                  title = "PX line plot",
                  template = 'plotly_white'
                  )
fig.show()
```

In addition to the already existing arguments, we've added `color = 'country'`. And this is exactly what you need to make an addition of lines to a larger set of countries. What happens under the hood, is that Plotly Express assigns a color from a certain [color sequence][13] to each unique value in the `country` column in `df` which are: `['Canada', 'Germany', 'Norway']`.



```{warning}
Without the color argument, an assignment of the y-axis to a multivariable column will create a [mess of a chart](https://i.stack.imgur.com/uS3TP.png) where all lines are blue, and the end-point of one line is connected to the starting point of another. How this appears is likely to be prone to changes for future versions of Plotly Express.
```

### 8.3.4 The interactivity of Plotly Figure Objects.
With `color = 'country'` initialized, a legend is also produced to let you know which line represents which country. The legend is interactive and lets you toggle the lines on and off.

[![enter image description here][14]][14]

Both axes also have interactive functionalities that depend on where you click on the axes. If you, for example, grab the middle of the `y-axis`, the complete axis will slide when you move the mouse. If you grab the top of the axis, all other than the minumum value will change, and vice versa.

[![enter image description here][15]][15]


### 8.3.5 Multidimensional data with lines and markers

You can combine lines *and* markers in `px.line()` to illustrate multiple dimensions of your dataset through the addition of the `symbol` argument. Below we've included `symbol = 'continent'` to our previous `px.line()` call. This works much like `color = 'country'`. But this time, we're applying a symbol sequence to the unique values in `df['continent']` which are `'Americas'` and `'Europe'`. The symbols assigned are `['Circle', 'Diamond']`:

[![enter image description here][16]][16] 

```python
import plotly.express as px
import pandas as pd

# sample dataset from plotly express
df = px.data.gapminder()

# subset 2
df = df[df['country'].isin(['Canada',  'Norway', 'Germany'])]

fig = px.line(df, x= 'year', y = 'lifeExp', color = 'country', symbol = 'continent',
                     title = "Multidimensional data",
                     template = 'plotly_white')
fig.show()
```

### 8.3.6 Scatter Charts with `px.scatter`

The only thing you have to do to drop the lines in our first figures and show markers only, is to replace the `px.line()` call with `px.scatter()` and otherwise use the same arguments.


[![enter image description here][17]][17]

```python
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# sample dataset from plotly express
df = px.data.gapminder()

# subset 2
df = df[df['country'].isin(['Canada',  'Norway', 'Germany'])]

fig = px.scatter(df, x= 'year', y = 'lifeExp', color = 'country', 
                     title = 'PX scatter plot',
                     template = 'plotly_white')
fig.show()
```

### 8.3.7 Animated Scatter / Bubble charts

`line_dash` is another argument that can illustrate dimensions of a dataset. But where things get really interesting is when you apply multiple settings like `animation_frame="year"`, `animation_group="country"` and `size="pop"`. The complete snippet below will create an interactive, animated chart that illustrates both life expectancies, GDP per capita and populatoin for a multitude of countries accross several continents through multiple years.

```python
import plotly.express as px
df = px.data.gapminder()
px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country", size="pop", color="continent", hover_name="country", log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
```

[![enter image description here][18]][18]

```{tip}
The snippet above introduces several new methods of the `fig` object. We won't go more into details here, but you can use them closer with `help(px.scatter)` and in the [docs](https://plotly.com/python/px-arguments/)

```

```{tip}

Some IDEs from time to time encounter probblems with running the animations of Plotly even if the figure itself has been produced. If this happens to you, try including the following snippet in your code. Take a look at [this post](https://github.com/microsoft/vscode-jupyter/issues/4364) for more details: 

```python
import plotly.io as pio
pio.renderers.default = 'notebook_connected'
```

## 8.4 A variety of Plotly Express figures

Now that you've got a sense of the powers hidden in all Plotly figures, the time has come to introduce more categries than line and scatter plots. We will not go into the details of every argument of every function call since you already know the main principles:


```{admonition} Main principles of PX
1. Defining a dataset `df` let's you reference all available variables in the function arguments
2. You can illustrate multiple dimensions of the dataset through variables like `color`, `symbol`.
3. You can create animations through arguments like `animation_frame` and `animation_group`
```

One thing all following chart types have in common, is that we're using the very same dataset and that very little data wrangling is required. The few data wrangling techniques that are used are only there because some chart types require a specific data format, or simply look better with a smaller subset of the gapminder dataset.

### 8.4.1 Stacked bar chart with `px.bar()`

`px.bar()` works similarly to `px.line()` in that it uses `color = country` the very same way. By default, each colored category is stacked on top of eachother for each unique occurence of `year` on the `x-axis`.

```python
import plotly.express as px
df = px.data.gapminder()

fig = px.bar(df, x= 'year', y = 'pop', color = 'country',
                     title = 'PX scatter plot',
                     template = 'plotly_white')
fig.show()
```

[![enter image description here][19]][19]



### 8.4.2 Grouped bar chart
Stacking the bars makes sense to illustrate accumulations for data such as `population`. But not so much for life expectancies. In order to group subcategories next to eachother instead, simply include `barmode = 'group'` in the function call.

```{tip}

Not all Plotly Express functions produce perfect layout for every dataset every time. Below we've used antoher method of the `fig` object before `fig.show()` to adjust the range of the y-axis; `fig.update_yaxes(range=[50, 80])`. Try the code snippet without that particular line and see if you agree with our design choices.

```

```python
import plotly.express as px
df = px.data.gapminder()
df = df[df['country'].isin([
    #    'France', 'Germany', 

    #    'Italy',
       'Spain', 'United Kingdom'])]

fig = px.bar(df, x= 'year', y = 'lifeExp', color = 'country',
                     barmode = 'group' ,
                     title = 'Grouped Bar Chart',
                     template = 'plotly_white')
fig.update_yaxes(range=[60, 80])
fig.show()
```

[![enter image description here][20]][20]



### 8.4.3 Histogram with `px.histogram()`

Histograms can be considered as a special kind of bar chart where the bars represent  groups of data instead of individual observations. By default, `px.histogram()` will also stack categories on top of eachother. To prevent that, and rather display distributions of data individually, jsut inclue `barmode = 'overlay'` as you can see in the snippet below.

```python
import plotly.express as px
df = px.data.gapminder()
df = df[df['continent'].isin(['Asia',  'Europe'])]
fig = px.histogram(df, x='lifeExp', nbins = 20, color = 'continent', barmode = 'overlay')
fig.show()
```

[![enter image description here][22]][22]

### 8.4.4 Box plot with `px.box()`

`po.box` lets you investigate distributions of data further. By default, `px.bar()` displays `mean`, `quartiles` and some `outliers` for the different categories in the order that they appear in the dataset. In the following example we've included the argument `category_orders` to display means for each group in a decreasing manner.

```python
import plotly.express as px
df = px.data.gapminder()

fig = px.box(df, x="continent", y="lifeExp",
             category_orders = {'continent': ['Oceania', 'Europe', 'Americas', 'Asia', 'Asia', 'Africa']})
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
fig.show()

```

[![enter image description here][21]][21]


### 8.4.5 Facet / Trellis plots

This section uses a new argument that splits a dataset into several subplots; `facet_col`. `facet_col_wrap` defines in how many columns you would like to organize your subplots.

```python
import plotly.express as px
df = px.data.gapminder()

# data subset
df = df[df['continent'].isin(['Europe',  'Americas', 'Asia'])]
df = df[df['year']>1962]

fig = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent', size='pop',
                facet_col='year', facet_col_wrap=3)
fig.show()
```

[![enter image description here][23]][23]

### 8.4.6 Treemap with `px.treemap()`

```python
import plotly.express as px
import numpy as np
df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=[px.Constant('world'), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'])
fig.show()
```

[![enter image description here][24]][24]


### 8.4.7 Heatmap with `px.density_heatmap()`

```python
import plotly.express as px
df = px.data.gapminder()
df = df[df['gdpPercap']<60000]
fig = px.density_heatmap(df, x="gdpPercap", y="lifeExp",
                        nbinsx=20, nbinsy=20, color_continuous_scale="Viridis")
fig.show()
```

[![enter image description here][25]][25]



### 8.4.8 Choropleth map with `px.choropleth()`

```python
fig = px.choropleth(gapminder, locations='iso_alpha', color='lifeExp', hover_name='country', 
                    animation_frame='year', color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
fig.show()
```

[![enter image description here][26]][26]


### 8.4.9 Timeline with `px.timeline()`

Timeline or GANTT charts often describe start and end points of events or tasks. In the following example, we've made a few changes to the gapminder dataset and removed some random dates. You can use this code snippet to illustrate what time periods that you have available data for a set of countries. Missing years *within* a time period are not taken into account.

```python
import plotly.express as px
import pandas as pd
import numpy as np

# data
df = px.data.gapminder()
df = df[df['country'].isin([
       'France', 'Germany', 
       'Sweden', 'Finland',
       'United Kingdom'])]
df = df.reset_index()

# instructions to drop random observations
np.random.seed(12)
remove_n = int(len(df)*0.6)
drop_indices = np.random.choice(df.index, remove_n, replace=False)
df = df.drop(drop_indices)

# pivot to country in column names, integer as index, and years as values
dfp = df.pivot(index='index', columns='country', values='year')
dfp = dfp.agg(['min','max'])
dfp = dfp.astype(int)
df = dfp.T
df = df.reset_index()
df = df.astype(str)

fig = px.timeline(df, x_start="min", x_end="max", y="country")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()
```

[![enter image description here][27]][27]

```{tip}
You can set Plotly to be the [plotting backend for pandas](https://stackoverflow.com/questions/66664935/plotly-how-to-make-different-plots-using-plotly-as-a-plotting-backend-for-panda/66664937#66664937), and produce Plotly Figures with `df.plot(kind)` where `kind` can be any of ` ['scatter', 'line', 'area', 'bar', 'barh', 'hist', 'box', 'violin', 'strip', 'funnel', 'density_heatmap', 'density_contour', 'imshow']`. This is a nice way to quickly explore more Plotly Express graphing options. Run the following snippet to see 11 different options.

```python
import random
import pandas as pd

random.seed(123)
df = pd.DataFrame({'x':[1,2,3,4,5,6]})
pd.options.plotting.backend = "plotly"

kinds = ['scatter', 'line', 'area', 'bar', 'barh', 'hist', 'box', 'violin', 'strip', 'funnel', 'density_heatmap', 'density_contour', 'imshow']

for k in kinds[:-1]:
    fig = df.plot(kind=k, title = k)
    fig.update_layout(title = dict(font=dict(color='#EF553B')))
    fig.show()
```


## 8.5 References and resources (more links at end of document)

https://www.kaggle.com/code/jhossain/explore-the-gapminder-dataset-with-plotly-express/notebook

https://cran.r-project.org/web/packages/gapminder/README.html

***More resources listed as links at the very end of the document***


```{admonition} Summary??


```

#########################################

---
# OUT-TAKES from round2 20220401
---

***...some initial thoughts...*** 

```{tip}

**Chapter 7 should(?) include the following:**

- data formats: long, wide and mixed
- Plotly express accepts all formats, but Long (tidy) format often best
- `pd.melt()` at the very least (wide to long)
- `pd.pivot()` (long to perhaps...
- subsetting dataframes, of course...
```

```{warning}

With quick transitions between lines of code, code snippets, text and figures, should we agree upon a special writing style in this regard?
```

***Style example 1:***

With the following addition, you'll get the result i the figure below:

```python
fig.update_layout(barmode = 'group')
```

[![enter image description here][28]][28]

***Style example 2:***

Just add

```python
fig.update_layout(barmode = 'group')
```

and you'll get:

[![enter image description here][28]][28]

## 8.2.1 Line chart



```python
import plotly.express as px
df = px.data.gapminder()
px.line(df, x= 'year', y = 'lifeExp', color = 'country', symbol = 'continent', template = 'plotly_white')
```

[![enter image description here][29]][29]

The current dataset is of a so-called long (or tidy) format:

[![enter image description here][30]][30]

***...needs more explaining if not covered in chapter 7...***

As you can see from the function call above, `color` and `symbol` don't take actual colors and symbols as  arguments, but rather columns of a dataset `df` from which unique values are assigned certain color and symbol sequences.

## 8.2.2 Scatter plot

You can drop the lines and produce a scatter plot with markers only if you substitute `px.line()` with `px.scatter()`:

[![enter image description here][31]][31]

```python
fig = px.scatter(df, x= 'year', y = 'lifeExp', color = 'country', symbol = 'continent', template = 'plotly_white')
```
## 8.2.3 Scatter plot with trendlines


From here you can also add a trendline for each trace by adding `trendline="ols"` to the mix:

[![enter image description here][32]][32]

In this case, the trendlines will indicate the increase in life expectanciese for each country over the years.

## 8.2.4 Regression - A special case of scatter plot

In order to compare a relationship between two specifc variables, you would have to wrangle the dataset a little so that you can assign individual sereis to `x` and `y`. But this is pretty straight-forward with `pd.pivot` like this

```python
df.pivot(index='year', columns='country', values='lifeExp')
```

### From long to wide with `pd.pivot()`

[![enter image description here][33]][33]

As you can see, the dataset is no longer of a long format. With column names that now describe unique variables instead of a category, we've moved on to a dataset with a wide format.

The complete setup to produce the figure below is now:

```python
df = df[df['country'].isin(['Canada', 'Germany'])]
dfp = df.pivot(index='year', columns='country', values='lifeExp')

fig = px.scatter(dfp, x= 'Canada', y = 'Germany',
                     trendline = "ols",
                     trendline_color_override="red",
                     title = "PX regression, life expectancies in Canada and Germany",
                     template = 'plotly_white')
fig.show()
```

[![enter image description here][34]][34]

```{tip}

You can retrieve regression results with `px.get_trendline_results(fig)` and include them in your figure as explained in [Fitting multiple lines and retrieving the model parameters][14]

```


## 8.2.4 Bar plot

So far, we've looked at chart types that are closely related in how they are structured. Bar charts are also widely used and introduces a few features that work a bit differently. Let's take a look at the populations in two different countries.

```python
fig = px.bar(df, x= 'year', y = 'pop', color = 'country',
                 
                     title = 'PX scatter plot',
                     template = 'plotly_white')
# fig.update_layout(barmode='group')
fig.show()
```

[![enter image description here][35]][35]

As you can tell from the figure, you can now study the change in the total populations of these countries over the years. This makes sense for `population`, but not so much if you were to study life expectancies. In the latter case it would make more sense to display the bars for each country next to each other. The following section will introduce how to edit the `barmode` attribute for the figure object both in the function call and *after* you've produced the figure.

## 8.2.5 How to edit chart features

By default `px.bar()` uses `barmode = 'stacked'` which does exactly what it says, namely stacking the populations for each `country` (discerned by `color`) on top of each other. But you can change this behavior through `barmode = 'group'` and get the following result:

[![enter image description here][36]][36]

```python
fig = px.bar(df, x= 'year', y = 'pop', color = 'country',
                     barmode = 'group' ,
                     title = "PX Bar plot with barmode = 'group'",
                     template = 'plotly_white')
fig.show()
```
Another option is to make use of one of the many methods of the `fig` object itself, namely:

```python
fig.update_layout(barmode = 'group')
```


.

---
# OUT-TAKES from initial suggestion
---




## 8.1.1 Breakdown of `px.line()` and relation to Plotly Graph Objects

Running [`px.line()`][4] will produce a [Plotly Graph Objects][37] figure object `go.Figure` (where `go` is the commonly used alias for `plotly.graph_objects`) which is one of the main building blocks of the Plotly library; the canvas (better to call it something else?). Running `go.Figure()` will produce a completely empty figure or canvas like this:
```python
import plotly.graph_objects as go
go.Figure()
```

[![enter image description here][38]][38]

What we're looking at here is a figure template with a few defined settings. We've got an x and an y-axis as well as white gridlines for both axes on a light-blue background. We can take a closer look at the underlying settings with `fig.show` that will reveal this dictionary:

```python
{
    'data': [], 'layout': {'template': '...'}
}
```

So at its core, a figure object is built up by a `data` and  `layout` element. As you'll soon learn, there are endless ways to construct a Plotly figure. But building on this basic example, you will have to populate the data attribute through the addition of traces, like a [`go.Scatter()`][39] trace (more on this and other options?). You can also edit the layout through [`go.Layout()`][40]. Below is an example where the dataset `x= [1,2,3,4]` and `y = [10,11,12,13]` is added to the empty canvas. We'll also specify a figure title.

```python
fig = go.Figure(data = [go.Scatter(x= [1,2,3,4], y = [10,11,12,13])],
                layout = go.Layout(title = 'My first Plotly figure'))
fig.show()
```

[![enter image description here][41]][41]

Now, if you run `fig.show` again, you'll see that our figure object is a bit more populated:

```python
{
    'data': [{'type': 'scatter', 'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13]}],
    'layout': {'template': '...', 'title': {'text': 'My first plotly figure'}}
}
```

The `layout` now has another dictionary:

```python
'title': {'text': 'My first plotly figure'}
```

And `data` has a list with one trace element:

```python
'data': [{'type': 'scatter', 'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13]}]
```

```{tip}
Notice how we've used both `fig.show()` and `fig.show` with and withou the parantheses at the end. The latter let's you study the content of the figure object while the former displays a visual representation of the figure.
```

## 8.1.2 Plotly Figure object methods
The figure object has numerous useful methods that you can study through `dir(fig)`. One of them, `fig.add_traces()`, adds new data to an already existing figure object, and works much in the same way as `go.Figure()` in that you'll have to specify a trace category as well. Below we'll use `fig.add_traces(go.Scatter())` to add another line to our lineplot.

    fig = go.Figure(data = go.Scatter(x= [1,2,3,4], y = [10,11,12,13]),
                    layout = go.Layout(title = 'My first Plotly figure with an extra trace'))
    fig.add_traces(go.Scatter(x= [1,2,3,4], y = [11,12,13,14]))
    fig.show()

[![enter image description here][42]][42]

Aside from the new trace, you'll see that the figure now also displays a legend as well as some default names for the different traces. The names of the traces aren't that interesting yet since we haven't specified any names.

## 8.1.3 DataFrames as data source

It's much more common to work with a pandas dataframe as your data source rather than individual lists. So let's apply some of the things we've learned in the previous chapter (depends on the content of chapter 7) and organize our data in a `df` like this:

    df = pd.DataFrame({'x':  [1,2,3,4],
                       'y':  [10,11,12,13],
                       'y1': [11,12,13,14]}
    )

Now we can reproduce the figure above with:

```python
fig = go.Figure(data = go.Scatter(x= df['x'], y = df['y']),
                layout = go.Layout(title = 'My first Plotly figure with an extra trace'))
fig.add_traces(go.Scatter(x= df['x'], y = df['y1']))
fig.show()
```

Notice the slight difference in how we specify the `y-values` for the second trace in the examples above. With `fig.add_traces(go.Scatter(x= [1,2,3,4], y = [11,12,13,14]))` there wasn't a problem with `y = [11,12,13,14]` since `go.Scatter()` would add that trace to the figure regardless of whether other traces had specified values for the same `y-axis`. But since a pandas dataframe requires uniqe column names, we had to specify `'y1': [11,12,13,14,]` in `pd.DataFrame()`. We can study this closer if we take another look at `fig.show` and the part with `'y1': [11, 12, 13, 14]`.

```python
{
    'data': [{'type': 'scatter', 'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13]},
                {'type': 'scatter', 'x': [1, 2, 3, 4], 'y1': [11, 12, 13, 14]}],
    'layout': {'template': '...', 'title': {'text': 'My first Plotly figure'}}
}
```

`'layout'` is still the same, but more importantly we can see that `'data'` now contains a list with **two** traces complete with data and a `type` description. And that's exactly what `fig.add_traces()` does; it just puts another `trace` into the `data` of an already existing figure.

## 8.1.4 Easy data handling with Plotly Express
As you can imagine, having to add a new line with `fig.add_traces(go.Scatter))` for each and every trace of data we'd like to include would quickly become very tedious. And this leads us right back to the start of this section. Using `px.line()` we don't have to worry about `go.Figure()`, `fig.add_traces()` or `go.Scatter()` at all. We can just create *almost* the very same figure through:

```python
fig = px.line(df, x='x', y = ['y', 'y1'], title = 'My first Plotly Express figure')
fig.show()
```

And as you can see, *almost* the same figure doesn't mean that it's *almost* as good as the previous figure. On the contrary, `px.line()` improves the readability of the figure through the assignment of trace names in the legend, and adding names to the axes:

[![enter image description here][43]][43]

## 8.1.5 Inspect the structure of a `px.line()` figure

There's even more happening under the hood if we take another look at the output from the current `fig` object with `dir(fig)`. (The output is quickly growing in size, so we'll reproduce the most relevant parts here).

```python
'data': [{'hovertemplate': 'variable=y<br>x=%{x}<br>value=%{y}<extra></extra>',
          'line': {'color': '#636efa', 'dash': 'solid'},
          'marker': {'symbol': 'circle'},
          'mode': 'lines',
          'showlegend': True,
          'type': 'scatter',
          'x': array([1, 2, 3, 4], dtype=int64),
          'xaxis': 'x',
          'y': array([10, 11, 12, 13], dtype=int64),
          'yaxis': 'y'},
          {<trace number 2>}],

'layout': {'legend': {'title': {'text': 'variable'}, 'tracegroupgap': 0},
           'template': '...',
           'title': {'text': 'My first Plotly Express figure'},
           'xaxis': {'anchor': 'y', 'domain': [0.0, 1.0], 'title': {'text': 'x'}},
           'yaxis': {'anchor': 'x', 'domain': [0.0, 1.0], 'title': {'text': 'value'}}}
```

By now you've probably noticed another difference between the two last figures; the `circle` markers are missing. This might seem a little strange at first, since `px.line()` has specified the markers to be circles through:

```python
'marker': {'symbol': 'circle'}
```

But we've also got:

```python
'mode': 'lines'
```

And this overrides the `marker` setting. This isn't only a preferred behaviour from the developer team. It has a very specific purpose that we'll get back to in a bit. Another crucial element is:

```python
'type': 'scatter'
```

This lets us know that the first trace of this figure is in fact a `go.Scatter()` trace. And even though the output has changed a great deal from the first time we ran `fig.show` in this section, we're still studying the same object regardless of whether it's been built using `go.Figure()` or `px.line()`.


```{tip}
Be aware that `fig.show` only reveals *some* of the attributes of `fig`. If you'd like to scrutinize further details, you'll have to use `fig.full_figure_for_development()` which we'll get back to in the chapter `Advanced plotly figure methods(???=)`.
```

---

## 8.1.6 How to edit the attributes of traces
If you, as an example, would like to include the circle symbol for each datapoint, you can either do so through the call to `px.line()` itself, with:

```python
fig = px.line(df, x='x', y = ['y', 'y1'],
                  title = 'My first Plotly Express figure',
                  markers = True)
```

Or you can use another method of the `fig` object, `fig.update_traces()` that let's you edit properties of already existing traces:

```python
fig.update_traces(mode = 'markers+lines')
```

```{admonition} Two methods, one goal
Even though these techniques seem very different, `px.line(markers = True)` and `fig.update_traces(mode = 'markers+lines')` do the very same thing to the underlying structure of the `fig` object, namely setting the following for the all traces contained in `data` in the figure dictionary:

```python
'mode': 'markers+lines'
```


Before we move on, you should also take notice of how the calls to `go.Figure()` and `px.line()` are fundamentally different in other ways. With `px.line()`, the data argument comes first. Just as with `go.Figure()`, but with different functionality. `data` in `go.Figure()` expects a collection of traces like `go.Scatter()`, while `data` in `px.line()` expects a reference to a single data source like a pandas dataframe. In `px.line()`, defining `df` as the data source also means that further specifications, like `x = 'x'` does not require you to include another reference to `df` in `x = df['x']` like you had to do for `go.Figure(go.Scatter(x = df['x'])`.

There's much to take in here, but the undeniable benefit is that what you have learnt now will prepare you to build beautiful, interactive and highly customizable figures that are also able to illustrate multiple dimensions of a dataset with often only one line of code.

## 8.1.7 Visualizing multiple dimensions of a dataset

Until now, we've only operated on a very simple dataset with made-up numbers. Let's apply some more of what we've learnt in the chapter 7, and add another dimenson to the dataset. In that process, we will change the structure of our dataframe with `pd.melt()`. But first, let's pretend that we're looking at some data for two countries `[Canada, Norway]` instead of two meaningless variables `['x', 'y']`:

```python
df = pd.DataFrame({'year': [2021,2022,2023,2024],
                   'Canada': [10,11,12,13],
                   'Norway': [11,12,13,14,]})
```

[![enter image description here][44]][44]

## 8.1.7.1 Long and wide data format
This dataframe is of a so-called wide format with a unique index in the left-most column, unique column names, and associated values for each index in the belonging rows. If you were to add data for another country, you would do so by adding another column, and the dataset would have become **wider**. Hence the name.

Plotly Express handles a dataset such as this with ease. But if we'd like to study and visualize more dimensions, like which continent each country belongs to, we'll benefint greatly by transforming the dataset to a so-called long format. Now we'll have duplicated values for the index, *one* column with country names, and one column for each new dimension in the dataset. If you were to add more countries with this format, you would have do so through adding more observations in the already existing columns. Thus the dataset would not have become wider, but **longer**.

Running the following snippet will turn our new dataframe into the long dataframe `df_long` below:

```python
df_long = pd.melt(df, id_vars = ['year'], value_vars = df.columns[1:],)
df_long.rename(columns = {'variable':'country'}, inplace = True)
```

[![enter image description here][45]][45]

First of all, this will make it even easier to reproduce the figure we have so far, with:

```python
fig = px.line(df_long, x='year', y = 'value', color = 'country')
```

Now you no longer need to specify a list of names from a wide dataframe for `y` in `px.line()`. With this setup, the function recognizes that the input is a dataframe of a long format, and setting `color = 'country'` will let the function know that there are multiple unique values in that particular column to which a color cycle is assigned.

[![enter image description here][46]][46]

## 8.1.7.2 Adding another dimension to a dataframe of a long format

From here we can add yet another dimension to the dataset through a new variable, `'continent'`, by mapping a dictionary to our already existing `'country'` column:

```python
    df_long['continent'] = df_long['country'].map({'Canada': 'Americas', 'Norway':'Europe'})
```

## Recap
By now you know the reasoning behind every part of:

```python
px.line(df_long, x='year', y = 'value', color = 'country')
```

The dataset is defined in the first argument, and the rest are just references to that dataset. And perhaps most importantly, `color` does not take actual colors as input, but rather a column with multiple values to which a color from a default color cycle is applied to each unique element. Now we can take our new variable / dimension `'continent'` into account as well with `symbol = 'continent'` in:

```python
fig = px.line(df_long, x='year', y = 'value', color = 'country', symbol = 'continent')
fig.show()
```

This works exactly the same way as `color = 'country'`, but this time a symbol sequence is used to represent unique values of a dataframe column.

[![enter image description here][47]][47]

And this explains why `px.line()` doesn't assign symbols to markers by default; the function is simply waiting for you to make use of the multidimensional capabilites of the library.

## 8.1.8 Templates

Our previous call to `px.line()` is now only missing one element compared to the initial figure, the `template`. There we used `plotly_white`. Other available templates are:

```python
['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark', 'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none']
```

Let's round off this section with `plotly_dark`:

[![enter image description here][48]][48]


Now that you're able to master some of the basic powers of Plotly Express, we'll soon move on to taking a look at how you can build other chart types than line charts and combine them with the template of your liking to create almost any chart with any design.

[![enter image description here][49]][49]

---

## IDEAS FOR THE NEXT SECTION:

[Plotly: How to make different plots using plotly?](https://stackoverflow.com/questions/66664935/plotly-how-to-make-different-plots-using-plotly-as-a-plotting-backend-for-panda/66664937#66664937)


  [1]: https://i.stack.imgur.com/M89Yh.png
  [2]: https://i.stack.imgur.com/21H9I.png
  [3]: https://plotly.com/python/plotly-express/
  [4]: https://plotly.com/python/line-charts/
  [5]: https://plotly.com/python/line-and-scatter/
  [6]: https://plotly.com/python/bar-charts/
  [7]: https://plotly.com/python/gantt/
  [8]: https://www.gapminder.org/
  [9]: https://plotly.com/python/wide-form/
  [10]: https://i.stack.imgur.com/fu8NX.png
  [11]: https://plotly.com/python/line-charts/#line-plots-with-plotlyexpress
  [12]: https://i.stack.imgur.com/GpgGe.png
  [13]: https://plotly.com/python/discrete-color/#color-sequences-in-plotly-express
  [14]: https://i.stack.imgur.com/jn4rl.gif
  [15]: https://i.stack.imgur.com/1CTmL.gif
  [16]: https://i.stack.imgur.com/3yB43.png
  [17]: https://i.stack.imgur.com/2jVzU.png
  [18]: https://i.stack.imgur.com/jvdM4.gif
  [19]: https://i.stack.imgur.com/pAkfB.png
  [20]: https://i.stack.imgur.com/5XnqR.png
  [21]: https://i.stack.imgur.com/YzXfG.png
  [22]: https://i.stack.imgur.com/9sw4h.png
  [23]: https://i.stack.imgur.com/gj6oW.png
  [24]: https://i.stack.imgur.com/6UVCx.png
  [25]: https://i.stack.imgur.com/AJswk.png
  [26]: https://i.stack.imgur.com/mIUah.gif
  [27]: https://i.stack.imgur.com/cVYGf.png
  [28]: https://i.stack.imgur.com/N1JSd.png
  [29]: https://i.stack.imgur.com/MYpK9.png
  [30]: https://i.stack.imgur.com/ENAiB.png
  [31]: https://i.stack.imgur.com/82TrL.png
  [32]: https://i.stack.imgur.com/EEylA.png
  [33]: https://i.stack.imgur.com/lDZUC.png
  [34]: https://i.stack.imgur.com/MHR22.png
  [35]: https://i.stack.imgur.com/zPuh9.png
  [36]: https://i.stack.imgur.com/xU3El.png
  [37]: https://plotly.com/python/graph-objects/
  [38]: https://i.stack.imgur.com/FFZFt.png
  [39]: https://plotly.com/python/line-and-scatter/#scatter-and-line-plots-with-goscatter
  [40]: https://plotly.com/python/reference/layout/
  [41]: https://i.stack.imgur.com/X88Ak.png
  [42]: https://i.stack.imgur.com/rSm7d.png
  [43]: https://i.stack.imgur.com/lCE6Y.png
  [44]: https://i.stack.imgur.com/N1uHD.png
  [45]: https://i.stack.imgur.com/B708M.png
  [46]: https://i.stack.imgur.com/VSCj0.png
  [47]: https://i.stack.imgur.com/xo5iL.png
  [48]: https://i.stack.imgur.com/bGs6b.png
  [49]: https://i.stack.imgur.com/uS3TP.png
