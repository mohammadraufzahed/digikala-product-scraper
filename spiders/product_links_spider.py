"""
ProductLinksSpider
"""
import scrapy
from scrapy.http.request import Request
from time import sleep


class ProductLinkSpider(scrapy.Spider):
    name = 'product_link'
    # Path that this library uses to store list of proxies
    ROTATING_PROXY_LIST_PATH = 'prox.txt'
    NUMBER_OF_PROXIES_TO_FETCH = 50  # Controls how many proxies to use
    custom_settings = {
        'ROBOTSTXT_OBEY': 'False',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DOWNLOADER_MIDDLEWARES': {
            'rotating_free_proxies.middlewares.RotatingProxyMiddleware': 610,
            'rotating_free_proxies.middlewares.BanDetectionMiddleware': 620,
        }
    }

    def __init__(self, **kwargs):
        # Page counter
        self.counter_page = 1
        self.page_range = kwargs.pop('page_range', [])
        self.category_url = kwargs.pop('category_url', [])

    # Set the HTTP Header
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        for ranges in self.page_range:
            urls = (f"{self.category_url}?sortby=4&pageno={x}" for x in range(
                ranges[0], ranges[1] + 1))
            for url in urls:
                yield Request(url, headers=headers)
            print("Sleeping for 1 minute")
            sleep(60)

    # Handle the received data
    def parse(self, response):
        # Grab all the product boxes
        product_boxs = response.css(
            'ul.c-listing__items li div.c-product-box')
        # Extract the all product links
        for product_box in product_boxs:
            product_url = product_box.css(
                "a:nth-child(4)::attr(href)").get()
            product_url = f'https://www.digikala.com{product_url}'
            page = self.counter_page
            if "None" not in product_url:
                # Append the product link object to list
                yield {
                    'product_link': product_url
                }
        self.counter_page += 1
