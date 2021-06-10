import argparse
import json
from twisted.internet import reactor
from modules.main import Main
from init import init

if __name__ == '__main__':
    arg_parse = argparse.ArgumentParser(description='Digikala Scraper')
    arg_parse.add_argument("--init",  type=bool, default=False,
                           help='Initial the database and required files')
    arg_parse.add_argument('--scrap', type=str, choices=('links',
                           'products'), help='Scrap the products or links')

    args = arg_parse.parse_args()
    # Create instans
    main = Main()
    if args.init:
        init()
    elif args.scrap == 'links':
        # Get category page link
        main.get_category_link()
        # Get page numbers
        main.get_page_numbers()
        # Start the spiders
        main.startProductUrlSpider()
