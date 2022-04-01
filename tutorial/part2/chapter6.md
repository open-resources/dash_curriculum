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


## incorporating data into our apps
Make sure to incorporate data at the begiingn of the app, above the layout. This is considered global data. 

show example of code:


## Read data from Excel or CSV

df = pd.read_csv()
print(head())
print(df.columns)

dropdown = dcc.Dropdown(id='our-dropdown', options=['My First app', 'Welcome to the App', 'This is the title'], value='My First app')

note: show how to write data into csv


## Load data from a URL

 df = pd.read_csv("https://www.website.com")
print(head())

## Create a simple Pandas dataframe

df = pd.DataFrame([.....])
print(head())


## Connect to API data

df = 


## Data wrangling in Dash

groupby
slicing in pandas
filtering

## Use cases for pre-processing data



## App at the end

dropdown with country data options

At the end of this chapter, [here is a zipped file](https://sportsnet.ca) of what your app should look like.
