#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from tensorflow import keras as tf
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("online_retail.csv")


# In[3]:


df


# In[4]:



df.dropna(inplace=True)


# In[5]:


df.drop_duplicates(inplace=True)


# In[6]:


df.fillna(0, inplace=True)


# In[7]:


df.drop("StockCode",axis=1,inplace=True)


# In[8]:


df


# In[9]:


df["Total_sales"] = df["Quantity"] * df["Price"]


# In[10]:


df


# In[15]:


product_pairs = df.groupby(['Customer ID', 'Description'])['Price'].count()
product_pairs


# In[16]:


df['year'] = pd.DatetimeIndex(df['InvoiceDate']).year
product_sales_by_year = df.groupby(['Description', 'year'])['Price'].sum()


# In[17]:


product_sales_by_year


# In[18]:


customer_sales = df.groupby('Customer ID')['Price'].sum()
customer_sales


# In[21]:


for Description, data in df.groupby('Description'):
    plt.scatter(data['InvoiceDate'], data['Price'], label=Description)

plt.xlabel('Invoice Date')
plt.ylabel('Price')
plt.title('Purchase product by Date')

plt.show()


# In[ ]:




