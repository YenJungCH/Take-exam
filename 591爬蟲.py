#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install requests


# In[3]:


pip install pyquery


# In[4]:


pip install beautifulsoup4


# In[5]:


pip install selenium


# In[1]:


import requests
import numpy as np
import pandas as pd
import bs4
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


# In[16]:


#抓網址
house_url = []
res = requests.get("https://rent.591.com.tw/?kind=0&region=1&shType=list")
soup = BeautifulSoup(res.text)
house = soup.find_all('h3')
for h in house:
    h_url = h.a['href']
    house_url.append("https:" + h_url )
for web in house_url:
    print(web)


# In[6]:


df = pd.DataFrame(columns = ["出租者", "出租者身分","連絡電話","型態","現況","性別要求"])
df


# In[7]:


def detail(x):
    page = requests.get(x)
    data_soup = BeautifulSoup(page.text)
    
    renter = data_soup.select(".avatarRight i")[0].text
    iden = data_soup.select(".avatarRight div")[0].text
    
    tel = data_soup.select('div:nth-child(2) > span.dialPhoneNum')[0]
    tel = (str(tel))
    n1_tel = tel.replace('<span class="dialPhoneNum" data-value="','')
    tel = n1_tel.replace('"></span>','')
    
    n1 = data_soup.select(".attr li:nth-child(1)")[0].text
    if n1.find("坪數") == -1:
        style = data_soup.select(".attr li:nth-child(4)")[0].getText()
    else:
        style = data_soup.select(".attr li:nth-child(3)")
        style = str(style)
    style = style[5:]
    

    situa = data_soup.select("#propNav a:nth-child(5)")[0].text
    
    
    sex = data_soup.select("ul.clearfix.labelList.labelList-1 > li:nth-child(8)")
    sex = str(sex)
    if sex.find("性別要求") == -1:
        sex = "無"
    else:
        sex = data_soup.select(".labelList-1 .clearfix:nth-child(8)")[0].text
        sex = sex[5:]
    
    new=pd.DataFrame({"出租者":renter,
                  "出租者身分":iden,
                  "連絡電話":tel,
                  "型態":style,
                  "現況":situa,
                  "性別要求":sex},index=[0]) 
    
    df1=df.append(new,ignore_index=True)   
    return df1   


# In[8]:


#一頁的房屋資料
for data_url in house_url:    
    df = detail(data_url)
df


# In[ ]:





# In[ ]:


#selenium
from selenium import webdriver
import time

driverPath = 'D:\gekodriver\chromedriver.exe'
browser = webdriver.Chrome(driverPath)
url = "https://rent.591.com.tw/?kind=0&region=1&shType=list"
browser.get(url)
page = 0
df = pd.DataFrame(columns = ["出租者", "出租者身分","連絡電話","型態","現況","性別要求"])
res = requests.get("https://rent.591.com.tw/?kind=0&region=1&shType=list")
soup = BeautifulSoup(res.text)
while page <3:
    
    house_url = []
    
    house = soup.find_all('h3')
    for h in house:
        h_url = h.a['href']
        house_url.append("https:" + h_url )
    
    for data_url in house_url:    
        datafile = requests.get(data_url)
        data_soup = BeautifulSoup(datafile.text)    
        df = detail(data_url)          
            
            
    page = page + 1
    next_page = browser.find_element_by_link_text("下一頁")
    next_page.click()
    time.sleep(2)

browser.quit()  


# In[5]:


df


# In[15]:


df


# In[76]:


df.to_csv("df.csv",index=None ,encoding="utf_8_sig")

