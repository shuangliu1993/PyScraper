import logging

from product_scrapper.utils import get_soup_from_url

logger = logging.getLogger(__name__)


class Product:
    def __init__(self):
        self.url = ""
        self.title = "Unknown"
        self.price = "Unknown"
        self.availability = "Unknown"
        self.ratings = "Unknown"
        self.soup = None

    def set_url(self, url):
        self.url = url

    def get_soup(self):
        if not self.url:
            logger.error("Url is not set!")
            assert ValueError
        self.soup = get_soup_from_url(self.url)

    def set_title(self, title):
        self.title = title

    def get_title_by_soup(self):
        assert NotImplementedError

    def set_price(self, price):
        self.price = price

    def get_price_by_soup(self):
        assert NotImplementedError

    def set_availability(self, availability):
        self.availability = availability

    def get_availability_by_soup(self):
        assert NotImplementedError

    def set_ratings(self, ratings):
        self.ratings = ratings

    def get_ratings_by_soup(self):
        assert NotImplementedError

    def scrape(self):
        """Scrape all data once url is set"""
        self.get_soup()
        self.get_title_by_soup()
        self.get_price_by_soup()
        self.get_availability_by_soup()
        self.get_ratings_by_soup()

    def __repr__(self):
        return (
            f"Product Info:\n"
            f"\tTitle: {self.title}\n"
            f"\tUrl: {self.url}\n"
            f"\tPrice: {self.price}\n"
            f"\tAvailability: {self.availability}\n"
            f"\tRatings: {self.ratings}"
        )
