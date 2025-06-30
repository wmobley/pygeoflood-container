from pathlib import Path
from pygeoflood import pyGeoFlood
import sys
import argparse


def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Run PyGeoFlood with configurable flow volume')
    parser.add_argument(
        '--flow-volume', 
        type=float, 
        default=2086,
        help='Custom flow volume (Q) for flood stage calculation (default: 2086)'
    )
    parser.add_argument(
        '--dem-path',
        type=str,
        default="data/dem.tif",
        help='Path to DEM file (default: data/dem.tif)'
    )
    parser.add_argument(
        '--flowline-path',
        type=str,
        default="data/Flowlines.shp",
        help='Path to flowlines shapefile (default: data/Flowlines.shp)'
    )
    parser.add_argument(
        '--catchment-path',
        type=str,
        default="data/Catchment.shp",
        help='Path to catchment shapefile (default: data/Catchment.shp)'
    )
    
    # Parse command line arguments
    args = parser.parse_args()
    
    # Initialize PyGeoFlood with provided arguments
    pgf = pyGeoFlood(dem_path=args.dem_path)
    
    pgf.flowline_path = args.flowline_path
    pgf.catchment_path = args.catchment_path
    
    # Configure with the flow volume from command line
    pgf.config = {"calculate_flood_stage": {"custom_Q": args.flow_volume}}
    
    print(f"Running PyGeoFlood with flow volume: {args.flow_volume}")
    print(f"DEM path: {args.dem_path}")
    print(f"Flowline path: {args.flowline_path}")
    print(f"Catchment path: {args.catchment_path}")
    
    # Run the flood inundation mapping workflow
    pgf.run_fim_workflow()
    
    print("PyGeoFlood workflow completed successfully!")


if __name__ == "__main__":
    main()