from dagster import asset, Output
from marvel_snap_analytics.etl import cards

@asset(io_manager_key="postgres_io_manager_cards")
def extract_cards():
    return cards.extract()
