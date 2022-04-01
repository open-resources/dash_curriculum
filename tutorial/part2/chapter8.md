# Chapter 8: Data Visualization

***...some initial thoughts...*** 

```{tip} Some initial thoughts from me to the team (not meant as part of the final product)

**Chapter 7 should include the following:**

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

[![enter image description here][1]][1]

***Style example 2:***

Just add

```python
fig.update_layout(barmode = 'group')
```

and you'll get:

[![enter image description here][1]][1]



```

***...chapter content starts here...***

```{admonition} Learning intentions

- What Plotly Express (`px`) is and why you should use it.
- How `px` uses attributes such as `color` and `symbol` to illustrate multiple dimensions of a dataset
- line, scatter, regression(?), area, bar, funnel(?), timeline(?)
- how different data structures work best with different px functions

```
## 8.1 Principles of Effective Visualizations

`Firas`

## 8.2 Introduction to Plotly Express

The [plotly.express module][2] (usually imported as px) contains functions that can create entire figures at once, and is referred to as Plotly Express or `px`. Plotly Express is a built-in part of the plotly library, and is the recommended starting point for creating most common figures like [line][3], [scatter][4], [area][5], [bar][6], [funnel][7] and [timeline][8] figures. Here, well take a look at how you can easily create a very informative figure from a complex dataset with only a few lines of code.

## 8.2.1 Line chart

Let's take a look at how `px.line()` used on `px.data.gapminder()` will let you illustrate several dimensons of the dataset through attributes like `color` and `symbol`.

```python
import plotly.express as px
df = px.data.gapminder()
px.line(df, x= 'year', y = 'lifeExp', color = 'country', symbol = 'continent', template = 'plotly_white')
```

[![enter image description here][9]][9]

The current dataset is of a so-called long (or tidy) format:

[![enter image description here][10]][10]

***...needs more explaining if not covered in chapter 7...***

As you can see from the function call above, `color` and `symbol` don't take actual colors and symbols as  arguments, but rather columns of a dataset `df` from which unique values are assigned certain color and symbol sequences.

## 8.2.2 Scatter plot

You can drop the lines and produce a scatter plot with markers only if you substitute `px.line()` with `px.scatter()`:

[![enter image description here][11]][11]

```python
fig = px.scatter(df, x= 'year', y = 'lifeExp', color = 'country', symbol = 'continent', template = 'plotly_white')
```
## 8.2.3 Scatter plot with trendlines


From here you can also add a trendline for each trace by adding `trendline="ols"` to the mix:

[![enter image description here][12]][12]

In this case, the trendlines will indicate the increase in life expectanciese for each country over the years.

## 8.2.4 Regression - A special case of scatter plot

In order to compare a relationship between two specifc variables, you would have to wrangle the dataset a little so that you can assign individual sereis to `x` and `y`. But this is pretty straight-forward with `pd.pivot` like this

```python
df.pivot(index='year', columns='country', values='lifeExp')
```

### From long to wide with `pd.pivot()`

[![enter image description here][13]][13]

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

[![enter image description here][14]][14]

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

[![enter image description here][15]][15]

As you can tell from the figure, you can now study the change in the total populations of these countries over the years. This makes sense for `population`, but not so much if you were to study life expectancies. In the latter case it would make more sense to display the bars for each country next to each other. The following section will introduce how to edit the `barmode` attribute for the figure object both in the function call and *after* you've produced the figure.

## 8.2.5 How to edit chart features

By default `px.bar()` uses `barmode = 'stacked'` which does exactly what it says, namely stacking the populations for each `country` (discerned by `color`) on top of each other. But you can change this behavior through `barmode = 'group'` and get the following result:

[![enter image description here][16]][16]

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





## 8.3 Incorporting PX graphs in a Dash app

We earlier talked about how a `dbc.Col` component resides in a `dbc.Row` component and serves as a wrapper for other components. One such component can be a `dcc.Graph()` component, which in turn is a wrapper for a Plotly figure object:

```python
app.layout = dbc.Container([dbc.Row(dbc.Col(dcc.Graph(id='figure1', figure=fig), width = 4))])
```

### App

[![enter image description here][17]][17]



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


## 8.4 References and resources

.

---
# OUT-TAKES from initial suggestion
---




## 8.1.1 Breakdown of `px.line()` and relation to Plotly Graph Objects

Running [`px.line()`][3] will produce a [Plotly Graph Objects][18] figure object `go.Figure` (where `go` is the commonly used alias for `plotly.graph_objects`) which is one of the main building blocks of the Plotly library; the canvas (better to call it something else?). Running `go.Figure()` will produce a completely empty figure or canvas like this:
```python
import plotly.graph_objects as go
go.Figure()
```

[![enter image description here][19]][19]

What we're looking at here is a figure template with a few defined settings. We've got an x and an y-axis as well as white gridlines for both axes on a light-blue background. We can take a closer look at the underlying settings with `fig.show` that will reveal this dictionary:

```python
{
    'data': [], 'layout': {'template': '...'}
}
```

So at its core, a figure object is built up by a `data` and  `layout` element. As you'll soon learn, there are endless ways to construct a Plotly figure. But building on this basic example, you will have to populate the data attribute through the addition of traces, like a [`go.Scatter()`][20] trace (more on this and other options?). You can also edit the layout through [`go.Layout()`][21]. Below is an example where the dataset `x= [1,2,3,4]` and `y = [10,11,12,13]` is added to the empty canvas. We'll also specify a figure title.

```python
fig = go.Figure(data = [go.Scatter(x= [1,2,3,4], y = [10,11,12,13])],
                layout = go.Layout(title = 'My first Plotly figure'))
fig.show()
```

[![enter image description here][22]][22]

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

[![enter image description here][23]][23]

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

[![enter image description here][24]][24]

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

[![enter image description here][25]][25]

## 8.1.7.1 Long and wide data format
This dataframe is of a so-called wide format with a unique index in the left-most column, unique column names, and associated values for each index in the belonging rows. If you were to add data for another country, you would do so by adding another column, and the dataset would have become **wider**. Hence the name.

Plotly Express handles a dataset such as this with ease. But if we'd like to study and visualize more dimensions, like which continent each country belongs to, we'll benefint greatly by transforming the dataset to a so-called long format. Now we'll have duplicated values for the index, *one* column with country names, and one column for each new dimension in the dataset. If you were to add more countries with this format, you would have do so through adding more observations in the already existing columns. Thus the dataset would not have become wider, but **longer**.

Running the following snippet will turn our new dataframe into the long dataframe `df_long` below:

```python
df_long = pd.melt(df, id_vars = ['year'], value_vars = df.columns[1:],)
df_long.rename(columns = {'variable':'country'}, inplace = True)
```

[![enter image description here][26]][26]

First of all, this will make it even easier to reproduce the figure we have so far, with:

```python
fig = px.line(df_long, x='year', y = 'value', color = 'country')
```

Now you no longer need to specify a list of names from a wide dataframe for `y` in `px.line()`. With this setup, the function recognizes that the input is a dataframe of a long format, and setting `color = 'country'` will let the function know that there are multiple unique values in that particular column to which a color cycle is assigned.

[![enter image description here][27]][27]

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

[![enter image description here][28]][28]

And this explains why `px.line()` doesn't assign symbols to markers by default; the function is simply waiting for you to make use of the multidimensional capabilites of the library.

## 8.1.8 Templates

Our previous call to `px.line()` is now only missing one element compared to the initial figure, the `template`. There we used `plotly_white`. Other available templates are:

```python
['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark', 'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none']
```

Let's round off this section with `plotly_dark`:

[![enter image description here][29]][29]


Now that you're able to master some of the basic powers of Plotly Express, we'll soon move on to taking a look at how you can build other chart types than line charts and combine them with the template of your liking to create almost any chart with any design.

---

## IDEAS FOR THE NEXT SECTION:

[Plotly: How to make different plots using plotly?](https://stackoverflow.com/questions/66664935/plotly-how-to-make-different-plots-using-plotly-as-a-plotting-backend-for-panda/66664937#66664937)


  [1]: https://i.stack.imgur.com/N1JSd.png
  [2]: https://plotly.com/python/plotly-express/
  [3]: https://plotly.com/python/line-charts/
  [4]: https://plotly.com/python/line-and-scatter/
  [5]: https://plotly.com/python/filled-area-plots/
  [6]: https://plotly.com/python/bar-charts/
  [7]: https://plotly.com/python/funnel-charts/
  [8]: https://plotly.com/python/gantt/
  [9]: https://i.stack.imgur.com/MYpK9.png
  [10]: https://i.stack.imgur.com/ENAiB.png
  [11]: https://i.stack.imgur.com/82TrL.png
  [12]: https://i.stack.imgur.com/EEylA.png
  [13]: https://i.stack.imgur.com/lDZUC.png
  [14]: https://i.stack.imgur.com/MHR22.png
  [15]: https://i.stack.imgur.com/zPuh9.png
  [16]: https://i.stack.imgur.com/xU3El.png
  [17]: https://i.stack.imgur.com/21H9I.png
  [18]: https://plotly.com/python/graph-objects/
  [19]: https://i.stack.imgur.com/FFZFt.png
  [20]: https://plotly.com/python/line-and-scatter/#scatter-and-line-plots-with-goscatter
  [21]: https://plotly.com/python/reference/layout/
  [22]: https://i.stack.imgur.com/X88Ak.png
  [23]: https://i.stack.imgur.com/rSm7d.png
  [24]: https://i.stack.imgur.com/lCE6Y.png
  [25]: https://i.stack.imgur.com/N1uHD.png
  [26]: https://i.stack.imgur.com/B708M.png
  [27]: https://i.stack.imgur.com/VSCj0.png
  [28]: https://i.stack.imgur.com/xo5iL.png
  [29]: https://i.stack.imgur.com/bGs6b.png
