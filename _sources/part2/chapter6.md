# Chapter 6 - Working with Data in Dash

## What you will learn
In this chapter we will introduce data into Dash Apps.
We will show where to import data into the App code and we will go through different ways to create and populate Pandas dataframes. We will also show some basic data wrangling techniques that are often used to aggregate data.

By the end of the chapter you'll be comfortable with writing and editing this code, in order to use your own data into your Dash App:

```
# Final code placeholder
```
[Download the file]

---

## 6.1 Where to import data within Dash apps
The data which is imported into Dash apps will be used by multiple objects: Dash components, callbacks, tables, etc.
For this reason, we recommend to import data before initialising any app. In this way, the data will be globally available to all objects that are created in the later parts of the code.

There are several types of objects that can be used to save our data: numpy arrays, dictionaries, Pandas dataframes, etc. We will be using Pandas dataframes, that can be created in the following ways.

An empty dataframe can be created in this way:
```
test_data = pd.DataFrame()
```

Some mock up data can be added using a dictionary, in this way:
```
test_data = pd.DataFrame({'Country':['United States','Norway','Italy','Sweden','France'],
                         'Country Code':['US','NO','IT','SE','FR']})
```

## 6.2 Uploading data into a dataframe
There are several ways of uploading data to Pandas dataframes, we will be focusing on these methodologies: reading data from files (.xls, .csv), reading data from URL, using Dash through the dcc.Upload component.

```{note}
If you need some test dataset to play with, consider using the px pre-loaded data, such as Gapminder, which can be added to your App with this command
```df = px.data.gapminder()```
```











```{admonition} Learning Intentions

- how to read data from excel or csv files to a Pandas dataframe
- loading a dataframe from a URL
- creating your own Pandas dataframe from scratch in the Python app script
```


## Read data from Excel or CSV

- Show a sample file with few data in it
- Upload data into the dataframe with read_csv explaining how to change properties such as: field separators, using or not using the field names)

df = pd.read_csv()
print(head())
print(df.columns)

## Load data from a URL

- Show an URL with some data in it
- Upload data into the dataframe

df = pd.read_csv("https://www.website.com")
print(head())

## Connect to API data

df = 

## Use of data in the app
- Show an example of a Dropdown object, with the option list loaded from the dataframe

dropdown = dcc.Dropdown(id='our-dropdown', options=['My First app', 'Welcome to the App', 'This is the title'], value='My First app')

note: show how to write data into csv

## Data wrangling in Dash

- Show some examples of basic data wrangling such as:
groupby
slicing in pandas
filtering

- Show performances by performing data wrangling before the app and inside the app, to show the most convenient one.


## App at the end

dropdown with country data options

At the end of this chapter, [here is a zipped file](https://sportsnet.ca) of what your app should look like.
