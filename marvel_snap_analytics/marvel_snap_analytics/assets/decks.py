from dagster import asset, Output
from marvel_snap_analytics.etl import decks

@asset
def extract_decks():
    return decks.extract()