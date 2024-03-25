# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:40:45 2022

@author: Hp
"""

import pandas as pd
df = pd.read_csv("missing data.csv")
print(df)

df1 = df.sort_values("Shani" , ascending = True)   #yeh values ko sort kry ga shani wali column ko dekhty hoey values ko accending order main sort kry ga  phr shani ki sub sy small value k sath sath puri row ki values first index pr aajai gii
print(df1)

df2 = df[["Ali" , "Khawar"]]   #yeh sirf 2 columns ko print krway ga
print(df2)


df3 = df.loc[2:5  , ["Ali" , "Khawar"]]    #yeh 2 sy 4 index tk data print krway ga khawar or ali k columns ka
print(df3)


print(max(df["Khawar"]))   #yeh khawar k column ki maximum value ko print kry ga


df["Finding"] = df["Shani"]>30      #es main finding ka 1 new column bany ka jis main conditions check krty howy true or false put krta jay ga
print(df)



#for index,row in df.iterrows():
#    average = (row["Ali"] + row["Bilal"] , row["Shani"])/3
#    print(round(average) , row["Finding"])