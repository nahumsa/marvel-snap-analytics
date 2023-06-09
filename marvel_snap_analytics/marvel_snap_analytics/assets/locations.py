from dagster import asset, Output
from marvel_snap_analytics.etl import locations

@asset(io_manager_key="postgres_io_manager_locations")
def extract_locations():
    return locations.extract()