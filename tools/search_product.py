import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Search Products on Supported Platforms")
    parser.add_argument(
        "--platform", "-p", required=True, help="Online Retail Platform", type=str
    )
    parser.add_argument(
        "--keyword", "-k", required=True, help="Product Keyword", type=str
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    platform = args.platform
    if platform == "amazon":
        from product_scrapper.amazon.amazon_search import AmazonSearch as Search
    else:
        raise NotImplementedError

    search = Search(keyword=args.keyword)
    search.scrape()
    print(search)


if __name__ == "__main__":
    main()