from dagster import asset, Output
from marvel_snap_analytics.etl import decks

@asset(io_manager_key="postgres_io_manager_decks")
def extract_decks():
    return decks.extract()