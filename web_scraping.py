
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd


# In[2]:


##locate chrome
chrome_path=r'D:\Download\chromedriver_win32\chromedriver.exe'
##build web driver
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(20)
##open website
driver.get('https://www.imdb.com/title/tt7605074/reviews?ref_=tt_urv')


# In[4]:


ids=list()
dates=list()
scores=list()
titles=list()
contents=list()
sorRews=list()


# In[5]:


def click_load_more(times,sleep_time):
    try:
        for i in range(times):
            driver.find_element_by_xpath('//*[@id="load-more-trigger"]').click()
            time.sleep(sleep_time)
    except:
        pass


# In[6]:


click_load_more(100,4)


# In[7]:


def get_reviews_data(start_t,end_t):
    for i in range(start_t,end_t+1):
        ## get ids
        try:
            imdb_id=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[2]/span[1]/a').text
        except:
            try:
                imdb_id=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[2]/span[1]/a').text
            except:
                try:
                    imdb_id=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[1]/span[1]/a').text
                except:
                    imdb_id=1
        ##get date
        try:
            date=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[2]/span[2]').text 
        except:
            try:
                date=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[2]/span[2]').text
            except:
                try:
                    date=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[1]/span[2]').text
                except:
                    date=i


        ##get score
        try:
            score=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[1]/span/span[1]').text
        except:
            try:
                score=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[1]/span/span[1]').text
            except:
                score='N/A'
                
        ##get title
        try:
            reviews_title=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/a').text
        except:
            try:
                reviews_title=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/a').text
            except:
                reviews_title=i
 

        ##get reviews

        try:
            reviews_content=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[3]/div[1]').text
        except:
            try:
                driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[4]/div/div').click()
                reviews_content=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[4]/div[1]').text
            except:
                
                try:
                    reviews_content=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[2]/div[1]').text
       
                    
                except:
                
                
                    reviews_content=i
                    print(i)
                
                
                
                
                
        ##get score of reviews
        try:
            score_of_reviews=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[3]/div[2]').text
        except:
            try:
                score_of_reviews=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[2]/div[2]/div[2]').text
            except:
                try:
                    score_of_reviews=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[3]').text
                except:
                    try:
                        
                        score_of_reviews=driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[2]/div[2]').text
                        
                    except:
                        score_of_reviews=i

        print('this is ' + str(i) )
            
        ids.append(imdb_id)
        dates.append(date)
        scores.append(score)
        titles.append(reviews_title)
        contents.append(reviews_content)
        sorRews.append(score_of_reviews)


# In[8]:


get_reviews_data(1,400)


# In[10]:


imbd_reviews_dt=pd.DataFrame()
imbd_reviews_dt['ids']=ids
imbd_reviews_dt['dates']=dates
imbd_reviews_dt['scores']=scores
imbd_reviews_dt['titles']=titles
imbd_reviews_dt['contents']=contents
imbd_reviews_dt['sorRews']=sorRews


# In[21]:


imbd_reviews_dt.to_csv('imbd_reviews.csv')

