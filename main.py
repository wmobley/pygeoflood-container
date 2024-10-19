from pathlib import Path
from pygeoflood import PyGeoFlood

def pygeoflood_full_workflow(dem, flowlines, catchments, streamflow):

    pgf = PyGeoFlood(dem_path = dem)

    pgf.flowline_path = flowlines

    pgf.catchment_path = catchments

    pgf.streamflow_forecast_path = streamflow

    pgf.apply_nonlinear_filter()

    pgf.calculate_slope()

    pgf.calculate_curvature()

    pgf.fill_depressions()

    pgf.calculate_mfd_flow_accumulation()

    pgf.calculate_d8_flow_direction()

    pgf.find_outlets()

    pgf.delineate_basins()

    pgf.define_skeleton()

    pgf.calculate_binary_hand()

    pgf.find_endpoints()

    pgf.extract_channel_network()

    pgf.calculate_hand()

    pgf.segment_channel_network()

    pgf.delineate_segment_catchments()

    pgf.calculate_src()

    pgf.calculate_flood_stage()

    pgf.inundate()

def parse_args():
    import argparse

    parser = argparse.ArgumentParser(
        description="Calculate the average of each row in a CSV file"
    )
    parser.add_argument("DEM", help="The CSV file to read")
    parser.add_argument("catchments", help="The file to write the average of each row to")
    parser.add_argument("flowlines", help="The file to write the average of each row to")
    parser.add_argument("streamflow", help="")
    return parser.parse_args()

args = parse_args()
dem = args.DEM
print(dem)

flowlines = args.flowlines
catchments = args.catchments
streamflow = args.streamflow

pygeoflood_full_workflow(dem, flowlines, catchments, streamflow)