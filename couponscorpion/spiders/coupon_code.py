# -*- coding: utf-8 -*-
import scrapy


class CouponCodeSpider(scrapy.Spider):
    name = 'coupon_code'
    allowed_domains = ['couponscorpion.com']
    start_urls = ['https://couponscorpion.com/']

    def parse(self, response):
        for coupon in response.xpath("//div[@class='info_in_dealgrid']/div[@class='grid_desc_and_btn']/div[@class='grid_row_info']"):
            yield {

                'Title' : coupon.xpath(".//h3/a/text()").get(),
                'link' : coupon.xpath(".//h3/a/@href").get(),
                'Category' : coupon.xpath("//div[@class='meta_for_grid']/div[@class='cat_store_for_grid floatleft']/div[@class='cat_for_grid lineheight15']/span/a/text()").get(),
                'time' : coupon.xpath("//div[@class='meta_for_grid']/div[@class='date_for_grid floatright']/span/text()[2]").get().strip()
            }
        next_page = response.xpath("//div[@class ='pagination']/ul/li[@class='next_paginate_link']/a/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)
