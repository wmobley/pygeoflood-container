from pathlib import Path
from pygeoflood import PyGeoFlood

from app.dem_processing import dem_processing
from app.inundation_mapping import inundation_mapping
from app.merge_point_data import merge_point_data

from multiprocessing import Pool 
import multiprocessing

def parse_args():
    import argparse

    parser = argparse.ArgumentParser(
        description="Calculate the average of each row in a CSV file"
    )
    parser.add_argument("DEM", help="The CSV file to read")
    parser.add_argument("catchments", help="The file to write the average of each row to")
    parser.add_argument("flowlines", help="The file to write the average of each row to")
    parser.add_argument("streamflow_path", help="")
    parser.add_argument("points", help="")
    parser.add_argument("fim_list", help="")
    return parser.parse_args()

if __name__ == "__main__":

    try:
        multiprocessing.set_start_method('spawn')
    except RuntimeError:
        print("Start method already set")
        pass  # Context has already been set; do nothing

    args = parse_args()
    dem = args.DEM
    flowlines = args.flowlines
    catchments = args.catchments
    streamflow_dir = args.streamflow_path
    points = args.points
    fim_list = args.fim_list

    src, hand, segment_catchments = dem_processing(dem, flowlines, catchments) 

    streamflow_files = list(Path(streamflow_dir).iterdir())

    # Prepare arguments for each streamflow_path file
    args = [(dem, src, hand, segment_catchments, streamflow_path, points, fim_list) for streamflow_path in streamflow_files]
        
    # Run inundation mapping in parallel using Pool
    with Pool(processes = 32) as pool:
        
        point_results = pool.starmap(inundation_mapping, args)
    
    events, point_depths = zip(*point_results)
    
    events_list = list(events)
    point_depths_list = list(point_depths)
    
    if points != "None":
        merge_point_data(dem, point_depths_list, events_list, points)