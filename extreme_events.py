# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 08:48:40 2022

@author: kzolea
"""
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
 

# Read in data
df = pd.read_csv('events_US_1980_2022.csv')
#print data
print(df)
# Create plot with the Top 5 most deadly Billon-Dollar Weather and Climate Disasters
df_top5_deaths = df.nlargest(5, 'Deaths')
plt.style.use('fivethirtyeight')
mplot=plt.bar(df_top5_deaths.Name,df_top5_deaths.Deaths,color = 'orange')
plt.xticks(color = 'navy',fontname = 'Comic Sans MS',
          size=10,rotation = 90,fontweight='bold')
plt.ylabel('Deaths', fontweight='bold', color = 'orange', fontsize='18',
          fontname = 'Comic Sans MS')
plt.title("Top 5 Most Deadly Billon-Dollar Weather and\nClimate Disasters In The US (1990-2022)",
          fontweight = "bold",size=22,color='navy', fontname = 'Comic Sans MS',pad=30)
plt.bar_label(mplot, color = 'black')
plt.annotate('Source: National Centers for\nEnvironmental Information',
            xy = (1, 0.9),
            xycoords='axes fraction',
            ha='right',
            va="center",
            fontsize=10,
            color = 'black',
            fontweight='bold',
            style='italic')
plt.annotate('Author: Kevin Zolea',
            xy = (1, 0.84),
            xycoords='axes fraction',
            ha='right',
            va="center",
            fontsize=10,
            color = 'black',
            fontweight='bold',
            style='italic')


plt.show()

plt.savefig('plot.png', dpi=300, bbox_inches='tight')
