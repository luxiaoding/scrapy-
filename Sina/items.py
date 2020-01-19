# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title= scrapy.Field()
    keywords = scrapy.Field()
    time= scrapy.Field()
    media = scrapy.Field()
    content = scrapy.Field()
    tag= scrapy.Field()
    pass
