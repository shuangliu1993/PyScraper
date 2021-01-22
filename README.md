# PyScraper

Web scraper built on request and bs4 to search and monitor product information on online retail platform

## Supported Platforms
-[x] Amazon
-[ ] Walmart (WIP)

## Installation

```shell
pip install requirements.txt
python setup.py develop
```

## Usage
```shell
# Search product by keywords
python tools/search_product.py -p amazon -k switch

# Monitor live product status (title, url, price, ratings, availability, etc.)
python tools/watch_product.py -p amazon -u https://www.amazon.com/Switch-Console-Supper-Earphone-Silicon/dp/B08FQWBT48
```
