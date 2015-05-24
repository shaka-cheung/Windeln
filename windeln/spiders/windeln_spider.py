from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from windeln.items import WindelnItem
from scrapy.selector import Selector
from windeln.utils import Utils
from scrapy.conf import settings

class WindelnSpider(CrawlSpider) :

    name = "windeln"
    allowed_domains = ["www.windeln.de"]
    start_urls = ["http://www.windeln.de/zh"]
    rules = (
        Rule(SgmlLinkExtractor(allow = (r'http://www\.windeln\.de/zh/$', )), callback = 'parse_page', follow = True),
        Rule(SgmlLinkExtractor(allow = (r'http://www\.windeln\.de/zh/[a-zA-Z_\-]+/$', )), callback = 'parse_page', follow = True),
        Rule(SgmlLinkExtractor(allow = (r'http://www\.windeln\.de/zh/[a-zA-Z_\-]+/[a-zA-Z_\-]+/$', )), callback = 'parse_page', follow = True),
    )
    #settings.overrides['DEFAULT_RESPONSE_ENCODING'] = 'zh-cn'

    def parse_page(self, response) :
        sel = Selector(response)
        sidebar_text = sel.xpath('//div[@class="sidebar-text"]')
        if sidebar_text:
            sidebar_text_html = sidebar_text.extract()[0]
            if Utils.hasChinese(sidebar_text_html):
                #print sidebar_text_html
                return None
            else :
                item = WindelnItem()
                item['name'] = sel.xpath('//title/text()').extract()[0].encode('utf-8')
                item['url'] = response.url
                item['description'] = sidebar_text_html.encode('utf-8')
                item['description_zh'] = Utils.gSlate(sidebar_text_html).encode('utf-8')
                return item
        return None
