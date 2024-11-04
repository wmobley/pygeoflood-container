#!/bin/bash
set -xe

DEM=$1
Streamflow=$2
Points=$3
fim_list=$4

# Print the parameters for debugging
echo "DEM: ${DEM}"
echo "Points: ${Points}"
echo "FIM List: ${fim_list}"

python /code/main.py Catchment/${DEM}.tif Catchment/Catchment.shp Catchment/Flowlines.shp Catchment/${Streamflow} ${Points} "$fim_list"

cp -r Catchment/Inundation $_tapisExecSystemOutputDir/Inundation
cp -r Catchment/Points $_tapisExecSystemOutputDir/Points
