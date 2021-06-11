# Digikala Spider

Digikala spider is a simple spider for extract the products info from digikala.

## About

Digikala spider created to help us to create database with Digikala products.

## Requirements

- Python: 3.9.4+
- Scrapy: 2.5.0
- autopep8: 1.5.6
- pylint: 2.7.4
- mysql-connector-python: 8.0.24
- colorama: 0.4.4
- stdiomask: 0.0.6
- rotating-free-proxies: 0.1.2
- jsonlines: 2.0.0

## Setup

First, we must install the pipenv to manage our packages:

```bash
$ pip install -U pipenv --user
```

after this, we must install our dependencies:

```bash
$ python -m pipenv install
```

after that, we must enter into the virtualenv that we created in the previous step:

```bash
python -m pipenv shell
```

after that, we must initial our database and required files:

```bash
$ python main.py --init y

Database Host: <Your Mysql server address>
Database Username: <Your mysql username>
Database Password: <Your mysql password>
Database Name: <Your mysql database name>
```

## Usage

> :warning: **You must run the links scraper first every time you want to scrap the product links for the productSpider**

<br/>

```bash
$ python main.py -h

usage: main.py [-h] [--init INIT] [--scrap {links,products}]

Digikala Scraper

optional arguments:
  -h, --help            show this help message and exit
  --init INIT           Initial the database and required files
  --scrap {links,products}
                        Scrap the products or links

```
