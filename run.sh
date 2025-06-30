#!/bin/bash
set -xe

Streamflow=$1
ls
pwd
python tapis/main.py --flow-volume $Streamflow

cp -r Catchment/Inundation $_tapisExecSystemOutputDir/Inundation
cp -r Catchment/Points $_tapisExecSystemOutputDir/Points
