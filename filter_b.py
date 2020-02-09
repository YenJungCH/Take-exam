#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df_a = pd.read_csv('a_lvr_land_a.csv')
df_b = pd.read_csv('b_lvr_land_a.csv') 
df_e = pd.read_csv('e_lvr_land_a.csv') 
df_f = pd.read_csv('f_lvr_land_a.csv') 
df_h = pd.read_csv('h_lvr_land_a.csv') 


# In[4]:


df_a = df_a.drop([0])
df_b = df_b.drop([0])
df_e = df_e.drop([0])
df_f = df_f.drop([0])
df_h = df_h.drop([0])


# In[5]:


df_all = pd.concat([df_a,df_b,df_e,df_f,df_h],axis=0,join='inner',ignore_index = True)


# In[6]:


df_all


# In[30]:


#總件數
total = len(df_all)
total


# In[64]:


#總車位數
ps = df_all['交易筆棟數'].str.split('位',expand=True)[1]
psv = ps.values
psv = pd.to_numeric(psv)
tpsv = psv.sum()
tpsv


# In[23]:


#平均總價元
df_all['總價元'] = pd.to_numeric(df_all['總價元'])
tv = df_all['總價元'].values
tv


# In[56]:


atv = tv.mean()
atv


# In[57]:


#平均車位總價元
df_all['車位總價元'] = pd.to_numeric(df_all['車位總價元'])
cv = df_all['車位總價元'].values
cv


# In[58]:


acv = cv.mean()
acv


# In[66]:


#filter_b
filter_b = pd.DataFrame([[total,tpsv,atv,acv]],columns=['總件數','總車位數','平均總價元','平均車位總價元'])
filter_b


# In[67]:


filter_b.to_csv("filter_b.csv",index=None ,encoding="utf_8_sig")

