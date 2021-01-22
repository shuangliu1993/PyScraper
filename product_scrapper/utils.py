import logging
import random
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

logger = logging.getLogger(__name__)


def get_soup_from_url(url):
    req = requests.get(url, headers=get_random_header(), proxies=get_random_proxy())
    req.raise_for_status()
    return BeautifulSoup(req.text, "html.parser")


def get_random_proxy():
    """TODO: Find a robust proxy rotation method"""
    return {}


def get_random_header():
    ua = UserAgent()
    agent = ua.safari  # Firefox agent has fewer compatibility issues
    header = {
        'User-Agent': agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    return header
