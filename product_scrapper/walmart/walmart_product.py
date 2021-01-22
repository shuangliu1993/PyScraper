import logging

from product_scrapper.product import Product

logger = logging.getLogger(__name__)


class WalmartProduct(Product):
    def __init__(self, url=None):
        super().__init__()
        self.set_url(url)
