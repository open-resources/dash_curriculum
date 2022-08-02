# Chapter 7: Wrangling data

## What you will learn
`Data wrangling` is the processing of `raw` data into a useable form. In this chapter we will explore data cleaning and filtering techniques to produce data useable in our dashbords.

## Cleaing up a CSV file
[CSV files](https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/) are a common method of storing data that doesn't involve a database.  We'll go through an example where we are given `time-series` temperature measurements in CSV format and need to clean in up.  Download this CSV file:
[csv_file](./ch7_files/temp_data).

Let's start by importing the data using `Pandas` and use the [head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) command to see the top 5 rows of data:
```python
import pandas as pd

raw_data = pd.read_csv('temp_data.csv')

print(raw_data.head()) 
```
![head](./ch7_files/df_head.png)

The huge numbers for the `time` column are in the [Unix time](https://en.wikipedia.org/wiki/Unix_time) format which is `the number of seconds from January 1st 1970`. Let' use `pd.to_datetime` to transform the times into a more readable format:

```python
import pandas as pd

raw_data = pd.read_csv('temp_data.csv')
raw_data['time'] = pd.to_datetime(raw_data['time'],unit='s')

print(raw_data.head()) 
```
![unix time transform](unix_transform.png)

We can also see that one of th evalues in the `Temp (C)` column is invalid: `@!#F`.  We have a few options for this erroneous data:
- Keep the data as is
  - This leads to unusable dataframe columns
- Drop the row of data
  - Dropping rows has greater impact as the number of columns grows
- Insert some value for the erroneous data


In this example we are measuring temperature so it's probably safe to insert the average of the surrounding cells to the erroneous cell.  We'll use Pandas `iterrows()` function to go through the dataframe line by line to replace data:

```python
import pandas as pd

raw_data = pd.read_csv('temp_data.csv')

for index, row in raw_data.iterrows():

```


## Basic Operations with Pandas

[Pandas](https://pandas.pydata.org/) is a data analysis and manipulation library

### Links to use for Pandas data wrangling
- https://towardsdatascience.com/data-wrangling-using-pandas-library-ae26f8bbbdd2
- https://towardsdatascience.com/7-must-know-data-wrangling-operations-with-python-pandas-849438a90d15
- https://realpython.com/python-data-cleaning-numpy-pandas/
- https://betterprogramming.pub/data-wrangling-with-pandas-57f7f72fe73c
- https://medium.com/database-laboratory/data-cleaning-with-pandas-f8f869f63404
```python
df.head() # shows top 5 rows of df
df.types() # shows data type of columns
df.describe() # computes various statistics for each column

# Dealing with missing values
df.isna().sum() # display how many **NA** entries in each row

```

## Processing data

Cleaning, processing, and wrangling data before use
