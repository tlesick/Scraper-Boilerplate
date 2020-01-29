# -*- coding: utf-8 -*-

import scrapy
class RedfinItem(scrapy.Item):
    address = scrapy.Field()
    listing_dates = scrapy.Field()
    CRMLS = scrapy.Field()
    event = scrapy.Field()
    price = scrapy.Field() 
    
class ProxyItem(scrapy.Item):
    protocol = scrapy.Field()
    address = scrapy.Field()
    port = scrapy.Field()
