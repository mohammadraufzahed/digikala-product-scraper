from digikala_post.digikala_post.spiders.config import category
import os


class Main():
    # Get the category link from user
    def get_category_link(self):
        self.__category_link = input("Please enter the category link: ")

    # Generate the pages to scrap
    def get_page_numbers(self):
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
    def saveData(self, category_link, page_number):
        data = f'''
        CATEGORY_LINK = str('{category_link}')
        PAGES_NUMBER = list({page_number})
        '''
        with open(os.getcwd() + '/digikala_post/digikala_post/spiders/config/category.py', 'w', encoding='utf8') as f:
            f.flush()
            f.write(data)
        os.system(
            f'autopep8 -i "{os.getcwd()}/digikala_post/digikala_post/spiders/config/category.py" ')

    # Run the spiders
    def startSpiders(self):
        for numbers in self.__page_numbers:
            self.saveData(category_link=self.__category_link,
                          page_number=numbers)
            os.system(
                'cd digikala_post/digikala_post/ && scrapy crawl product_link && scrapy crawl product')
