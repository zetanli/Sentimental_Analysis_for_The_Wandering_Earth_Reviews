
# coding: utf-8



import wordcloud
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#load data that we scrapped
imbd_rev=pd.read_csv('imbd_reviews.csv')
###word cloud
reviewcontents = ''
for i in imbd_rev['contents']:
    reviewcontents=reviewcontents+' '+i
reviewstitle = ''
for i in imbd_rev['titles']:
    reviewstitle = reviewstitle+' '+i



##contents
wc_cont = wordcloud.WordCloud(max_font_size = 50, max_words = 100, background_color = "white").generate(reviewcontents)
plt.imshow(wc_cont, interpolation = 'bilinear')
plt.axis("off")
plt.show()



##titles
wc_titles = wordcloud.WordCloud(max_font_size = 50, max_words = 100, background_color = "white").generate(reviewstitle)
plt.imshow(wc_titles, interpolation = 'bilinear')
plt.axis("off")
plt.show()



##scores

##average score

mean_score = imbd_rev.scores.mean()


##score distribution
n,bins,patches = plt.hist(imbd_rev.scores,bins=10,density=True,alpha=0.7)
sns.kdeplot(imbd_rev.scores)
plt.axvline(x = mean_score,linestyle = '--',color = 'r')
plt.title('The wandering earth score distribution')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.xlim(0,10)
plt.show()

