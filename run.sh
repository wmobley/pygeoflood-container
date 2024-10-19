#!/bin/bash
set -xe

DEM=$1
Streamflow=$2

python /code/main.py Catchment/{DEM}.tif Catchment/Catchment.shp Catchment/Flowlines.shp Catchment/{Streamflow}_Streamflow.csv

cp Catchment/{DEM}_src.csv $_tapisExecSystemOutputDir/{DEM}_src.csv
cp Catchment/{DEM}_HAND.tif $_tapisExecSystemOutputDir/{DEM}_HAND.tif
cp Catchment/{DEM}_segment_catchments.tif $_tapisExecSystemOutputDir/{DEM}_segment_catchments.tif