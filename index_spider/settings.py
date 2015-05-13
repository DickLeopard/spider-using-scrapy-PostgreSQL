# -*- coding: utf-8 -*-

# Scrapy settings for index project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'index'

SPIDER_MODULES = ['index_spider.spiders']

ITEM_PIPELINES = ['index_spider.pipelines.IndexPipeline']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'zz',  
    'password': '',  
    'database': 'indexscrape'
}
