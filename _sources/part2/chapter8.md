# Chapter 8: Data Visualization

```{admonition} Some initial thoughts from me to the team (not meant as part of the final product)

## Main goal:

Empower the students to understand how Plotly Express works, which dataformat is best suited, how to inspect the structure of a figure, and how to edit elements of a figure. With this suggested chapter structure, some students may find it to be a punch in the face. If so, that's only a wake-up call to prepare them for the powers they are about to obtain =)

## Why talk about plotly.graph_objects?
Plotly express is fantastic, and should be the preferred approach to using Plotly with Dash. But in the wild, the students will quickly come across Plotly Graph Objects as well. Particularly in the docs where the first examples for visualizations like line graphs often start out with a `go.Figure` example. So even if this suggested section might seem too detailed, it's all there to avoid future confusion. 

## Ability to inspect and edit figures => empowerment
Personally, one reason why I love Plotly is because it's so much fun to work with if you know how to **build**, **inspect** and **edit** the figures that `px` will let you produce. The sooner the students learn how to do this, the better. This MIGHT get a little confusing, BUT I'm hoping the following section will pulverize that confusion and quickly give the students a feeling of ***empowerment*** using the plotly library.

## Plotly express works best with data of a long format
As of [plotly.py 4.8](https://community.plotly.com/t/announcing-plotly-py-4-8-plotly-express-support-for-wide-and-mixed-form-data-plus-a-pandas-backend/40048) px also handles data of a wide format.
Bt you can't unleash the true powers of px without knowing how it works with data of a long format.
Thus, chp 7 ***must*** include the difference between wide and long, and methods of transformation:

- `pd.melt()` at the very least
- `pd.pivot()` perhaps?
```


```{admonition} Learning Intentions

-  What Plotly Express (`px`) is and why you should use it.
- How `px` relates Plotly Graph Objects (`go`)
- How to build a basic `go.Figure` **canvas**
- How to **display** a figure with `fig.show()`
- How to **inspect** a figure with `fig.show`
- How using `px` with, for example `px.line` structurally  will produce the same object as a basic `go.Figure()` call
- The **structure** of a `go.Figure()` object
- How to **add data** (traces) to a `go.Figure()` object
- How to easily handle larger **datasets** with `px`
- How to **edit** a figure object after setting it up with `px` 

```


## 8.1 Introduction to Plotly Express
Plotly's arguably greatest power is how easily you can make beautiful interactive graphs. Plotly express adds to the versatility of Plotly through two specific features:

1) You can easily create almost any plot with only one line of code like

```python
px.line(df, x= 'year', y = 'lifeExp'`, [...])
```
2) You can visualize multidimensional data through attributes like `color` and `symbol`. Here's an example that we'll learn to build and understand from scratch:

```python
import plotly.express as px
df = px.data.gapminder()
px.line(df, x= 'year', y = 'lifeExp', color = 'country', symbol = 'continent', template = 'plotly_white')
```

[![enter image description here][1]][1]

Plotly Express is commonly imported like this:

```python
import plotly.express as px
```

`px.data` holds several datasets. In the figure above you have seen how to easily build a lineplot with a built-in dataset. `px` can produce a lot more than line charts, but we'll take a closer look at that in a later section. Right now, let's see how `px.line()` creates the awesome looking figure above. 


## 8.1.1 Breakdown of `px.line()` and relation to Plotly Graph Objects

Running [`px.line()`][2] will produce a [Plotly Graph Objects][3] figure object `go.Figure` (where `go` is the commonly used alias for `plotly.graph_objects`) which is one of the main building blocks of the Plotly library; the canvas (better to call it something else?). Running `go.Figure()` will produce a completely empty figure or canvas like this:
```python
import plotly.graph_objects as go
go.Figure()
```

[![enter image description here][4]][4]

What we're looking at here is a figure template with a few defined settings. We've got an x and an y-axis as well as white gridlines for both axes on a light-blue background. We can take a closer look at the underlying settings with `fig.show` that will reveal this dictionary:

```python
{
    'data': [], 'layout': {'template': '...'}
}
```

So at its core, a figure object is built up by a `data` and  `layout` element. As you'll soon learn, there are endless ways to construct a Plotly figure. But building on this basic example, you will have to populate the data attribute through the addition of traces, like a [`go.Scatter()`][5] trace (more on this and other options?). You can also edit the layout through [`go.Layout()`][6]. Below is an example where the dataset `x= [1,2,3,4]` and `y = [10,11,12,13]` is added to the empty canvas. We'll also specify a figure title.

```python
fig = go.Figure(data = [go.Scatter(x= [1,2,3,4], y = [10,11,12,13])],
                layout = go.Layout(title = 'My first Plotly figure'))
fig.show()
```

[![enter image description here][7]][7]

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

[![enter image description here][8]][8]

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

[![enter image description here][9]][9]

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

## 8.1.6 Plotly Express marker symbols
If you would like to include the circle symbol for each datapoint, you can either do so through the call to `px.line()` itself, with:

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

[![enter image description here][10]][10]

## 8.1.7.1 Long and wide data format
This dataframe is of a so-called wide format with a unique index in the left-most column, unique column names, and associated values for each index in the belonging rows. If you were to add data for another country, you would do so by adding another column, and the dataset would have become **wider**. Hence the name.

Plotly Express handles a dataset such as this with ease. But if we'd like to study and visualize more dimensions, like which continent each country belongs to, we'll benefint greatly by transforming the dataset to a so-called long format. Now we'll have duplicated values for the index, *one* column with country names, and one column for each new dimension in the dataset. If you were to add more countries with this format, you would have do so through adding more observations in the already existing columns. Thus the dataset would not have become wider, but **longer**.

Running the following snippet will turn our new dataframe into the long dataframe `df_long` below:

```python
df_long = pd.melt(df, id_vars = ['year'], value_vars = df.columns[1:],)
df_long.rename(columns = {'variable':'country'}, inplace = True)
```

[![enter image description here][11]][11]

First of all, this will make it even easier to reproduce the figure we have so far, with:

```python
fig = px.line(df_long, x='year', y = 'value', color = 'country')
```

Now you no longer need to specify a list of names from a wide dataframe for `y` in `px.line()`. With this setup, the function recognizes that the input is a dataframe of a long format, and setting `color = 'country'` will let the function know that there are multiple unique values in that particular column to which a color cycle is assigned.

[![enter image description here][12]][12]

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

[![enter image description here][13]][13]

And this explains why `px.line()` doesn't assign symbols to markers by default; the function is simply waiting for you to make use of the multidimensional capabilites of the library.

## 8.1.7 Templates

Our previous call to `px.line()` is now only missing one element compared to the initial figure, the `template`. There we used `plotly_white`. Other available templates are:

```python
['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark', 'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none']
```

Let's round off this section with `plotly_dark`:

[![enter image description here][14]][14]


Now that you're able to master some of the basic powers of Plotly Express, we'll soon move on to taking a look at how you can build other chart types than line charts and combine them with the template of your liking to create almost any chart with any design.

---

## IDEAS FOR THE NEXT SECTION:

[Plotly: How to make different plots using plotly?](https://stackoverflow.com/questions/66664935/plotly-how-to-make-different-plots-using-plotly-as-a-plotting-backend-for-panda/66664937#66664937)


  [1]: https://i.stack.imgur.com/qCaDf.png
  [2]: https://plotly.com/python/line-charts/
  [3]: https://plotly.com/python/graph-objects/
  [4]: https://i.stack.imgur.com/FFZFt.png
  [5]: https://plotly.com/python/line-and-scatter/#scatter-and-line-plots-with-goscatter
  [6]: https://plotly.com/python/reference/layout/
  [7]: https://i.stack.imgur.com/X88Ak.png
  [8]: https://i.stack.imgur.com/rSm7d.png
  [9]: https://i.stack.imgur.com/lCE6Y.png
  [10]: https://i.stack.imgur.com/N1uHD.png
  [11]: https://i.stack.imgur.com/B708M.png
  [12]: https://i.stack.imgur.com/VSCj0.png
  [13]: https://i.stack.imgur.com/xo5iL.png
  [14]: https://i.stack.imgur.com/bGs6b.png
