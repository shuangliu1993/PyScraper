import logging

from product_scrapper.product import Product

logger = logging.getLogger(__name__)


class AmazonProduct(Product):
    def __init__(self, url=None):
        super().__init__()
        self.set_url(url)

    def get_title_by_soup(self):
        try:
            self.title = self.soup.select("#productTitle")[0].text.replace("\n", "")
        except IndexError:  # no title available
            logger.warning("Cannot get title info from soup")

    def get_price_by_soup(self):
        try:
            self.price = self.soup.select("#price_inside_buybox")[0].text.replace("\n", "")
        except IndexError:  # no price available
            logger.warning("Cannot get price info from soup")

    def get_availability_by_soup(self):
        try:
            self.availability = self.soup.select("#availability")[0].text.replace("\n", "")
        except IndexError:
            logger.warning("Cannot get availability info from soup")

    def get_ratings_by_soup(self):
        try:
            reviews = self.soup.select("#averageCustomerReviews")[0].text.replace("\n", "")
            split_id = reviews.find("stars") + len("stars")
            self.ratings = reviews[:split_id] + ", " + reviews[split_id:]
        except IndexError:
            logger.warning("Cannot get ratings info from soup")
