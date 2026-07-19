#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

df = pd.read_csv("clean_cafe_sales.csv")

avg_revenue = df["Total Spent"].mean()

# Grouping items and find their total sum
grouped_item = (df.groupby("Item")["Total Spent"].sum()
                .reset_index(name = "Total Revenue")
                .sort_values(["Total Revenue"],ascending=False)

    )
grouped_item = grouped_item[grouped_item["Item"] != "Unknown"] # Excluding the unknown from the df of grouped items
print(grouped_item)
print()

print("AVG Revenue:",avg_revenue)
print()

def avg_classify(Total_Revenue):
        if Total_Revenue > avg_revenue:
            return "High"
        else:
            return "Low"

df["Revenue Rating"] =  df["Total Spent"].apply(avg_classify)
print(df.head())

leading_item = df[df["Total Spent"] > avg_revenue].nlargest(1, "Total Spent")

print("==============TOP ITEM=============\n",leading_item)
print()
print("========== SUMMARY STATISTICS ==========\n",df.describe())

df.to_csv("cafe_sales_features.csv")
print("csv created")


# In[ ]:




