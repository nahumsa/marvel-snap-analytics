from dagster import asset, Output
from marvel_snap_analytics.etl import cards

@asset
def extract_cards():
    return cards.extract()