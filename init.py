import os
from colorama.ansi import Fore
from stdiomask import getpass

# Collect the data
DB_HOST = str(input("Database Host: "))
DB_USER = str(input("Database Username: "))
DB_PASS = str(getpass(prompt="Database Password: "))
DB_NAME = str(input("Database Name: "))

# Create template
data = f'''
DB_HOST = str('{DB_HOST}')
DB_USER = str('{DB_USER}')
DB_PASS = str('{DB_PASS}')
DB_NAME = str('{DB_NAME}')
'''

# Write the template to file
with open(os.getcwd() + '/digikala_post/digikala_post/spiders/config/config.py', 'w+', encoding='utf8') as f:
    f.flush()
    f.write(data)
    os.system(
        f'autopep8 -i "{os.getcwd()}/digikala_post/digikala_post/spiders/config/config.py" ')
    f.close()
# Create the links.json
with open(os.getcwd() + '/digikala_post/digikala_post/links.json', 'w+') as f:
    f.write('[]')
    f.close()
