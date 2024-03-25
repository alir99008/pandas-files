# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:11:57 2022

@author: Hp
"""

import pandas as pd
df = pd.read_csv("missing data.csv")
print(df)

print(df.isnull())        #yeh hamary data frame main cehck kry ga jonsa cell null howa usko true kr dy ga bak sun ko false kr dy ga

print(df.isnull().sum())  #yeh hamain btaty ga k konsy collumn main kitny cell null hain un sub ko total kr k btay ga



#df_new = df.dropna()   #yeh jis B row main 1 B blank cell howa wo puri row ignore kr dy ga print krty waqt
#print(df_new)
#df_new = df.dropna(how = "all")    #yeh jis B row main sary cell blank  howa wo puri row ignore kr dy ga print krty waqt
#print(df_new)
#df_new = df.dropna(thresh = 2)    #yeh agr kisi row main 2 B esy cell howy to jis main values hoe to cell print krwa dy ga
#print(df_new)




#print(df_new.dropna(how = "any").shape)      #yeh row or column return kr dy ga
#print(df_new.dropna(how = "any"))      #jis row main 1 B cell blank howa wo row print nai kry ga sirf wohi row print kry ga jis main sub column howy
#print(df_new.dropna(subset = ["Ali" , "Ahmed"] , how = "any"))    #hum apni marzi k cell b check kr sakty hain es bar wo check kry ga k ali or ahmed k cell jis row main 2no majood hain wo row print kr dy ga
#print(df_new.dropna(how = "all"))    #es main jab tak puri row blank na hoe tab tak print krta rhy ga




#Fillna

#new_df = df.fillna(0)      #yeh function blank cell or NaN values ko zero sy fill kr dy ga 
#print(new_df)
#new_df = df.fillna("no")      #yeh function blank cell or no values ko zero sy fill kr dy ga 
#print(new_df)
#new_df = df.fillna({"Ali" : 0 , "Sania" : "na" , "Ahmed" : 0})      #es function sy hum apni marzi k apni marzi k cell mai changing kr sakty hain
#print(new_df)




#new_df = df.fillna(method = "ffill")      #yeh forwad fill ha khali cell main uper waly cell ki value copy kr k fill kr dy ga
#print(new_df)
#new_df = df.fillna(method = "bfill")    #yeh backward fill ha khali cell main neechay waly cell ki value copy kr k fill kr dy ga
#print(new_df)
#new_df = df.fillna(method = "ffill" , axis = "columns")   #yeh forwad fill ha lakin column wise peechay waly left side waly khali cell  ki value copy kr k fill kr dy ga
#print(new_df)
#new_df = df.fillna(method = "bfill" , axis = "columns")  #yeh backward fill ha lakin column wise agy waly right side waly khali cell  ki value copy kr k fill kr dy ga
#print(new_df)
#new_df = df.fillna(method = "ffill" , limit = 1)     #yeh forwad fill ha khali cell main uper waly cell ki value copy kr k fill kr dy ga lakin agr 2 cell 1 sath khali aagay to yeh sirf 1 cell main value paste kry ga 2sry main nai
#print(new_df)
#new_df = df.fillna(method = "bfill" , limit = 2)     #yeh forwad fill ha khali cell main uper waly cell ki value copy kr k fill kr dy ga lakin agr 3 cell 1 sath khali aagay to yeh sirf 2 cell main value paste kry ga 3sry main nai
#print(new_df)
