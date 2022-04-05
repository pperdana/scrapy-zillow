# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
from sympy import Domain

def url_abs(relative_url):
    domain_url = 'https://www.zillow.com'
    abs_url = domain_url + relative_url
    return abs_url

class ZillowItem(scrapy.Item):
    id = scrapy.Field(
        output_processor=TakeFirst()
    )
    img_src = scrapy.Field(
        output_processor=TakeFirst()
    )
    detail_url = scrapy.Field(
        input_processor=MapCompose(url_abs),
        output_processor=TakeFirst()
    )
    status_type = scrapy.Field(
        output_processor=TakeFirst()
    )
    status_text = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        output_processor=TakeFirst()
    )
    address = scrapy.Field(
        output_processor=TakeFirst()
    )
    beds = scrapy.Field(
        output_processor=TakeFirst()
    )
    baths = scrapy.Field(
        output_processor=TakeFirst()
    )
    area_sqft = scrapy.Field(
        output_processor=TakeFirst()
    )
    broker_name = scrapy.Field(
        output_processor=TakeFirst()
    )
    broker_phone = scrapy.Field(
        output_processor=TakeFirst()
    )
