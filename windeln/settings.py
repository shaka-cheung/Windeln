# -*- coding: utf-8 -*-

# Scrapy settings for windeln project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'windeln'

#CONCURRENT_REQUESTS = 200
#LOG_LEVEL = 'INFO'
#COOKIES_ENABLED = True
#DEFAULT_RESPONSE_ENCODING = 'zh-cn'
#DOWNLOAD_DELAY = 0.25

SPIDER_MODULES = ['windeln.spiders']
NEWSPIDER_MODULE = 'windeln.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'windeln (+http://www.yourdomain.com)'
ITEM_PIPELINES = {'windeln.pipelines.Pipeline': 100,
                  'windeln.pipelines.DBPipeline': 200}


#FEED_URI = 'items.csv'
#FEED_FORMAT = 'csv'
#FEED_EXPORTERS = {
#    'csv':'windeln.pipelines.CSVPipeline',
#}

DB_PROPERTIES_USER = 'testuser'
DB_PROPERTIES_PASSWD = 'testuser'
DB_PROPERTIES_HOST = 'localhost'
DB_PROPERTIES_DB = 'testdb'
