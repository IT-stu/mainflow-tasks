import pandas as pd
data=pd.read_csv("01.Data Cleaning and Preprocessing.csv") #loading CSV file
data.info

print(data.describe())
data = data.drop_duplicates() # clean the Duplicate value
print(data.isnull())
print(data.isnull().sum())
print(data.notnull())
print(data.isnull().sum().sum())

data2 = data.fillna(value=0) #Another Way to cleaning

data3 = data.fillna(method="pad") #Another Way to cleaning

data4 = data.fillna(method="bfill") #Another Way to cleaning

import numpy as np
from scipy import stats
print(data2.columns)

data2.drop(["Observation"],axis=1, inplace=True)
print(data2.columns)

Q1=data2.quantile(0.25)
Q2=data2.quantile(0.75)
IQR =Q3-Q1
print(IQR)

data6 = data2[~((data2<(Q1-1.5*IQR))|((data2<(Q2+1.5*IQR))).any(axis=1))]
print(data6)
