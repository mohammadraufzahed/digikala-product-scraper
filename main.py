"""
Main script
"""
import argparse
from init import init

if __name__ == '__main__':
    # Initial the argument parser
    arg_parse = argparse.ArgumentParser(description='Digikala Scraper')
    # Add the arguments
    arg_parse.add_argument("--init",  type=bool, default=False,
                           help='Initial the database and required files')
    arg_parse.add_argument('--scrap', type=str, choices=('links',
                           'products'), help='Scrap the products or links')
    # Parse the args
    args = arg_parse.parse_args()
    # If init argument was passed run the init def
    if args.init:
        init()
    # Else if scrap argument was passed with the value of links run the ProductLink Spider
    elif args.scrap == 'links':
        from modules.productLink import ProductLink
        productLink = ProductLink()
        # Get category page link
        productLink.get_category_link()
        # Get page numbers
        productLink.get_page_numbers()
        # Start the Product Url Spider
        productLink.startProductUrlSpider()
    # Else if scrap argument was passed with value of products run the Product Spider
    elif args.scrap == 'products':
        from modules.product import Product
        # Create instants of Product class
        product = Product()
        # Call the ProductSpider
        product.startProductSpider()
    # If arguments do not pass to the script. show the help
    else:
        arg_parse.print_help()
