import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser
from .. items import ZillowItem
import json


class ZillowHouseSpider(scrapy.Spider):
    name = 'zillow_house'
    allowed_domains = ['www.zillow.com']

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            cookies=cookie_parser()
        )

    def parse(self, response):
        json_rep = json.loads(response.body)
        houses = json_rep.get('cat1').get('searchResults').get('mapResults')
        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id', house.get('zpid'))
            loader.add_value('img_src', house.get('imgSrc'))
            loader.add_value('detail_url', house.get('detailUrl'))
            loader.add_value('status_type', house.get('statusType'))
            loader.add_value('status_text', house.get('statusText'))
            loader.add_value('price', house.get('price'))
            loader.add_value('address', house.get('address'))
            loader.add_value('beds', house.get('beds'))
            loader.add_value('baths', house.get('baths'))
            loader.add_value('area_sqft', house.get('area'))
            loader.add_value('latitude', house.get('latitude'))
            loader.add_value('longtitude', house.get('longitude'))

            yield loader.load_item()
            # print(house)
