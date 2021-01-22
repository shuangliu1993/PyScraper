from product_scrapper.search import Search
from product_scrapper.amazon.amazon_product import AmazonProduct


class AmazonSearch(Search):
    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword
        self.set_url()

    def set_url(self):
        self.url = f"https://www.amazon.com/s?k={self.keyword}"

    def get_entries(self):
        self.entries = self.soup.select("div[data-component-type='s-search-result']")

    def parse_entry(self, entry):
        product = AmazonProduct()

        # title
        product.set_title(
            entry.select("h2 a.a-link-normal.a-text-normal")[0].text.replace("\n", "")
        )

        # url
        try:
            url = entry.select("h2 a.a-link-normal.a-text-normal")[0].get("href")
            url = url[url.index("url=") + len("url="):]
            url = url[:url.index("ref")]
            url = "http://amazon.com" + url.replace("%2F", "/")
        except ValueError:
            url = entry.select("h2 a.a-link-normal.a-text-normal")[0].get("href")
            url = url[:url.index("ref")]
            url = "http://amazon.com" + url
        product.set_url(url)

        try:
            product.set_ratings(
                f"{entry.select('div.a-row.a-size-small span:nth-of-type(1)')[0].get('aria-label')}, "
                f"{entry.select('div.a-row.a-size-small span:nth-of-type(2)')[0].get('aria-label')} ratings."
            )
        except IndexError:  # no ratings available
            pass

        try:
            product.set_price(
                entry.select('span.a-price:nth-of-type(1) span.a-offscreen')[0].text.replace("\n", "")
            )
        except IndexError:  # no price available
            pass
        return product
