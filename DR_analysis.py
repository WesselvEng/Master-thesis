# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:06:39 2024

@author: Wessel
"""

import os 
import pandas as pd
import dabest

os.chdir('C:\\Users\\Wessel\\Documents\\Studie\\master\\Internship\\Thesis\\Data_analysis\\Dual_Regression')
#%%
data = pd.read_excel('DR_all_means_all_improved.xlsx', decimal='.')
data['Group']=data['Group'].astype(str)
data['Mouse ID']=data['Mouse ID'].astype(str)
data['Batch']=data['Batch'].astype(str)

#%%
#create dictionary to store statistic results of each ICA
results = {}

#Create a loop to iterate over all ICA_columns in Data
for y in range(18):
    
    #create a looped y-input for dabest.load function
    experiment_column = f'ICA_{y + 1}'
    
    # Load the data of first ICA into dabest
    dabest_obj = dabest.load(data=data.iloc[:,[0,1,2,(3+y)]], x="Group", y=experiment_column,
                          idx=("4", "1", "3"))

    # Plot the data of the first ICA
    # Add swarm_label="Mean activation" to change y-label
    dabest_obj.mean_diff.plot(swarm_label="Mean activation"); # *If you want to check for batch effects, add 'color_col="Batch" as argument
    
    #store stat results in dictionary
    results[f'ICA_{y + 1}'] = dabest_obj.mean_diff.results

