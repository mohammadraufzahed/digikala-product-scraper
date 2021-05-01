import json

import scrapy
from scrapy.http.request import Request

# Define the needed list
base_link = 'https://www.digikala.com/search/category-office-machines/?has_selling_stock=1&'
links = list()
product_links = list()
page_range = range(201, 278)
# Generate the page links
for i in page_range:
    links.append(
        base_link + f"?sortby=4&pageno={i}")


class ProductLinkSpider(scrapy.Spider):
    name = 'product_link'
    start_urls = links

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
