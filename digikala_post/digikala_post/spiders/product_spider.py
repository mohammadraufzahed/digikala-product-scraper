import scrapy
import json


class QuoteSpider(scrapy.Spider):
    name = "product"
    start_urls = [
        "https://www.digikala.com/product/dkp-777295/%D8%AF%D9%88%D8%B1%D8%A8%DB%8C%D9%86-%D8%AF%DB%8C%D8%AC%DB%8C%D8%AA%D8%A7%D9%84-%DA%A9%D8%A7%D9%86%D9%86-%D9%85%D8%AF%D9%84-eos-4000d-%D8%A8%D9%87-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D9%84%D9%86%D8%B2-18-55-%D9%85%DB%8C%D9%84%DB%8C-%D9%85%D8%AA%D8%B1-dc-iii"
    ]

    def parse(self, response):
        # Select the hole page
        page = response.css("div.container")
        # Product title
        product_title = str(
            page.css("h1.c-product__title::text").get()).strip()
        # Product overview
        product_overview = str(page.css(
            "section.c-content-expert__summary .c-mask__text::text").get()).strip()
        # Product details
        product_details = list()
        # Product general information
        for product_general_info in page.css('#params article.c-params__border-bottom section ul li'):
            print(product_general_info)
            title = str(product_general_info.css("div.c-params__list-key span::text").get()).strip()
            info = str(product_general_info.css("div.c-params__list-value span::text").get()).strip()
            product_details.append({'title': title, 'info': info})
        product = {
            "product_title": product_title,
            "product_overview": product_overview,
            "product_general_specifications": product_details,
        }
        with open("ap.txt", 'w', encoding="utf-8") as f:
            f.write(str(product))
        yield product
