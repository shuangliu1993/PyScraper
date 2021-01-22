import argparse
import time


def parse_args():
    parser = argparse.ArgumentParser(description="Search Products on Supported Platforms")
    parser.add_argument(
        "--platform", "-p", required=True, help="Online Retail Platform", type=str
    )
    parser.add_argument(
        "--url", "-u", required=True, help="url of the product", type=str
    )
    parser.add_argument(
        "--interval", "-i", help="Interval in seconds of each request attempt. Small interval causes higher risks of "
                                 "being detected as bot!",
        type=int, default=60
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    platform = args.platform
    if platform == "amazon":
        from product_scrapper.amazon.amazon_product import AmazonProduct as Product
    else:
        raise NotImplementedError

    while True:
        product = Product(url=args.url)
        product.scrape()
        print(product)
        print("\n")
        time.sleep(args.interval)


if __name__ == '__main__':
    main()
