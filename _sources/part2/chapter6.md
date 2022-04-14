# Chapter 6 - Working with Data in Dash

## What you will learn
In this chapter we will introduce data into Dash Apps.
We will show how to import data into the App code and we will go through different ways to create and populate Pandas dataframes. We will also show some basic data wrangling techniques that are often used to prepare data for reporting.

By the end of the chapter you'll be comfortable with writing and editing this code, in order to use your own data into your Dash App:

```
# Final code placeholder
```
[Download the file]

---

## 6.1 Where to import data within Dash apps
The data which is imported into Dash apps will be used by multiple objects: Dash components, callbacks, tables, etc.
For this reason, we recommend to import data before initialising the app. In this way, the data will be globally available to all objects that are created in the code.

There are several types of objects that can be used to store our data: numpy arrays, dictionaries, Pandas dataframes, etc. We will be using Pandas dataframes, that can be created in the following ways.

An empty dataframe is created with the code below::
```
test_data = pd.DataFrame()
```

Some mock-up data can be added using a dictionary, in this way:
```
test_data = pd.DataFrame({'Country':['United States','Norway','Italy','Sweden','France'],
                         'Country Code':['US','NO','IT','SE','FR']})
```
(In the code above, the dictionary keys will be the field names of the Pandas dataframe).

## 6.2 Uploading data into a dataframe
In case our data is available on files or on the internet, we will read the data from the source and upload it into the dataframe.
There are several ways of uploading data to Pandas dataframes, we will be focusing on these methodologies:
- reading data from files (.xls, .csv)
- reading data from URL
- using Dash dcc.Upload component

```{note}
If you need some test dataset to play with, consider using the Plotly Express pre-loaded data, such as Gapminder, which can be added to your App with these commands:

import plotly.express as px
df = px.data.gapminder()
```

### 6.2.1 Reading data from files

#### Excel files
We will now upload an Excel file ([link](https://github.com/open-resources/dash_curriculum/blob/main/tutorial/part2/ch6_files/data_01.xlsx)) - extracted from the Gapminder data - into a dataframe:

```
filepath = 'C:/Users/User1/Downloads/data_01.xlsx'
df1 = pd.read_excel(filepath, sheet_name='Sheet1')
df1
```
- The code above would work in situations where you have some local files (e.g. into the Downloads folder) that you want to use in the App
- We uploaded one Excel tab (named "Sheet1") to a data frame called "df1".
- After the data upload, the dataframe looks like the following:

![Excel data 01](./ch6_files/data01.JPG)

#### csv files
We will now upload the same data from above, but from a .csv file ([link](https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_02.csv)).

```
filepath = 'C:/Users/User1/Downloads/data_02.csv'
col_names = ['country','continent','year','pop']
df2 = pd.read_csv(filepath, sep='\|\?\|', usecols=col_names)
df2.head()
```

- In the .csv file used, the data has some different column separators: '|?|'. With the "sep" argument, we have defined which characters should be considered field separators. (We used the the backslash " \ " as an escape character in order to properly interpret the field separator).
- We have also selected a subset of columns to be uploaded, with the "usecols" argument. With this argument, the remaining columns that are present in the file will be ignored
- After the data upload, the dataframe looks like the following:

![csv data 02](./ch6_files/data02.JPG)

### 6.2.2 Read data from a URL
We will now upload the same data from above, but from ([this ULR](https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt)) (containing a raw .txt file).

```
url = 'https://raw.githubusercontent.com/open-resources/dash_curriculum/main/tutorial/part2/ch6_files/data_03.txt'
df3 = pd.read_table(url, sep=';')
df3.head()
```

The code above, will generate a dataframe that looks like:

![url data 03](./ch6_files/data03.JPG)

### 6.2.3 Read data from dcc.Upload

XXX



## 6.3 Data wrangling basics
Once we have our dataframe available, some transformations may be needed in order to use this data on our App.
There is a vaste list of methods and functions that can be applied to Pandas dataframes ([link](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) to Pandas documentation). In this section we'll cover some of the basic data wrangling techniques which are ofter necessary to do some data exploration, slice or filter our data and aggregate it.

We'll show some data wrangling examples based on the "df3" dataframe that we created above, reading data from a URL.

#### Unique values
When exploring data, we may often need to identify the unique values in our columns:

```
df3.continent.unique()
```
With the above command, an array containing the unique values in the column will be displayed.
![df3_unique](./ch6_files/df3_unique.JPG)

#### Slicing
The .loc method can be used on Pandas dataframes, allowing to slice or filter them based on boolean conditions. 
The ```.loc[(), ()]``` method allows to filter based on row conditions (to be specified in the first bracket ()) and on column conditions (to be specified in the second bracket ()).
Let's see two examples:

```
df3_Slice1 = df3.loc[(df3['continent']=='Americas'), :]

df3_Slice2 = df3.loc[(df3['continent']=='Americas') & (df3['year'].isin([2002,2007])), ['country','year','pop']]
df3_Slice2.head()
```
- The first command will filter the df3 dataframe picking rows that have 'Americas' as continent. The ':' indicates that we don't want to specify any column-filtering conditions, hence, all columns will be selected.
- The second command, adds more row-filtering conditions: rows will be filtered based on American continent and also on 'year', which must be either 2002 or 2007. Additionally, only three columns will be saved into df3_Slice2, namely: country, year, pop. The second command resul will look like:

![df3_Slice2](./ch6_files/df3_Slice2.JPG)

#### Grouping
The .groupby method can be used on Pandas dataframes to aggregated data: data will be splitted according to the unique values in the grouped fields allowing to perform computations on each group. 

As an example, let's calculate the yearly population by continent, summing up the populations from all countries within each continent:
```
df3.groupby(['continent','year'])['pop'].sum()
```
- The data will be aggregated by continent and year, summing up 'pop' column. The result will look like:

![df3_groupby1](./ch6_files/df3_groupby1.JPG)


## 6.4 Using data in the App

- Show an example of a Dropdown object, with the option list loaded from the dataframe

dropdown = dcc.Dropdown(id='our-dropdown', options=['My First app', 'Welcome to the App', 'This is the title'], value='My First app')

note: show how to write data into csv


## Summary


App code at the end:
dropdown with country data options

At the end of this chapter, [here is a zipped file](https://sportsnet.ca) of what your app should look like.
