#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from Data_preprocessing import df,df_bigram
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
import random


# In[42]:


##unigram
GBDT_C=GradientBoostingRegressor(loss='ls')
GBDT_C.fit(df.iloc[:,:382],df.iloc[:,382])
pred_y=GBDT_C.predict(df.iloc[:,:382])
y=df.iloc[:,382]
train_mape = sum([abs((y[i]-pred_y[i])/y[i])  for i in range(392)  ])/392
train_mape


# In[3]:


##classification
class_uni=list()
for i in df.iloc[:,382]:
    if i>0 and i<5:
        class_uni.append(0)
    elif i>=5 and i<8:
        class_uni.append(1)
    else:
        class_uni.append(2)
lr=LogisticRegression(multi_class='multinomial',solver ='newton-cg')
lr.fit(df.iloc[:,:382],class_uni)
lr.score(df.iloc[:,:382],class_uni)


# In[17]:


df['class']=class_uni
test_idx=random.sample(range(392), 40)
train_idx=[i for i in range(392) if i not in test_idx]
test_df2 = df.iloc[test_idx]
train_df2 = df.iloc[train_idx]


# In[22]:


lr2=LogisticRegression(multi_class='multinomial',solver ='newton-cg')
lr2.fit(train_df2.iloc[:,:382],train_df2.iloc[:,383])
lr2.score(train_df2.iloc[:,:382],train_df2.iloc[:,383])


# In[23]:


lr2.score(test_df2.iloc[:,:382],test_df2.iloc[:,383])


# In[24]:


###bigram
GBDT_C=GradientBoostingRegressor(loss='ls')
GBDT_C.fit(df_bigram.iloc[:,:626],df_bigram.iloc[:,626])
pred_y=GBDT_C.predict(df_bigram.iloc[:,:626])
y=df_bigram.iloc[:,626]
train_mape = sum([abs((y[i]-pred_y[i])/y[i])  for i in range(392)  ])/392
train_mape


# In[6]:


###classification:
###split score into 3 grade
###1-4  don't like as 0
###5-7  medium     as 1
###8-10 very like  as 2


# In[30]:


class_bigram=list()
for i in df_bigram.iloc[:,626]:
    if i>0 and i<5:
        class_bigram.append(0)
    elif i>=5 and i<8:
        class_bigram.append(1)
    else:
        class_bigram.append(2)


# In[31]:


lg=LogisticRegression(multi_class='multinomial',solver ='newton-cg')
lg.fit(df_bigram.iloc[:,:626],class_bigram)
lg.score(df_bigram.iloc[:,:626],class_bigram)


# In[37]:


df_bigram['class']=class_bigram
test_idx=random.sample(range(392), 40)
train_idx=[i for i in range(392) if i not in test_idx]
test_df2 = df_bigram.iloc[test_idx]
train_df2 = df_bigram.iloc[train_idx]


# In[38]:


lg2=LogisticRegression(multi_class='multinomial',solver ='newton-cg')
lg2.fit(train_df2.iloc[:,:626],train_df2.iloc[:,627])
lg2.score(train_df2.iloc[:,:626],train_df2.iloc[:,627])


# In[39]:


lg2.score(test_df2.iloc[:,:626],test_df2.iloc[:,627])
##result is not too bad


# In[ ]:




