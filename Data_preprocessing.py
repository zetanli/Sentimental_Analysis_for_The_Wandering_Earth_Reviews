
# coding: utf-8

# In[102]:


import re
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
import numpy as np
import collections


# In[3]:


### import dataset
imbd_rev = pd.read_csv('imbd_reviews.csv')
imbd_rev = imbd_rev.drop(columns = 'Unnamed: 0')
imbd_rev=imbd_rev[imbd_rev['scores']>=0]


# In[90]:


stop_words = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()


# In[85]:


### remove punctuation characters/numbers/other characters 
def remove_characters(reviews):
    ##reviews is a list or panda series
    after_char=list()
    for items in reviews:
        after_char.append(re.sub(r'[\W]',' ',items).lower())
    return after_char

###tokenize

def tokenizer(after_char):
    tokens_set=list()
    for items in after_char:
        tokens_set.append(items.split())
    return tokens_set

###lemmatize
def lematizer(tokens_set):
    for tokens in tokens_set:
        for idx in range(len(tokens)):
            tokens[idx]=wordnet_lemmatizer.lemmatize(tokens[idx],pos="v")
    
### remove stop words            
def remove_stopWords(tokens_set):
    set2=list()
    for tokens in tokens_set:
        token2=list()
        for word in tokens:
            if word not in stop_words:
                token2.append(word)
        set2.append(token2)
    return set2

###vectorize
def Vectorizer(tokens_set,counts_threshold):
    ###grab all words
    cols1=list()
    for i in tokens_set:
        cols1.extend(i)
    counts=dict(collections.Counter(cols1))
    cols=list()
    for key in counts:
        if counts[key]>counts_threshold:
            cols.append(key)
    cols.append('UNK')
    rev_count=len(tokens_set)
    #initialize a matrix(data frame)
    vect=pd.DataFrame(0,index=range(rev_count),columns=cols)
    for i in range(len(tokens_set)):
        for j in tokens_set[i]:
            try:
                vect[j][i]+=1
            except KeyError:
                vect['UNK'][i]+=1
    return vect


# In[168]:


def textProcess(texts,min_counts):
    ###texts should be a list or panda series
    step1=remove_characters(texts)
    step2=tokenizer(step1)
    lematizer(step2)
    step3=remove_stopWords(step2)
    results=Vectorizer(step3,min_counts)
    return results


# In[184]:


token_dt=textProcess(imbd_rev['contents'],30)
df = pd.concat([token_dt.reset_index(drop=True), imbd_rev['scores'].rename('Movie_Scores').reset_index(drop=True)], axis=1)

