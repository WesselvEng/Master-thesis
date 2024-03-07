# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:45:10 2024

@author: Wessel
"""

#import libraries

import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import math



#move to data folder
os.chdir(r'C:/Users/Wessel/Documents/Studie/master/Internship/Thesis/Data_analysis/OFT')

#I finished script for total center time and total distance travelled (only need to make plots for cumulative distance travelled)
#I also need to write stas script for total distance traveleld


#below you can find the part of the script calculating total time spent in center
#%%
#for all csv files with 4 mice
pixel_info = pd.read_excel('pixel_info.xlsx', header=0)
indiv = pixel_info.iloc[:,0]
center_time_4mice= {}

#read into all files in root directory using glob
for b in glob.glob('*_el.h5', root_dir= r'C:\Users\Wessel\Documents\Studie\master\Internship\Thesis\Data_analysis\OFT\4mice_data'):  
    
    #create dictionary to store data 
    video_data = {}
    
    for a in range(len(indiv)):
        video_data[indiv[a]] = [] #create a key for each video in dictionary which is going to be a list
        
        data = pd.read_hdf(f'4mice_data/{b}')
        #take the center-coordinates to see the mouse was present in the center of the maze
        betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[a,4])), 1, 0)
        betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
        betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[a,6])), 1, 0)
        betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
        
        #add frame numbers to each value
        betweenx_df['frame']=range(len(betweenx_df))
        betweenx_df['frame']=betweenx_df['frame'].astype(str)
        betweeny_df['frame']=range(len(betweeny_df))
        betweeny_df['frame']=betweeny_df['frame'].astype(str)
        
        #merge X and Y data and add extra column 'true' that looks if both X and Y column are equal to 1. If both 1, then 
        #center coordinate was in center
        
        merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
        merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
        
        #sum up total of frames in which center coordinate in centre of maze and divide with fps of video to get total time in sec
        time = (sum(merged_between['true']))/24
        video_data[indiv[a]].append(time)
        c = video_data
    
    center_time_4mice[f'{b}'] = c
#%%
#because the mice in de 2 mice videos do not all have the same field number a seperate loop is made for every video specifically

indiv = ['ind1','ind2']
center_time_2mice = {}

video1_data={}

for a in range(len(indiv)):
    video1_data[indiv[a]]=[]
    
    data = pd.read_hdf(r'2mice_data\030124_1333_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5')
    betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[2+a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[2+a,4])), 1, 0)
    betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
    betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[2+a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[2+a,6])), 1, 0)
    betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
    
    betweenx_df['frame']=range(len(betweenx_df))
    betweenx_df['frame']=betweenx_df['frame'].astype(str)
    betweeny_df['frame']=range(len(betweeny_df))
    betweeny_df['frame']=betweeny_df['frame'].astype(str)
    
    merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
    merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
    
    time = (sum(merged_between['true']))/24
    video1_data[indiv[a]].append(time)

video2_data={}

for a in range(len(indiv)):
    video2_data[indiv[a]]=[]
    
    data = pd.read_hdf(r'2mice_data\110124_1316_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5')
    betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[0+3*a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[0+3*a,4])), 1, 0)
    betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
    betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[0+3*a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[0+3*a,6])), 1, 0)
    betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
    
    betweenx_df['frame']=range(len(betweenx_df))
    betweenx_df['frame']=betweenx_df['frame'].astype(str)
    betweeny_df['frame']=range(len(betweeny_df))
    betweeny_df['frame']=betweeny_df['frame'].astype(str)
    
    merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
    merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
    
    time = (sum(merged_between['true']))/24
    video2_data[indiv[a]].append(time)

video3_data={}

for a in range(len(indiv)):
    video3_data[indiv[a]]=[]
    
    data = pd.read_hdf(r'2mice_data\131223_1324_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5')
    betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[0+3*a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[0+3*a,4])), 1, 0)
    betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
    betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[0+3*a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[0+3*a,6])), 1, 0)
    betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
    
    betweenx_df['frame']=range(len(betweenx_df))
    betweenx_df['frame']=betweenx_df['frame'].astype(str)
    betweeny_df['frame']=range(len(betweeny_df))
    betweeny_df['frame']=betweeny_df['frame'].astype(str)
    
    merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
    merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
    
    time = (sum(merged_between['true']))/24
    video3_data[indiv[a]].append(time)

video4_data={}

for a in range(len(indiv)):
    video4_data[indiv[a]]=[]
    
    data = pd.read_hdf(r'2mice_data\141223_1305_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5')
    betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[0+3*a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[0+3*a,4])), 1, 0)
    betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
    betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[0+3*a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[0+3*a,6])), 1, 0)
    betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
    
    betweenx_df['frame']=range(len(betweenx_df))
    betweenx_df['frame']=betweenx_df['frame'].astype(str)
    betweeny_df['frame']=range(len(betweeny_df))
    betweeny_df['frame']=betweeny_df['frame'].astype(str)
    
    merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
    merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
    
    time = (sum(merged_between['true']))/24
    video4_data[indiv[a]].append(time)

center_time_2mice= {'030124_1333_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5': video1_data, 
                    '110124_1316_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5': video2_data, 
                    '131223_1324_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5': video3_data, 
                    '141223_1305_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5': video4_data}


#%%
#merge both 2 mice and 4 mice datasets together
center_time = {**center_time_2mice, **center_time_4mice}

center_time_df = pd.DataFrame.from_dict(center_time)

#save as a csv
center_time_df.to_csv('Center_time.csv' , index=False)


#%%
#in excel the csv is processed such that it is compatible to use in Dabest estimation stats
#%%
#below you can find part of the script that will calculate total distance travelled
    
#%%
#for all data file of 4 mice data 


pixel_info = pd.read_excel('pixel_info.xlsx', header=0)
indiv = pixel_info.iloc[:,0]
ratio = float(pixel_info['Ratio (cm/px)'].loc[pixel_info['Field'] == 'individual1'])

cumul_travelled_all_4mice = {}
total_travelled_all_4mice = {}



for c in glob.glob('*_el.h5', root_dir= r'C:\Users\Wessel\Documents\Studie\master\Internship\Thesis\Data_analysis\OFT\4mice_data'):  
    
    distances_frames= {}
    no_nan_list = {}
    data = pd.read_hdf(f'4mice_data/{c}')
    
    for a in range(len(indiv)):
        distances_frames[f'{indiv[a]}'] = []
    
        for index in range((len(data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x']))-1):
            
            row_t0 = data.loc[index]
            row_t1 = data.loc[index + 1]
        
            if row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] > 0:
        
                x0 = row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x']
                y0 = row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y']
    
                x1 = row_t1['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x']
                y1 = row_t1['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y']
        
            else:
                x0 = row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'Tailbase','x']
                y0 = row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'Tailbase','y']
    
                x1 = row_t1['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'Tailbase','x']
                y1 = row_t1['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'Tailbase','y']
    
            #use pythagoras to calculate distance between frames
            distance = (math.sqrt((x0-x1)**2 + (y0-y1)**2))*ratio
    
            distances_frames[f'{indiv[a]}'].append(distance)
     
        distances_frames_df = pd.DataFrame(distances_frames)
        #check how much original NaN values
        no_nan_list[f'{indiv[a]}'] = distances_frames_df[f'{indiv[a]}'].isnull().sum() 
    
        #remove remaining NaNs 
        distances_frames_df = distances_frames_df.fillna(0)

    #create dictionary to store video data
    cumul_travelled = {}

    #store cumuluative summed distances travelled per individu
    for b in range(len(indiv)):
        cumul_travelled[indiv[b]]= []
        cumlen = distances_frames_df.loc[:,indiv[b]].cumsum()
        cumul_travelled[indiv[b]]= cumlen
    
    cumul_travelled_df = pd.DataFrame(cumul_travelled)

    #total distances values
    total_travelled_df = distances_frames_df.sum() 
    
    total_travelled_all_4mice[c] = total_travelled_df

    cumul_travelled_all_4mice[c] = cumul_travelled_df

#%%
#for all data file of 2 mice data 

pixel_info = pd.read_excel('pixel_info.xlsx', header=0)
indiv = ['ind1','ind2']
ratio = float(pixel_info['Ratio (cm/px)'].loc[pixel_info['Field'] == 'individual1'])

cumul_travelled_all_2mice = {}
total_travelled_all_2mice = {}



for c in glob.glob('*_el.h5', root_dir= r'C:\Users\Wessel\Documents\Studie\master\Internship\Thesis\Data_analysis\OFT\2mice_data'):  
    
    distances_frames= {}
    no_nan_list = {}
    data = pd.read_hdf(f'2mice_data/{c}')
    
    for a in range(len(indiv)):
        distances_frames[f'{indiv[a]}'] = []
    
        for index in range((len(data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x']))-1):
            
            row_t0 = data.loc[index]
            row_t1 = data.loc[index + 1]
        
            if row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] > 0:
        
                x0 = row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x']
                y0 = row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y']
    
                x1 = row_t1['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x']
                y1 = row_t1['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y']
        
            else:
                x0 = row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'Tailbase','x']
                y0 = row_t0['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'Tailbase','y']
    
                x1 = row_t1['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'Tailbase','x']
                y1 = row_t1['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'Tailbase','y']
    
            distance = (math.sqrt((x0-x1)**2 + (y0-y1)**2))*ratio
    
            distances_frames[f'{indiv[a]}'].append(distance)
     
        distances_frames_df = pd.DataFrame(distances_frames)
        #check how much original NaN values
        no_nan_list[f'{indiv[a]}'] = distances_frames_df[f'{indiv[a]}'].isnull().sum() 
    
        #remove remaining NaNs 
        distances_frames_df = distances_frames_df.fillna(0)

    #create dictionary to store video data
    cumul_travelled = {}

    #store cumsum distances travelled per individu
    for b in range(len(indiv)):
        cumul_travelled[indiv[b]]= []
        cumlen = distances_frames_df.loc[:,indiv[b]].cumsum()
        cumul_travelled[indiv[b]]= cumlen
    
    cumul_travelled_df = pd.DataFrame(cumul_travelled)

    #total distances values
    total_travelled_df = distances_frames_df.sum() 
    
    total_travelled_all_2mice[c] = total_travelled_df

    cumul_travelled_all_2mice[c] = cumul_travelled_df

#%%
#merge both 2 mice and 4 mice datasets together
total_travelled_all = {**total_travelled_all_2mice, **total_travelled_all_4mice}
total_travelled_data = pd.DataFrame.from_dict(total_travelled_all)

#save total_travelled data to use in Dabest
total_travelled_data.to_csv('totaldistance.csv', index=False)
#%%
#plot cumul distance 4 mice videos
for a in glob.glob('*_el.h5', root_dir= r'C:\Users\Wessel\Documents\Studie\master\Internship\Thesis\Data_analysis\OFT\4mice_data'):
    plt.figure(figsize=(15,5))
    plt.plot(cumul_travelled_all_4mice[a])
    plt.xlabel('frame number')
    plt.ylabel('cumulative distance (cm)')
    plt.xlim(right=45000)
    plt.xticks(ticks= [5000,10000,15000,20000,25000,30000,35000,40000,45000])
    plt.legend(['individual1','individual2','individual3','individual4'])
    plt.suptitle(b)
    plt.show()

#plot cumul distance 2 mice videos
for b in glob.glob('*_el.h5', root_dir= r'C:\Users\Wessel\Documents\Studie\master\Internship\Thesis\Data_analysis\OFT\2mice_data'):
    plt.figure(figsize=(15,5))
    plt.plot(cumul_travelled_all_2mice[b])
    plt.xlabel('frame number')
    plt.xlim(right=45000)
    plt.xticks(ticks= [5000,10000,15000,20000,25000,30000,35000,40000,45000])
    plt.ylabel('cumulative distance (cm)')
    plt.legend(['individual1','individual2'])
    plt.suptitle(b)
    plt.show()
    
#%%
#entries 4 mice videos
pixel_info = pd.read_excel('pixel_info.xlsx', header=0)
indiv = pixel_info.iloc[:,0]
entries_4mice = {}


for b in glob.glob('*_el.h5', root_dir= r'C:\Users\Wessel\Documents\Studie\master\Internship\Thesis\Data_analysis\OFT\4mice_data'):  
    entry_data_video = {}
    
    
    for a in range(len(indiv)):
        entry_data_video[indiv[a]] = []
        
        data = pd.read_hdf(f'4mice_data/{b}')
        #take the center-coordinates to see the mouse was present in the center of the maze
        betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[a,4])), 1, 0)
        betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
        betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[a,6])), 1, 0)
        betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
        
        #add frames numbers to values
        betweenx_df['frame']=range(len(betweenx_df))
        betweenx_df['frame']=betweenx_df['frame'].astype(str)
        betweeny_df['frame']=range(len(betweeny_df))
        betweeny_df['frame']=betweeny_df['frame'].astype(str)
        
        #see if center coordinates was in maze centre
        #then see at what frames there is a difference in the 'true' column --> means switch between in or out centre
    
        merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
        merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
        merged_between['entry']= merged_between['true'].diff()
        entry_data_video[indiv[a]]=sum(merged_between['entry']==1) #positive values means moved into the centre
    
    entries_4mice[f'{b}']= entry_data_video
    
    
#entries 2 mice videos
indiv = ['ind1','ind2']
entries_2mice = {}

entry_vid1_data={}

for a in range(len(indiv)):
    entry_vid1_data[indiv[a]]=[]
    
    data = pd.read_hdf(r'2mice_data\030124_1333_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5')
    betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[2+a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[2+a,4])), 1, 0)
    betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
    betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[2+a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[2+a,6])), 1, 0)
    betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
    
    betweenx_df['frame']=range(len(betweenx_df))
    betweenx_df['frame']=betweenx_df['frame'].astype(str)
    betweeny_df['frame']=range(len(betweeny_df))
    betweeny_df['frame']=betweeny_df['frame'].astype(str)
    
    merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
    merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
    merged_between['entry']= merged_between['true'].diff()
    entry_vid1_data[indiv[a]]=sum(merged_between['entry']==1)
    

entry_vid2_data={}

for a in range(len(indiv)):
    entry_vid2_data[indiv[a]]=[]
    
    data = pd.read_hdf(r'2mice_data\110124_1316_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5')
    betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[0+3*a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[0+3*a,4])), 1, 0)
    betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
    betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[0+3*a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[0+3*a,6])), 1, 0)
    betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
    
    betweenx_df['frame']=range(len(betweenx_df))
    betweenx_df['frame']=betweenx_df['frame'].astype(str)
    betweeny_df['frame']=range(len(betweeny_df))
    betweeny_df['frame']=betweeny_df['frame'].astype(str)
    
    merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
    merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
    merged_between['entry']= merged_between['true'].diff()
    entry_vid2_data[indiv[a]]=sum(merged_between['entry']==1)

entry_vid3_data={}

for a in range(len(indiv)):
    entry_vid3_data[indiv[a]]=[]
    
    data = pd.read_hdf(r'2mice_data\131223_1324_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5')
    betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[0+3*a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[0+3*a,4])), 1, 0)
    betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
    betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[0+3*a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[0+3*a,6])), 1, 0)
    betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
    
    betweenx_df['frame']=range(len(betweenx_df))
    betweenx_df['frame']=betweenx_df['frame'].astype(str)
    betweeny_df['frame']=range(len(betweeny_df))
    betweeny_df['frame']=betweeny_df['frame'].astype(str)
    
    merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
    merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
    merged_between['entry']= merged_between['true'].diff()
    entry_vid3_data[indiv[a]]=sum(merged_between['entry']==1)

entry_vid4_data={}

for a in range(len(indiv)):
    entry_vid4_data[indiv[a]]=[]
    
    data = pd.read_hdf(r'2mice_data\141223_1305_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5')
    betweenx = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] >= int(pixel_info.iloc[0+3*a,3])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','x'] <= int(pixel_info.iloc[0+3*a,4])), 1, 0)
    betweenx_df = pd.DataFrame(betweenx, columns=['fieldcenterx'])
    betweeny = np.where((data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center', 'y'] >=int(pixel_info.iloc[0+3*a,5])) & (data['DLC_resnet50_OFT_batch123Jan19shuffle1_100000',indiv[a],'center','y'] <= int(pixel_info.iloc[0+3*a,6])), 1, 0)
    betweeny_df = pd.DataFrame(betweeny, columns=['fieldcentery'])
    
    betweenx_df['frame']=range(len(betweenx_df))
    betweenx_df['frame']=betweenx_df['frame'].astype(str)
    betweeny_df['frame']=range(len(betweeny_df))
    betweeny_df['frame']=betweeny_df['frame'].astype(str)
    
    merged_between= pd.merge(betweenx_df,betweeny_df, on='frame')
    merged_between['true']=np.where((merged_between['fieldcenterx']==1) & (merged_between['fieldcentery']==1) , 1 , 0)
    merged_between['entry']= merged_between['true'].diff()
    entry_vid4_data[indiv[a]]=sum(merged_between['entry']==1)

entries_2mice= {'030124_1333_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5': entry_vid1_data,
                '110124_1316_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5': entry_vid2_data, 
                '131223_1324_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5': entry_vid4_data, 
                '141223_1305_R3-CUTDLC_resnet50_OFT_batch123Jan19shuffle1_100000_el.h5': entry_vid4_data}

entries_all = {**entries_2mice, **entries_4mice}
entries_all_df = pd.DataFrame.from_dict(entries_all)
entries_all_df.to_csv('entries.csv', index=False)


