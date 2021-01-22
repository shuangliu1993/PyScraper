import logging

from product_scrapper.utils import get_soup_from_url

logger = logging.getLogger(__name__)


class Search:
    def __init__(self):
        self.keyword = None
        self.url = ""
        self.soup = None
        self.entries = []
        self.results = []

    def set_url(self):
        raise NotImplementedError

    def get_soup(self):
        if not self.url:
            logger.error("Url is not set!")
            assert ValueError
        self.soup = get_soup_from_url(self.url)

    def get_entries(self):
        raise NotImplementedError

    def parse_entry(self, entry):
        raise NotImplementedError

    def get_results(self):
        self.results = [self.parse_entry(entry) for entry in self.entries]

    def scrape(self):
        """Scrape all data once url is set"""
        self.get_soup()
        self.get_entries()
        self.get_results()

    def __repr__(self):
        return "\n".join(res.__repr__() for res in self.results) + "\n"
