import unittest

from product_scrapper.amazon.amazon_search import AmazonSearch


class TestAmazonSearch(unittest.TestCase):
    def setUp(self):
        self.keyword = "switch"

    def test_amazon_product(self):
        search = AmazonSearch(self.keyword)
        search.scrape()
        print(search)
