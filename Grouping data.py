# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:57:29 2022

@author: Hp
"""

import pandas as pd
df = pd.read_csv("missing data.csv")
print(df)



#set_data_count = df.groupby(by = ["Ali"]).count()    #count of each value per group
#print(set_data_count)

#set_data_mean = df.groupby(by = ["Ali"]).mean()
#print(set_data_mean)

#set_data_sum = df.groupby(by = ["Ali"]).sum()
#print(set_data_sum)


print(df.corr())      #finding corelation between all columns


print(df["Sania"].corr(df["Bilal"]))   #finding corelation between 2 columns