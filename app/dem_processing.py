from pathlib import Path
import os

from pygeoflood import PyGeoFlood

def dem_processing(dem, flowlines, catchments):

    pgf = PyGeoFlood(dem_path = dem)

    pgf.flowline_path = flowlines

    pgf.catchment_path = catchments

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

    return pgf.src_path, pgf.hand_path, pgf.segment_catchments_raster_path