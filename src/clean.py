#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
df = pd.read_csv("dirty_cafe_sales.csv")
print(df.head())
#print(df.info())
#print(df.isnull().sum())
#print(df.duplicated().sum())
columns = [
    "Item",
    "Quantity",
    "Price Per Unit",
    "Total Spent",
    "Payment Method",
    "Location",
    "Transaction Date"
]
missing_values = ["r'^\s*$'","NONE", "N/A", "NULL", "NAN","ERROR"]
df[columns] = df[columns].replace(missing_values,np.nan,regex = True)


numeric = [
    "Quantity",
    "Price Per Unit",
    "Total Spent",
]
for col in numeric:
    df[col]=df[col].fillna(0).replace("UNKNOWN",0) 


content = [
    "Item",
    "Payment Method",
    "Location"
]
for col in content:
    df[col]=df[col].fillna("Unknown").str.strip().str.title()

df["Transaction Date"] = (
    pd.to_datetime(df["Transaction Date"],errors='coerce',format='mixed')
    .fillna(pd.Timestamp('2026-01-01'))
)

df = df.sort_values(
    ["Item", "Transaction Date"]
)

df.to_csv("clean_cafe_sales.csv", index=False)

print("a csv generated")
report ={
    "ROWS":len(df),
    "COLUMNS":len(df.columns),
    "DUPLICATES":df.duplicated().sum(),
    "MISSING VALUES":df.isnull().sum()
}


for k, v in report.items():
    print(k, "\n", v)
print()    
print(df.head())


# In[ ]:




