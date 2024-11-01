import geopandas as gpd
import os

def merge_point_data(dem, point_depths, events, points):

    catchment_dir = os.path.dirname(dem) + '/'

    points_path =  catchment_dir + points + '.shp'

    critical_points = gpd.read_file(points_path)

    for i, event in enumerate(events):

        critical_points['D_' + event] = point_depths[i]
    
    critical_points.to_file(points_path)