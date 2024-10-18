#!/bin/bash
set -xe

Catchment = $1
DEM = $2
Streamflow = $3

python main.py {Catchment}/{DEM}.tif {Catchment}/Catchment.shp {Catchment}/Flowlines.shp {Catchment}/{Streamflow}_Streamflow.csv


cp /usr/src/app/{Catchment}/{DEM}_src.csv $_tapisExecSystemOutputDir/{DEM}_src.csv
cp /usr/src/app/{Catchment}/{DEM}_HAND.tif $_tapisExecSystemOutputDir/{DEM}_HAND.tif
cp /usr/src/app/{Catchment}/{DEM}_segment_catchments.tif $_tapisExecSystemOutputDir/{DEM}_segment_catchments.tif