# -*- coding: utf-8 -*-
"""
@author: Jonathan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('train.csv',usecols=['Dates','Category'], parse_dates=['Dates'])
keep_list = ['LARCENY/THEFT','BURGLARY','ROBBERY','ASSAULT','DRUG/NARCOTIC','VEHICLE THEFT']
hours_list = [hour for hour in range(24)]
df = df.query('Category in @keep_list').replace(['LARCENY/THEFT','DRUG/NARCOTIC','VEHICLE THEFT'],['LT','DN','VT'])
df['Hour'] = df['Dates'].apply(lambda x: int(x.hour))
df = df.drop(['Dates'],axis = 1)
dfdum = pd.get_dummies(df,columns=['Category'])

sample_space = len(df)

lt_probability = [dfdum[dfdum.Hour == hour].Category_LT.sum()/float(sample_space) for hour in hours_list]
burglary_probability = [dfdum[dfdum.Hour == hour].Category_BURGLARY.sum()/float(sample_space) for hour in hours_list]
robbery_probability = [dfdum[dfdum.Hour == hour].Category_ROBBERY.sum()/float(sample_space) for hour in hours_list]
assault_probability = [dfdum[dfdum.Hour == hour].Category_ASSAULT.sum()/float(sample_space) for hour in hours_list]
dn_probability = [dfdum[dfdum.Hour == hour].Category_DN.sum()/float(sample_space) for hour in hours_list]
vt_probability = [dfdum[dfdum.Hour == hour].Category_VT.sum()/float(sample_space) for hour in hours_list]
formatted_hours_list = ['12 AM']+['%d AM' %hour for hour in range(1,12)]+['12 PM']+['%d PM' %hour for hour in range(1,12)]

plt.figure(1)
plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
plt.bar(hours_list,lt_probability)

plt.figure(2)
plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
plt.bar(hours_list,burglary_probability)

plt.figure(3)
plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
plt.bar(hours_list,robbery_probability)

plt.figure(4)
plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
plt.bar(hours_list,assault_probability)

plt.figure(5)
plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
plt.bar(hours_list,dn_probability)

plt.figure(6)
plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
plt.bar(hours_list,vt_probability)

#TODO: format this in a more algorithmic way, create a better visualisation