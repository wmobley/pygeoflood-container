#!/bin/bash
set -xe

DEM=$1

# Print the parameters for debugging
echo "DEM: ${DEM}"

python /code/main.py /Catchment/${DEM}.tif /Catchment/Catchment.shp /Catchment/Flowlines.shp /Catchment/Streamflow

cp -r /Catchment/Inundation $_tapisExecSystemOutputDir/Inundation