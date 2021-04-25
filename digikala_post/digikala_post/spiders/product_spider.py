import scrapy
import json


class QuoteSpider(scrapy.Spider):
    name = "product"
    start_urls = [
        "https://www.digikala.com/product/dkp-2264825/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%87%D9%88%D8%B4%D9%85%D9%86%D8%AF-%D9%85%D9%88%D8%AF%DB%8C%D9%88-%D9%85%D8%AF%D9%84-mw01"
    ]

    def parse(self, response):
        # Select the hole page
        page = response.css("div.container")
        # Product title
        product_title = str(
            page.css("h1.c-product__title::text").get()).strip()
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
            details_data = list()
            for details in product_details.css("ul li"):
                title = str(details.css(
                    "div.c-params__list-key span::text").get()).strip()
                info = str(details.css(
                    "div.c-params__list-value span::text").get()).strip()
                details_data.append({'title': title, 'info': info})
            details_box = {
                'title': header,
                'details': details_data,
            }
            product_details_data.append(details_box)

        product = {
            # Product title
            'product_title': product_title,
            # Product model
            'product_model': product_model,
            # Product warranty
            'product_warranty': product_warranty,
            # Product colors
            'product_colors': product_colors,
            # Product overview
            'product_overview': product_overview,
            # Product general specifications
            'product_general_specifications': product_general_details,
            # Product all specifications
            'product_details_box': product_details_data}
        yield product
