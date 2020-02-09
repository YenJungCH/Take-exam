#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df_a = pd.read_csv('a_lvr_land_a.csv')
df_b = pd.read_csv('b_lvr_land_a.csv') 
df_e = pd.read_csv('e_lvr_land_a.csv') 
df_f = pd.read_csv('f_lvr_land_a.csv') 
df_h = pd.read_csv('h_lvr_land_a.csv') 


# In[3]:


df_a = df_a.drop([0])
df_b = df_b.drop([0])
df_e = df_e.drop([0])
df_f = df_f.drop([0])
df_h = df_h.drop([0])


# In[6]:


df_all = pd.concat([df_a,df_b,df_e,df_f,df_h],axis=0,join='inner',ignore_index = True)


# In[8]:


df_all["總樓層數"].value_counts()


# In[21]:


digit = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
def trans(s):
    num = 0
    if s:
        idx_s = s.find('十')
        if idx_s != -1:
            num += digit.get(s[idx_s - 1:idx_s], 1) * 10
        if s[-1] in digit:
            num += digit[s[-1]]
    return num


# In[11]:


df_all["總樓層數"]=df_all["總樓層數"].str.replace("層","")


# In[12]:


df_all["總樓層數"]=df_all["總樓層數"].fillna(0)


# In[17]:


for i in range(7124):
    print(i)
    if type(df_all["總樓層數"][i]) != int:
        df_all["總樓層數"]=df_all["總樓層數"].replace(df_all["總樓層數"][i],trans(df_all["總樓層數"][i]))   
    else:
        continue


# In[183]:


mask1 = df_all["主要用途"] == "住家用"
mask2 = df_all["建物型態"].str.contains("住宅大樓") 
mask3 = df_all["總樓層數"] >= 13


# In[188]:


filter_a=df_all[(mask1 & mask2 & mask3)] 


# In[202]:


filter_a.to_csv("filter_a.csv",index=None ,encoding="utf_8_sig")

