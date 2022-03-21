# Chapter 3 - Dash Components and Layouts

## What you will learn

In this chapter we will explore Dash various **components** and how to position them with **layout** as well as add styling with **CSS**\
- [p1c3_start.py](../assets/p1c2/p1c2_end.py)
- [p1c3_end.py](../assets/p1c3/p1c3_end.py)

## Dash Components

**Components** are the building blocks of the app such as dropdown menus, buttons (radio, checkbox, etc...), slider bars, graphs, and many others.
We will learn a few common components in this chapter.

**Properties** are attributes of components (TODO: add more here)\

````{dropdown} Buttons
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
Buttons are clickable components that will be used to trigger other actions such as submitting a form or plotting data.  We will pass in a **child** property to give the button a name in the dashboard.


```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()
```

![button](../assets/p1_c3/button.gif)

````

````{dropdown} Checklist
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

Checklists display a set of options for the user to choose.
We will pass in a list of **options** when we create the checklist component below:


```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()

```

![checklist](../assets/p1_c3/checklist.gif)
  
````

````{dropdown} Radio items
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

  

Radio items are lists of options that a user can only select one option.
Similar to the checklst we will pass in a list of **options** when we create the component.

```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()

```

![radio_item](../assets/p1_c3/radio.gif)

````

````{dropdown} Dropdown
    :container: + shadow
    :title: bg-primary text-white font-weight-bold

    
```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
                dropdown,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()

```

![drop_down](../assets/p1_c3/dropdown.gif)
  
````

````{dropdown} Slider
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    
```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__)

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 10, 1)

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
                dropdown,
                slider,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()

```

![slider](../assets/p1_c3/slider.gif)
````

## CSS

Next, we'll add styling to our application with a Cascading Style Sheets or **CSS**.
We will use the Bootstrap [stylesheet](https://www.w3schools.com/css/css_intro.asp) for this application.  

    
```python
# Import packages 
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown('My First app')
button = html.Button("Button")
checklist = dcc.Checklist(['New York City', 'Montréal', 'San Francisco'])
radio = dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'])
dropdown = dcc.Dropdown(['NYC', 'MTL', 'SF'])
slider = dcc.Slider(0, 10, 1)

# App Layout 
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
                dropdown,
                slider,
])

# Run the App 
if __name__ == '__main__':
    app.run_server()
```
 
![css_diff](../assets/p1_c3/style_comparison.png)


## Layout

So far, we've only organized our app **layout** in a `dbc.Container()` component without any further specifications:

```python
app.layout = dbc.Container([
                markdown,
                button,
                checklist,
                radio,
                dropdown,
                slider,
])
```

And we've seen that this will place our app components sequentually in one single column.  In order to neatly place the different components in a more functional and visually pleasing way, we'll have to introduce `dbc.Row()` and `dbc.Column()`. Together with `dbc.Container()` these are the main [Layout][1] components in dash-bootstrap-components.

```{margin}
Should we mention Bootstrap here?\
Now let's learn about layout and how to place the components at specific locations on the page instead.
We will use **Dash Bootstrap Components** to do this.
**Bootstrap** is [the most popular CSS Framework for developing responsive and mobile-first websites](https://www.w3schools.com/whatis/whatis_bootstrap.asp).

  
* [Layout in Bootstrap](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/) is controlled using the grid system. The Bootstrap grid has twelve columns
![Bootstrap layout](../assets/p1_c3/bootstrap_grid.png)

-SM
```

A `container` wraps the entire app, and a  `row` is a wrapper for `columns` than in turn contains elements such as controls, figures, tables, text and so on.  The layout of your app should thereofre be built as a series of rows of columns.

```{margin}
I'd like to take out this bold section and give the students a demonstration of the Rows/Columns immediately as I think the concept of **wrapper** or **wrapping** might confuse them

- SM
```
**The `col` component should always be used as an immediate child of Row and is a wrapper for your content that ensures it takes up the correct amount of horizontal space.
But let's get back to spacing and adjustments after we've seen how the already defined components `markdown`, `checklist`, `radio`, `slider` and `button` can all fit together with `rows` and `columns`.**

The following snippet will produce the app shown in the image below:

    app.layout = dbc.Container(
        [
            dbc.Row(dbc.Col(markdown)),
            dbc.Row([dbc.Col(dropdown), dbc.Col(slider)]),
            dbc.Row(dbc.Col(slider)),
            dbc.Row(dbc.Col(button)),
        ]
    )

[![enter image description here][2]][2]

***missing: details about default width: 12***

```{margin}
Editor's Note: Discuss setting width to variable 3, 6, 8, 12 etc...

- FM
```

There are two main learning points here.
First, notice how you can freely put `dbc.Col(markdown)` as the only argument in the first `dbc.Row()` component.
If you have more than one element, like in the second `Row`, you'll have to encapsulate them in a list like this: `dbc.Row([dbc.Col(dropdown), dbc.Col(slider)])`.
Second, notice how the rows still appear sequentually in a vertical fashion, and that our two `Col` components withnin a `Row`  appear horizontally within the common `Row`:

[![enter image description here][3]][3]


***this paragraph possibly redundant by now???***

```{margin}
Editor's Note: I think it's fine to have a "Summary" section to review/recap

- FM
```
For best results, also make sure you adhere to the following two rules when constructing your layouts:

1. Only use `Row` and `Col` inside a Container. 
2. A single Container wrapping your entire app's content is ideal, at least at this stage.
3. The immediate children of any `Row` component should always be `Col` components. Your further content should go inside the `Col` components.

```{margin}
Editor's Note: Is a "Row component" and a "Col component" the right terminology? Should we use a different word to disambiguate Dash components?

- FM
```

### Introducing styling

```{margin}
Editor's Note: Idon't fully see the value of this section here...I suggest we defer the style stuff to a later section? Or at least discuss the goal of it.

- FM
```

With more advanced apps, it can be a bit hard to discern where the different rows and columns start and end.
Or, in other words, in which row and column a specific element like for example our `dbc.Col(slider)` is embedded.
That's not crucial to our current example, but it's a good opportunity to introduce how to edit the layout and appearence of the different `col` components.
One way to do that, is to add `CSS` elements through the `style` attribute of like `dbc.Col(slider)` like this:

***the following section is the complete addition, and needs to be explained more in details:***

### Snippet

```{margin}
Editor's Note: As discussed in the meeting, leave in code, remove "style", and add "width =" to show that it doesn't HAVE to span the full page.

- FM
```

    app.layout = dbc.Container(
        [
            dbc.Row(dbc.Col(markdown, style={"background-color": '#636EFA'})),
            dbc.Row([dbc.Col(dropdown, style={"background-color": '#00CC96'}),
                     dbc.Col(slider, style={"background-color": '#EF553B'})]),
            dbc.Row(dbc.Col(slider, style={"background-color": '#AB63FA'})),
            dbc.Row(dbc.Col(button, style={"background-color": '#00CC96'})),
        ]
    )


### Image

[![enter image description here][4]][4]


  [1]: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout
  [2]: https://i.stack.imgur.com/M8j6q.png
  [3]: https://i.stack.imgur.com/3Yk7o.png
  [4]: https://i.stack.imgur.com/a8aB3.png
