#!/bin/bash
set -xe

DEM = $1
Streamflow = $2

python main.py ${_tapisExecSystemInputDir}/{DEM}.tif ${_tapisExecSystemInputDir}/Catchment.shp ${_tapisExecSystemInputDir}/Flowlines.shp ${_tapisExecSystemInputDir}/{Streamflow}_Streamflow.csv


cp /usr/src/app/{Catchment}/{DEM}_src.csv $_tapisExecSystemOutputDir/{DEM}_src.csv
cp /usr/src/app/{Catchment}/{DEM}_HAND.tif $_tapisExecSystemOutputDir/{DEM}_HAND.tif
cp /usr/src/app/{Catchment}/{DEM}_segment_catchments.tif $_tapisExecSystemOutputDir/{DEM}_segment_catchments.tif