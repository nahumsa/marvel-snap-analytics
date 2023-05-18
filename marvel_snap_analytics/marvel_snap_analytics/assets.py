from dagster import asset
from marvel_snap_analytics.etl import cards

@asset
def hackernews_wordcloud():
    print(cards.extract())