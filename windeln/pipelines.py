# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.conf import settings

class WindelnPipeline(object):

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class CSVPipeline(object):
    def __init__(self):
        self.file = codecs.open(settings.getlist())


class Pipeline(object):
    def process_item(self, item, spider):
        return item

import MySQLdb

class DBPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=settings.get('DB_PROPERTIES_USER'), passwd=settings.get('DB_PROPERTIES_PASSWD'), host=settings.get('DB_PROPERTIES_HOST'), db=settings.get('DB_PROPERTIES_DB'))
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("INSERT INTO test (url, title, description, description_zh) VALUES (%s, %s, %s, %s)", (item['url'], item['name'], item['description'], item['description_zh']))
            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item