#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
df = pd.read_csv(url, sep ="\t")


# In[4]:


df.head()


# In[5]:


chipo = df


# In[6]:


#number of observations
chipo.shape 
chipo.info


# In[7]:


chipo.columns


# In[8]:


chipo.shape[1]


# In[9]:


#count_row = df.shape[0]  # gives number of row count
#count_col = df.shape[1]  # gives number of col count


# In[10]:


chipo.columns


# In[11]:


chipo.index


# In[12]:


chipo.head()


# In[13]:


chipo['quantity'].value_counts()


# In[14]:


#Most ordered item
c = chipo.groupby(by="item_name")


# In[15]:


c = c.sum()


# In[16]:


c = c.sort_values(by="quantity",ascending=False)


# In[17]:


c.head(1)


# In[18]:


choice = chipo.groupby(by="choice_description")
choice = choice.sum()
choice = choice.sort_values(by="quantity", ascending=False)
choice.head(1)


# In[19]:


chipo["quantity"].sum()


# In[20]:


chipo["item_price"].dtype


# In[21]:


function = lambda x : float(x[1:-1])
chipo.item_price = chipo["item_price"].apply(function)


# In[22]:


chipo.item_price.dtype


# In[23]:


chipo.item_price.sum()


# In[24]:


revenue = (chipo["quantity"] * chipo["item_price"]).sum()


# In[25]:


revenue


# In[26]:


print("Revenue was $" + str(np.round(revenue,2)))


# In[27]:


chipo['revenue_per_order'] = (chipo["quantity"] * chipo["item_price"])


# In[28]:


order_grouped = chipo.groupby(by="order_id").sum()

order_grouped
# In[29]:


order_grouped.mean()['revenue_per_order']


# In[30]:


chipo.head()


# In[31]:


chipo['item_name'].value_counts().count()


# In[32]:


chipo


# In[33]:


url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep = "\t")
chipo


# In[34]:


chipo(['item_products']  10)


# In[35]:


#Pandas Cheatsheet


# In[36]:


pd.melt(chipo)


# In[37]:


chipo


# In[40]:


#Spread rows into the columns
chipo.pivot


# In[43]:


#Order rows by values of a column(low to high)
chipo.sort_values(by="item_price")


# In[46]:


#Rename a column
chipo.rename(columns = {'order_id':'id'})


# In[47]:


chipo.rename(columns = {'id':'order_id'})


# In[48]:


#Sort the index of the dataframe
chipo.sort_index()


# In[49]:


#Reset the index of DataFrame to row numbers, moving index to columns
chipo.reset_index()


# In[52]:


#Drop columns from dataframe
chipo.drop(columns=['quantity'])


# In[58]:


#Extract column that meets the logical criteria
chipo[chipo.order_id > 7 ]


# In[59]:


#REmove duplicates
chipo.drop_duplicates()


# In[62]:


#Randomly select fraction of rows
chipo.sample()


# In[63]:


#Select and order bottom n entries
chipo.nsmallest(4, 'quantity')


# In[65]:


#select and order top n entries
chipo.nlargest(4, 'order_id')


# In[67]:


#Select multiple columns with specific names
chipo[['order_id','item_name']]


# In[68]:


# Select single column with specific name.
chipo[['order_id','item_name']]


# In[70]:


#Select columns whose name matches regular expression regex
chipo.filter(regex='Bowl$')


# In[79]:


#assess a single value by row and column
chipo.iat[4,2]


# In[80]:


chipo.sum()


# In[ ]:




