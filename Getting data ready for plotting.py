# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:24:57 2022

@author: Hp
"""

import pandas as pd
df = pd.read_csv("missing data.csv")
print(df)


#df["Bilal"].plot(kind="hist" , title = "Bilal HIST" , bins = 10 , figsize=(12,10))     #yeh bilal k data ka histogram bnay ga jiski figure ka size 12,10 hoga


#df["Sania"].plot()   #uper wala prper treeka tha histogram show krny yeh just plot drawing ha without titles and bins

#df["Shani"].rolling(3).mean().plot()      #yeh data ka mean ly kr usko plot krta much nicer to plot



#df.plot(kind="scatter" , x="Bilal" , y="Subjects" , title="Subjects VS Marks")   #es main x values or y values hum apni marzi k data k columns dy sakty hain 


def cell_count(x):
    if x<30:
        return "low"
    else:
        return "high"

df["new data"] = df["Bilal"].apply(cell_count)       #es main hum ny 1 new colun bnaya jis main hum bilal waly column ki values 1 , 1 kr k functions ko bhejain gy  or wahan jo return hoga uslo function main put krty jain gy
print(df)

df.boxplot(column = "Bilal" , by="new data")    #boxplot hamain mean deta ha hamary result ka