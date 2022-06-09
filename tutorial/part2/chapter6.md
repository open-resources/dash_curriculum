# Chapter 6 - Working with Data in Dash

## What you will learn
In this chapter we will show you how to incorporate data into Dash apps. There are many ways one could add data to an app, but we will focus on a few of the most common ways when working with Dash. We will also show you a brief introduction to a few common data wrangling operations that we will use in the rest of the tutorial.

```{admonition} Learning Intentions
- Import data into the app
- Create and populate Pandas dataframes
- Basic data wrangling techniques to prepare data for reporting
```

By the end of this chapter you will know how to build this app:

![fina-app](./ch6_files/chap6-final-app.gif)

````{dropdown} See the code
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
  
```
# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# Import data
url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
df3 = pd.read_table(url, sep=';')
y=2007
df3 = df3.loc[(df3['year']==y), :]

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
_header = html.H1(children = 'Population by country in 2007', style = {'textAlign' : 'center'})
continent_dropdown = dcc.Dropdown(id = 'continent-dropdown', placeholder = 'Select a continent', options = [c for c in df3.continent.unique()])
country_dropdown = dcc.Dropdown(id = 'country-dropdown', placeholder = 'Select a country')
_output = html.Div(id = 'final-output')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([_header], width=8)]),
        dbc.Row([dbc.Col([continent_dropdown], width=8)]),
        dbc.Row([dbc.Col([country_dropdown], width=6)]),
        dbc.Row([dbc.Col([_output], width=6)])
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='country-dropdown', component_property='options'),
    Input(component_id='continent-dropdown', component_property='value')
)
def country_list(continent_selection):
    country_options = [c for c in df3.loc[df3['continent']==continent_selection, 'country'].unique()]
    return country_options


@app.callback(
    Output(component_id='final-output', component_property='children'),
    Input(component_id='country-dropdown', component_property='value'),
prevent_initial_call=True
)
def pop_calculator(country_selection):
    pop_value = df3.loc[df3['country']==country_selection]
    pop_value = pop_value.loc[:, 'pop'].values[0]  # select only first value in pop column
    output = ('The population in '+country_selection+' was: '+pop_value.astype(str))
    return output

# Run the App
if __name__ == '__main__':
    app.run_server()
```

````

[Click to download the complete code file for this chapter](https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/chapter6_fin_app.py)

## 6.1 Where to read in the data?

The data will be used by multiple objects in our Dash app: Dash components, callbacks, tables, layout, etc.
To keep the code organized and separate the data processing from the app creation,
we recommend importing the data before initialising the app, right above this line of code:

```
# Data imported here

# Initialise app
app = Dash(__name__)
```

If we just need to quickly test out a piece of code, we can create a pandas dataframe from some mock up data:

```
# Data imported here
df = pd.DataFrame({
    'Country': ['United States','Norway','Italy','Sweden','France'],
    'Country Code': ['US','NO','IT','SE','FR']
})

# Initialise app
app = Dash(__name__)
```

```
The dictionary keys `Country` and `Country code` will represent the column names of the pandas dataframe.
```

```{note}
If you need access to pre-built data sets to test your code, consider using the Plotly Express built-in data, such as Gapminder or [other of of the many other dataset in plotly express](https://plotly.com/python-api-reference/generated/plotly.express.data.html). To load in the Gapminder data we could use the following line of code: `df = px.data.gapminder()`.
```

## 6.2 Reading in data to use in Dash

Data exists in multiple formats (e.g. `.csv`, `.json`, and `.xlsx`) and could be located on our computer or on the internet. Here we will use the powerful pandas library to show how you can read in data from various sources before using it in your app.

### 6.2.1 Reading data from files on your computer

#### Excel files

Let's see an example of how to read in an Excel file into a dataframe.
The file we'll be using is available here [data_01](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part2/ch6_files/data_01.xlsx): follow the link and click on "Download"; find the folder where the file was downloaded and copy the path. Note that you will need to `pip install openpyxl` into your terminal in order to work with `.xlsx` files.

```
import pandas as pd


# Your file path might look different
filepath = r'C:\Users\YourUser\Downloads\data_01.xlsx'
df1 = pd.read_excel(filepath, sheet_name='Sheet1')
```

In this example, we have accessed the data (Excel file) outside the folder where our main app is located; therefore, we specified an absolute filepath (also called "the full path"). The path is saved as a raw string (hence the "r" just before the string containing the path. This is done because VS Code may trigger a warning when using a normal string).

If the data file is located directly inside the folder where your main app file is (or within the VS Code working directory), the full path is not required; you may only specify the filename (also called "the relative path"). The code will then become:

```
filepath = 'data_01.xlsx'
df1 = pd.read_excel(filepath, sheet_name='Sheet1')
```

If we would peak at the data we read into the dataframe `df1`, it would look like the following:

![Excel data 01](./ch6_files/data01.JPG)

```{note}
If you experience any difficulties in finding your filepath, please check [this screenshot](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part2/ch6_files/Helper01.JPG), showing how to find the filepath directly from VS Code.
```

```{tip}
In production versions, when apps get deployed, the best practice is to have a "data" folder, where all data files are stored and therefore accessed by the app code. This will be covered in [Chapter 14](https://open-resources.github.io/dash_curriculum/part4/chapter14.html).
```

#### CSV files

We will now read in the same data from above, but from a .csv file named [data_02](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part2/ch6_files/data_02.csv). Please follow the link and click the "Raw" button in the top right corner of the file, right click the new page that opened and select "Save page as"/"Save as" and save it as "data_02.csv". Find the path of your file to update the `filename` in the code below.

```
filepath = r'C:\Users\User1\Downloads\data_02.csv'
col_names = ['country','continent','year','pop']
df2 = pd.read_csv(filepath, sep='|', usecols=col_names)
```

- Similarly to the previous example, we have accessed the data located outside the app folder, and therefore specified a full path to the file.
- In most cases, you will see `.csv` files with comma column separators (hence the name, csv standing for "comma-separated values"). Here, we used a different separator: '|'. The `sep` argument allows to specify whatever characters should be considered field separators: pandas will separate data into different columns any time it encounters these characters.
- We have also selected a subset of columns to be uploaded, listed in the `usecols` argument. The remaining columns that are present in the file will be ignored.

The data looks the same whether it is read from a CSV or Excel file:

![csv data 02](./ch6_files/data02.JPG)

### 6.2.2 Reading data from a URL

Instead of manually downloading the file first, we could read it from the URL directly:

```
url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
df3 = pd.read_csv(url, sep=';')
```

The code above, will generate a dataframe that looks like:

![url data 03](./ch6_files/data03.JPG)

#### Reading data from a json file

We will now upload data stored in json format. You may encounter this file format when working with API or web services as it is mostly used to interchange data among applications. In our case, the json data we'll upload is available on [this URL](https://cdn.jsdelivr.net/gh/timruffles/gapminder-data-json@74aee1c2878e92608a6219c27986e7cd96154482/gapminder.min.json).

- Pandas includes a specific function to process json files: pd.read_json()

```
url = 'https://cdn.jsdelivr.net/gh/timruffles/gapminder-data-json@74aee1c2878e92608a6219c27986e7cd96154482/gapminder.min.json'
df4 = pd.read_json(url)
```

The code above, will generate a dataframe that looks like:

![json_data_04](./ch6_files/json_data_04.JPG)

## 6.3 Data wrangling basics

Once we have our dataframe available, some transformations may be needed in order to use the data in our app.
There is a vast list of methods and functions that can be applied to Pandas dataframes (you may refer to [this documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) for more info). In this section we'll cover a few wrangling techniques that are most commonly used when building Dash apps.

The below examples are based on the ["df3" dataframe](https://open-resources.github.io/dash_curriculum/part2/chapter6.html#reading-data-from-a-url) that we created above by reading data from a URL.

#### Unique values

When exploring data, we may often need to identify the unique values in each column:

```
df3['continent'].unique()
```

With the above command, an array containing the unique values in the column will be displayed.

![df3_unique](./ch6_files/df3_unique.jpg)

#### Slicing

The .loc method can be used in Pandas dataframes to slice or filter the data based on boolean conditions (True, False).
The `.loc[rows, columns]` method will filter based on row conditions (to be specified in the first bracket ()) and on column conditions (to be specified in the second bracket ()).
Let's see two examples:

```
df3_Slice1 = df3.loc[(df3['continent']=='Americas'), :]

df3_Slice2 = df3.loc[(df3['continent']=='Americas') & (df3['year'].isin([2002,2007])), ['country','year','pop']]
```
The first command will filter the df3 dataframe picking rows that have 'Americas' as continent. The `:` indicates that we don't want to specify any column-filtering conditions, hence, all columns will be selected. This is just an example to see how the syntax works and normally we would use `df3[df3['continent']=='Americas']` if we want to select all columns while filtering only the rows.

The second command adds more row-filtering conditions: rows will be filtered based on American continent and also on 'year', which must be either 2002 or 2007. Additionally, only three columns will be saved into `df3_Slice2`, namely: country, year, pop. The second command results in:

![df3_Slice2](./ch6_files/df3_Slice2.JPG)

#### Grouping

The `.groupby` method can be used on Pandas dataframes to aggregate data: data will be split according to the unique values in the grouped fields, allowing to perform computations on each group.

As an example, let's calculate the yearly population by continent, summing up the populations from all countries within each continent:

```
df3.groupby(['continent','year'])['pop'].sum()
```

The result will look like:

![df3_groupby1](./ch6_files/df3_groupby1.JPG)

## 6.4 Using data in the App

Let's now see how to use the data we've uploaded through a couple of examples.

### Example 1

In the below app, we import the ["df3" dataframe](https://open-resources.github.io/dash_curriculum/part2/chapter6.html#reading-data-from-a-url) that we created above, and use the list of unique continents to create the "options" of a Dropdown component. Using the callback, an output message is shown based on the selected dropdown value.

```
# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# Read in data
url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
df3 = pd.read_table(url, sep=';')

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
continent_dropdown = dcc.Dropdown(id='continent-dropdown', options=[c for c in df3.continent.unique()])
continent_output = html.Div(id='continent-output')

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([continent_dropdown], width=8)]),
        dbc.Row([dbc.Col([continent_output], width=8)])
    ]
)

# Configure callback
@app.callback(
    Output(component_id='continent-output', component_property='children'),
    Input(component_id='continent-dropdown', component_property='value')
)
def dropdown_sel(value_dropdown):
    selection = (f'You've selected: {value_dropdown}')
    return selection

# Run the App
if __name__ == '__main__':
    app.run_server()
```
The above code will generate the following App:

![Example 1](./ch6_files/Example01.JPG)

### Example 2

We will now build upon the previous example, including a second dropdown, linked to the first one.
The second dropdown will show the list of countries from the continent selected in the first dropdown.
Based on the selected country, the total population will be displayed.

```{note}
This is often referred to as the chained callback. See [Dash documentation](https://dash.plotly.com/basic-callbacks#dash-app-with-chained-callbacks) for more examples.
```

```
# Import packages
from dash import Dash, dcc, Input, Output, html
import dash_bootstrap_components as dbc
import pandas as pd

# Import data
url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
df3 = pd.read_table(url, sep=';')
y=2007
df3 = df3.loc[(df3['year']==y), :]

# Initialise the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
_header = html.H1(children = 'Population by country in 2007', style = {'textAlign' : 'center'})
continent_dropdown = dcc.Dropdown(id = 'continent-dropdown', placeholder = 'Select a continent', options = [c for c in df3.continent.unique()])
country_dropdown = dcc.Dropdown(id = 'country-dropdown', placeholder = 'Select a country')
_output = html.Div(id = 'final-output')

# app Layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([_header], width=8)]),
        dbc.Row([dbc.Col([continent_dropdown], width=8)]),
        dbc.Row([dbc.Col([country_dropdown], width=6)]),
        dbc.Row([dbc.Col([_output], width=6)])
    ]
)


# Configure callbacks
@app.callback(
    Output(component_id='country-dropdown', component_property='options'),
    Input(component_id='continent-dropdown', component_property='value')
)
def country_list(continent_selection):
    country_options = [c for c in df3.loc[df3['continent']==continent_selection, 'country'].unique()]
    return country_options


@app.callback(
    Output(component_id='final-output', component_property='children'),
    Input(component_id='country-dropdown', component_property='value'),
prevent_initial_call=True
)
def pop_calculator(country_selection):
    pop_value = df3.loc[df3['country']==country_selection]
    pop_value = pop_value.loc[:, 'pop'].values[0]  # select only first value in pop column
    output = ('The population in '+country_selection+' was: '+pop_value.astype(str))
    return output

# Run the app
if __name__ == '__main__':
    app.run_server()
```

```{tip}
In the code above, you may notice that in the second callback we have added this prop: `prevent_initial_call=True`. This was necessary, since the 'country-dropdown' component doesn't have any default option (the options, in fact, depend on the first dropdown selection). By default, Dash calls every callback when initialising the app. We want to prevent this initial call, as Dash wouldn't find any input value for this callback.
```

The above code will generate the following app:

![fina-app](./ch6_files/chap6-final-app.gif)

## Summary
In this chapter, we have explored several options to upload data into a pandas dataframe that will be used inside a Dash app. We went through some basic data wrangling techniques that prepare our data for usage by Dash components.
In the next chapter we will dive into data visualisation, exploring the Plotly Express graphing library.
