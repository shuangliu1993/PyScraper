import unittest

from product_scrapper.walmart.walmart_search import WalmartSearch


class TestWalmartSearch(unittest.TestCase):
    def setUp(self):
        self.keyword = "SKII"

    def test_amazon_product(self):
        search = WalmartSearch(self.keyword)
        search.scrape()
        print(search)
