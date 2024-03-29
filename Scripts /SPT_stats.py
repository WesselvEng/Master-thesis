"""
Created on Tue 16 Jan 2024
Last edited on 17-01-2024

@author: Wessel
"""

import os 
import pandas as pd
import dabest

os.chdir('C:\\Users\\Wessel\\Documents\\Studie\\master\\Internship\\Thesis\\Data_analysis\\SPT')
#%%
data = pd.read_excel('SPT_Data.xlsx', decimal=',')
data['Group']=data['Group'].astype(str)
data['Batch']=data['Batch'].astype(str)

# Load the above data into `dabest`.
ratio_dabest = dabest.load(data=data, x="Group", y="Ratio S/Tot",
                          idx=("Control", "Fluoxetine", "TBG"))

# Produce a Cumming estimation plot.
ratio_dabest.mean_diff.plot(raw_marker_size=5,
                            swarm_label = 'Preference');
ratio_results = ratio_dabest.mean_diff.results

#%%
total_drunk_dabest = dabest.load(data=data, x='Group', y='Total drunk',
                                 idx=("Control", "Fluoxetine", "TBG"))

total_drunk_dabest.mean_diff.plot(raw_marker_size=5,
                                  swarm_label= 'Total drunk (mL)')
Total_drunk_results = total_drunk_dabest.mean_diff.results
