"""
Contains a class to interact with ProductLinkSpider
"""
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from spiders.product_links_spider import ProductLinkSpider


class ProductLink():
    """
    A class to interact with ProductLink Spider
    """
    # Get the category link from user

    def get_category_link(self):
        """
        Get the category link for ProductLinkSpider
        """
        self.__category_link = input(
            "Please enter the category link(https://www.digikala.com/search/category-mobile/): ")

    # Generate the pages to scrap
    def get_page_numbers(self):
        """
        Get the page numbers and convert them to the list for ProductLinkSpider
        """
        # Save the recieved number from user
        page_number = int(input("How many page this category have? "))
        # Initial the numbers list
        page_numbers_list = [0]

        # Seprate the numbers 100
        while not (page_number <= 0):
            if(page_number >= 100):
                page_number -= 100
                page_numbers_list.append((100+page_numbers_list[-1]))
            else:
                page_numbers_list.append(page_number + page_numbers_list[-1])
                page_number -= page_number
        # Initial pages number variable
        self.__page_numbers = list()
        # Append the page numbers list to page numbers list
        for index, number in enumerate(page_numbers_list):
            if(number == 0):
                continue
            else:
                last_index = index - 1
                self.__page_numbers.append(
                    [page_numbers_list[last_index], number + 1])

    # Save the result data in category file for spiders
    def saveData(self: object, category_link: str, page_number: list):
        data = f'''
CATEGORY_LINK = str('{category_link}')
PAGES_NUMBER = list({page_number})
        '''
        with open(os.getcwd() + '/spiders/config/category.py', 'w', encoding='utf8') as f:
            f.flush()
            f.write(data)
            f.close()

    # Run the spiders
    def startProductUrlSpider(self):
        """
        Start the ProductLinkSpider
        """
        with open('links.jl', "w+", encoding='utf8') as f:
            f.flush()
            f.close()

        configure_logging()
        process = CrawlerProcess(settings={
            'FEEDS': {
                'links.jl': {'format': 'jsonlines'},
            }
        })
        process.crawl(ProductLinkSpider, page_range=self.__page_numbers,
                      category_url=self.__category_link)
        process.start()
