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
