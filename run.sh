#!/bin/bash
set -xe

Streamflow=$1
ls
pwd
python /code/main.py --flow-volume $Streamflow

cp -r Catchment/data $_tapisExecSystemOutputDir

