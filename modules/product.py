"""
Contain class to interact with ProductSpider
"""
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from spiders.product_spider import ProductSpider


class Product:
    """
    A class to interact with Product Spider
    """

    def startProductSpider(self):
        """
        Start the ProductSpider
        """
        configure_logging()
        process = CrawlerProcess()
        process.crawl(ProductSpider)
        process.start()
