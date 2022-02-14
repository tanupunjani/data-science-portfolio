#!/usr/bin/env python
# coding: utf-8

# In[154]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[155]:


df = pd.read_json('modcloth_final_data.json', lines=True)
df


# In[156]:


#check for missing value
df.isna().sum()


# In[157]:


df.info()


# In[158]:


df.info()


# # Handling missing values

# In[159]:


## Create a function to store all the columns having missing values.
## Use simple imputer 
## Check if the imputation was done correctly.


# In[160]:


#You can also drop those columns
new_data = df.dropna(axis=1)


# In[161]:


new_data


# In[162]:


#Create a function to do the same
data_with_null = [col for col in df.columns
                 if df[col].isnull().any()] 


# In[ ]:





# In[163]:


new_data = df.drop(data_with_null, axis=1)


# In[164]:


new_data


# In[165]:


df.isna().sum()


# In[166]:


df.info()


# In[167]:


from sklearn.impute import SimpleImputer
df_numerical = df.select_dtypes(exclude='object').isna()


# In[168]:


im = SimpleImputer(strategy="mean")
new_numerical_data = pd.DataFrame(im.fit_transform(df_numerical))


# In[169]:


new_numerical_data.head()


# In[170]:


df.isna().sum()


# In[171]:


#Handling missing values
df['waist'].fillna(df['waist'].mean(), inplace=True)
df['quality'].fillna(df['quality'].mean(), inplace=True)
df['hips'].fillna(df['hips'].mean(), inplace=True)
df['bra size'].fillna(df['bra size'].mean(), inplace=True)
df['user_id'].fillna(df['hips'].mean(), inplace=True)
df['shoe size'].fillna(df['bra size'].mean(), inplace=True)


# In[172]:


df.isna().sum()


# In[177]:


from sklearn.impute import SimpleImputer
im = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
x = im.fit_transform(df)
df_new = pd.DataFrame(x)


# In[178]:


df_new.isna().sum()


# # Categorical encoding

# In[176]:


df_new.dtypes


# In[77]:


df2 = df_new.iloc[:60,:]


# In[78]:


df2


# In[79]:


df3 = pd.get_dummies(df2)


# In[90]:


df3.shape


# In[81]:


from sklearn.preprocessing import StandardScaler


# In[82]:


scaler = StandardScaler()
scaler.fit(df3)


# In[83]:


df4 = scaler.transform(df3)
df4


# In[84]:


from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()

df5=pd.DataFrame(minmax.fit_transform(df3))


# In[85]:


corr = df5.corr()
corr


# In[86]:


sns.heatmap(corr)


# # Feature Selection
# 1. Variance threshold
#  

# In[88]:


from sklearn.feature_selection import VarianceThreshold
var = VarianceThreshold(threshold=.8*(1 - 0.8))

var.fit_transform(df5)


# In[89]:


df5.shape


# In[138]:


titanic = pd.read_csv('titanic.csv')


# In[ ]:





# In[92]:


titanic


# In[93]:


titanic.isna().sum()


# In[139]:


titanic['Age'].fillna(titanic['Age'].mean(),inplace=True)


# In[140]:


from sklearn.impute import SimpleImputer
sm = SimpleImputer(missing_values=np.nan,strategy="most_frequent")
x = sm.fit_transform(titanic)
df_new = pd.DataFrame(x)


# In[141]:


df_new.isna().sum()


# In[142]:


df_new.head()


# In[143]:


titanic = pd.read_csv('titanic.csv')
titanic


# In[144]:


df_new.columns =titanic.columns


# In[145]:


df_new


# In[152]:


df_new.isna().sum()


# In[153]:


final = pd.get_dummies(df_new)

