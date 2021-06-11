import json
import jsonlines
import scrapy
from scrapy.http.request import Request
from .Database.Mysql import Mysql
from .config import config


class ProductSpider(scrapy.Spider):

    name = "product"
    start_urls = list()
    custom_settings = {
        'ROBOTSTXT_OBEY': 'False',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def __init__(self):
        # Create database connection
        self.db = Mysql(config.DB_HOST, config.DB_USER,
                        config.DB_PASS, config.DB_NAME)

   # Set the HTPP Header
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        with jsonlines.open('links.jl') as jl:
            for link in jl:
                yield Request(link["product_link"], headers=headers)

    def parse(self, response):
        # Select the hole page
        page = response.css("div.container")
        # Product url
        product_url = response.request.url
        # Product title
        product_title = str(
            page.css("h1.c-product__title::text").get()).strip()
        # Product category
        product_category = page.css("ul.c-breadcrumb li ::text").getall()
        product_category = '/'.join(product_category)
        # Product model
        product_model = str(
            page.css("span.c-product__title-en::text").get()).strip()
        # Product overview
        product_overview = str(page.css(
            "div.c-mask__text ::text").get()).strip()
        # Product warranty
        product_warranty = str(
            page.css("div.c-mini-buy-box__warranty::text").get()).strip()
        # Product colors
        product_colors = list()
        for products_color in page.css("ul.js-product-variants li"):
            color = str(products_color.css("::text").get()).strip()
            product_colors.append(color)
        # Product general details
        product_general_details = list()
        # Product general information
        for product_general_info in page.css('#params article.c-params__border-bottom section ul li'):
            # Select info title
            title = str(product_general_info.css(
                "div.c-params__list-key span::text").get()).strip()
            # Select info body
            info = str(product_general_info.css(
                "div.c-params__list-value span::text").get()).strip()
            # Append it to product general details
            product_general_details.append({'title': title, 'info': info})
        # Scrap the product details
        product_details_data = list()
        for product_details in page.css("div.c-params__collapse--content section"):
            # Header
            header = str(product_details.css("h3::text").get()).strip()
            # Details list
            details_data = list()
            # Scrap the details
            for details in product_details.css("ul li"):
                # detail title
                title = str(details.css(
                    "div.c-params__list-key span::text").get()).strip()
                # Detail info
                info = str(details.css(
                    "div.c-params__list-value span::text").get()).strip()
                # Append the detail to details list
                details_data.append({'title': title, 'info': info})
            details_box = {
                'title': header,
                'details': details_data,
            }
            # Append the data to the list
            product_details_data.append(details_box)
        # Prepare the query to commit to database
        sql = f'''INSERT INTO `digikala_products`(`product_title`, `product_link`, `product_category`, `product_model`, `product_warranty`, `product_colors`, `product_overview`, `product_general_specifications`, `product_details_box`)
         VALUES 
         ("{product_title}","{product_url}","{product_category}","{product_model}","{product_warranty}","{product_colors}","{product_overview}","{product_general_details}","{product_details_data}")'''
        self.db.query(sql)
        self.db.commit()
