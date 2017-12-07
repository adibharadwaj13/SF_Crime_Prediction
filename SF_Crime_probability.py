# -*- coding: utf-8 -*-
"""
@author: Jonathan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def do_plot(data,num,title_str):
    plt.figure(num)
    plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
    plt.xlabel('Time of Occurrence')
    plt.ylabel('Relative Probability in %', rotation = 'vertical')
#    plt.yticks(data, )
    plt.title('Probability of ' + title_str + ' Relative to Other Common Crimes')
    plt.bar(hours_list,data)

#Read in our dataset
df = pd.read_csv('train.csv',usecols=['Dates','Category'], parse_dates=['Dates'])

#Prepare lists for filtering and displaying data
keep_list = ['LARCENY/THEFT','BURGLARY','ROBBERY','ASSAULT','DRUG/NARCOTIC','VEHICLE THEFT']
titles_list = ['Larcenies or Thefts', 'Burglaries', 'Robberys', 'Assaults', 'Drug Offenses', 'Vehicle Thefts']
crimes_list = ['LT','BURGLARY','ROBBERY','ASSAULT','DN','VT']
hours_list = [hour for hour in range(24)]
formatted_hours_list = ['Midnight']+['%d AM' %hour for hour in range(1,12)]+['Noon']+['%d PM' %hour for hour in range(1,12)]
color_list = ['#050C42','#0284A8','#02BEC4','#A9E8DC','#E1F7E7'] 

#Filter              
df = df.query('Category in @keep_list').replace(['LARCENY/THEFT','DRUG/NARCOTIC','VEHICLE THEFT'],['LT','DN','VT'])
df['Hour'] = df['Dates'].apply(lambda x: int(x.hour))
df = df.drop(['Dates'],axis = 1)

#List of lists for relative probability
prob_list = [[(df.loc[(df['Hour'] == hour) & (df['Category'] == catstr), 'Category'].count()/float(len(df.loc[df['Hour'] == hour])))*100 for hour in hours_list] for catstr in crimes_list]
#List of lists for frequency
quant_list = [[df.loc[(df['Hour'] == hour) & (df['Category'] == catstr), 'Category'].count() for hour in hours_list] for catstr in crimes_list]

#Need counter for next bit
i=0
#Create a plot for every crime in the list
for L in prob_list:
    do_plot(L,i,titles_list[i])
    i+=1
#Create a plot for a single crime in the list
do_plot(L,i,titles_list[i])

#Stackplot fun
plt.figure(i)
i+=1
plt.stackplot(hours_list,prob_list,baseline='zero',labels = titles_list,colors=color_list)
plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
plt.xlabel('Time of Occurrence')
plt.title('Percentage of Common Crimes')   
plt.legend()

plt.figure(i)
i+=1
plt.stackplot(hours_list,quant_list,baseline='zero',labels = titles_list,colors=color_list)
plt.xticks(hours_list, formatted_hours_list, rotation='vertical')
plt.xlabel('Time of Occurrence')
plt.title('Frequency of Common Crimes')
plt.legend()