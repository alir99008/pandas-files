# -*- cding: utf-8 -*-
"""
Created on Sun Mar 20 11:41:50 2022

@author: Hp
"""

import pandas as pd
df = pd.read_csv("missing data.csv")
print(df)

#df1 = df.drop("Khawar" , axis=1)      #drop ka matlab yeh 1 column delete kr dy ga khawar wala axis = 1 ka matlab k column delete krna agr axis =0 hota to es ka matlab row delete krna
#print(df1)


#df2 = df.drop(["Ali" , "Bilal" , "Khawar"] , axis=1)    #es main humny 3 column 1 sath delete kiye ALi khawar bilal 
#print(df2)


df3 = df.drop(df.index[1])     #yeh 1 index wali row main jo data para hoga usko delete kr dy remeber yeh row wise delete krny ga index dekhty howy
print(df3)



df4 = df.iloc[3: , ]    #es ka matlab k yeh 3 row sy ly kr end tk show kry ga jis main sary column include hongay
print(df4 )


df5 = df[df["Bilal"]!=20]   #yeh condition lagai ha eska matlab k bilal k jis index main 20 aarha ha usko ko chor kr baki sara data ly ly ga us index pr baki jo collumns honagy unka B data nai ly ga
print(df5)


#ff=df
#ff["Date"] = "2019-05-06"      #yeh pehly check kry ga k hamary data main koi Date wala column ha agr howa to yeh date us column main insert ho jay gi agr Date wala column na howa phr new column date k name sy bany ga or us main yeh date insert ho jay gii  or puray column main same he date enter hogi
#print(ff)


#dd=df
#dd["Date"] = pd.to_datetime("2021-03-21")    #yeh hamary pas date time enter krny ka 1 or tarika
#print(dd)


#dd.to_csv("new changing in csv file.csv")     #eska matlab k csv main changing krny k bad dubara save krwana


