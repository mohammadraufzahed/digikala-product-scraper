# Digikala Spider
Digikala spider is a simple spider for extract the products info from digikala.
## About
___
Digikala spider created to help us to create database with Digikala products.

## Requirements
___
* Python: 3.9.4+ <br>
* Scrapy: 2.5.0
* autopep8: 1.5.6
* pylint: 2.7.4
* mysql-connector-python: 8.0.24
* colorama: 0.4.4
## Setup
___
First we must install the requirements:
```shell
$ pip install -r requirements.txt
```
after this you must give your database information to the app buy running init script:
```shell
$ python init.py
```
after that you must import the sql tables to your database:
```shell
# sudo mysql -u USERNAME -p DATABASE_NAME < db.sql
```
now you can use the program.
## Usage
___
```shell
# python main.py
Please enter the category link(https://www.digikala.com/search/category-mobile/): https://www.digikala.com/search/category-mobile/
How many page this category have?  277
............
```