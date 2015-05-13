#   scrapy shell 'http://indekspasar.com' --nolog
#   scrapy shell 'http://www.indekspasar.com/market/return.php'  

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from index.item import Index

class IndexSpider(BaseSpider):# IndexSpider is inherit from class BaseSpider 
                        # which is in the (), so IndexSpider has the attributes
                        # of Spider and we can define additional attributes
    name = "index"
    allowed_domains = ["indekspasar.com"]
    start_urls = ["http://www.indekspasar.com/market/return.php"]
    
    index_xpath = '*'
    item_fields = {
        '1': '//font[@color="black"][1]/text()'
        '2': '//font[@color="black"][2]/text()'
        '3': '//font[@color="black"][3]/text()'
        '4': '//font[@color="black"][4]/text()'
        '5': '//font[@color="black"][5]/text()'
        '6': '//font[@color="black"][6]/text()'
        '7': '//font[@color="black"][7]/text()'
        '8': '//font[@color="black"][8]/text()'
        '9': '//font[@color="black"][9]/text()'
        '10': '//font[@color="black"][10]/text()'
        '01': '//span[@class][1]/text()'
        '02': '//span[@class][2]/text()'
        '03': '//span[@class][3]/text()'
        '04': '//span[@class][4]/text()'
        '05': '//span[@class][5]/text()'
        '06': '//span[@class][6]/text()'
        '07': '//span[@class][7]/text()'
        '08': '//span[@class][8]/text()'
        '09': '//span[@class][9]/text()'
        '010': '//span[@class][10]/text()'

    def parse(self, response):
        selector = HtmlXPathSelector(response)
        for data in selector.xpath(self.index_xpath):
            loader = XpathItemLoader(Index(),selector = data)
        
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()
            
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
