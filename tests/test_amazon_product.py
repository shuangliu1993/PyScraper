import unittest

from product_scrapper.amazon.amazon_product import AmazonProduct


class TestAmazonProduct(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.amazon.com/Switch-Console-Supper-Earphone-Silicon/dp/B08FQWBT48"

    def test_amazon_product(self):
        product = AmazonProduct(self.url)
        product.scrape()
        print(product)
