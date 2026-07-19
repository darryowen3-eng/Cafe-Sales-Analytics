#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
from sqlalchemy import create_engine

engine=create_engine(
    "postgresql://powerbi:darry%402005@localhost/analytics"
)

df = pd.read_csv("clean_cafe_sales.csv")

df.to_sql(
    "cafe_sales",
    engine,
    if_exists="replace",
    index=False
)


# In[ ]:




