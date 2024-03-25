# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:44:12 2022

@author: Hp
"""

import pandas as pd
df = pd.read_csv("data.csv")
#print(df.head())  #es sy start sy 5 index deta ha baki sub ko chor kr
#print(df.columns)     #it shows all columns names of our data
#print(df.info)       #yeh hamay sary data ki info btata ha k kis main data ha kis main nai or kis column main kitn adata ha
#print(df.shape)    #yeh hamary data ki rows or columns btata ha
#print(df.head(2))    ##head ki bracket k andr hum jitna likhain gy uthny column dy ga start st

#print(df.tail())   #es sy end sy 5 index deta ha baki sub ko chor kr
#print(df.tail(3))   #head ki bracket k andr hum jitna likhain gy uthny column dy ga end sy

#print(df.index)   #yeh hamy btata ha k hamary data main rowa kitni hain index btata ha
#df.set_index("subjects")     #es sy hum apni marzi sy koi B columns index main set kr sakty hain

#print(df.head())
#print(df["Ali"].unique())   #yeh hamain unique values btay ga matlab k jo values repeat ho rhi hain unko sirf 1 bar btay ga
#dc = df.rename(columns={"Ali":"Ali G"})   #yeh hamary column ko rename krta ha column ka name change krta ha
#print(dc)
print(df.dtypes)   #yeh hamain hamary data ki typre btata ha k ky adata types ha
print(df.describe())    #yeh hamary sary data ko describe krta ha matlab k data ka mean median mode or B bht zada informatiion deta ha data k bary main


#data=[[20, 40, 60, 20, 40, 30],
 #     [70, 50, 60, 20, 40, 30],
 #     [20, 70, 30, 40, 60, 80],
  #    [20, 40, 60, 20, 40, 60]]

#df=pd.DataFrame(data)
#df = pd.DataFrame(data , index=[1,2,3,4] , columns=["science","math","phy","isl","pf","OD"])   #es main agr hum apny data ko rows and columns nai btain gy to wo by default 0 sy indexing start kr k put kr dy ga
#print(df)