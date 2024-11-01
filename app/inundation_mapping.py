from pathlib import Path
import os
from pygeoflood import PyGeoFlood

from .point_depth_extraction import point_depth_extraction

# Function to handle a single streamflow_path file
def inundation_mapping(dem, src, hand, segment_catchments, streamflow_path, points, fim_list):

    catchment_dir = os.path.dirname(dem) + '/'
    
    pgf = PyGeoFlood(dem_path=dem)
    
    event = Path(streamflow_path).stem
    stage_path = Path(catchment_dir + 'Stage/' + event)
    inundation_path = Path(catchment_dir + 'Inundation/' + event)
    
    pgf.calculate_flood_stage(
        custom_src=src, 
        custom_streamflow_forecast_path=streamflow_path, 
        custom_path=stage_path
    )
    pgf.inundate(
        custom_hand=hand, 
        custom_flood_stage=stage_path, 
        custom_segment_catchments_raster=segment_catchments, 
        custom_path=inundation_path
    )
    
    # If points are provided, extract point depths
    if points != "None":

        points_path = catchment_dir + 'Points/' + points + '.shp'

        point_depths = point_depth_extraction(inundation_path.with_suffix(".tif"), points_path)
    
    # Manage output files based on fim_list
    if fim_list == 'All' or event in fim_list.split():
        print("Saved " + str(inundation_path.with_suffix(".tif")))
    else:
        os.remove(inundation_path.with_suffix(".tif"))

    return event, point_depths