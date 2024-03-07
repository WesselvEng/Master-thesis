# Master-thesis
These scripts I have used for the data analysis of my master thesis '...'

1)SPT_stat.py
  Used to process sugar preference test results. It uses the 'Dabest' estimation statistics python package. 
  Python version ==3.8

2)fMRI_Analysis_tresh6.ipy
  Used to process nifti files received after raw MRI data was processed with RABIES (--> RABIES.txt)
  Python version == 3.11

3)DR_stats.py
Used to process data received from fMRI_Analysis_tresh6.ipy script to compare mean activation results per ICA. It uses the 'Dabest' estimation statistics python package. 
Python version ==3.8

4)OFT_analysis_final.py
Use to process raw DeepLabCut data (.h5 files) and get the total distance travelled, amount of time spent in centre and centre entries. For all parameters the coordinates of the 'center'-bodypart were used. Inside the script there are comments that explains the code and the logic behind it.
Python version==3.11

5) OFT_stat.py
Used to process the data output from the OFT_analysis_final.py script. It used the 'Dabest' estimation statistics python package.
Python version ==3.8

6)
