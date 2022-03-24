# Chapter 7: Wrangling data

## What you will learn
In this chapter we will explore data data cleaning, processing, and wrangling


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
