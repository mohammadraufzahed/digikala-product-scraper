"""
Main script
"""
import argparse
from modules.productLink import ProductLink
from init import init

if __name__ == '__main__':
    arg_parse = argparse.ArgumentParser(description='Digikala Scraper')
    arg_parse.add_argument("--init",  type=bool, default=False,
                           help='Initial the database and required files')
    arg_parse.add_argument('--scrap', type=str, choices=('links',
                           'products'), help='Scrap the products or links')

    args = arg_parse.parse_args()
    # Create instans
    if args.init:
        init()
    elif args.scrap == 'links':
        productLink = ProductLink()
        # Get category page link
        productLink.get_category_link()
        # Get page numbers
        productLink.get_page_numbers()
        # Start the Product Url Spider
        productLink.startProductUrlSpider()
    elif args.scrap == 'products':
        pass
