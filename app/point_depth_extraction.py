import rasterio as rio
import geopandas as gpd

def point_depth_extraction(inundation_path, points_path, event):

    fim_raster = rio.open(inundation_path)

    fim_raster_crs = fim_raster.crs

    points = gpd.read_file(points_path)

    points_reprojected = points.to_crs(fim_raster_crs)

    point_values = []

    for point in points_reprojected.geometry:

        # Extract the coordinates of the point
        row, col = fim_raster.index(point.x, point.y)  # Get the row, col of the point
        value = fim_raster.read(1)[row, col]  # Read the value at that location
        point_values.append(value)
    
    points_reprojected[event + '(m)'] = point_values

    points_reprojected.to_file(points_path)