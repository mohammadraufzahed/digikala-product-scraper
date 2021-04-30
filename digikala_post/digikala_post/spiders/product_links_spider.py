from time import sleep
import scrapy
from scrapy.http.request import Request
import json

links = list()
product_links = list()

# Generate the page links
for i in range(1, 8):
    links.append(
        f"https://www.digikala.com/search/category-mobile-phone/?has_selling_stock=1&pageno={i}&sortby=4")


class ProductLinkSpider(scrapy.Spider):
    name = 'product_link'
    start_urls = links

    # Set the HTTP Header
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)
    counter_page = 1
    # Handle the received data

    def parse(self, response):
        # Grab all the product boxes
        product_boxs = response.css(
            'ul.c-listing__items li div.c-product-box')
        # Extract the all product links
        for product_box in product_boxs:
            product_url = product_box.css("a::attr(href)").get()
            product_url = f'https://www.digikala.com{product_url}'
            page = self.counter_page
            # Append the product link object to list
            product_links.append({
                'product_link': product_url,
                'page': page
            })
        self.counter_page += 1
        # Export the all links
        with open('links.json', 'w+', encoding='utf8') as f:
            json.dump(product_links, f, ensure_ascii=False)
