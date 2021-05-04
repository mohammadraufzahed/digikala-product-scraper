# Digikala Spider
Digikala spider is a simple spider for extract the products info from digikala.
## About
Digikala spider created to help us to create database with Digikala products.

## Requirements
* Python: 3.9.4+ <br>
* Scrapy: 2.5.0
* autopep8: 1.5.6
* pylint: 2.7.4
* mysql-connector-python: 8.0.24
* colorama: 0.4.4
## Setup
First we must install the requirements:
```bash
$ pip install -r requirements.txt
```
after this you must give your database information to the app buy running init script:
```bash
$ python init.py
```
after that you must import the sql tables to your database:
```bash
$ sudo mysql -u USERNAME -p DATABASE_NAME < db.sql
```
now you can use the program.
## Usage
```bash
$ python main.py
Please enter the category link(https://www.digikala.com/search/category-mobile/): https://www.digikala.com/search/category-mobile/
How many page this category have?  277
............
```
