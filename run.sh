#!/bin/bash
set -xe

Streamflow=$1
ls
pwd
python /code/main.py --flow-volume $Streamflow

gdalwarp -t_srs "+proj=longlat +datum=WGS84 +no_defs" dem_fim.tif dem_fim.wgs84.tif
rio cogeo create dem_fim.wgs84.tif $_tapisExecSystemOutputDir/dem_fim.tif
# cp -r data $_tapisExecSystemOutputDir

