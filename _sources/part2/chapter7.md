# Chapter 7: Wrangling data

## What you will learn
`Data wrangling` is the processing of `raw` data into a useable form. In this chapter we will explore data cleaning and filtering techniques to produce data useable in our dashbords.

## Exploring Data
Let's start by exploring the data.  We'll learn about several different `Pandas` functions to explore the data.
### Head
Commonly, after we  import the data we'll use the [head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) command to see the top 5 rows of data:
```python
import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

print(raw_data.head())
```
![head](./ch7_files/df_head.png)

We see that this is `time-series` data which contains timestamped temperature readings.  

### Shape
Let's see how big the data is by using [shape](https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.shape.html):

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

print(raw_data.head())
print(raw_data.shape)
```
![shape](./ch7_files/shape.png)

### Info
The Pandas `info` method will return information on the `dataframe` such as: 
- data types
- column names
- memory usage

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

print(raw_data.head())
print(raw_data.shape)
print(raw_data.info())
```
![info](./ch7_files/info.png)


### Describe
The Pandas `describe` method will return statistics on the dataframe such as:
- min/max
- unique values
- count of non-null values in column

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

print(raw_data.head())
print(raw_data.shape)
print(raw_data.info())
print(raw_data.describe())
```
![describe](./ch7_files/describe.png)


## Cleaning Data

### Dropna
From exploring the data we see that some of the values are `null`.  We can drop those values from this dataset because temperature is a slowly changing characteristic:

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

print(raw_data.head())
print(raw_data.shape)
print(raw_data.info())
print(raw_data.describe())

raw_data.dropna(axis=0,inplace=True)
print(raw_data.describe())
```
![dropna](./ch7_files/dropna.png)

There are now `3` less rows after droping the `null` value rows.

### Iterrows and Try-Except

There are several non-numeric values that we'd like to drop from the dataset. First we need to `iterate` through each row in the dataframe with `iterrows()`. Then we'll use Python's [try-expect](https://www.geeksforgeeks.org/python-try-except/) logic test if the row has valid `float` data:

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

print(raw_data.head())
print(raw_data.shape)
print(raw_data.info())
print(raw_data.describe())

raw_data.dropna(axis=0,inplace=True)

print(raw_data.describe())

for index, row in raw_data.iterrows():
    try:
        float(row[2]) # 'temp' column is index 2
    except:
        raw_data.drop(index, axis=0, inplace=True)
        
print(raw_data.head())
```
![isnumeric](./ch7_files/filter_numeric.png)


### Reset Index
After we drop rows the `index` of the dataframe will be off.  Let's reset the index with `reset_index` method:

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

print(raw_data.head())
print(raw_data.shape)
print(raw_data.info())
print(raw_data.describe())

raw_data.dropna(axis=0,inplace=True)

print(raw_data.describe())

for index, row in raw_data.iterrows():
    try:
        float(row[2]) # 'temp' column is index 2
    except:
        raw_data.drop(index, axis=0, inplace=True)

print(raw_data.head())
raw_data.reset_index(drop=True, inplace=True)
print(raw_data.head())
```
![reset_index](./ch7_files/reset_index.png)

## Filter Data
Now that the data is clean we can filter the data.

### Filter by value & astype()
Let's filter the data for temperatures over `18C`.  Notice that we need to use the Pandas method `astype(float)` to use the `temp` data as float data instead of string data. 

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch7_files/temp_data.csv'
raw_data = pd.read_csv(url)

print(raw_data.head())
print(raw_data.shape)
print(raw_data.info())
print(raw_data.describe())

raw_data.dropna(axis=0,inplace=True)

print(raw_data.describe())

for index, row in raw_data.iterrows():
    try:
        float(row[2]) # 'temp' column is index 2
    except:
        raw_data.drop(index, axis=0, inplace=True)

print(raw_data.head())
raw_data.reset_index(drop=True, inplace=True)
print(raw_data.head())

print(raw_data.describe())
fltr_df = raw_data[raw_data['temp'].astype(float) >= 18.5]
print(fltr_df.describe())
```

## Other Resources

[Pandas](https://pandas.pydata.org/) is a data analysis and manipulation library

### Links to use for Pandas data wrangling
- https://towardsdatascience.com/data-wrangling-using-pandas-library-ae26f8bbbdd2
- https://towardsdatascience.com/7-must-know-data-wrangling-operations-with-python-pandas-849438a90d15
- https://realpython.com/python-data-cleaning-numpy-pandas/
- https://betterprogramming.pub/data-wrangling-with-pandas-57f7f72fe73c
- https://medium.com/database-laboratory/data-cleaning-with-pandas-f8f869f63404

## Summary
In this chapter we learned to explore, clean, and filter data.  These techniques are important to real-world data analysis.
