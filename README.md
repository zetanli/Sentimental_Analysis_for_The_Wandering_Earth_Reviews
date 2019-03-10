# <center>Sentimental Analysis for The Wandering Earth Reviews on IMDB  </center>

**Description**  

During Chinese New Year, an unprecedented Chinese Sci-Fi movie released. It's box office gross is more than 4 billion CNY(that is about $70,000,000 dollars) in China. On this analysis, I scraped audience reviews from IMDB. Then applied sentimental analysis on the data we scraped.

**EDA**

Please see the code directly, which is not hard to read.

In this part, I drew a word cloud after tokenizing, lematizing and removing stop words. So I only kept meaningful words.

**Data Preparation**

I follow the belowing steps to do data preparation.  

```        
* remove characters like punctuation, numbers, other characters.  
* tokenize  
* lematize  
* remove stop words  
* vectorize  
```  
And I reshaped data into both bigram and unigram formats.

**Regression**

In this part, I seem the full dataset as training data. Apply GBDT to the dataset and compute mean absolute percentage error.

**Classification**

Based on the distribution plot of the score. The score shows a skewed distribution. It seems not possible that the score follows a normal distribution. Thus it is not proper to use a OLS based GBDT to do regression. The score is a categorical variable indeed, which is another reason that we choose classification method. 

The variable was divided into 3 class, 1-4 as don't like, 5-7 as medium, 8-10 as very like. I chose a simple but efficient classification method, multinomial regression. 
