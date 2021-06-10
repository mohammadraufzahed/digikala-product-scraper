import os
from colorama.ansi import Fore
from stdiomask import getpass
from spiders.Database.Mysql import Mysql


def init():
    """
    Initial the database and required files
    """
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
    with open(os.getcwd() + '/spiders/config/config.py', 'w+', encoding='utf8') as f:
        f.flush()
        f.write(data)
        f.close()
    # Initial the database
    with open("db.sql", 'r', encoding="utf8") as dbQuery:
        db = Mysql(DB_HOST, DB_USER, DB_PASS)
        db.query(f"DROP DATABASE IF EXISTS {DB_NAME}")
        db.query(f"CREATE DATABASE {DB_NAME}")
        db.query(f"USE {DB_NAME}")
        db.query(dbQuery.read())
        db.commit()
    # Create the links.json
    with open(os.getcwd() + '/links.json', 'w+') as f:
        f.write('[]')
        f.close()
    print("Database and required files initialized")
