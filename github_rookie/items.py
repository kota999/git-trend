# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GithubTrendItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    lang = scrapy.Field()
    all_stars = scrapy.Field()
    forks = scrapy.Field()
    stars = scrapy.Field()
    timescale = scrapy.Field()
