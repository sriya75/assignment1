import pandas as pd  # importing pandas and numpy
import numpy as np


df = pd.read_csv("Book1.csv")  # converting spreadsheet to dataframe

print(type(df['Close'][0]))    # checking the datatype of 0th index of column- 'close'


df['Close']=df['Close'].str.replace(',','')    # removing the comma (,) from the values
df['Open']=df['Open'].str.replace(',','')
df['High']=df['High'].str.replace(',','')
df['Low']=df['Low'].str.replace(',','')


df['Close'] = df['Close'].astype('float')    # converting strings to float datatype-
df['Open'] = df['Open'].astype('float')
df['High'] = df['High'].astype('float')
df['Low'] = df['Low'].astype('float')


print(df.dtypes)  # checking the datatype of all the columns


index = range(0, 516)    # creating a new column in existing dataframe
df['index'] = index


print(df[df['index'] >= 20]['Close'].mean())  # ques 1 -- Make a average which has last 21 days close price.
print(df[df['index'] >= 50]['Close'].mean())  # ques 2 -- Make a average which has last 50 days close price.
print(df[df['Open'] == df['High']])           # ques 3 -- Give a data set which has all the open=high values.
print(df[df['Open'] == df['Low']])            # ques 4 -- Give a data set which has all the open=low values.