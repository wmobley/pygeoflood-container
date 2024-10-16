from app import woodville_test

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


if __name__ == "__main__":

    args = parse_args()
    dem = args.DEM
    flowlines = args.flowlines
    catchments = args.catchments
    streamflow = args.streamflow

    woodville_test.pygeoflood_woodville(dem, flowlines, catchments, streamflow)