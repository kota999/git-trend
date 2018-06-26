# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GithubTrendRepoItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    lang = scrapy.Field()
    all_stars = scrapy.Field()
    forks = scrapy.Field()
    stars = scrapy.Field()

class GithubTrendItem(scrapy.Item):
    # define the fields for your item here like:
    lang = scrapy.Field()
    timescale = scrapy.Field()
    repos = scrapy.Field()
