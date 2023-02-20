import scrapy

class CardItem(scrapy.Item):
    name = scrapy.Field()
    object_type = scrapy.Field()
    cost = scrapy.Field()
    power = scrapy.Field()
    ability = scrapy.Field()
    date_added = scrapy.Field()
    collection = scrapy.Field()
    slug = scrapy.Field()

    # Metadata fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()

