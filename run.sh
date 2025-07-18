#!/bin/bash
set -xe

Streamflow=$1
ls
pwd
python /code/main.py --flow-volume $Streamflow

gdalwarp -t_srs "EPSG:4326" data/dem_fim.tif data/dem_fim.wgs84.tif
rio cogeo create data/dem_fim.wgs84.tif $_tapisExecSystemOutputDir/dem_fim.tif
# cp -r data $_tapisExecSystemOutputDir

