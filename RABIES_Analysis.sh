#!/bin/bash

# author: Joanes Grandjean
# date: 05.05.2022
# last modified:01.02.2024 (Wessel)

root_dir="/project/4180000.23/Wessel_test_fMRI/batch_1"
og_bids="bids"
RABIES="/opt/rabies/0.4.8/rabies.sif"


#arguments for RABIES preprocessing, confound regression, analysis
prep_arg='--TR 1 --commonspace_reg masking=false,brain_extraction=false,template_registration=SyN,fast_commonspace=true --commonspace_resampling 0.3x0.3x0.3' 
conf_arg='--TR 1 --highpass 0.01 --smoothing_filter 0.5 --lowpass 0.1 --conf_list global_signal mot_6'
analysis_arg='--prior_maps /project/4180000.23/Wessel_test_fMRI/templates/DSURQE_100micron_DRICA.nii.gz --FC_matrix --DR_ICA --group_ica apply=true,dim=10,random_seed=1'


mkdir -p $root_dir/tmp_script
mkdir -p $root_dir/tmp_bids
mkdir -p $root_dir/func_preprocess
mkdir -p $root_dir/func_confound
mkdir -p $root_dir/func_analysis


ls -d $root_dir/$og_bids/sub*/ | while read scan
do

  func_scans=()

  functional=$(find $scan -name *_bold.nii.gz) 
  anat=$(find $scan -name *_T2w.nii.gz)  
  func_scans+=($functional)
  echo $func_scans

  for func in ${func_scans[*]}
  do

    func_basename=$(basename -- "$func") 
    func_noext="${func_basename%.*}"

    #check that all the files are where they should be 
    if [ -z "$func" ]; then
    echo "func missing in "$scan
    continue
    fi

    if [ -z "$anat" ]; then
    echo "anat missing in "$scan
    continue
    fi


    #get subject and session name from directory name 
    sub=$func_noext
    bids=${root_dir}/tmp_bids/${sub}

    #RABIES directories.
    preprocess=$root_dir/func_preprocess/${sub}
    confound=$root_dir/func_confound/${sub}
    analysis=$root_dir/func_analysis/${sub}
    
    mkdir -p $preprocess
    mkdir -p $confound
    mkdir -p $analysis

    #####write to tmp scripts#####
    #env variables and modules
    echo "module load apptainer"  > ${root_dir}/tmp_script/scrip_${sub}.sh
    echo "module load ANTs"  >> ${root_dir}/tmp_script/scrip_${sub}.sh
    echo "module unload ANTs"  >> ${root_dir}/tmp_script/scrip_${sub}.sh
    echo "module unload freesurfer"  >> ${root_dir}/tmp_script/scrip_${sub}.sh
    echo "module unload fsl"  >> ${root_dir}/tmp_script/scrip_${sub}.sh

    #make dir and cp anat and func folders
    echo "mkdir -p "${bids}  >> ${root_dir}/tmp_script/scrip_${sub}.sh
    echo "mkdir -p "${bids}"/func"  >> ${root_dir}/tmp_script/scrip_${sub}.sh
    echo "mkdir -p "${bids}"/anat"  >> ${root_dir}/tmp_script/scrip_${sub}.sh
    echo "cp -r "${func}" "${root_dir}"/tmp_bids/"${sub}"/func"   >> ${root_dir}/tmp_script/scrip_${sub}.sh
    echo "cp -r "${anat}" "${root_dir}"/tmp_bids/"${sub}"/anat"   >> ${root_dir}/tmp_script/scrip_${sub}.sh

    #preprocess
    echo "apptainer run -B "${bids}":/input_bids:ro -B "${preprocess}":/preprocess_outputs/ "${RABIES}" -p MultiProc preprocess /input_bids/ /preprocess_outputs/ "${prep_arg} >> ${root_dir}/tmp_script/scrip_${sub}.sh

    #confound
    echo "apptainer run -B "${bids}":/input_bids:ro -B "${preprocess}":/preprocess_outputs/ -B "${confound}":/confound_correction_outputs/ "${RABIES}" confound_correction /preprocess_outputs/ /confound_correction_outputs/ "${conf_arg} >> ${root_dir}/tmp_script/scrip_${sub}.sh

    #analysis
    echo "apptainer run -B "${bids}":/input_bids:ro -B "${preprocess}":/preprocess_outputs/ -B "${confound}":/confound_correction_outputs/ -B "${analysis}":/analysis_outputs/ "${RABIES}" -p MultiProc analysis /confound_correction_outputs/ /analysis_outputs/ "${analysis_arg} >> ${root_dir}/tmp_script/scrip_${sub}.sh

    done
  
  done

for file in ${root_dir}/tmp_script/*
do

  qsub -l 'walltime=48:00:00,mem=32gb,procs=2' $file

done

