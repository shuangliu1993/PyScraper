from setuptools import find_packages, setup


if __name__ == "__main__":
    setup(
        name='product-scrapper',
        version='1.0.0',
        packages=find_packages(include="product_scrapper"),
        url='',
        license='MIT',
        author='ShuangLiu',
        author_email='shuangliu1993@gmail.com',
        description='Product Scraping Tools'
    )
