#!/bin/bash
set -xe

python main.py data/Woodville_DEM.tif data/Woodville_Catchments.shp data/Woodville_Flowlines_Docker.shp data/streamflow.csv


cp /usr/src/app/data/Woodville_DEM_src.csv /usr/src/app/output/Woodville_DEM_src.csv
cp /usr/src/app/data/Woodville_DEM_HAND.tif /usr/src/app/output/Woodville_DEM_HAND.tif
cp /usr/src/app/data/Woodville_DEM_segment_catchments.tif /usr/src/app/output/Woodville_DEM_segment_catchments.tif