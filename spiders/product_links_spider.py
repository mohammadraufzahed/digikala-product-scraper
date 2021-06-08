
from .config import category
import json
import scrapy
from scrapy.http.request import Request
from scrapy.crawler import CrawlerProcess


class ProductLinkSpider(scrapy.Spider):
    name = 'product_link'
    custom_settings = {
        'ROBOTSTXT_OBEY': 'False',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def __init__(self):
        # Define the needed list
        base_link = category.CATEGORY_LINK
        self.start_urls = list()
        self.product_links = list()
        page_range = range(category.PAGES_NUMBER[0], category.PAGES_NUMBER[1])
        # Generate the page links
        for i in page_range:
            self.start_urls.append(
                base_link + f"?sortby=4&pageno={i}")
    # Set the HTTP Header

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        for url in self.start_urls:
            yield Request(url, headers=headers)

    # Page counter
    counter_page = 1

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
            # Append the product link object to list
            self.product_links.append({
                'product_link': product_url,
                'page': page
            })
        self.counter_page += 1
        # Export the all links
        with open('links.json', 'w+', encoding='utf8') as f:
            json.dump(self.product_links, f, ensure_ascii=False)
