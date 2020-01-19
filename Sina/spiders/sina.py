# -*- coding: utf-8 -*-
import scrapy
from Sina.items import SinaItem
import json
class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['feed.mix.sina.com.cn','sina.com.cn']
    #国内新闻
    start_urls = ["https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2510&k=&num=50&page={}".format(page) for page in range(10)]
    # name = 'sina'
    # allowed_domains = ['feed.mix.sina.com.cn','sina.com.cn']
    # start_urls = ["https://news.sina.com.cn/roll/#pageid=153&lid=2509&k=&num=50&page=1"]

    def parse(self, response):
        result = response.text
        data = json.loads(result).get('result').get('data')
        for news in data:
            url = news.get('url')
            yield scrapy.Request(url, callback=self.parsecontents)

    def parsecontents(self,response):
        title = response.xpath('//title/text()').extract()[0]
        meta = response.xpath('//meta/@content').extract()
        keywords = meta[2]
        time = meta[10]
        media = meta[13]
        paragraph = response.xpath('//div[@class="article"]/p/text()').extract()
        content = ""
        for p in paragraph:
            content = content + p
        item = SinaItem()
        item['title'] = str(title)
        item['keywords'] = str(keywords)
        item['time'] = str(time)
        item['media'] = str(media)
        item['content'] = str(content)
        item['tag'] = "news"
        yield item
