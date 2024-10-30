import requests
from bs4 import BeautifulSoup
import json
import re

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,"
    "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "dpr": "1",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

product_summary = requests.get(
    "https://www.target.com/s?searchTerm=laptop",
    headers=headers,
).text

print(product_summary)