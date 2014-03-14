# -*- coding: utf-8 -*-       

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request 
from sm.items import SmItem 
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

class SmSpider(BaseSpider):

    name = "sm"

    start_urls = ["http://www.guangruntech.com/cat.asp?catid=405"]

    def __init__(self):
        self.items = []
        self.conNum = 0;

    def parse(self, response):
        print "parse"         

        content = HtmlXPathSelector(response)

        baseUrl = get_base_url(response) 
        
        nodes = content.select("//tr/td/a/strong")
        print len(nodes)
        
        for node in nodes:
            item = SmItem()
            item['smType'] = 20 
            item['smTitle'] = node.select('font/text()').extract()
            getUrl = node.select('../@href').extract()
            item['smUrl'] = urljoin_rfc(baseUrl,getUrl[0])
            
            self.items.append(item);

            print item['smType']
            print item['smTitle']
            print item['smUrl'] 
            yield Request(urljoin_rfc(baseUrl,getUrl[0]), callback=self.parseContent)


    def parseContent(self, response):
        print "parse content"
        self.conNum += 1
        print self.conNum
        print response.url

        content = HtmlXPathSelector(response)
        c1 = content.select('//td[@width="760"]/table/tr/td[@width="70%"]').extract()
        c2 = content.select('//td[@width="760"]/table[@cellspacing="5"]').extract()

        
        for item in self.items:
            if item['smUrl'] == response.url:
                print "have find"
                break
        
        item['smContent'] = c1+c2
        return item




