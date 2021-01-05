#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

data = pd.read_csv


# In[4]:


#Remplacement des valeurs vides par la moyenn
data = data.replace('unknown', np.nan)

data('prod_cost') = pd.to_numeric(data['prod_cost'])
print(data['prod_cost'])
data('prod_cost') = data('prod_costr').replace(np.nan, data['prod_cost'].mean())
print(data['prod_cost'])


# In[5]:


data = pd.read_csv('mover_market_snapshot.csv', sep=";")
data('warranty')=pd.to_numeric(data["warranty"].str[0])
print(data('warranty'))


# In[6]:


data=pd.read_csv('mover_market_snapshot.csv', sep=";")
data.product_type= pd.Categorical(data.product_type)
data['product_type']=data.product_type.cat.codes
data['product_type']= pd.factorize(data['product_types'])[0] + 1
print(data['product_type'])


# In[7]:


df = pd.read_csv('mover_market_snapshot.csv', rep=";")
df = pd.get_dummies(df.product_type, prefix='product_type')
df.head()


# In[ ]:




