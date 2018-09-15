# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/1']

    def parse(self, response):
        duanzis=response.xpath("//div[@id='content-left']/div")
        for duanzi in duanzis:
            author=duanzi.xpath(".//h2//text()").get().strip()
            content=duanzi.xpath(".//span//text()").get().strip()
            item=QsbkItem(author=author,content=content)
            yield item


