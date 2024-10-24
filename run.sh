#!/bin/bash
set -xe

DEM=$1
Points=$2
fim_list=$3

# Print the parameters for debugging
echo "DEM: ${DEM}"
echo "Points: ${Points}"
echo "Points: ${fim_list}"

python /code/main.py Catchment/${DEM}.tif Catchment/Catchment.shp Catchment/Flowlines.shp Catchment/Streamflow Catchment/Points/${Points}.shp "$fim_list"

cp -r Catchment/Inundation $_tapisExecSystemOutputDir/Inundation
cp -r Catchment/Points $_tapisExecSystemOutputDir/Points
