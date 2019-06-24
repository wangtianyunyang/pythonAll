# coding=utf-8
import pandas as pd
from pandas import DataFrame

data=pd.read_csv("data/Fremont.csv",index_col="Date",parse_dates=True)
print(data.head())

data.columns=["West","East"]
print(data.head())
data["total"]=data["West"]+data["East"]
print(data.head())
pivoted_table=data.pivot_table("total",index=data.index.time,columns=data.index.date)
print(pivoted_table.head())







