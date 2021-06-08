from modules.main import Main

if __name__ == '__main__':
    # Create instans
    main = Main()
    # Get category page link
    main.get_category_link()
    # Get page numbers
    main.get_page_numbers()
    # Start the spiders
    main.startSpiders()
    print("Press Ctrl+C to close the programmer")
