import scrapy
import json
import socket
from datetime import datetime

from scrapy.loader.processors import TakeFirst
from scrapy.loader import ItemLoader

from marvelsnap_scraper.items import CardItem
class CardsSpider(scrapy.Spider):
    name = 'cards'
    allowed_domains = ['marvelsnap.io']
    start_urls = ['https://marvelsnap.io/api/search.php?database&type=character']

    def parse(self, response):
        cards_json = json.loads(response.body)["card"]

        for card in cards_json:
            loader = ItemLoader(item=CardItem())

            loader.add_value("name", card["name"])
            loader.add_value("object_type", card["type"])
            loader.add_value("cost", card["cost"])
            loader.add_value("power", card["power"])
            loader.add_value("ability", card["ability"])
            loader.add_value("date_added", card["date_added"])
            loader.add_value("collection", card["method"])
            loader.add_value("slug", card["slug"])

            # metadata
            loader.add_value("url", response.url)
            loader.add_value("project", self.settings.get("BOT_NAME"))
            loader.add_value("spider", self.name)
            loader.add_value("server", socket.gethostname())
            loader.add_value("date", datetime.utcnow())

            # Take the first value from the list
            loader.default_output_processor = TakeFirst()

            yield loader.load_item()