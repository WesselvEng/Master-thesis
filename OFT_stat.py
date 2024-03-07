# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:49:09 2024

@author: Wessel
"""

import os
import pandas as pd
import dabest
import matplotlib.pyplot as plt
plt.style.use("default")

os.chdir(r'C:/Users/Wessel/Documents/Studie/master/Internship/Thesis/Data_analysis/OFT')

stats_data = pd.read_excel('center_time_improved.xlsx')
stats_data['Group']=stats_data['Group'].astype(str)
stats_data['Mouse ID']=stats_data['Mouse_ID'].astype(str)
stats_data['Batch']=stats_data['Batch'].astype(str)

#create dictionary to store statistic results of each ICA
center_time_results = dabest.load(data=stats_data, x="Group", y="center_time",
                                  idx=("Control", "Fluoxetine", "TBG"))

center_time_results.mean_diff.plot(raw_marker_size=5,
                                   swarm_label= 'Center Time (sec)');
center_time_results_values = center_time_results.mean_diff.results
#%%

stats_data = pd.read_excel('total_distance_improved.xlsx')
stats_data['Group']=stats_data['Group'].astype(str)
stats_data['Mouse ID']=stats_data['Mouse_ID'].astype(str)
stats_data['Batch']=stats_data['Batch'].astype(str)

#create dictionary to store statistic results of each ICA
total_distance_results = dabest.load(data=stats_data, x="Group", y="total_distance",
                                  idx=("Control", "Fluoxetine", "TBG"))

total_distance_results.mean_diff.plot(raw_marker_size=5,
                                   swarm_label= 'Total distance (cm)');
total_distance_results_values = center_time_results.mean_diff.results

#%%

stats_data = pd.read_excel('entries_improved.xlsx')
stats_data['Group']=stats_data['Group'].astype(str)
stats_data['Mouse ID']=stats_data['Mouse_ID'].astype(str)
stats_data['Batch']=stats_data['Batch'].astype(str)

#create dictionary to store statistic results of each ICA
center_entries_results = dabest.load(data=stats_data, x="Group", y="entries",
                                  idx=("Control", "Fluoxetine", "TBG"))

center_entries_results.mean_diff.plot(raw_marker_size=5,
                                   swarm_label= 'Center entries #');
center_entries_results_values = center_entries_results.mean_diff.results