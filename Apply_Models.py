
# coding: utf-8

# In[1]:


import pandas as pd
from Data_preprocessing import df
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error


# In[12]:


GBDT_C=GradientBoostingRegressor(loss='ls')


# In[16]:


GBDT_C.fit(df.iloc[:,:118],df.iloc[:,118])


# In[29]:


pred_y=GBDT_C.predict(df.iloc[:,:118])
y=df.iloc[:,118]


# In[30]:


train_mape = sum([abs((y[i]-pred_y[i])/y[i])  for i in range(392)  ])/392

