import pandas as pd

raw_data = pd.read_csv('temp_data.csv')
raw_data['time'] = pd.to_datetime(raw_data['time'],unit='s')
print(raw_data.head())

for index, row in raw_data.iterrows():
    
    df_cal.loc[len(df_cal.index)] = [row['Serial Number'], int(row['Value'])]     
