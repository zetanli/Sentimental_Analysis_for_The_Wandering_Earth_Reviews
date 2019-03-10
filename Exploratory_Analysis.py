
# coding: utf-8

# In[1]:


import wordcloud
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_preprocessing import tokens


# In[8]:


#load data that we scrapped
imbd_rev=pd.read_csv('imbd_reviews.csv')
###word cloud
reviewcontents = ''
for i in imbd_rev['contents']:
    reviewcontents=reviewcontents+' '+i
reviewstitle = ''
for i in imbd_rev['titles']:
    reviewstitle = reviewstitle+' '+i


# In[9]:


tokens_text=''
for i in tokens:
    for j in i:
        tokens_text=tokens_text+' '+j


# In[10]:


##contents
wc_cont = wordcloud.WordCloud(max_font_size = 50, max_words = 100, background_color = "white").generate(tokens_text)
plt.imshow(wc_cont, interpolation = 'bilinear')
plt.axis("off")
plt.show()


# In[11]:


##scores

##average

mean_score = imbd_rev.scores.mean()



# In[12]:


##distribution
n,bins,patches = plt.hist(imbd_rev.scores,bins=10,density=True,alpha=0.7)
sns.kdeplot(imbd_rev.scores)
plt.axvline(x = mean_score,linestyle = '--',color = 'r')
plt.title('The wandering earth score distribution')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.xlim(0,10)
plt.show()

