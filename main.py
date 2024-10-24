from pathlib import Path
from pygeoflood import PyGeoFlood

from app.dem_processing import dem_processing
from app.inundation_mapping import inundation_mapping

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

args = parse_args()
dem = args.DEM
flowlines = args.flowlines
catchments = args.catchments
streamflow_dir = args.streamflow_path
points = args.points
fim_list = args.fim_list

src, hand, segment_catchments = dem_processing(dem, flowlines, catchments)    

inundation_mapping(dem, src, hand, segment_catchments, streamflow_dir, points, fim_list)