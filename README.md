# Master-thesis
This repository contains the data and scripts that I have used for my master thesis '...'

Dual_regression_data-Folder:
contains dual regression data output from RABIES of all animals
*note: In the processed data folder .xlxs files can be found what group each animal was assigned to.

Processed Data-Folder:
Contains all the processed data that was used as input for the estimation statistics python package 'Dabest' (version 2023.2.14) (! python==3.8)
*note: These .xlsx files are produced from the raw .csv files that were the output of the scripts that are mentioned in the Scripts-Folder. Data from .csv files were imported tot .xlsx files and ordered such that they were compatible to be used as input for the Dabest package.

Scripts-Folder:
Contains all the scripts that have been used to process the data. For each script the input is described, the output is described as well as the program (and program version if relevant)

**1) Cutting videos**
   This piece of code is used to cut the raw video files from the camera to 30 minute long files (45.000 frames) which were the input for the
   DeepLabCut analysis.
   Performed in Linux

**2) DR_stats.py**
   Used to process data received from fMRI_Analysis_tresh6.ipy script to compare mean activation results per ICA. It uses the 'Dabest' estimation statistics python   package. Python version ==3.8
   
**3) OFT_analysis_final.py**
   Use to process raw DeepLabCut data (.h5 files) and get the total distance travelled, amount of time spent in centre and centre entries. For all parameters the      coordinates of the 'center'-bodypart were used. Inside the script there are comments that explains the code and the logic behind it.
   Python version==3.11
   
**4) RABIES_Analysis.sh**
   This is the shell script that was used fed into the RABIES software process the functional MRI data in BIDS format
   Performed in Linux

**5) SPT_stat.py**
  Used to process sugar preference test results. It uses the 'Dabest' estimation statistics python package. 
  Python version ==3.8

**6) OFT_stat.py**
   Used to process the data output from the OFT_analysis_final.py script. It used the 'Dabest' estimation statistics python package.
   Python version ==3.8

**7) fMRI_Analysis_tresh6.ipy**
  Used to process nifti files received after raw MRI data was processed with RABIES (--> RABIES.txt)
  Python version == 3.11








