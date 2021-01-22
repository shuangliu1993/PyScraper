from product_scrapper.search import Search
from product_scrapper.walmart.walmart_product import WalmartProduct


class WalmartSearch(Search):
    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword
        self.set_url()

    def set_url(self):
        self.url = f"https://www.walmart.com/?query={self.keyword}"

    def get_entries(self):
        from IPython import embed
        embed()

    def parse_entry(self, entry):
        from IPython import embed
        embed()
