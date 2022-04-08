# Chapter 6 - Working with Data in Dash

Overview introduction placehoder.

## Learning Intentions

In this chapter we intend you to learn:

```{admonition} Learning Intentions

- how to read data from excel or csv files to a Pandas dataframe
- loading a dataframe from a URL
- creating your own Pandas dataframe from scratch in the Python app script
- using data from an Application Programming Interface (API)
- perform minimal data wrangling inside the app, and learn the trade-offs with speed compared to working with pre-processed data
```

## Incorporating data into Dash apps

- Where to incorporate data within the app   (Make sure to incorporate data at the begiingn of the app, above the layout. This is considered global data. )
- Creating pandas dataframes (briefly define dataframe and pandas and show the python statement to create an empty df)
- Ways of uploading data into the dataframe (files, URL, API)

## Create data into Pandas dataframes

- Show how to include data into the dataframe using dictionaries

df = pd.DataFrame([.....])
print(head())

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

## Use cases for pre-processing data



## App at the end

dropdown with country data options

At the end of this chapter, [here is a zipped file](https://sportsnet.ca) of what your app should look like.
